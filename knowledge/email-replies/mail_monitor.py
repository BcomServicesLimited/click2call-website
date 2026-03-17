import imaplib
import smtplib
import ssl
from email import message_from_bytes
from email.message import EmailMessage
from email.header import decode_header, make_header
from email.utils import parseaddr
from pathlib import Path
from datetime import datetime, timezone

BASE_DIR = Path('/home/ubuntu/click2call-website/knowledge/email-replies')
ENV_PATH = BASE_DIR / '.env.mail_monitor'
LOG_DIR = BASE_DIR / 'logs'
DRAFT_DIR = BASE_DIR / 'drafts'
STATE_FILE = BASE_DIR / '.mail_monitor_state'

LOG_DIR.mkdir(parents=True, exist_ok=True)
DRAFT_DIR.mkdir(parents=True, exist_ok=True)

AUTO_IGNORE_SENDERS = {
    'mailer-daemon@googlemail.com',
    'no-reply@accounts.google.com',
    'noreply@google.com',
    'no-reply@google.com',
}

AUTO_IGNORE_SUBJECT_KEYWORDS = [
    'security alert',
    'delivery status notification',
    'message blocked',
    'mail delivery subsystem',
    'undeliverable',
]


def load_env(path: Path):
    data = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        key, value = line.split('=', 1)
        data[key.strip()] = value.strip()
    return data


def decode_mime(value):
    if not value:
        return ''
    try:
        return str(make_header(decode_header(value)))
    except Exception:
        return value


def extract_text(msg):
    if msg.is_multipart():
        parts = []
        for part in msg.walk():
            ctype = part.get_content_type()
            disp = str(part.get('Content-Disposition', ''))
            if ctype == 'text/plain' and 'attachment' not in disp.lower():
                payload = part.get_payload(decode=True)
                if payload:
                    charset = part.get_content_charset() or 'utf-8'
                    parts.append(payload.decode(charset, errors='replace'))
        return '\n'.join(parts).strip()
    payload = msg.get_payload(decode=True)
    if not payload:
        return ''
    charset = msg.get_content_charset() or 'utf-8'
    return payload.decode(charset, errors='replace').strip()


def load_last_uid():
    if STATE_FILE.exists():
        return STATE_FILE.read_text().strip()
    return ''


def save_last_uid(uid: str):
    STATE_FILE.write_text(uid)


def classify_sender(sender_email, auto_sender):
    return 'auto' if sender_email.lower() == auto_sender.lower() else 'approval_only'


def should_ignore_message(sender_email, subject, body_text):
    sender = (sender_email or '').lower().strip()
    lowered_subject = (subject or '').lower()
    lowered_body = (body_text or '').lower()

    if sender in AUTO_IGNORE_SENDERS:
        return True, 'ignored_system_sender'

    for keyword in AUTO_IGNORE_SUBJECT_KEYWORDS:
        if keyword in lowered_subject:
            return True, 'ignored_system_subject'

    if 'if you didn\'t generate this password' in lowered_body:
        return True, 'ignored_security_notice'

    return False, ''


def decide_outcome(subject, body_text):
    text = f'{subject}\n{body_text}'.lower()
    escalation_keywords = [
        'billing dispute', 'outage', 'refund', 'legal', 'lawyer', 'solicitor',
        'porting', 'port my number', 'number port', 'complaint', 'phishing',
        'suspicious', 'account ownership', 'credit', 'compensation'
    ]
    clarification_keywords = ['call me', 'need help', 'can you help', 'urgent']

    if any(keyword in text for keyword in escalation_keywords):
        return 'needs_escalation'
    if len((body_text or '').strip()) < 40 or any(keyword in text for keyword in clarification_keywords):
        return 'needs_clarification'
    return 'ready_for_approval'


def build_reply(subject, sender_name, body_preview, mode, outcome):
    greeting_name = sender_name or 'there'
    if mode == 'auto':
        body = (
            f'Hello {greeting_name},\n\n'
            'Thank you for your email. This is an automatic reply from Click2Call Support confirming that your message has been received. '
            'I will continue handling it under the approved rule set for this sender.\n\n'
            'Kind regards,\n'
            'Click2Call Support\n'
            'support@click2call.com.au\n'
        )
    elif outcome == 'needs_clarification':
        body = (
            f'Hello {greeting_name},\n\n'
            'Thank you for contacting Click2Call Support. To help properly, I need a little more information before I prepare the final response. '
            'Please confirm the relevant service, phone number, account details, and the issue you need help with.\n\n'
            'Kind regards,\n'
            'Click2Call Support\n'
            'support@click2call.com.au\n'
        )
    elif outcome == 'needs_escalation':
        body = (
            f'Hello {greeting_name},\n\n'
            'Thank you for contacting Click2Call Support. I have reviewed your message and prepared this as an escalation item for internal review before any reply is sent.\n\n'
            'Kind regards,\n'
            'Click2Call Support\n'
            'support@click2call.com.au\n'
        )
    else:
        body = (
            f'Hello {greeting_name},\n\n'
            'Thank you for contacting Click2Call Support. I have prepared this draft reply for approval before sending.\n\n'
            'Based on your message, I will respond using the approved Click2Call guidance and current website information.\n\n'
            'Kind regards,\n'
            'Click2Call Support\n'
            'support@click2call.com.au\n'
        )
    return f'Re: {subject}' if subject and not subject.lower().startswith('re:') else subject or 'Re: your email', body


def save_draft_record(uid, sender_email, subject, mode, outcome, original_body, body):
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    path = DRAFT_DIR / f'{stamp}_uid{uid}_{mode}_{outcome}.md'
    preview = (original_body or '').strip()[:1500]
    path.write_text(
        f'# Email Handling Record\n\n'
        f'| Field | Value |\n'
        f'|---|---|\n'
        f'| UID | {uid} |\n'
        f'| Sender | {sender_email} |\n'
        f'| Subject | {subject} |\n'
        f'| Mode | {mode} |\n'
        f'| Outcome | {outcome} |\n\n'
        f'## Original message preview\n\n{preview}\n\n'
        f'## Draft body\n\n{body}\n'
    )
    return path


def send_email(cfg, to_addr, subject, body):
    msg = EmailMessage()
    msg['From'] = cfg['MAILBOX']
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(cfg['SMTP_HOST'], int(cfg['SMTP_PORT']), context=context) as server:
        server.login(cfg['MAILBOX'], cfg['APP_PASSWORD'])
        server.send_message(msg)


def send_approval_notification(cfg, original_sender, original_subject, draft_path, outcome):
    notify_to = cfg.get('APPROVAL_NOTIFICATION_EMAIL', '').strip()
    if not notify_to:
        return
    subject = f'Approval needed: {original_subject or "New Click2Call email"}'
    body = (
        'A new Click2Call email handling record is waiting for review.\n\n'
        f'Original sender: {original_sender}\n'
        f'Original subject: {original_subject or "(no subject)"}\n'
        f'Workflow outcome: {outcome}\n'
        f'Draft record: {draft_path}\n\n'
        'Please review the saved draft before any reply is sent.\n'
    )
    send_email(cfg, notify_to, subject, body)


def main():
    cfg = load_env(ENV_PATH)
    last_uid = load_last_uid()
    latest_seen = last_uid
    log_lines = []

    with imaplib.IMAP4_SSL(cfg['IMAP_HOST'], int(cfg['IMAP_PORT'])) as imap:
        imap.login(cfg['MAILBOX'], cfg['APP_PASSWORD'])
        imap.select('INBOX')
        status, data = imap.uid('search', None, 'ALL')
        if status != 'OK':
            raise RuntimeError('Failed to search inbox')
        uids = data[0].split()
        if last_uid:
            new_uids = [u for u in uids if int(u) > int(last_uid)]
        else:
            new_uids = uids[-10:]

        for uid_bytes in new_uids:
            uid = uid_bytes.decode()
            status, msg_data = imap.uid('fetch', uid, '(RFC822)')
            if status != 'OK':
                continue
            raw = msg_data[0][1]
            msg = message_from_bytes(raw)
            subject = decode_mime(msg.get('Subject', ''))
            from_name, from_email = parseaddr(msg.get('From', ''))
            body_text = extract_text(msg)

            ignore, ignore_reason = should_ignore_message(from_email, subject, body_text)
            if ignore:
                log_lines.append(f'{uid}\t{from_email}\t{subject}\t{ignore_reason}\t-')
                latest_seen = uid
                continue

            mode = classify_sender(from_email, cfg['AUTO_APPROVED_SENDER'])
            outcome = 'auto_sent' if mode == 'auto' else decide_outcome(subject, body_text)
            reply_subject, reply_body = build_reply(subject, from_name, body_text, mode, outcome)
            draft_path = save_draft_record(uid, from_email, subject, mode, outcome, body_text, reply_body)

            if mode == 'auto':
                send_email(cfg, from_email, reply_subject, reply_body)
                action = 'auto_sent'
            else:
                send_approval_notification(cfg, from_email, subject, draft_path, outcome)
                action = f'draft_saved_and_notified:{outcome}'

            log_lines.append(f'{uid}\t{from_email}\t{subject}\t{action}\t{draft_path}')
            latest_seen = uid

    if latest_seen:
        save_last_uid(latest_seen)

    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    log_path = LOG_DIR / f'run_{stamp}.tsv'
    log_path.write_text('uid\tsender\tsubject\taction\tdraft_path\n' + '\n'.join(log_lines) + ('\n' if log_lines else ''))
    print(log_path)


if __name__ == '__main__':
    main()
