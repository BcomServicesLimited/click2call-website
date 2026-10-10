# Click2Call Help Centre — full text of every guide

Click2Call is an Australian Cloud PBX, VoIP and AI voice provider (Bcom Services Pty Ltd, ABN 92 636 893 108). This file contains the complete text of every guide in the Click2Call Help Centre, for AI assistants and search engines. Each section links to the live page. Index: https://www.click2call.com.au/help/ · Site summary: https://www.click2call.com.au/llms.txt

# Getting Started

## Starting a Call from a Web Link (Call Setup API)

Source: https://www.click2call.com.au/help/call-setup-api

The call setup API connects two phone numbers with a single web request. Click2Call rings the first number, and when it's answered, dials the second. It's a simple way to add click-to-call to a website, CRM or script. For webhooks, call records and AI features, see the full [Developer API](https://www.click2call.com.au/api/).

Last reviewed: October 2026

### The request

Send a GET or POST request to:

```
https://portal.click2call.com.au/api/call.php
```

| Parameter | Required | What it is |
| login | Yes | The Click2Call number making the call, as shown in Line Manager. Calls are billed to this number. |
| password | Yes | That number's line password, not your portal password |
| aparty | Yes | The first number to ring, usually your own phone |
| bparty | Yes | The number to connect to once the first answers |
| delay | No | Seconds to wait before starting the call. Default is immediately. |

### Example

```
https://portal.click2call.com.au/api/call.php?login=61370500989&password=YOUR_LINE_PASSWORD&aparty=61370500989&bparty=0412345678
```

Use POST in your own code so the password doesn't end up in browser history or server logs.

### Responses

The API replies in JSON.

```
{"Result":"1","Status":"Success","Message":"Call Setup Successful"}
{"Result":"-1","Status":"Error","Message":"Password incorrect"}
```

### Charges

Both legs are normal outgoing calls. If neither number is on your Click2Call account, you pay for both legs: the call to the first number and the call to the second.

### Keep the password safe

Anyone with the line password can make calls on your account. Never put it in a public web page. Call the API from your own server instead.

## Browser Calling with WebRTC (SIP over WebSocket)

Source: https://www.click2call.com.au/help/webrtc-sip-over-websocket

You can register a Click2Call number from a web browser, using SIP over a secure WebSocket (WSS). This lets you build calling into your own web app with a WebRTC library such as SIP.js or JsSIP.

Last reviewed: October 2026

### Connection settings

| Setting | What to enter |
| WebSocket server | wss://wss.securevoip.nz:7443 |
| SIP domain | sip.click2call.com.au |
| Username | The number or extension Login from Line Manager |
| Password | That line's password |

### TURN server

If your users are behind strict firewalls, a TURN server relays the audio. Click2Call's is optional, and you can use your own TURN or STUN servers instead.

```
turns:wss.securevoip.nz:5349
```

Sign in to it with the same number and line password.

### Keep credentials off the page

Anyone who can see the line password can make calls on your account. Don't hard-code it in JavaScript that users can view. Fetch it from your own server after the user has logged in.

## Connecting Zoho CRM

Source: https://www.click2call.com.au/help/zoho-crm-integration

Click2Call connects to Zoho CRM so your team can click a number in Zoho to call it, see who's calling before they answer, and keep every call, note and recording in the CRM. The integration is free for all Click2Call customers.

Last reviewed: October 2026

### Step 1: install the extension in Zoho

- In Zoho CRM, go to **Settings → Channels → Telephony**.
- In the telephony marketplace, find your phone provider's PhoneBridge extension and click **Install**. If you can't find it, contact support and we'll help.
- Choose which users get calling, or **All Users**.

### Step 2: connect it in the Click2Call portal

- In the portal, go to **Voice → CRM Integration** and click the Zoho logo.
- Click the link to register with the **Zoho Phone Bridge Service**.
- Sign in with your Zoho account and click **Accept**.
- Back in the portal, check **Zoho Phone Bridge Connected** is ticked, then click **Enable Zoho Integration**.

### Step 3: match Zoho users to phone numbers

Your Zoho users are listed with their email addresses. For each one:

- Under **Monitored Phone number(s)**, choose the numbers whose calls should appear in their Zoho. Hold Ctrl (or Cmd on a Mac) to pick more than one.
- Under **Click to Dial**, choose the phone that rings when they click a number in Zoho.

Click **Apply Settings** and check for errors.

### Using it

- **Calling out:** hover over a number in Zoho and click **Call**. Your phone rings first. Answer it, and Click2Call dials the customer.
- **During the call:** a popup shows the call status and a timer. Type notes as you talk.
- **After the call:** add notes and follow-up actions, then click **Done**.
- **Incoming calls:** a popup shows the caller's details if they're in Zoho.

Every call appears under the **Calls** tab in Zoho. If call recording is on, the recording is attached to the call and can be played in Zoho after a minute or two. See [Viewing call recordings](https://www.click2call.com.au/help/how-to-view-call-recordings).

## Turning On Two-Factor Login

Source: https://www.click2call.com.au/help/two-factor-login

Two-factor login adds a one-time code to your portal sign-in. Even if someone learns your password, they can't get into your account without the code, which is emailed to you each time you log in.

Last reviewed: October 2026

### Turn it on for everyone

- Log in to the portal and go to **Account → Details**.
- At the bottom, under **Two Factor Authentication (2FA)**, choose **Enabled for all users**. Codes are sent by email.
- Optionally tick **Remember trusted locations**. You won't be asked again when you log in from the same internet connection. Leave it unticked for the highest security.
- Click **Update Details** and log out.

Next time anyone logs in, they're asked for a code sent to their email address.

### Turn it on for the main login only

Choose **Enabled for account login only** instead. Only logins with the 8-digit account number need a code.

### Turn it on for one person

- Go to **Account → Logins** and click the person's name.
- Under two-factor authentication, choose **Email verification**.
- Save.

### Not getting the code?

Check your spam folder, and check the email address on your login is correct. See [Adding portal logins](https://www.click2call.com.au/help/how-to-add-portal-logins).

## Using the API and Webhooks on a Trial Account

Source: https://www.click2call.com.au/help/webhooks-and-api-during-your-trial

Your Click2Call trial includes the full API and webhooks, with no trial limits, from the day you sign up. This guide covers setting up a webhook, the events and fields it sends, how to check one fired, the usual reasons one does not arrive, and what to send support if you are still stuck.

Last reviewed: October 2026

Who this guide is for

Developers and businesses testing an integration during the 7-day free trial — a CRM hook, an automation in Zapier or Make, or your own app that reacts to calls. API and webhook configuration is self-service: Click2Call supports the platform and its documentation, but not your integration code.

### What is available during the 7-day free trial?

The API and webhooks are fully featured during the trial, with no trial-specific limits. Everything is available from the moment the account is created:

- •**API access** — the full JSON REST API. See the full API documentation in the client portal.
- •**Webhooks** — every call state, including the `aianalysis` event that carries the transcript and AI call summary.
- •**$11 of trial credit** — enough to activate one local number ($10) and make a few test calls. Inbound calls are free, so you can test incoming-call webhooks for the whole trial.
What the trial does not include: help configuring the API, webhooks or a third-party integration (configuration is self-service), and Microsoft Teams Direct Routing.

### How do I set up a webhook?

Webhooks are set up in the client portal. The webhook documentation explains where to add your webhook URL, the payload format and every field. You can set a webhook on one number or across every number on the account.
Each webhook is an HTTP POST with `Content-Type: application/json` and your secret token in the `Authorization` header. You can change that header to a custom header name of your choosing.

### Which webhook events can I receive?

Every webhook carries a `state` field that tells you what happened:

| Call direction | States |

| Received (incoming) | ringing, answered, ended, missed (an incoming call that was not picked up) |
| Dialed (outgoing) | ringing, answered, ended, and when the call does not connect: busy, invalid, rejected, notavailable, blocked, noanswer |
| AI analysis | aianalysis — the transcript and AI call summary are ready |

#### Fields worth knowing

| Field | What it is |

| id | Unique identifier for this call. Use it to match a webhook to a call and to ignore duplicates. |
| originid | The call this one came from. Same as id for the first call in a sequence; different for a transferred or forwarded leg. |
| type | received (incoming) or dialed (outgoing). |
| from, to | Calling and called numbers. |
| start_time | UTC, YYYY-MM-DD HH:MM:SS. Sent only on ended or missed/failed events. |
| duration | Call length in seconds. Sent only on a successful ended event. |
| voiceuri | Link to the recording. Sent only on a successful ended event, and only when call recording is enabled. |
| aiuri, transcript, callsummary | Sent only on the aianalysis event, and only when AI transcription is enabled. callsummary includes a short and full summary, categories, names mentioned and scores such as sentiment. |

### How do I check whether a webhook fired?

Work from the call outward: first prove the call happened, then whether your endpoint received the event.

1

#### Make a test call you can identify

Call your Click2Call number from another phone and note the time, the number you called from and whether the call was answered. An answered call and a missed call produce different states, so decide which one you are testing.

2

#### Confirm the call reached your number

In the portal, open **Account → Records** and find the call by time and caller. If it is not there, the problem is the call, not the webhook — see the reasons below.

3

#### Check your endpoint's logs

Look for a POST at the time of the call. Your server's access log is the best evidence of delivery. Log the `state` and `id` of every webhook you receive so you can see exactly which events arrived.

4

#### Match events by call ID

All the events for one call share its `id`, so you can follow a call from `ringing` to `ended`, and to `aianalysis` afterwards. Build your receiver to tolerate the same event arriving more than once — skip any `id` and `state` pair you have already processed. For retry behaviour on failed deliveries, see the webhook documentation.

5

#### Still nothing? Ask us to check

If the call is in Records but your endpoint received nothing, contact support and we'll check for you whether the webhook was sent from our side.

### Why didn't my webhook arrive?

#### Your endpoint is not reachable from the internet

Click2Call posts from the internet, so `localhost`, a private IP address, a machine behind a firewall or a development server that is switched off will never receive it. Use a public address, or a tunnelling tool while you develop. For endpoint requirements, see the full API documentation.

#### The URL is wrong, or set on a different number

Check for typos, `http` versus `https`, the path and a trailing slash. If the webhook is set on one number, calls to a different number — or to an extension — will not trigger it. Set it across all numbers while testing if you are unsure.

#### Your endpoint rejected it

If your receiver checks the `Authorization` header (or the custom header you chose), make sure it compares against the same secret token you set. Return a 2xx status quickly and do slow work afterwards; a receiver that times out looks like a failure.

#### No aianalysis event, transcript or recording link

The `aianalysis` event, with `aiuri`, `transcript` and `callsummary`, is sent only when AI transcription is enabled. `voiceuri` is sent only when call recording is enabled. Expect `aianalysis` a little after the call ends, not during it.

#### The trial credit has run out

Inbound calls are free, but outgoing calls use credit. Check the balance on the portal Summary page and see [Adding Account Credit](https://www.click2call.com.au/help/how-to-add-account-credit).

#### The account has gone past its $5 IOU limit

Every account can run a small negative balance — an IOU of up to $5. Once the balance goes past −$5, outgoing calls are blocked automatically, and anyone trying to call out hears a message that outgoing calls can't be made. A blocked call never connects, so it produces no `answered` or `ended` events. Topping up releases the block automatically.

#### The account is not active yet

New accounts are activated within 24 hours of signup, and identity verification usually takes a few hours. Until the account and number are active, test calls will not connect.

### What should I send support if it still isn't working?

Email support@click2call.com.au with:

- •Your account number and the Click2Call number you called
- •The date and time of the test call (AEST), and the number you called from
- •The state you expected (for example `answered`, `missed` or `aianalysis`)
- •The call `id` from any webhook that did arrive for that call
- •Your endpoint URL — **never** your API token or the webhook secret
- •What your endpoint logged at that time: the status code it returned, or that it received nothing
Support can check whether Click2Call sent the event. Debugging your integration code is not included in support.

## Activating Your Account

Source: https://www.click2call.com.au/help/how-to-activate-account

This guide walks you through what happens after you complete the Click2Call signup form and how to access your portal for the first time.

Last reviewed: August 2026

### Activating Your Account, Step by Step

1

#### Sign up for a free trial

Visit portal.click2call.com.au/join and complete the signup form. You will need to provide your name, email address, and a password. No credit card is required to start your 7-day free trial.

After submitting the form, check your inbox for a confirmation email from Click2Call. Click the verification link to activate your account before logging in.

2

#### Log in to your portal

Go to portal.click2call.com.au and enter your email address and password, then click **Log in**.

The Click2Call portal login screen

3

#### Review your Account Summary

After logging in you will land on the **Account Summary** page. This shows your account name, account number, next billing date, current balance, and your active phone services. During your free trial, your Cloud PBX plan will be listed here.

The Account Summary page — your starting point after login

4

#### Update your account details

Click **Details** in the left sidebar to open the Account Details page. Fill in your personal details, service address, and contact information. This information is used for billing and support. Click **Update Details** to save your changes.

The Account Details page — update your contact and billing information here

We recommend enabling **Two Factor Authentication (2FA)** on this page to keep your account secure. You can choose to be prompted once per location for convenience.

5

#### Review your plan and channels

Click **Plan** in the left sidebar to view your current plan details. You will see your active services, included channels, and any line plans assigned to your numbers. Your account starts with **2 free channels** (simultaneous call lines) by default.

The Account Plan page — view your services, channels, and line plans

6

#### Start adding your phone services

Click **Voice** in the top navigation bar to go to the Voice Numbers page. From here you can add phone numbers, create extensions for your team, and provision desk phones and softphones. Use the buttons at the top — **Add Phone Number**, **Add Extension**, and **Add Channels** — to get started.

The Voice Numbers page — your hub for managing extensions and phone numbers

Your account is now active and ready to use. Follow the guides below to add your first phone number, set up extensions for your team, and configure your call flows.

## Understanding Your Free Trial

Source: https://www.click2call.com.au/help/understanding-your-free-trial

Everything you need to know about your 7-day free trial, the $11 account credit, and what happens when the trial ends.

Quick Summary

- Your account comes with **$11 free credit** automatically loaded.

- This covers the cost of one **local landline number ($10)** and leaves **$1 for test outbound calls**.

- Inbound calls are completely free.

- No credit card is required to start the trial.

### What the $11 credit covers

When you create a free Click2Call account, we automatically load it with $11 of credit. This credit is designed to let you test the system fully before committing.

The $11 is exactly enough to:

- **Activate one local regional landline number** (02, 03, 07, or 08) which costs $10 per month.

- **Make a handful of test outbound calls** using the remaining $1 credit.

Because inbound calls are completely free, this setup gives you the full 7 days to add a number, set up an auto-attendant, register a softphone or desk phone, and test receiving calls without spending a cent.

**Note on 1300/1800 numbers:** National 1300 and 1800 numbers cost more than local numbers and are not covered by the $11 trial credit. If you wish to test a 1300 number, you will need to add a credit card and top up your account balance.

### What to do during your 7 days

To get the most out of your trial, we recommend following these steps:

- **Add a number:** Go to Account → Numbers and add a local number.

- **Set up a device:** Download our softphone app or register a SIP desk phone.

- **Test inbound calls:** Call your new Click2Call number from your mobile to ensure it rings your device.

- **Test outbound calls:** Use your remaining $1 credit to make a few short test calls to your mobile.

- **Explore features:** Set up a voicemail greeting, create a ring group, or build an auto-attendant menu.

### What happens after the trial?

At the end of the 7 days, or when your $11 credit runs out (whichever comes first), your outbound calling will be suspended until you add a payment method and top up your account.

#### Building your setup after the trial

The $10 Inbound Business Number you activated during the trial is ideal for **receiving inbound calls**. Many businesses keep it exactly as it is — routing inbound calls to an auto-attendant, applying after-hours rules, or directing callers to the right team. There is no need to change it.

For staff who need to make outbound calls, simply add one or more **Cloud PBX User** plans ($25/month each) to your account. Each Cloud PBX User includes 300 outbound minutes per month to standard Australian numbers and can be assigned their own extension. Your $10 inbound number continues to sit alongside these users, handling all incoming calls.

For example, a small business might keep the $10 number for inbound calls and add two Cloud PBX Users for two staff members who make outbound calls — a total of $60/month for a fully functional phone system.

To get started, simply log in to the portal, add a credit card, and add the plans you need under the Subscriptions tab.

### What to do next

Ready to keep it? Here’s what to do before your 7 days are up.

[#### Add a card and credit

Outbound calls stop at day 7, or sooner if the $11 runs out](https://www.click2call.com.au/help/how-to-add-account-credit)
[#### Keep your existing number

Bring it across for $100 inc GST. It keeps working until it moves.](https://www.click2call.com.au/help/how-to-port-number)
[#### Add your team

$25 a user a month ex GST, each with their own number and 300 outbound minutes](https://www.click2call.com.au/help/how-to-add-user)
[#### Have us set it up

Managed setup from $300 ex GST for up to 3 users, done in 1–2 business days](https://www.click2call.com.au/contact/)

## Making Your First Call

Source: https://www.click2call.com.au/help/how-to-make-your-first-call

Getting Started
5 min read

## How to Make Your First Call

Before you can make an outbound call with Click2Call, you need two things: a **phone number** on your account (so you have a caller ID to display) and a **registered device** to dial from. This guide walks you through both steps and covers all three ways to make calls — softphone app, SIP desk phone, or diverting to your mobile.

Last reviewed: August 2026

Your 7-day trial includes $11 credit and 10 test calls

New accounts are loaded with $11 credit automatically — enough to make your first test calls without adding a payment method. Outbound calls to Australian mobiles and landlines are charged at standard per-minute rates.

### What you need before making a call

1

#### A phone number

A local Australian number (02, 03, 07, or 08) or a 1300 number on your account. This is your outbound caller ID — what the person you call will see on their screen.

2

#### A registered device

A softphone app on your phone or computer, a SIP desk phone, or a mobile divert. You cannot make outbound calls without at least one registered device or divert.

1

### Add a phone number to your account

If you have not added a number yet, log in to the portal and navigate to **Account → Numbers**. Click **Add a new Number**, select **Australia** as the country, choose your city (area code), select **Voice** as the line type, and choose a plan. Numbers cost $10/month ex GST.

For a full walkthrough of every field, see the [Adding a Phone Number](https://www.click2call.com.au/help/how-to-add-phone-number) guide.

2

### Choose how you will make calls

Click2Call supports three ways to make and receive calls. Choose the option that best suits your setup — you can use more than one at the same time.

#### Option A — Softphone app

Recommended

A softphone app turns your smartphone or computer into a business phone. Calls go over your internet connection — no extra hardware needed. Click2Call recommends the **Secure VoIP App** for iPhone, Android, and Windows, and the **Telephone App** for Mac.

In the portal, go to **Apps** in the top navigation to find your download links and SIP credentials. For a full setup walkthrough, see the [Setting Up a Softphone App](https://www.click2call.com.au/help/how-to-set-up-softphone) guide.

#### Option B — SIP desk phone

A SIP-compatible desk phone (such as a Yealink, Grandstream, or Cisco) connects directly to your internet router and registers with Click2Call using your SIP credentials. You configure the phone via its built-in web interface by entering your SIP server, username, and password.

For a full step-by-step walkthrough including SIP server details, see the [Registering a SIP Desk Phone](https://www.click2call.com.au/help/how-to-add-desk-phone) guide.

#### Option C — Divert to mobile

If you do not want to install an app or configure a desk phone, you can divert inbound calls to your existing mobile number. Inbound calls to your Click2Call number will ring your mobile, and you can answer them normally.

**Note:** Diverting to mobile handles inbound calls only. To make outbound calls displaying your Click2Call number as the caller ID, you will need a softphone app or desk phone registered to your account.

To set up a divert, log in to the portal, go to **Extensions → Edit** for your extension, and enter your mobile number in the **Call Forwarding** field. You can also set up a call flow to ring your extension first, then divert to mobile if unanswered.

3

### Confirm your outbound caller ID

Before making your first call, confirm that your outbound caller ID is set correctly. In the portal, navigate to **Voice → Numbers** and check that your number is listed and active. You can also set the outbound caller ID per-extension by going to **Extensions → Edit** and selecting the number from the **Outbound Caller ID** dropdown.

For more detail on caller ID configuration, see the [Setting Your Outbound Caller ID](https://www.click2call.com.au/help/how-to-set-outbound-caller-id) guide.

4

### Make your first call

Open your softphone app or pick up your desk phone. Dial any Australian number — mobile or landline — and press **Call**. Your Click2Call number will appear as the caller ID on the recipient's screen.

#### Dialling format

| Destination | Format to dial | Example |

| Australian landline | 0X XXXX XXXX | 02 9000 0000 |

| Australian mobile | 04XX XXX XXX | 0412 345 678 |

| 1300 / 1800 number | 1300 XXX XXX | 1300 884 879 |

| International | + [country code] [number] | +64 9 000 0000 |

**Tip:** Your trial account includes $11 credit. A call to an Australian mobile costs approximately $0.09/min, so you have around 120 minutes of test calls available. Check your balance at any time in the portal under **Account → Summary**.

### Troubleshooting

The app says “Registration failed” or “Not connected”

Check that you are using your **phone number** (not your account email or account number) as the username. The format should match what is shown in the portal under **Extensions** — for example, 07 4444 1234.

Also confirm you are using your **line password**, not your account login password. You can set or change your line password in the portal under **Voice → Line Manager**: type a new password into the Password box on the number’s row and click **Save Changes**.

My outbound calls show the wrong caller ID

In the portal, go to **Extensions → Edit** for your extension and check the **Outbound Caller ID** dropdown. Make sure it is set to the number you added in Step 1. If the dropdown is empty, the number may not yet be active — check **Voice → Numbers** to confirm it shows a green status.

I can make calls but there is no audio

On mobile, check that the app has been granted **microphone permission**. On iOS, go to **Settings → Privacy → Microphone** and ensure the app is enabled. On Android, go to **Settings → Apps → [App name] → Permissions**.

On desktop, check that the correct audio input and output devices are selected in the app settings. If you are behind a corporate firewall, your IT team may need to open UDP ports 10000–20000 for RTP audio traffic.

My call failed with “Insufficient credit”

Your account balance has run out. Log in to the portal, go to **Account → Payments**, and add credit. We recommend enabling **auto top-up** so your balance is topped up automatically when it falls below a threshold you set. See the [Adding Account Credit](https://www.click2call.com.au/help/how-to-add-account-credit) guide for details.

### What to do next

Calls working? Here’s how to make it your business line.

[#### Ring your mobile when you’re out

Business hours to your mobile, voicemail to email after hours](https://www.click2call.com.au/help/how-to-forward-calls-to-mobile)
[#### Keep your existing number

Bring it across for $100 inc GST. It keeps working until it moves.](https://www.click2call.com.au/help/how-to-port-number)
[#### Add your team

$25 a user a month ex GST, each with their own number and 300 outbound minutes](https://www.click2call.com.au/help/how-to-add-user)
[#### Keep it after the trial

Add a card and credit before day 7 so outbound calls keep working](https://www.click2call.com.au/help/how-to-add-account-credit)

## Adding Credit: Top-ups and Automatic Payments

Source: https://www.click2call.com.au/help/how-to-add-account-credit

Click2Call is prepaid: your monthly charges and calls come out of your account credit. You can top up by hand, or store a card and let it pay automatically.

Last reviewed: October 2026

### Add credit now

- Go to **Account → Payments** and click **Make a One Off Payment**. Your current balance is shown at the top.
- Enter the **Top-up Amount**. The minimum is $10.00.
- Enter your card details. Tick **Save this card for easier payments** if you want to use it for automatic payments later.
- Click **Top up**.

### Store a card

On **Account → Payments**, click **Enter Card Details**, enter your card and click **Save Card**. Card details are processed by our payment provider; Click2Call never stores your card number.

### Automatic payments and automatic top-ups

Once a card is stored, you can turn on either or both:

| Setting | What it does |
| Enable automatic payments | Charges your card at the start of each billing cycle for your known monthly costs: plans, bundles and line charges. It does not cover call charges. |
| Enable automatic top-ups | Adds the Auto Top-up Amount to your credit when your balance runs low, so call charges are covered too. |

Using both together is usually best. Tick the boxes, enter your Auto Top-up Amount, and click **Update**.

### Get an email when credit is low

Under **Notification Settings**, tick **Receive warning email when account credit drops below**, enter an amount, and click **Update**.

### If your credit runs out

Incoming calls keep working. Outgoing calls stop once your balance goes below −$5: anyone who tries to call out hears a message that they cannot make calls. Add credit and outgoing calls start working again automatically.

Your invoices and receipts are under **Account → History**.

**Good to know:** All prices are in Australian dollars. Add credit before you add numbers or channels, because their monthly charges come out of your credit.

## Adding Portal Logins for Your Team

Source: https://www.click2call.com.au/help/how-to-add-portal-logins

, Step by Step

1

#### Open Logins

Go to **Account → Logins**. The table lists every existing login, its access level and whether two-factor authentication is on.

2

#### Add the new login

Under Add a New Login enter the person’s email address (this is also their username) and full name.

3

#### Choose an access level

Pick the level that fits: **Administrator** or **Full Access** for owners; **Billing Access Only** for a bookkeeper; **Console Access Only** or **Console + SMS** for a receptionist; **Records + Reports Access Only** for a manager; **Read Only Access** for anyone who should look but not change anything. There is also Full Access with no Call Costs or Minutes Displayed.

4

#### Set the password and security options

Enter a password of 8+ characters with upper and lower case letters and a number. Optionally enable **Two-factor authentication** (email verification), tick Remember trusted locations to only prompt once per office connection, and tick **Prevent recording deletion** if this person should never be able to delete call recordings. Click **Add Login**.

**Good to know:** To change your own name, password or 2FA, use the account menu in the top-right corner of the portal and choose Manage my login.

## Your Portal Password and Your Phone Passwords

Source: https://www.click2call.com.au/help/account-and-line-passwords

Click2Call uses two kinds of password: the one you log in to the portal with, and a separate password for each phone number and extension, which your apps and desk phones use. Changing one can change the other, so read this before you change your portal password.

Last reviewed: October 2026

### The two kinds of password

| Password | What uses it | Where to change it |
| Portal login | You, signing in at portal.click2call.com.au | Account → Details → Change Password |
| Phone password | Apps, desk phones and PBXs, which log in with the number and this password | Voice → Line Manager (numbers) or Voice → User Extensions (extensions) |

Staff who have their own portal login have their own password too. Manage those under **Account → Logins**.

### Before you change your portal password

On **Account → Details**, the **Change Account Password** section asks where to **apply the password change**. It starts on **Account login and all non-restricted phone number passwords**.

If you leave that selected, your phones get the new password too, and every app and desk phone on the account stops working until you enter the new password on each one.

To change only your portal password, choose **Account login only — do not change phone number passwords**.

Passwords need at least 8 characters, with uppercase and lowercase letters and a number. Allowed symbols are `! @ _ - # ? = * + : ; .`.

### Change one phone’s password

- **A phone number:** go to **Voice → Line Manager**, type the new password in the number’s Password column, and click **Save Changes**.
- **An extension:** go to **Voice → User Extensions**, open the extension, enter a new password (or click **Generate a random password**), and click **Update Extension**.

Then enter the new password in the app or phone that uses that number. The username stays the same: the number exactly as Line Manager shows it.

### Forgot your portal password?

Click **Forgot your password?** on the portal login page.

**Good to know:** If an app suddenly says “wrong username or password”, check whether the portal password was changed recently. The app needs the new phone password.

# Phone Numbers

## Sending and Receiving Faxes by Email (Faxmail)

Source: https://www.click2call.com.au/help/faxmail

Faxmail replaces a fax machine with email. Faxes sent to your number arrive in your inbox as attachments, and you send a fax by emailing a document. There's no fax machine, phone line or paper to manage.

Last reviewed: October 2026

### Getting a fax number

Add a number in the portal and choose **Faxmail** as the line type. See [Adding a phone number](https://www.click2call.com.au/help/how-to-add-phone-number).

If you're porting an existing fax number, contact support once it arrives and we'll convert it to a Faxmail line. The fax line is $10 a month, the same as any other number.

### Receiving faxes

- Go to **Voice → Line Manager** and click your fax number.
- Open **Faxmail Delivery Options**.
- Enter the email addresses that should receive incoming faxes, one per line.
- Save.

### Sending faxes

#### Allow your email address

- Open your fax number and choose **Faxmail Sending Options**.
- Enter each email address allowed to send faxes, one per line.
- Save. Each address can be linked to one fax number.

#### Send a fax

Email the document to the fax number you're sending to:

```
0731234567@fax.click2call.com.au
```

Attach a PDF, JPEG, PostScript or TIFF file. Word documents aren't supported, so save them as PDF first. You'll get an email confirming whether the fax went through, usually within 5 to 10 minutes.

### How reliable is it?

Faxing over the internet uses a standard called T.38, which resends any data lost on the way. Most faxes go through first time, but it isn't quite as reliable as an old copper fax line. If your business can't risk a single failed fax, for example in emergency medical care, keep a traditional fax service.

These can cause failures:

- **Fax machine to fax machine.** Plugging a fax machine into an adaptor skips the email gateway and its retries. Email works best.
- **Colour faxes.** Faxmail is black and white only.
- **Fast fax machines.** Machines that can't slow down to a standard fax speed may fail.
- **Machines in answering-machine mode.** The other end needs to answer as a fax, not a voice call.

### Getting the clearest fax

- Use pure black on a white background. Colours and greys turn into dots.
- Use a plain font like Calibri or Verdana at size 10 or larger.
- Avoid large black areas. They slow the fax and use the other end's toner.
- If you scan pages, use no more than 300 × 300 dpi.
- For TIFF files, make pages 1728 pixels wide and 2200 pixels tall for fine quality, or 1100 tall for standard.

Received faxes can look rough on screen. Zoom a PDF to 150%, or print it, to see the true quality.

## Sending SMS from Your Business Number

Source: https://www.click2call.com.au/help/sending-sms

You can send text messages from the portal, by email, or from your own software. Texts are sent from a shared SMS number, not your own phone number, and can only go to mobiles. Replies come back to you by email, and you can forward them to a mobile.

Last reviewed: October 2026

### Turn on sending first

Sending is off until our support team turns it on. Contact support and ask for SMS to be enabled; we verify your identity before sending is allowed. Until then, the Compose and Groups pages under **SMS** say that sending is not enabled.

### Send from the portal

- Click **SMS** in the top menu.
- Click **Send a new Message**.
- Enter the mobile number and your message, and send.

Sent messages and replies appear under **Messages**. Use **Groups** to send the same text to a list of people.

### Send by email

#### Allow your email address

- Go to **Voice → Line Manager**, click the number to send from, and choose **Other Settings → SMS Messaging**.
- Enter each email address allowed to send texts, one per line.
- Optionally set a passphrase. Put it in the subject of every SMS email. It's removed before the text is sent.
- Save.

#### Send a text

Email the mobile number at the SMS gateway. The subject and body are joined to make the message. Leave the subject blank if you only want the body.

```
To: 0412345678@sms.click2call.com.au
Subject: Hi Sam,
Body: your order is ready to collect.
```

A text holds 160 characters. Anything longer is cut off, so split long messages into several emails. For numbers outside Australia, include the country code.

### Replies

When someone replies, you get an email showing their reply, their number and your original message. Replies go to the email address set for the sending number, or to your account email if none is set.

To change that for the whole account, go to **SMS → Settings**:

- **Disable SMS Reply Emails** stops reply emails.
- **SMS Reply Email Address(es)** sends replies to the addresses you list.
- **SMS Forwarding Number** forwards each reply to a mobile. Each forwarded reply is charged as a text.
- **SMS Webhook Callback URL** sends replies to your own system, with the **SMS API Key**.

For one number only, use the same options on its **Other Settings → SMS Messaging** page.

You can only receive texts that reply to a message you sent.

### Send from your own software

The portal API includes SMS functions to send messages, read replies and manage groups. In the portal, go to **API → SMS Functions** for the details. See also the [Developer API](https://www.click2call.com.au/api/).

### Cost

Each text costs a flat 50c (AUD), billed to your account.

## Adding a Phone Number

Source: https://www.click2call.com.au/help/how-to-add-phone-number

Phone Numbers
5 min read

## How to Add a Phone Number

Add a new Australian phone number to your Click2Call account. Choose between a **Cloud PBX** line (full PBX features including Auto Attendant) or a **Inbound Business Number** line (basic inbound/outbound). Numbers are available in all major Australian cities including Sydney, Melbourne, Brisbane, Perth, Adelaide and more.

Last reviewed: August 2026

Before you begin

- You must be logged in to the Click2Call portal as an account administrator.

- Ensure your account has sufficient credit — a pro-rata charge applies for the current billing period.

- A Inbound Business Number costs **$10/month ex GST**. An Inbound Business Number costs **$10/month ex GST**.

1

### Log in to the Click2Call portal

Go to portal.click2call.com.au and sign in with your administrator email and password.

2

### Navigate to Account → Numbers

From the top navigation bar, click **Account**, then select **Numbers** from the left sidebar. This page shows all your current VOIP numbers and the Add a new Number form at the top.

3

### Select Country: Australia

In the **Select Country** dropdown, choose **Australia**. The **Area** dropdown will appear automatically, showing all available Australian cities.

4

### Select your Area

Choose the city area for your new number. Available areas include **Sydney, Melbourne, Brisbane, Perth, Adelaide, Canberra, Hobart** and more. In this example we are selecting **Sydney** to get a 02 number.

**Area code reference:**

**02** — Sydney / NSW
**03** — Melbourne / VIC
**07** — Brisbane / QLD
**08** — Perth / WA
**08** — Adelaide / SA
**02** — Canberra / ACT

5

### Select Line Type: Voice

Choose the **Line Type** for your number. For a standard inbound/outbound phone number, select **Voice**. Other options include Faxmail, Web Conference, and Microsoft Teams.

6

### Select Line Plan

Choose the billing plan for your number. Two options are available:

| Plan | Monthly Cost | Best for |

| Inbound Business Number | $10+ / month | Inbound-only or basic voice line |

| Inbound Business Number | $10+ / month | Full inbound & outbound PBX line. Required for Auto Attendant (IVR) features. |

**Important:** If you plan to set up an **Auto Attendant (IVR menu)** where callers press 1 for Sales, 2 for Support, etc., you **must** select the **Inbound Business Number** plan. The Inbound Business Number plan does not support Auto Attendant features.

7

### Select your phone number

A list of available numbers for your selected area will appear in the **Select Number** dropdown. Choose the number you want — in this example we are selecting **02 7238 0358** (displayed as 61272380358 in international format).

8

### Enter number details and confirm

The **Enter Number Details** section will appear. Fill in the optional fields as needed, then review the monthly cost and click **Add Number to my Account**.

| Field | Required? | Description |

| CLI Name | Optional | The name shown on outbound caller ID (e.g. "Acme Support") |

| Extension Number | Optional | Assign this number directly to an extension |

| Line Password | Optional | SIP authentication password for this line |

| Email Address | Optional | Receive voicemail-to-email notifications for this number |

| Billing Group | Optional | Group this number under a billing category |

9

### Number added successfully

A green confirmation message will appear: "Phone number 61272380358 has been successfully added to your account." Your new number is now active and ready to use.

10

### View your number in Voice → Numbers

Navigate to **Voice → Numbers** to see your new phone number listed under **Phone Numbers**. From here you can assign it to a user, set a CLI name, configure a call flow, or add it to a ring group.

#### ✓ Your number is ready to use

Your new Sydney number **02 7238 0358** is now active. Next steps you might want to take:

- [Set up a call flow](https://www.click2call.com.au/help/how-to-set-up-call-flow) to route inbound calls to the right destination

- [Create a ring group](https://www.click2call.com.au/help/how-to-create-ring-group) to ring multiple extensions simultaneously

- [Add an extension](https://www.click2call.com.au/help/how-to-add-extension) and assign this number to a user

- [Set up voicemail-to-email](https://www.click2call.com.au/help/how-to-set-up-voicemail) for this number

#### Related articles

[How to Port an Existing Number
Transfer your current number to Click2Call](https://www.click2call.com.au/help/how-to-port-number)
[How to Set Up a Call Flow
Route inbound calls to the right destination](https://www.click2call.com.au/help/how-to-set-up-call-flow)
[How to Add an Extension
Create a new user extension in the portal](https://www.click2call.com.au/help/how-to-add-extension)
[How to Create a Ring Group
Ring multiple extensions at the same time](https://www.click2call.com.au/help/how-to-create-ring-group)

## Porting an Existing Number

Source: https://www.click2call.com.au/help/how-to-port-number

Number porting allows you to transfer your existing phone number — including local geographic numbers and Australian mobile numbers — from your current provider to Click2Call. Your number stays the same; only the carrier changes.

### Porting Your Number, Step by Step

**Important Information Before You Start:**

- **Cost:** Porting any number — landline, mobile, 1300 or 1800 — costs a flat $100 including GST.

- **Mobile number porting:** Click2Call can port most Australian mobile numbers. Eligibility depends on your current carrier — contact us to confirm before submitting a request.

- **Timeframe:** The process typically takes 5-10 business days, but can vary depending on your current provider.

- **Required Document:** You MUST supply a copy of your most recent phone bill for the number you wish to port. This is a legal requirement to prove ownership.

1

#### Navigate to the Number Porting Form

Log in to the portal, go to the **Voice** tab, and select **Numbers** from the left-hand menu. On the 'Add a new Number' page, click the **Port an existing number** button.

2

#### Submit Your Port Request Details

For an Australian number, tick This request is for International / Non New Zealand numbers and leave the Current Provider menu as it is. Then fill in your account details with your current provider and the port date you want. The details must exactly match the phone bill from your current provider.

3

#### Add the Numbers to Port

At the bottom of the form, enter the phone number(s) you wish to port. You can add multiple numbers one by one, enter a list of numbers, or upload a CSV file for bulk porting. Once you have added your numbers, click **Continue** to submit the request. Our team will then contact you to obtain a copy of your phone bill.

**What happens after you submit?**

- You will receive email notifications to keep you updated throughout the porting process.

- On the day of the port, your number will be **pre-provisioned** on your account. This gives you time to set up your call flow in advance, so the moment the number is ported it starts working on your call flow.

# Extensions & Users

## Extension Numbers, Calling Groups and Caller Names

Source: https://www.click2call.com.au/help/extension-numbers-and-groups

Every line on your account can have a short extension number and a name. Staff dial the extension instead of the full number, callers can enter it at your auto attendant, and the name shows on the other person's phone.

Last reviewed: October 2026

### Setting extension numbers and names

- Go to **Voice → Line Manager**.
- In each row, set the **extension number** (2 to 5 digits) and the **name**.
- Save at the bottom of the page.
- Restart any desk phones so they show the new names.

If you use an auto attendant, plan your numbers so they're easy to say in the greeting, for example 11 to 19 for sales.

### Calling groups

Each line has a **calling group**. Parking, call pickup, intercom and extension dialling only work between lines in the same calling group. Most small businesses keep everyone in one group. Use separate groups to keep teams or sites apart.

### Billing groups

The **billing group** sorts call costs by team or site in your reports. It doesn't change how calls work.

### Intercom

To let colleagues call a phone and have it answer on speaker, open that line's **Incoming Calls → Caller ID, Call Waiting & Intercom** and tick **Enable Intercom Feature on this line**. Others in the group then dial `*85` plus the extension.

## Adding a New Extension

Source: https://www.click2call.com.au/help/how-to-add-extension

Extensions are the internal numbers used within your phone system. Each user or device typically has its own extension. This guide walks you through adding a new extension in the Click2Call portal, using a real example with step-by-step screenshots.

Last reviewed: August 2026

### Adding an Extension, Step by Step

1

#### Log in to the portal

Navigate to portal.click2call.com.au and sign in with your account credentials. Once logged in, you will land on the **Account Summary** page.

The Voice Numbers page after logging in

2

#### Go to Voice → Numbers

Click **Voice** in the top navigation bar. You will see the **Phone Numbers** and **User Extensions** table, along with three action buttons at the top: **Add Phone Number**, **Add Extension**, and **Add Channels**.

The Voice Numbers page showing the Add Extension button

3

#### Click “Add Extension”

Click the **Add Extension** button. The portal will navigate to the **User Details** page, where you can see all existing extensions and a **New User** entry ready to be configured.

User Details page — click “New User” to open the form

4

#### Click “New User” to open the form

Click **New User** at the top of the list. The **Add a new User** form will appear with all the fields required to set up the extension. The extension number is automatically pre-filled with the next available number (e.g. **102**).

The Add a new User form — extension number is pre-filled automatically

5

#### Fill in the user details

Complete the form fields for the new extension. The key fields are:

| Field | Description | Example |

| User Name * | Full name of the person using this extension | Sarah Mitchell |

| Extension Number * | Internal extension number (auto-filled) | 102 |

| Number Assignment | Choose Extension Only or assign an Inbound Business Number number | Extension Only |

| Display Name | Name shown on outbound caller ID | Sarah Mitchell |

| Email Address | Used for voicemail-to-email delivery | sarah@yourbusiness.com.au |

| PIN Number | 4-digit PIN for voicemail access | 1234 |

| User Role | Optional label for the user’s role | Sales Manager |

| Password * | SIP/portal password — click “Generate” for a secure one | Auto-generated |

Example: form filled in for Sarah Mitchell, Ext. 102, Sales Manager

6

#### Generate a password and click “Add New User”

Click **Generate a random password** to create a secure SIP password automatically — the Password and Confirm Password fields will be filled in. Then click the **Add New User** button to save the extension.

**Important:** Make a note of the generated password before saving — you will need it to register a desk phone or softphone app to this extension. The password is not shown again after the form is submitted.

Password generated — click “Add New User” to create the extension

7

#### Extension created — next steps

Once saved, the new extension will appear in the **User Extensions** list on the Voice Numbers page. The extension is now active and ready to be assigned to a device. Your next steps are:

- Register a desk phone using the extension number and SIP password

- Or install a softphone app (e.g. Zoiper, Bria) and log in with the SIP credentials

- Add the extension to a ring group or call flow to receive inbound calls

## Adding a New User

Source: https://www.click2call.com.au/help/how-to-add-user

This guide explains how to create a new user in the Click2Call portal, configure their access level, and send them their login details. Each user gets their own secure login to the portal, allowing them to manage their own extension, view call recordings, and access features based on the permissions you assign.

### Adding a User, Step by Step

1

#### Navigate to Logins

Log in to the Click2Call portal, click the **Account** tab in the top navigation bar, and then select **Logins** from the left-hand navigation menu. This section lists all existing users on your account.

2

#### Add a New User

Click the **Add New User** button to open the user creation form. The user's email address will serve as their username for logging in to the portal.

Key fields to complete:

- **First Name & Last Name:** The user's full name as it will appear in the portal and on call records.

- **Email Address:** This becomes the user's login username. A welcome email with login instructions is sent to this address.

- **Access Level:** Controls what the user can see and do. Administrator provides full account access including billing and configuration. User restricts access to their own extension and call history only.

- **User Restrictions:** Tick this box to prevent the user from deleting call recordings — useful for compliance and quality assurance purposes.

- **Two-Factor Authentication (2FA):** When enabled, the user must verify each login via a one-time code sent to their email address, adding an extra layer of security.

Once all fields are completed, click the **Add New User** button to save. The new user will appear in the Logins list immediately.

3

#### User Receives Welcome Email

After the user is created, the system automatically sends a welcome email to the address you provided. This email contains a link for the user to set their own password and access the portal for the first time. If the user does not receive the email, ask them to check their spam or junk folder, or use the **Resend Welcome Email** option from the Logins list.

4

#### Assign an Extension (Optional)

Once the user login is created, you can link it to an extension so the user can make and receive calls. Navigate to **Extensions & Users** in the portal, select the relevant extension, and assign the new user's login from the dropdown. This allows the user to log in to a softphone or desk phone using their credentials. See the [Adding a New Extension](https://www.click2call.com.au/help/how-to-add-extension) guide for full details.

### Frequently Asked Questions

How many users can I add to my account?

There is no limit on the number of user logins you can create. You can add as many users as your team requires at no additional cost.

What is the difference between an Administrator and a User?

An **Administrator** has full access to all account settings, including billing, call flows, phone numbers, and all other users' call recordings. A **User** can only access their own extension, their own call history, and any features you have not restricted.

The new user did not receive their welcome email — what should I do?

First, ask the user to check their spam or junk folder. If it is not there, go to **Account > Logins**, find the user, and use the **Resend Welcome Email** option. If the issue persists, verify the email address is correct and contact our support team.

Can I change a user's access level after they have been created?

Yes. Go to **Account > Logins**, click the edit icon next to the user, and update their Access Level. Changes take effect immediately on their next login.

How do I delete a user?

Go to **Account > Logins** and click the delete icon next to the user you wish to remove. Deleting a user does not affect their associated extension or any call recordings — it only removes their portal login access.

## Setting Outbound Caller ID

Source: https://www.click2call.com.au/help/how-to-set-outbound-caller-id

By default, when you make an outbound call from an extension, your main account number is presented to the person you are calling. The **Caller ID and Privacy** settings let you change this on a per-extension basis — presenting a different number from your account, a verified external number, or hiding your number entirely for private calls.

Last reviewed: August 2026

### How to Set Outbound Caller ID, Step by Step

1

#### Log in to the portal

Navigate to portal.click2call.com.au and sign in with your account credentials.

2

#### Open the extension’s Call Flow

Click **Voice** in the top navigation bar, then click on the extension you want to configure. This opens the **Call Flow** page for that extension, which shows the incoming and outgoing call routing diagram.

3

#### Select “Caller ID and Privacy” from the Outgoing Calls menu

On the Call Flow page, click the teal **Incoming Calls** dropdown button. A menu will appear showing both Incoming and Outgoing call options. Under **Outgoing Calls**, select **Caller ID and Privacy**.

The Call Flow dropdown — select Caller ID and Privacy under Outgoing Calls

4

#### Choose your Caller ID type

The **Caller ID and Privacy** page will open. The first setting is a dropdown labelled **Select the type of Caller ID you wish to present on outbound calls**. The available options are:

| Option | What it does |

| Default | Presents the main account number (the default behaviour) |

| Present another phone number from my account | Choose a specific number from your account to display on outbound calls |

| Present a verified off-net number | Present an external number (e.g. a mobile) that has been verified as belonging to you |

| Random from a calling group | Rotate through multiple numbers from a defined calling group on each outbound call |

If you select **Present another phone number from my account**, a second dropdown will appear labelled **On-net Phone number selection**. Choose the number you want to present from the list of numbers on your account.

The Caller ID and Privacy settings page

5

#### Configure additional options

Below the Caller ID type dropdown, there are several additional options you can enable. Each is controlled by a checkbox:

Force Caller ID to be sent on all calls (including diverted calls)

When a call is diverted or forwarded to an external number such as a mobile, the caller ID can sometimes change. Ticking this option ensures your chosen caller ID is always presented, even when calls are diverted.

Enable persistent Call Privacy by hiding your Caller ID when making Outbound calls

Tick this to permanently suppress your number on all outbound calls from this extension. The person you call will see “Private Number” or “No Caller ID” on their screen.

Block Caller ID on an individual call by dialling *67 before the number

Enables the ***67** star code. Dial *67 followed by the number to hide your caller ID for that single call only, without changing the persistent setting. You can optionally require a confirmation prompt before the call connects.

Allow Caller ID on an individual call by dialling *65 before the number

Enables the ***65** star code. Useful when persistent privacy is enabled but you want to reveal your number for one specific call. Dial *65 followed by the number to show your caller ID for that call only.

**Microsoft Teams Users:** If this extension is assigned to a Microsoft Teams user, enter their Teams user details in the field at the bottom of the page. This is only required for Teams-enabled lines.

6

#### Verify an external number (optional)

If you want to present a mobile number or a number from another provider as your outbound caller ID, you first need to verify that the number belongs to you. Click the blue **“Click here if you wish to verify a new external Caller ID for your account”** button at the bottom of the page. The portal will guide you through the verification process, which typically involves receiving a call or SMS to confirm ownership.

Once verified, the number will appear in the **Verified Off-net number selection** dropdown and can be selected as your outbound caller ID.

7

#### Save your settings

Once you have configured your preferred options, click the **refresh / save** icon at the top right of the Caller ID and Privacy page to save your changes. The settings take effect immediately on the next outbound call made from this extension.

**Note:** You can only present numbers that belong to your Click2Call account, or external numbers that have been verified. You cannot present an arbitrary number that is not associated with your account.

### Frequently Asked Questions

What is outbound caller ID?

Outbound caller ID is the phone number that appears on the screen of the person you are calling. By default, Click2Call presents your account’s main number. You can change this per extension to show a different number from your account, or hide your number entirely.

Can I present a different number on outbound calls?

Yes. Select **Present another phone number from my account** and choose the number from the On-net Phone number selection dropdown. You can only present numbers that belong to your Click2Call account.

Can I make my number private or anonymous?

Yes. Tick **Enable persistent Call Privacy by hiding your Caller ID when making Outbound calls**. This suppresses your number on all outbound calls from that extension. You can also use ***67** before a number to hide your caller ID on a single call without changing the persistent setting.

What does “Force Caller ID on diverted calls” mean?

When a call is diverted or forwarded to an external number (such as a mobile), the caller ID can sometimes change. Ticking this option forces your chosen caller ID to be presented even on diverted calls, ensuring the caller always sees your business number.

What are the *67 and *65 star codes?

Dialling ***67** before a number hides your caller ID for that single call. Dialling ***65** before a number shows your caller ID for that single call — useful if persistent privacy is enabled but you want to reveal your number for one specific call. Both star codes must be enabled in the settings before they can be used.

What is a Verified Off-net number?

A Verified Off-net number is an external number — such as a mobile or a number from another provider — that has been verified as belonging to you. Once verified, you can present it as your outbound caller ID. Click the blue verification button at the bottom of the Caller ID and Privacy page to begin the verification process.

Can I set a different caller ID for each extension?

Yes. Each extension has its own independent Caller ID and Privacy settings. For example, your sales team could present the main business number while your support team presents a dedicated support line. Navigate to each extension’s Call Flow separately to configure them individually.

Does this setting affect incoming calls?

No. The Caller ID and Privacy settings only affect outbound calls made from this extension. Incoming call routing is configured separately in the **Incoming Calls** section of the Call Flow.

## Setting Up Global Contacts and Speed Dials

Source: https://www.click2call.com.au/help/how-to-set-up-speed-dials

The **Global Contacts** feature allows you to save names and numbers to your Click2Call account. Once saved, these contact names will automatically display on your phone screen when they call you. You can also assign a speed dial code to each contact, allowing you to call them quickly by dialling ** followed by their speed dial number from any phone on your account.

Last reviewed: August 2026

### Setting Up Speed Dials, Step by Step

1

#### Log in to the portal

Navigate to portal.click2call.com.au and sign in with your account credentials.

2

#### Navigate to Global Contacts

Click **Voice** in the top navigation bar, then select **External Contacts** from the left-hand menu. This will open the **Global Contacts and Speed Dials** page.

The Global Contacts and Speed Dials page

3

#### Add a contact manually

To add a single contact, use the form at the bottom of the contacts list. Enter the **Contact Name**, their **Contact Phone Number**, and an optional **Speed Dial** code (e.g., 123). Click the green **Add** button to save the contact.

**Tip:** Once a contact is saved, their name will automatically appear on your phone screen when they call you. To call them using their speed dial code, dial ****** followed by the code (e.g., **123).

4

#### Import contacts via CSV (optional)

If you have a large list of contacts, you can import them all at once using a CSV file. Scroll down to the **CSV Import** section.

The CSV Import section

Your CSV file must have exactly 3 columns with no header row: **Name**, **Number**, and **Speed Dial** (optional). You can import up to 1,000 entries per file. Click **Choose file** to select your CSV, then click the blue **Upload File** button.

5

#### Manage your contacts

You can search for existing contacts using the search bar above the contacts list. If you need to clear your entire contact list, scroll to the bottom of the page and click the red **Delete All Contacts** button. This action cannot be undone.

### Frequently Asked Questions

What is a Global Contact?

A Global Contact is a saved name and phone number that applies to your entire Click2Call account. When a saved contact calls any number on your account, their name will be displayed on the phone screen instead of just their phone number.

How do I use a speed dial code?

To call a contact using their speed dial code, pick up any phone on your account and dial ****** followed by the speed dial number you assigned to them. For example, if you assigned the speed dial code 123 to a contact, you would dial **123 to call them.

What format should my CSV file be in?

Your CSV file must have exactly 3 columns with no header row. The columns must be in this order: **Name**, **Number**, and **Speed Dial**. The Speed Dial column is optional, but the column itself must exist in the file. You can import up to 1,000 entries per file.

Can I delete all my contacts at once?

Yes. Scroll to the bottom of the Global Contacts and Speed Dials page and click the red **Delete All Contacts** button. Please note that this action is permanent and cannot be undone.

# Phones & Devices

## Call Quality: Codecs, Your Connection and Starlink

Source: https://www.click2call.com.au/help/call-quality-and-starlink

Most call quality problems come from the internet connection, not the phone service. This guide covers the settings that affect quality, what your connection needs, and using Click2Call over Starlink.

Last reviewed: October 2026

### What your connection needs

Each call uses about 100 kbps each way. More important than speed is a steady connection: low delay, no dropouts and no other traffic swamping the line. If calls break up when someone uploads large files or joins a video meeting, your router may need quality-of-service (QoS) settings that put voice first.

### Codecs

A codec is how your phone compresses the voice. Click2Call supports:

| Codec | Quality |
| G.722 | Best (HD voice) |
| G.711 A-law and µ-law | Excellent |
| G.729 | Good, uses less bandwidth |

Use a packet time (ptime) of 20 ms. 10 ms isn't supported. Phones set up through the portal already use the right settings.

To change this, open the number and choose **Other Settings → Voice Quality & Codecs**. Under **Select your voice quality preferences**, you can prefer excellent quality (more bandwidth) or good quality (less bandwidth). On a slow or busy connection, choose **Prefer good quality calls with low bandwidth requirements**. The codec tick boxes below are for advanced users, and most people should leave them alone. Restart your phone after changing anything here.

### Using Click2Call over Starlink

Click2Call works over Starlink like any other internet connection. Starlink has a little more delay than fibre, but calls are normally clear.

- To plug in a desk phone or adaptor, you'll need Starlink's Ethernet adapter. A Wi-Fi phone or the Secure VoIP app needs nothing extra.
- Use TLS on your phones. It avoids problems caused by router features that interfere with calls.
- Expect short dropouts during heavy weather or when the dish's view is blocked.

You can keep your existing number. See [Porting your number](https://www.click2call.com.au/help/how-to-port-number).

### Choppy or one-way audio?

See [Fixing one-way audio and dropped registrations](https://www.click2call.com.au/help/sip-alg-one-way-audio).

## Which Phones Can I Use? (And Alarm Systems)

Source: https://www.click2call.com.au/help/which-phones-can-i-use

Click2Call works with IP desk phones, the Secure VoIP app on your mobile or computer, and ordinary analogue phones through an adaptor. Back-to-base alarm systems are the one thing we don't recommend connecting.

Last reviewed: October 2026

### IP desk phones

Any standard SIP phone works. The portal sets up these brands for you automatically:

| Brand | Guide |
| Yealink | Adding a desk phone |
| Grandstream | Grandstream desk phones |
| Polycom | Polycom VVX phones |
| Fanvil | Fanvil phones |
| Panasonic | Panasonic SIP phones |
| Alcatel-Lucent | Alcatel-Lucent phones |
| FlyingVoice | FlyingVoice phones |
| Cisco SPA | Cisco SPA phones |

### Your mobile or computer

The free Secure VoIP app turns your phone or PC into a business line. See [Setting up the Secure VoIP app](https://www.click2call.com.au/help/how-to-set-up-softphone).

### An existing analogue phone or fax

Ordinary phones plug into an analogue telephone adaptor (ATA), such as a [Grandstream HT801 or HT802](https://www.click2call.com.au/help/grandstream-ht801-ht802) or a [Yeastar TA](https://www.click2call.com.au/help/yeastar-ta-adaptors).

### Alarm systems

We don't recommend running a monitored alarm over any internet phone service, including Click2Call. Alarm diallers send tones that internet calls can't always carry reliably. Ask your alarm company about an IP or 4G alarm communicator instead.

## Protecting Your Account from Toll Fraud

Source: https://www.click2call.com.au/help/toll-fraud-protection

Toll fraud is when someone breaks into a phone account and uses it to make expensive overseas calls. It's the biggest security risk for any internet phone service, and a few simple settings stop almost all of it.

Last reviewed: October 2026

### How it happens

Attackers scan the internet for phones and phone systems with weak passwords or open ports. Once in, they call premium numbers in high-cost countries, often overnight or at the weekend, when nobody is watching.

### How Click2Call protects you

Click2Call runs its own fraud detection on every account:

- Calls to high-risk overseas destinations are watched in real time. An unusual call, such as one in the middle of the night to a country you've never called, is ended and further attempts are blocked.
- Hourly and daily spending limits catch sudden jumps in call costs.
- Connections that keep guessing passwords, or that come from known hacking tools, are blocked automatically.

Sometimes a staff member misdials an international prefix and the system blocks it as a precaution. If that happens, contact support and we'll unblock the account once we've spoken with you. If your account was blocked for suspected fraud, change your line passwords before we turn calling back on.

These checks limit the damage, but they can't replace securing your own phones. The steps below stop most attacks before they start.

### Five steps to protect your account

- **Use strong line passwords.** Each line password in **Voice → Line Manager** should be long and random. Never use simple passwords like 1234 or the phone number.
- **Don't forward ports to your phones.** Click2Call works behind your router without port forwarding. Opening ports exposes your phones to the internet.
- **Use TLS.** It encrypts your phone's sign-in details. See [SIP settings for desk phones, adapters and PBX systems](https://www.click2call.com.au/help/sip-settings-for-devices-and-pbx).
- **Restrict overseas calls.** If you don't call overseas, open each number, choose **Outgoing Calls → Call Barring**, tick **Enable the call Barring feature for this line** and tick **Block all All Overseas Calls**. If only some staff do, require a PIN. See [PIN codes and call assignment](https://www.click2call.com.au/help/outgoing-call-pin-and-call-assignment).
- **Lock your account to your office.** If your phones always connect from the same fixed IP address, add it to the **Access Control List** in your profile under **Voice → Profiles** (one address or subnet per line), so connections from anywhere else are refused.

### Using your own PBX

Prefer a registered SIP trunk to IP peering. If you do use peering, only allow SIP traffic from Click2Call's addresses through your firewall. See [Connecting your own PBX with a SIP trunk](https://www.click2call.com.au/help/sip-trunk-pbx-setup).

### Protect your portal login

Turn on two-factor login so a stolen password isn't enough. See [Two-factor login](https://www.click2call.com.au/help/two-factor-login).

### If you think you've been hacked

Change every line password, check **Reports** for calls you don't recognise, and contact support straight away.

## Setting Up Zoiper

Source: https://www.click2call.com.au/help/zoiper-setup

Zoiper is a free SIP softphone for Windows, Mac, Linux, iPhone and Android. It works with Click2Call as a standard SIP app. Click2Call recommends its own Secure VoIP app, but Zoiper is a good alternative if you already use it.

Last reviewed: October 2026

### What you need

From **Voice → Line Manager**, note the number (or the extension's Login) and its line password. See [Setting up a softphone and fixing registration problems](https://www.click2call.com.au/help/softphone-setup-and-troubleshooting) if you're not sure where these are.

### Zoiper on a computer

Open **Preferences → Accounts**, add a SIP account and enter:

| Setting | What to enter |
| Domain | sip.click2call.com.au |
| Username | Your number as shown in Line Manager, e.g. 61370500989 |
| Password | The line password |
| Caller ID name | Your name or business name |
| Auth. username | Leave blank, or the same as the username |
| Outbound proxy | Leave blank |

Save. The account shows as registered within a few seconds.

### Zoiper on iPhone or Android

- Install Zoiper from the App Store or Google Play.
- Open **Settings → Accounts** and tap **Add account**.
- Answer **Yes** to "Do you already have an account?", then choose **Manual configuration** and **SIP**.
- Set **Account name** to Click2Call, **Host** to sip.click2call.com.au, and enter your **Username** and **Password**.
- Under **Network settings → Transport type**, choose **TLS**.
- Go back. A green tick means the account is ready.

### Not registering?

Check the username has no + or leading 0, and that you've used the line password, not your portal login. If TLS won't connect, try TCP. Then see [Fixing one-way audio and dropped registrations](https://www.click2call.com.au/help/sip-alg-one-way-audio).

## Setting Up Bria Teams

Source: https://www.click2call.com.au/help/bria-teams-setup

Bria Teams is a paid softphone from CounterPath that lets an administrator set up calling for the whole team from one web dashboard. It connects to Click2Call as a standard SIP service.

Last reviewed: October 2026

### Step 1: add Click2Call as a voice service

- Log in to the Bria Teams dashboard at teams.softphone.com.
- Go to **Voice and Video** and click **Add Voice Configuration**.
- Choose **Configure SIP Settings** and enter:

| Setting | What to enter |
| Service label | Click2Call |
| Domain | sip.click2call.com.au |
| Port | Auto (or 5061 for TLS) |
| Register with domain and receive calls | Ticked |
| Transport | TLS |

- Click **Save and Close**.

### Step 2: give each team member their line

- Go to **Team Members** and edit a user.
- Enter their **SIP username** (the number or extension Login from **Voice → Line Manager**) and their **SIP password** (that line's password).
- Save. Repeat for each person.

The settings reach each person's Bria app the next time it signs in.

## Transferring Calls in the Secure VoIP App

Source: https://www.click2call.com.au/help/secure-voip-app-transfers

You can pass a call to a colleague from the Secure VoIP app in two ways. A blind transfer sends the call straight through. An attended transfer lets you speak to your colleague first, so you can check they're free before handing over.

Last reviewed: October 2026

### On iPhone or Android

The Secure VoIP mobile app supports both blind and attended transfers from the in-call screen. During a call, open the in-call options and choose transfer. Then pick the number or the other call you want to hand over to.

If you can't find the option, use the keypad codes in the next section. They work in any app or phone.

### On Windows (Micro Edition)

#### Blind transfer

- During the call, click the **Call Transfer** icon.
- Enter the number and click **OK**.

#### Attended transfer

First make sure **Single Call Mode** is turned off in **Settings**.

- Click **Hold** to put the first call on hold.
- Call your colleague.
- When you're ready, click **Transfer → Attended Transfer** and choose the other call.

### Transferring from any phone

During an incoming call, open the keypad and dial `#0` then the number for an attended transfer, or `##` then the number for a blind transfer. These work in every app and desk phone because Click2Call handles them, not the app. See [Parking, picking up and transferring calls](https://www.click2call.com.au/help/call-parking-pickup-transfers).

## Secure VoIP on Windows: Clean Reinstall, Default Calling App and Linux

Source: https://www.click2call.com.au/help/secure-voip-windows-tips

This guide covers three things for the Secure VoIP Micro Edition app on Windows. You can reinstall it cleanly, make it open when you click a phone number, and run it on Linux.

Last reviewed: October 2026

### Clean reinstall

Uninstalling the app keeps your settings, so a fresh install picks up where you left off. If the app misbehaves after an update, remove its saved data as well:

- Quit the app. Check Task Manager to make sure it isn't still running.
- Open **Settings → Apps**, find Secure VoIP and click **Uninstall**.
- In File Explorer, open **View** and turn on **Hidden items**.
- Go to C:\Users\your name\AppData. Look in the Local and Roaming folders for the app's folder, usually named after the app (for example SecureVOIP), and delete it.
- Reinstall from the link in [Setting up the Secure VoIP app](https://www.click2call.com.au/help/how-to-set-up-softphone) and log in again.

### Make phone links open Secure VoIP

- Open **Settings → Apps → Default apps**.
- Search for **TEL**, click it and choose Secure VoIP.
- Do the same for **CALLTO**.

Phone numbers on web pages and in email now open in Secure VoIP when clicked.

### Running it on Linux (not tested by Click2Call)

The Windows app can run on Linux using Wine.

- Install Wine. On Debian or Ubuntu, run the command below. For other systems, see winehq.org.
- Download the Micro Edition installer from the softphone guide.
- Open the installer with Wine, then log in with your number and line password.

```
sudo apt install wine64
```

If you'd rather use a native Linux app, Linphone works too. See [Setting up Linphone](https://www.click2call.com.au/help/how-to-set-up-linphone).

## Secure VoIP on Android: Fixing Missed Calls and Battery Saving

Source: https://www.click2call.com.au/help/secure-voip-android-background-mode

Android phones save battery by putting apps to sleep. The Secure VoIP app is woken by a push notification when a call comes in, but some phones' battery savers block that, so calls are missed while the app is closed. A few settings fix it.

Last reviewed: October 2026

### Signs of the problem

Calls ring when the app is open, but are missed or go to voicemail when the phone is locked or the app has been closed for a while.

### Let the app run in the background

- Open your phone's **Settings → Apps → Secure VoIP**.
- Open **Battery** and choose **Unrestricted** (on some phones, **Don't optimise** or **Allow background activity**).
- Check **Notifications** are allowed for the app.
- On Samsung, Xiaomi, Oppo and Huawei phones, also remove the app from any "sleeping apps" or battery-saver list.

If the app has its own background or keep-alive setting in its settings, turn it on as well.

### Test it

Close the app, lock your phone, and call your number from another phone. If it rings, you're set. If it doesn't, check the settings above again, or set a [ring group](https://www.click2call.com.au/help/how-to-create-ring-group) so calls also ring your mobile number directly.

## Busy Lamp Field (BLF): Watching Lines, Queues and Voicemail

Source: https://www.click2call.com.au/help/busy-lamp-field-blf

A BLF key is a button on a desk phone with a light that shows what another line is doing. Green means free, red means on a call, and flashing red means ringing, so you can press it to pick the call up. BLF keys can also watch call queues and voicemail boxes.

Last reviewed: October 2026

| Light | Meaning |
| Green | Free. Press to call. |
| Solid red | On a call, or on do not disturb |
| Flashing red | Ringing. Press to answer it. |

### Watching a colleague's line

- In the portal, open the line you want to watch and choose **Other Settings → Line Monitoring**. Tick **Enable Monitoring for the Line** and save.
- In **Voice → Phones**, edit the phone that will do the watching. Set a spare key to **BLF** and choose the line. See [Programming phone keys](https://www.click2call.com.au/help/programming-phone-keys).
- Save and restart the phone.

If you set up phones by hand, set the key type to BLF and the value to the full number or the extension's Login, not the short extension number.

### Watching a voicemail box

A mailbox key flashes red when there are new messages. Press it to listen.

With a phone set up through the portal, choose **Mailbox Monitoring** as the key type and pick the mailbox. The portal turns on monitoring for that mailbox for you.

By hand, open the number's **Voicemail** settings and tick **Enable mailbox monitoring through SUBSCRIBE events**. Then set a BLF key with `VM` after the number, for example 61370500989VM.

### Watching a call queue

Open the queue's settings and tick **Support BLF monitoring and call pickup directly from the queue**. The queue must use the Ring All strategy. A BLF key for the queue flashes when callers are waiting, and pressing it answers the longest-waiting caller.

### Do not disturb

Lines on do not disturb show solid red. See [Do not disturb and call screening](https://www.click2call.com.au/help/do-not-disturb-and-call-screening).

### Not lighting up?

Wait a minute, or restart the phone to make it ask for the status again.

## Hot Desking: Logging In to Any Phone

Source: https://www.click2call.com.au/help/hot-desking

Hot desking lets anyone log in to a shared desk phone with their own extension using a short code. The phone reloads with their number and keys, then goes back to its usual number when they log out.

Last reviewed: October 2026

### Before you start

Hot desking only works on phones set up through **Voice → Phones**. Each hot desk phone needs its own default number or extension, which it uses when nobody is logged in.

### Setting up a hot desk phone

- In **Voice → Phones**, add or edit the phone.
- Turn on **Hot Desk Facility**.
- Optionally, add keys for hot desk log in and log out so people can use one button.
- Save.

### Logging in

- Dial `*45` on the hot desk phone.
- Enter your extension (for example 12) or your full number, then press #.
- If your extension has a PIN, enter it and press #.

The phone reloads with your settings in 10 to 20 seconds. Some models restart to do this, which takes a little longer. You can also dial `*45` followed by your extension in one go.

Logging in on one phone logs you out of any other hot desk phone.

### Logging out

Dial `*46`. The phone goes back to its default number. To log yourself out of a phone you've left, dial `*46` followed by your extension from any phone.

If you hear a connection error, the phone isn't set up as a hot desk phone. Check step 2.

## Different Ringtones for Internal Calls (Yealink and Grandstream)

Source: https://www.click2call.com.au/help/distinctive-ring-internal-calls

You can make your desk phones ring differently when a colleague calls, so you know it's an internal call before you answer. Click2Call tags internal calls with a word you choose, and the phone plays a different ringtone when it sees that word.

Last reviewed: October 2026

### Step 1: tag internal calls in the portal

- Go to **Voice → Line Manager** and click the number or extension.
- From the **Incoming Calls** menu, choose **Caller ID, Call Waiting & Intercom**.
- In **Distinctive Ring Identifier**, enter a word such as `Internal`.
- Save. Repeat for each number or extension that should hear the different ring.

By default the tag is only added to internal calls. Tick **Apply Distinctive Ring to ALL calls** only if you want every call to use it.

### Step 2: choose the ringtone on a Yealink phone

The easiest way is through the portal, so the setting survives a factory reset. Edit the phone in **Voice → Phones** and add these lines to **Custom Configuration**:

```
distinctive_ring_tones.alert_info.1.text = Internal
distinctive_ring_tones.alert_info.1.ringer = Resource:Ring5.wav
```

Change Ring5.wav to the ringtone you want, save, and restart the phone. You can also set it by hand in the phone's web page under **Settings → Ring**.

### Step 2: choose the ringtone on a Grandstream phone

Edit the phone in **Voice → Phones** and add these lines to **Custom Configuration** for account 1:

```
<P1488>Internal</P1488>
<P1489>7</P1489>
```

P1488 is the word to match and P1489 is the ringtone number from the phone's list (7 means the seventh ringtone). Save and restart the phone. By hand, it's under **Accounts → Call Settings → Matching Rule** in the phone's web page.

For other accounts on the same phone, use these setting numbers:

| Account | Word to match | Ringtone |
| 1 | P1488 | P1489 |
| 2 | P1494 | P1495 |
| 3 | P1500 | P1501 |
| 4 | P1506 | P1507 |
| 5 | P1512 | P1513 |
| 6 | P1518 | P1519 |

### Other phones

Most SIP phones can pick a ringtone from the Alert-Info header. If you're not sure where the setting is on yours, contact support and we'll check for you.

## Setting Up Fanvil Phones

Source: https://www.click2call.com.au/help/fanvil-phones

Click2Call sets up Fanvil desk phones for you. Add the phone in the portal, point it at our provisioning server once, and it downloads your numbers and keys automatically.

Last reviewed: October 2026

### Step 1: connect the phone

Plug the handset cord into the port with the phone icon. Plug the network cable into the port marked Internet (or LAN) and into your router or switch. If your phone doesn't use a power adaptor, it needs a PoE switch. The phone shows a welcome screen once it has started.

### Step 2: add the phone in the portal

- Go to **Voice → Phones** and click **Add a new phone**.
- Choose **Fanvil** as the manufacturer, then your model as the **Phone Type**.
- Enter the **MAC address** from the sticker on the back of the phone.
- Enter a description so you can recognise the phone. A VLAN ID is optional.
- Under **Account 1**, choose the phone number for the first line. Add more accounts if your model has more lines.
- Set up any line keys you want (speed dials, voicemail, pickup, BLF). See [Programming phone keys](https://www.click2call.com.au/help/programming-phone-keys).
- Save the phone. Keep the page open: it shows the provisioning settings and your **Configuration File Encryption Key** for the next step.

### Step 3: enter the provisioning settings on the phone

#### Log in

On the phone, press **Menu → Status** and note the **IPv4** address. Enter that address in a browser on the same network and log in as **admin** (default password admin).

#### Set the upgrade server

Open the **Upgrade** tab, set the upgrade server to `fanvil.securevoip.nz` and click **Apply**.

#### Set auto provisioning

Open the **Auto Provision** tab and enter:

| Setting | What to enter |
| Configuration File Encryption Key | The key shown in the portal for your account |
| Static Provisioning Server | fanvil.securevoip.nz |
| Config File Name | $mac.xml |
| Protocol Type | HTTP |
| Update Mode | Update after reboot |

Click **Apply**. When the page reloads, click **Autoprovision Now**, then restart the phone. It registers when it comes back up.

### Making changes later

Edit the phone in **Voice → Phones**, save, then restart the phone to pick up the changes.

## Setting Up Panasonic SIP Phones

Source: https://www.click2call.com.au/help/panasonic-sip-phones

Click2Call auto-provisions Panasonic SIP phones, including the KX-HDV, KX-UT, KX-TGP, KX-TPA and KX-HGT ranges. Panasonic's KX-NT phones only work with Panasonic phone systems, so they can't be used with Click2Call.

Last reviewed: October 2026

### Step 1: open the phone's web interface

Web access is off by default on Panasonic phones. On the phone, press **Menu** and go to **System Settings → Network Settings → Embedded Web**, change it to **On** and press OK.

Then find the phone's address: **Menu → System Settings → Status → IPv4 Settings → IP Address**. Enter it in a browser on the same network, for example http://192.168.1.123. Log in as **admin** with the default password **adminpass**.

### Step 2: factory reset the phone

Open the **Maintenance** tab, choose **Reset to Defaults**, click **Reset to Carrier Defaults** and confirm. The phone restarts with its settings wiped. Repeat step 1 to log back in.

### Step 3: add the phone in the portal

- Go to **Voice → Phones** and click **Add a new phone**.
- Choose **Panasonic** and then your model as the **Phone Type**.
- Enter the phone's **MAC address**. It's on the back of the phone, or under **Status → Network Status** in the web interface.
- Choose the numbers for each account and set up any line keys. See [Programming phone keys](https://www.click2call.com.au/help/programming-phone-keys).
- Save the phone.

Copy the **Standard File URL** shown under Phone Type. It looks like https://panasonic.securevoip.nz/{MAC}-xxxxxxxx.cfg. The long part at the end is a private key for your account, so don't share it.

### Step 4: enter the URL on the phone

In the phone's web interface, open **Maintenance → Provisioning Maintenance**. Paste the address into **Standard File URL**, replacing anything already there. You can leave the Product File and Master File URL fields as they are. Click **Save** and check the save is confirmed.

### Step 5: restart and wait

Go to **Maintenance → Restart**, click **Restart** and confirm. The phone downloads its settings after it restarts. This can take several minutes, even after the phone looks ready.

### Model not listed?

Contact support with your model number and we'll check whether it can be added.

## Setting Up Alcatel-Lucent Enterprise H and M Series Phones

Source: https://www.click2call.com.au/help/alcatel-lucent-phones

Click2Call auto-provisions Alcatel-Lucent Enterprise H3, H6, M3, M5, M7 and M8 phones. Provisioning keeps the firmware up to date and sets up your lines, line keys and phonebook. The phone must be on the latest firmware, which provisioning installs for you on the first run.

Last reviewed: October 2026

### Step 1: find the phone's address and MAC

On the phone's keypad menu, open **Network Status** to find its IP address. Enter it in a browser and log in as **admin** (default password 123456). Copy the **MAC address** from **Status → Network**.

### Step 2: add the phone in the portal

- Go to **Voice → Phones** and click **Add a new phone**.
- Choose **Alcatel-Lucent** and your model (for example H3G) as the **Phone Type**.
- Paste the MAC address, choose the numbers for each line and set up any line keys. See [Programming phone keys](https://www.click2call.com.au/help/programming-phone-keys).
- Save the phone.

### Step 3: point the phone at the provisioning server

In the phone's web interface, open **Provision → Auto Provision**. Enter `http://al.securevoip.nz` in the **DM URL** field and click **Submit**. Then click **Auto Provision Now**.

If the phone needs new firmware, it upgrades and restarts. Wait for it to finish.

### Step 4: provision securely

Log back in and open **Auto Provision** again. The address should now read https://al.securevoip.nz. Click **Auto Provision Now** once more. After a couple of minutes the phone is set up and ready.

The phone's admin password changes to the one set in the portal after provisioning.

## Setting Up FlyingVoice Phones

Source: https://www.click2call.com.au/help/flyingvoice-phones

Click2Call auto-provisions several FlyingVoice phones. Add the phone in the portal, enter a few provisioning settings on the phone, and it downloads your numbers and keys.

Last reviewed: October 2026

### Step 1: add the phone in the portal

- Go to **Voice → Phones** and click **Add a new phone**.
- Choose **FlyingVoice** and your model as the **Phone Type**.
- Enter the **MAC address** from the back of the phone or the sticker on its box.
- Choose the numbers for each account and set up any line keys. See [Programming phone keys](https://www.click2call.com.au/help/programming-phone-keys).
- Save the phone.

### Step 2: enter the provisioning settings on the phone

Log in to the phone's web interface as **admin** (default password admin). Open **Administration → Provision** and set:

| Setting | What to enter |
| Provision Enable | Enable |
| Option 66 | Disable |
| Option 67 | Disable |
| Config File Name | $(MA) |
| Profile Rule | https://flyingvoice.securevoip.nz/ |
| Enable Upgrade | Enable |
| Upgrade Rule | https://flyingvoice.securevoip.nz/ |

Click **Save & Apply**. If the phone doesn't pick up its settings, turn it off and on again.

### Not provisioning?

Older firmware can't use the secure provisioning certificate. Update the phone to the latest firmware from flyingvoice.com first. Or set the **Upgrade Rule** to `http://flyingvoice.securevoip.nz` (without the s) to download our latest firmware, then change it back to https.

If your model isn't listed in the portal, contact support with the model number.

## Setting Up Yeastar TA Analogue Adaptors

Source: https://www.click2call.com.au/help/yeastar-ta-adaptors

The Yeastar TA100, TA200, TA400 and TA800 connect ordinary analogue phones to Click2Call. The portal builds the adaptor's settings for you, so you only enter the server address and a key.

Last reviewed: October 2026

### Step 1: add the adaptor in the portal

- Go to **Voice → Phones** and click **Add a new phone**.
- Choose **Yeastar** and your model as the **Phone Type**.
- Enter the **MAC address** from the label on the back of the unit.
- Enter a description, an admin password for the adaptor, and whether you want call waiting.
- Choose the number for each phone port and save.
- Copy the **AES Key** shown on the page. You need it in step 4.

### Step 2: reset and connect the adaptor

If the adaptor has been used before, log in and choose **System → Reset and Reboot → Reset to Factory Defaults**. Connect it to your network and power, and plug a phone into the phone port.

### Step 3: find the adaptor's address

Pick up the phone and dial `***1`. The adaptor reads out its IP address. Enter that address in a browser on the same network and log in as **admin** (default password password).

### Step 4: enter the provisioning settings

Open the **System** page and scroll to **Auto Provision Settings**:

| Setting | What to enter |
| Provisioning Method | Server URL |
| Server URL | http://yeastar.securevoip.nz |
| AES Key | The key you copied from the portal |

Click **Save**, then **Apply Settings**, then restart the adaptor. It downloads its settings, updates its firmware if needed, and your numbers register. Make a test call each way.

## Setting Up Gigaset Cordless IP Phones

Source: https://www.click2call.com.au/help/gigaset-ip-phones

Gigaset IP cordless phones aren't in the portal's auto-provisioning list, so you set them up by hand in the base station's web page. It takes about five minutes per handset.

Last reviewed: October 2026

### Before you start

In **Voice → Line Manager**, note the number and set a line password for it. See [SIP settings for devices and PBX](https://www.click2call.com.au/help/sip-settings-for-devices-and-pbx) if you need help.

### Step 1: find the base station's address

On the handset, press the control button on the right, open **Settings** (the spanner icon) and choose **Registration**. Note the IP address shown. Enter it in a browser on the same network, for example http://192.168.2.2. Log in with the default PIN **0000**.

### Step 2: add your number

Go to **Settings → Telephony → Connections** and click **Edit** on the connection you want to use. Enter:

| Setting | What to enter |
| Authentication Name | Your number as shown in Line Manager, e.g. 61370500989 |
| Authentication Password | The line password from Line Manager |
| User Name | Same as the authentication name |
| Domain | sip.click2call.com.au |
| Proxy Server Port | 5060 (or 50600 if 5060 is blocked) |
| Registration Server | sip.click2call.com.au |
| Registration Refresh Time | 180 seconds |

Click **Set** to save. Gigaset bases are slow to show the status. Allow 30 seconds for it to change to Registered.

### Still not registering?

Check the line password and number first. Then see [SIP ALG and one-way audio](https://www.click2call.com.au/help/sip-alg-one-way-audio).

## Setting Up the Phone Port on a FRITZ!Box

Source: https://www.click2call.com.au/help/fritzbox-phone-port

Many FRITZ!Box routers have a built-in phone port. You can register a Click2Call number on it and plug an ordinary analogue phone straight in. This guide covers the phone settings only.

Last reviewed: October 2026

### Before you start

In **Voice → Line Manager**, note the number and set a line password for it. If the FRITZ!Box screens misbehave in Chrome, try another browser.

### Step 1: log in

Connect to the FRITZ!Box network and open http://192.168.178.1 (or http://fritz.box). Log in with the FRITZ!Box password.

### Step 2: add a telephone number

Go to **Telephony → Telephone Numbers**. Delete any number you aren't using. Click **New Telephone Number**, choose **IP-based Line**, and click **Next**. Enter:

| Setting | What to enter |
| Telephony Provider | Other Provider |
| Telephone number for registration | Your number as shown in Line Manager, e.g. 61370500989 |
| Internal telephone number | The same number |
| User name | The same number |
| Authentication name | The same number |
| Password | The line password from Line Manager |
| Registrar | sip.click2call.com.au |
| Proxy server | sip.click2call.com.au |
| DTMF transmission | RTP/AVP |
| Use telephone number for registration | Ticked |
| Connect via | IPv4 only |
| Country code and area code prefixing | None for both |

Click **Next** twice. The FRITZ!Box tests the connection, and a green light appears next to the number when it registers.

### Step 3: test

Plug your phone into phone port 1 (FON 1). Call a landline and a mobile, then call your number to check incoming calls.

### Star codes on a FRITZ!Box

The FRITZ!Box uses star codes of its own. To use a Click2Call code, put `*#` in front. For example, dial `*#*55` for voicemail. See [Star codes](https://www.click2call.com.au/help/star-codes).

## Programming Phone Keys (BLF, Speed Dial, Pickup and More)

Source: https://www.click2call.com.au/help/programming-phone-keys

When you add a desk phone under Voice → Phones, you can also decide what each programmable key on the phone does — a second line, a busy lamp for a colleague, a speed dial, call pickup and more. The settings are pushed to the phone automatically, so you never touch the phone's own menus.

Last reviewed: October 2026

### Which phones does this work for?

Any phone added under **Voice → Phones** — Alcatel-Lucent, Cisco, Fanvil, FlyingVoice, Grandstream, Panasonic, Polycom, Yealink and Yeastar models. The portal lists every supported model when you choose the manufacturer.

### Step 1: choose which numbers the phone uses (Accounts)

In the **Accounts** section, pick a number or extension for **Account 1**. Add more under Account 2, 3 and so on if the phone should handle several numbers. Each account is a separate line the phone can make and receive calls on.

### Step 2: set up each key (DSS Keys)

Below the accounts is the **DSS Keys** section, with one row per key (Key 01, Key 02 and so on). For each key choose the **type**, the **account** it belongs to, then either pick a **Number** from the list or type one under **or value**, and add a **Label** to show on the phone's screen.

| Key type | What it does |
| Phone Line | Another line appearance for one of the phone's accounts |
| BLF | Lights up when a colleague's line is busy or ringing. Press it to call them, or to pick up their ringing call |
| Speed Dial | Calls a saved number with one press |
| Mailbox Monitoring | Lights up when a voicemail box has new messages |
| Voice Mail | Opens your voicemail |
| Pickup / Group Pickup | Answers a call ringing on another phone, or anywhere in your pickup group |
| Call Park | Parks the current call so someone else can pick it up |
| Intercom | Calls a colleague's phone, which answers on speaker |
| Conference / Transfer / Hold / Forward | One-press call controls |
| Do not Disturb | Turns DND on and off |
| Start Manual Recording / Pause Recording / Resume Recording | Controls recording on the current call |
| Hot Desk Login / Hot Desk Logout | Signs a user in or out of a shared phone |
| Multicast Paging | Broadcasts an announcement to a group of phones |
| DTMF | Sends a set of keypad digits during a call |

### Step 3: save and push it to the phone

Click **Add Phone** (or save the phone's settings if you're editing it). To apply changes straight away, tick **Send a reboot request to the handset to force a provisioning update**. Otherwise the phone picks them up at its next scheduled check, which you can set with **Reboot request to phone** (never, daily, weekly or monthly at 2 am).

### Other handy settings on the same page

- **Transport** — leave on **TLS (recommended)**.
- **Web Admin Password / Web User Password** — set your own; they default to admin and user if left blank.
- **Call Waiting** and **Call Waiting Tones** — whether a second call can come in while you're on one.
- **DSS Key Transfer Mode** — what the phone does when you press a BLF key during a call: blind transfer, attended transfer, or a new call.
- **Remote Phonebook** — shows your internal extensions and external contacts in the phone's directory. Tip: a line or extension with "Virtual" in its name won't appear in the phonebook.
- **Hot Desk Facility** — lets different people log in to the same phone.

## Setting Up Grandstream Desk Phones

Source: https://www.click2call.com.au/help/grandstream-desk-phones

Click2Call can set up most Grandstream desk, cordless and conference phones for you — GRP, GXP, GXV, GHP, DP and WP models. You add the phone in the portal, point the phone at Click2Call's provisioning server, and it configures itself.

Last reviewed: October 2026

### Step 1: add the phone in the portal

#### Open the Phones page

Log in to the portal and go to **Voice → Phones → Add a new phone**.

#### Choose the model

Set **Phone Manufacturer** to **Grandstream** and pick your model under **Phone Type**.

#### Fill in the details

Enter the phone's **MAC Address** (on a sticker on the back of the phone or on its box), a **Description** so you can recognise it, and choose the number for **Account 1**. Leave **Transport** on **TLS (recommended)**. Set up any extra keys — see [Programming Phone Keys](https://www.click2call.com.au/help/programming-phone-keys). Click **Add Phone**.

### Step 2: point the phone at Click2Call

#### Find the phone's IP address

On the phone, open the menu and look under **Status** or **Network** for its IP address.

#### Log in to the phone

On a computer on the same network, type that IP address into a browser and log in as **admin** (the default password is admin, or the one printed on the phone). Use Firefox, Edge or Safari — some GXP firmware won't let Chrome log in.

#### Set the provisioning server

Go to **Maintenance → Upgrade and Provisioning**:

- **Config Upgrade Via:** HTTPS, **Config Server Path:** gs.securevoip.nz
- **Firmware Upgrade Via:** HTTPS, **Firmware Server Path:** gs.securevoip.nz
- **Allow DHCP Option 43 and Option 66 to Override Server:** No

The portal shows the same server address on the phone's settings page, so you can copy it from there.

#### Provision

Save, then click **Provision** at the top of the page. The phone downloads its settings and any firmware it needs. A firmware update can take several minutes and several restarts — don't unplug it.

### Older GXP phones that won't provision

Older GXP phones need up-to-date firmware before they can provision, and the update has to be done in stages. Check the current firmware on the phone's **Status** page, then go to **Maintenance → Upgrade and Provisioning**, set **Firmware Upgrade via** to **HTTP** (not HTTPS) and use the path for your version:

| Firmware below 1.0.7 | gs.securevoip.nz/107 |
| Firmware 1.0.7 | gs.securevoip.nz/108 |
| Firmware 1.0.8 | gs.securevoip.nz/109 |
| Firmware 1.0.9 | gs.securevoip.nz |

Save and restart after each step, and repeat until the phone is on the latest firmware (1.0.11 or later). Then set **Firmware Upgrade via** back to **HTTPS** and follow Step 2 above.

## Connecting an Analogue Phone or Fax with a Grandstream HT801 / HT802

Source: https://www.click2call.com.au/help/grandstream-ht801-ht802

A Grandstream HT801 or HT802 (an analogue telephone adaptor, or ATA) lets you plug an ordinary home or office phone — or a fax machine — into Click2Call. Click2Call configures the adaptor for you.

Last reviewed: October 2026

### Step 1: add the adaptor in the portal

Go to **Voice → Phones → Add a new phone** and set:

- **Phone Manufacturer:** Grandstream
- **Phone Type:** Grandstream HT801 (one phone port) or HT802 (two ports) — or your HT81x model
- **MAC Address:** from the sticker on the bottom of the adaptor
- **Description:** a name you'll recognise, e.g. Reception fax
- **Account 1** (and **Account 2** on an HT802): the number for each phone port
- **Call Waiting:** Disabled if a fax machine is connected

Click **Add Phone**.

### Step 2: find the adaptor's IP address

If the adaptor has been used before, factory-reset it first: hold the **Reset** button on the back for about 10 seconds with a paperclip. Plug a phone into the **Phone** port and the adaptor into your router. Lift the handset and dial `***02` — a voice reads out the adaptor's IP address.

### Step 3: log in and set the provisioning server

On a computer on the same network, enter the IP address in a browser and log in as **admin** (default password admin, or the password printed on the bottom of the adaptor). Go to the **Upgrade** section:

- **Firmware** tab: Firmware Upgrade via **HTTPS**, Firmware Server Path **gs.securevoip.nz**
- **Config File** tab: Config Upgrade via **HTTPS**, Config Server Path **gs.securevoip.nz**
- **Provision** tab: untick **Allow DHCP Option 43 or 66 or 160 to Override Server**

On older HT801/HT802 firmware the same settings are under **Advanced Settings** instead of separate tabs.

### Step 4: save and restart

Click **Save and Apply**, then **Reboot** if the adaptor doesn't restart by itself. It downloads its settings from Click2Call and the phone port is ready to use. Lift the handset and check for dial tone, then make a test call.

## Setting Up Polycom VVX Phones

Source: https://www.click2call.com.au/help/polycom-vvx-phones

Click2Call can set up Polycom VVX phones (VVX 101 to VVX 601) for you. Add the phone in the portal, point it at Click2Call's provisioning server, and it configures itself.

Last reviewed: October 2026

### Step 1: add the phone in the portal

Go to **Voice → Phones → Add a new phone**, set **Phone Manufacturer** to **Polycom**, pick your VVX model, and enter the **MAC Address** (on the back of the phone, on the box, or in the phone's menu under Network settings), a **Description** and the number for **Account 1**. Set up any extra keys (see [Programming Phone Keys](https://www.click2call.com.au/help/programming-phone-keys)) and click **Add Phone**.

### Step 2: factory-reset the phone (recommended)

Start from factory settings so old configuration can't interfere. In the phone's web interface (Step 3 explains how to log in), go to **Utilities → Global Settings** and click **Restore**.

### Step 3: log in to the phone's web interface

#### Find the IP address

Press **Home → Settings → Status → Network → TCP/IP Parameters**. The address is next to **IPv4 Addr**.

#### Change the admin password if asked

After a reset the phone may not let you log in with the default password 456. On the phone, go to **Settings → Advanced**, enter 456, then **Administration Settings → Change Admin Password** and set a new one.

#### Log in

On a computer on the same network, enter the IP address in a browser and log in as **Admin** with that password.

### Step 4: set the provisioning server

Go to **Settings → Provisioning Server** and set:

- **Server Type:** HTTPS
- **Server Address:** polycom.securevoip.nz

Click **Save**. The phone downloads its settings from Click2Call and restarts.

### Old firmware

Phones on firmware 3.3 or older can't use web provisioning. Update the firmware first under **Utilities → Software Upgrade → Check for Update**; some older models need two updates to reach version 4.1.1 or later.

### Handset volume

Polycom phones normally reset the handset volume after every call. Phones set up through Click2Call keep the volume you choose.

## Cisco SPA Phones and SPA112 / SPA122 Adapters

Source: https://www.click2call.com.au/help/cisco-spa-phones

Older Cisco SPA phones (SPA301 to SPA525G) and the SPA112 and SPA122 phone adaptors still work with Click2Call, and the portal can configure them for you. Cisco no longer updates these devices, so read the security note before you start.

Last reviewed: October 2026

### Before you start: security

Cisco stopped releasing updates for the SPA range years ago, and they have known security weaknesses. Keep them behind your router — never make them reachable from the internet, and don't forward ports to them. If you're buying new equipment, choose a supported model instead, such as a Grandstream HT801 or HT802 adaptor ([Connecting an Analogue Phone or Fax with a Grandstream HT801 / HT802](https://www.click2call.com.au/help/grandstream-ht801-ht802)).

### Step 1: add the device in the portal

Go to **Voice → Phones → Add a new phone**, set **Phone Manufacturer** to **Cisco**, pick your model, and enter the **MAC Address** (on the back of the device, in the phone's menu, or in its web interface), a **Description** and the number for **Account 1**.

On SPA phones, every account you want active needs its own **Phone Line** key. Use spare keys for BLF, speed dials and so on (see [Programming Phone Keys](https://www.click2call.com.au/help/programming-phone-keys)). Click **Add Phone**.

### Step 2: copy your Profile Rule

The phone's settings page in the portal shows **Provision Enable: Yes** and a **Profile Rule** — a web address starting http://cisco.securevoip.nz/ followed by a long code. The code is unique to your account and protects your configuration, so copy it from the portal rather than typing it.

### Step 3: factory-reset the device

On a phone, use the menu key and scroll to **Factory Reset**. On an SPA112/122 adaptor, use the reset option in its web interface.

### Step 4: enter the Profile Rule on the device

#### Log in

Find the IP address — on SPA504G: menu option 9, **Network → Current IP**; on SPA525G: **Settings → Status → Network Status**; on an SPA112/122, plug in a phone and dial `****` then `110#`. Enter the address in a browser and log in as **admin** (default password admin). Choose **admin** / **advanced** to see all settings.

#### Set provisioning

Open **Voice → Provisioning** and set:

- **Provision Enable:** Yes
- **Profile Rule:** the address you copied from the portal
- **Resync Periodic:** 60 (makes the first update quicker; Click2Call sets it back to an hour afterwards)

Click **Submit All Changes**. The device downloads its settings within about a minute — restart it if it doesn't.

### Adaptors set up manually, without the portal

If an SPA112 or SPA122 was configured by hand, it needs a certificate before it can use TLS, because its built-in certificate list is out of date. Under **Voice → Provisioning → CA Settings**, set **Custom CA URL** to http://www.securevoip.nz/sip.securevoip.nz-rootca-2023.pem, save and restart. Devices set up through the portal don't need this.

## Connecting Your Own PBX with a SIP Trunk

Source: https://www.click2call.com.au/help/sip-trunk-pbx-setup

If you already have a PBX — 3CX, FreePBX, Asterisk or another SIP-capable system — you can keep it and use Click2Call for your phone numbers and calls. One registration from your PBX carries every number on the account. This guide sets that up.

Last reviewed: October 2026

### Which connection type should I use?

Connection types are set on the **Voice → Profiles** page, in the **Connection Type** list.

- **Registered SIP Trunk** — your PBX logs in once, with one of your numbers (the pilot number), and every other number on the profile is delivered over that login. Right for most PBXs.
- **SIP Peering (Direct IP)** — no login: Click2Call and your PBX trust each other by IP address. Needs a static public IP. Suits larger installations that route many numbers.
- **IAX2 Registration** — for Asterisk-based systems that prefer the IAX2 protocol.

If you're not sure, use **Registered SIP Trunk**.

### How do I set up a Registered SIP Trunk?

#### 1. Decide whether to use the Default profile or a new one

Every number on the Default profile will route to your PBX once you change it. If some numbers should stay on Click2Call's apps and phones, click **Create New Profile** and set up the trunk on the new profile instead.

#### 2. Set the connection type

On **Voice → Profiles**, set **Connection Type** to **Registered SIP Trunk** and choose your **pilot number** — usually your main number. This is the number your PBX will log in with.

#### 3. Save the profile

Click **Save 'Default' Profile** (or save the new profile). If you created a new profile, go to **Voice → Line Manager** and choose that profile in the **Profile** column for each number that should go to the PBX.

#### 4. Set a line password on the pilot number

In **Voice → Line Manager**, type a password into the Password box on the pilot number's row and click **Save Changes**. This is the password your PBX uses — not your portal login.

#### 5. Register your PBX

Create a SIP trunk on your PBX with:

- Username / authentication ID: the pilot number exactly as shown in Line Manager, e.g. 61370500989
- Password: the line password from step 4
- Registrar / proxy: sip.click2call.com.au
- Port: 5060 (UDP or TCP), 50600 as an alternative, or 5061 for TLS

#### 6. Check it's online

In **Voice → Line Manager** the pilot number's status turns online, and the line page shows **Last Registered** with your PBX's IP address. Make a test call in and out.

### How are my other numbers delivered?

Every number on the profile now behaves as a direct-dial (DDI) number. Calls arrive over the trunk with the dialled number in the SIP request, so your PBX can route each number to the right extension, queue or menu. Numbers you add to the account later are routed to the trunk automatically.

### Caller ID from your PBX

Over a Registered SIP Trunk, your PBX can present any number on your Click2Call account as the caller ID — set it per extension or per route in the PBX. You don't need to register each number separately.

### Limiting simultaneous calls

The **Limit Channels** setting on the profile caps how many calls the trunk can carry at once (No limit, 1 or 2 channels). Leave it on **No limit** unless you want a cap.

### What does a SIP trunk cost?

Changing the connection type does **not** change your billing. To get SIP trunk pricing, change the pilot number's line plan to **SIP Trunk** yourself in **Account → Plan → Line Plans**. The SIP Trunk plan is $50 per month ex GST and includes 500 outbound minutes, unlimited inbound calls and unlimited simultaneous calls. If you're unsure which plan your other numbers should be on, contact support and we'll check for you.

### Troubleshooting

If the PBX won't register, or calls connect with no audio, see [SIP Settings for Desk Phones, Adapters and PBX Systems](https://www.click2call.com.au/help/sip-settings-for-devices-and-pbx) and [Fixing One-Way Audio and Dropped Registrations](https://www.click2call.com.au/help/sip-alg-one-way-audio). Don't forward ports 5060 or 5061 to your PBX — see [Stopping Ghost and Spam Calls](https://www.click2call.com.au/help/ghost-and-spam-calls).

## Connecting Asterisk or FreePBX (PJSIP)

Source: https://www.click2call.com.au/help/asterisk-freepbx-pjsip

Asterisk and systems built on it (FreePBX, Issabel and similar) connect to Click2Call as a Registered SIP Trunk using the PJSIP channel driver. Set up the trunk in the portal first — see [Connecting Your Own PBX with a SIP Trunk](https://www.click2call.com.au/help/sip-trunk-pbx-setup) — then add the configuration below.

Last reviewed: October 2026

### Before you start

You need your pilot number exactly as shown in **Voice → Line Manager** (e.g. 61370500989) and the line password set on that row. In the examples, replace PILOTNUMBER and LINEPASSWORD with yours.

### Example: pjsip.conf over UDP

```
[transport-udp]
type=transport
protocol=udp
bind=0.0.0.0

[click2call-reg]
type=registration
outbound_auth=click2call-auth
server_uri=sip:sip.click2call.com.au
client_uri=sip:PILOTNUMBER@sip.click2call.com.au
retry_interval=60

[click2call-auth]
type=auth
auth_type=userpass
username=PILOTNUMBER
password=LINEPASSWORD

[click2call]
type=aor
contact=sip:sip.click2call.com.au:5060

[click2call]
type=endpoint
context=from-external
disallow=all
allow=g722,alaw,ulaw
outbound_auth=click2call-auth
aors=click2call
from_user=PILOTNUMBER

[click2call]
type=identify
endpoint=click2call
match=sip.click2call.com.au
```

### Example: pjsip.conf over TLS (recommended)

Use a TLS transport and port 5061. Everything else is the same as the UDP example.

```
[transport-tls]
type=transport
protocol=tls
bind=0.0.0.0:5061
method=tlsv1_2

[click2call]
type=aor
contact=sip:sip.click2call.com.au:5061;transport=tls
```

### FreePBX

In FreePBX, go to **Connectivity → Trunks → Add Trunk → Add SIP (chan_pjsip) Trunk** and enter the same values: username and authentication username = pilot number, secret = line password, SIP server = sip.click2call.com.au, port 5060 (or 5061 with TLS), registration = Send. Codecs: G.722, then G.711 A-law, then G.711 µ-law. Set your inbound routes against the DDI numbers.

### Notes

- Use a packet time (ptime) of 20 ms; 10 ms isn't supported.
- Keypad tones: use RFC 2833 (the PJSIP default, `dtmf_mode=rfc4733`).
- To present a different number on your account as caller ID, set it in the outbound route or with `CALLERID(num)` in the dialplan.
- Click2Call also supports IAX2 Registration for Asterisk; choose it under **Voice → Profiles** if you prefer IAX2 to SIP.

## Connecting 3CX

Source: https://www.click2call.com.au/help/3cx-sip-trunk

3CX connects to Click2Call as a Registered SIP Trunk. These steps are for 3CX version 20 and later.

Last reviewed: October 2026

### Step 1: set up the trunk in the Click2Call portal

#### Use a separate profile if some numbers should stay on Click2Call

On **Voice → Profiles**, numbers on the Default profile will all route to 3CX once you change it. If any should stay on Click2Call's apps or phones, click **Create New Profile** and use that for 3CX.

#### Set the connection type and number format

Set **Connection Type** to **Registered SIP Trunk** and choose your pilot number (usually your main number). Set the number format to **+E.164 Format (+CountryCode Number)** — 3CX v20 expects numbers like +61370500989. Save the profile.

#### Set the pilot number's line password

In **Voice → Line Manager**, type a password into the Password box on the pilot number's row and click **Save Changes**.

### Step 2: add the trunk in 3CX

#### 1. Open trunk settings

Log in to the 3CX admin console and go to **Voice & Chat → Add Trunk**.

#### 2. Choose a provider template

3CX v20 doesn't offer a generic trunk. Choose **Australia** and any provider template, then replace its server details with Click2Call's in the next step.

#### 3. Enter the trunk details

- Name: anything, e.g. Click2Call
- Main Trunk Number: your pilot number in +E.164, e.g. +61370500989
- Authentication ID (SIP User ID): the pilot number exactly as shown in Line Manager, without the + (e.g. 61370500989)
- Authentication Password: the line password from Line Manager
- Registrar / Server: sip.click2call.com.au, port 5060

#### 4. Add your other numbers

On the **DIDs** tab, add each of your other Click2Call numbers in +E.164 format (e.g. +61370500990). Route them to extensions as you normally would in 3CX.

#### 5. Set codec priority

On the **Options** tab, put **G.722** first, then **G.711 A-law**, then **G.711 U-law**.

#### 6. Pass the original caller ID on forwarded calls (recommended)

Still on **Options**, open **Caller ID Control** and set the **P-Asserted-Identity Display Name** to **OriginatorCallerID**, so forwarded calls show the original caller's number.

#### 7. Save and check

Click **Save**, wait a few seconds and refresh **Voice & Chat**. A green icon next to the trunk means it has registered. Make a test call in and out.

### If the trunk won't register

Check the Authentication ID has no + and matches Line Manager exactly, and that the password is the line password, not your portal login. For network problems see [Fixing One-Way Audio and Dropped Registrations](https://www.click2call.com.au/help/sip-alg-one-way-audio).

## SIP Settings for Desk Phones, Adapters and PBX Systems

Source: https://www.click2call.com.au/help/sip-settings-for-devices-and-pbx

Any SIP-compatible desk phone, analogue adapter or PBX can connect to Click2Call. Use the settings below for any device we don't have a step-by-step guide for. The device must support SIP version 2.

Last reviewed: October 2026

### What settings do I enter?

| Setting | What to enter |
| Username / User ID / Login | Your number exactly as shown in Voice → Line Manager, e.g. 61370500989 (no +, no leading 0). For an extension, use its Login from the User Extensions table. |
| Authentication name | Same as the username |
| Password | The line password from the Password box on that number's row in Voice → Line Manager — not your portal login. New numbers have no password until you set one and click Save Changes. |
| SIP server / Proxy / Domain / Registrar | sip.click2call.com.au |
| Outbound proxy | sip.click2call.com.au (or leave blank if your device doesn't need one) |
| Transport | TLS (recommended), TCP or UDP |
| Port | 5060 for UDP or TCP · 50600 as an alternative to 5060 · 5061 for TLS |
| DTMF (keypad tones) | RFC 2833 (sometimes called AVT or out-of-band). SIP INFO also works. |
| Voice codecs | G.722 (best quality), G.711 A-law, G.711 µ-law, G.729 |
| Packet time (ptime) | 20 ms. 10 ms is not supported. |
| STUN server | Not required |

#### Why TLS is recommended

TLS encrypts the call setup between your device and Click2Call. Routers can't read or rewrite encrypted traffic, so TLS avoids the most common cause of one-way audio and failed registrations (a router feature called SIP ALG — see [Fixing One-Way Audio and Dropped Registrations](https://www.click2call.com.au/help/sip-alg-one-way-audio)). If your device can't use TLS, try port 50600 instead of 5060: routers don't recognise it as a SIP port, which has a similar effect.

#### Where the port goes

Most devices take the port on the end of the server address, e.g. sip.click2call.com.au:50600. Some have a separate Port field. Enter Click2Call's port there, not your device's own local SIP port.

### Do I need firewall rules?

Usually not. Click2Call handles devices behind NAT and most firewalls, and you should never need to forward ports 5060 or 5061 to your phone or PBX. If your firewall blocks outbound traffic by default, allow your devices to reach sip.click2call.com.au (103.55.116.140) on the ports above. Call audio uses UDP to the same address.

### Can I encrypt the audio too? (Secure RTP)

TLS encrypts the call setup; Secure RTP (SRTP) encrypts the voice itself. To require it on a line: Voice → Line Manager → click the number → Other Settings → Voice Quality & Codecs → turn on Secure Encrypted RTP → Save. Only do this if your device is set up for SRTP — calls will fail otherwise. The same page lets you force a particular transport or restrict codecs. Leave codecs alone unless you have a reason; the defaults suit nearly everyone.

### Registration, peering or IAX2 — which connection type?

Each line's connection type is set in Voice → Profiles.

- **SIP Registration** (the default): your phone or PBX logs in with the username and password above. Right for almost everyone.
- **SIP Peering (Direct IP)**: your PBX and Click2Call trust each other by IP address instead of a login. Needs a static public IP. Useful for PBXs that route many numbers.
- **IAX2**: for Asterisk-based systems (FreePBX and similar). Uses one port for signalling and audio, which can make firewalls simpler and uses less bandwidth per call.

Not sure which you need? Use SIP Registration.

### Still not registering?

See [Setting Up a Softphone and Fixing Registration Problems](https://www.click2call.com.au/help/softphone-setup-and-troubleshooting) for the checklist, and [Fixing One-Way Audio and Dropped Registrations](https://www.click2call.com.au/help/sip-alg-one-way-audio) if calls connect but audio fails.

## Fixing One-Way Audio and Dropped Registrations (SIP ALG and NAT)

Source: https://www.click2call.com.au/help/sip-alg-one-way-audio

If calls connect but you can't hear the other person (or they can't hear you), if incoming calls ring but go silent when answered, or if your phone keeps dropping its registration, the cause is almost always your router — specifically a feature called SIP ALG. This guide explains the fix.

Last reviewed: October 2026

### What is SIP ALG and why does it cause problems?

SIP ALG (Application Layer Gateway) is a router feature meant to help phone calls get through NAT. There is no standard for it, so many routers rewrite the call setup messages incorrectly. The result is one-way audio, silence on answered calls, or phones that stop registering. It is often intermittent and clears for a while after a router restart, which makes it hard to pin down. Every VoIP provider recommends turning it off.

### Fix 1: switch your phone to TLS (no router access needed)

TLS encrypts the call setup, so the router can't interfere with it. On your phone or PBX set:

- Server / proxy: sip.click2call.com.au
- Transport: TLS
- Port: 5061

If your device doesn't support TLS, use port 50600 instead of 5060 (sip.click2call.com.au:50600). Routers don't treat 50600 as a SIP port, so they leave it alone.

### Fix 2: turn off SIP ALG on your router

Look in your router's settings under Advanced, WAN, NAT, Firewall or VoIP for "SIP ALG", "SIP Helper", "SIP Transformations" or "SIP passthrough", and turn it off. Restart the router and your phones afterwards. The exact steps depend on your router — your router's manual or manufacturer can tell you where the setting is. If you can't change the router, use Fix 1.

### Fix 3: phones that keep dropping registration (NAT timeout)

Some routers forget a phone's connection after a short idle time, so incoming calls can't find it. If your router lets you set a UDP NAT timeout, set it to 60 seconds or more. Otherwise, set the phone's registration expiry (often "Registration Timeout" or "Expires") to 60 seconds so it checks in every minute and keeps the connection open. TLS and TCP also avoid this, because they hold the connection open.

### Don't forward ports to your phone

You don't need port forwarding for Click2Call, and forwarding 5060 or 5061 to a phone or PBX exposes it to internet scanners (see [Stopping Ghost and Spam Calls](https://www.click2call.com.au/help/ghost-and-spam-calls)). Remove any such rules.

## Keypad Presses Not Recognised (DTMF Problems)

Source: https://www.click2call.com.au/help/dtmf-keypad-presses-not-working

If callers press options in your auto attendant and nothing happens, or you can't enter a PIN or menu option when you call a bank or another business, your phone or PBX is probably sending keypad tones (DTMF) the wrong way.

Last reviewed: October 2026

### Which DTMF setting should I use?

Set your phone or PBX's DTMF mode to **RFC 2833** (some devices call it AVT, RTP Event, Telephone Event or out-of-band). It's the standard and works in almost every case. If it still fails, try **SIP INFO**. Avoid **Inband**: it sends the keypad tones as ordinary audio, and on internet calls they get distorted and often aren't recognised — it's the usual cause of the problem.

### Where is the setting?

It's in your phone or PBX, not the Click2Call portal — usually under Account, Line, Codecs or Advanced, labelled "DTMF", "DTMF Type" or "DTMF Mode". On the Click2Call apps it's already set correctly.

### Only some callers have the problem?

If your own phones are fine but certain callers can't use your menu, the problem is at their end. If it affects your auto attendant generally, contact support with a few example call times and we'll check for you.

## Setting Up a Softphone and Fixing Registration Problems

Source: https://www.click2call.com.au/help/softphone-setup-and-troubleshooting

If your softphone won't log in, or calls stop arriving when the app is closed, this guide covers the fix. It lists the apps that work with Click2Call, shows exactly which credentials to use, explains the iPhone background-calls problem, and how to check whether a line is registering.

Last reviewed: October 2026

The short version

Most registration problems are one of three things: the line has no password set, the app is using the portal login instead of the line password, or the username is not the number exactly as Line Manager shows it. Check those first.

### Which softphones work with Click2Call?

| App | Platforms | Status |

| Secure VoIP | iPhone, Android, Windows | Recommended — setup guide |
| Telephone | Mac | Recommended — setup guide |
| Linphone | iPhone, Android, Windows, Mac | Tested by Click2Call — setup guide |
| Groundwire | iPhone, Android | Not tested — should work as a standard SIP app |
| Other SIP softphones (e.g. Zoiper, MicroSIP) | Various | Not tested — standard SIP apps generally work |

Any standard SIP softphone can usually connect with the same credentials, but Click2Call can only help configure the apps above. If you want someone else to set up a third-party app for you, managed setup is available — see [Pricing](https://www.click2call.com.au/pricing/). Using simPRO? It has its own guide: [Connecting simPRO](https://www.click2call.com.au/help/how-to-connect-simpro).

### Where are my SIP credentials?

Log in to the portal, open **Voice → Line Manager**. Every number is in the Phone Numbers table and every extension in the User Extensions table.

| Field in your app | What to enter |

| Username | The number exactly as Line Manager shows it, e.g. 61370500989 — no +, no leading 0, no spaces. For an extension, use its Login from the User Extensions table, e.g. 832800190001 |
| Password | The line password from the Password box on that row — not your portal login password |
| Domain / SIP server | sip.click2call.com.au |
| Transport | TLS (recommended), TCP or UDP — all three are supported. TCP and UDP use port 5060. If your app won't connect over TLS, switch it to TCP or UDP, then contact support and we'll check for you |
| Authentication ID, outbound proxy | Leave blank |

#### What the password field means
Each number and extension has its own **line password**, separate from the password you use to log in to the portal. New numbers have no password: the box is empty, which is why the app cannot log in. Type any password into the box on that number's row and click **Save Changes** (bottom right). The eye icon under the Password heading shows or hides the saved value. If you change it later, every device using that number must be updated, or it will stop registering.
One set of credentials per device is the safest setup. When two devices log in with the same number, the one that registered last can take the calls.

### Why do calls stop arriving when the app is closed on iPhone?

iOS suspends apps that are not on screen. A phone app can only ring while it is closed or the iPhone is locked if it uses Apple's VoIP push notifications: a push server wakes the app when a call arrives. If push is not working for an app, it rings while open and goes quiet as soon as it is in the background — the exact symptom most people report.
The Secure VoIP app supports background calls on a best-effort basis: it usually rings when it is closed or the iPhone is locked, but iOS does not guarantee it, so some calls may not ring. If you can't afford to miss calls, use one of the options below.

#### What you can do now

- •**Use Linphone on iPhone** — it is the recommended app for receiving calls in the background on iOS. Follow the [Linphone guide](https://www.click2call.com.au/help/how-to-set-up-linphone), allow notifications, and turn on Background App Refresh for it in Settings → General → Background App Refresh.
- •**Don't swipe the app away** — force-quitting an app on iOS stops it receiving calls until you open it again.
- •**Ring your mobile as well** — the most reliable option is to have the number ring your mobile at the same time as the app. See [Ring Your Mobile and Still Get Voicemail](https://www.click2call.com.au/help/call-flow-ring-mobile-then-voicemail).

### How do I check whether a line is registering?

1

#### Look at the app

A registered app shows a green or Registered status, usually on the main screen or in its account settings. An error such as Registration failed or Disconnected means the app could not log in.

2

#### Look at Line Manager

In **Voice → Line Manager**, each line has a status dot. Red means the line is offline or not registered.

3

#### Open the line's page

Click the number. The call-flow diagram shows the registration state (Not Registered, Offline or online), and the status panel shows the **IP Address** and **Last Registered** time. If Last Registered is recent and the IP address is yours, the device is connecting.

4

#### Make a test call both ways

Call the number from another phone, then call out from the app. Registration problems usually stop incoming calls; outgoing problems are often the number format you dialled.

#### Can support see failed registration attempts?
Yes — contact support with the number or extension and the time of a failed attempt, and we'll check for you. Noting the exact time makes it much quicker to trace.

#### What common errors mean

- •**Login refused or authentication failed** — the username or line password is wrong, or no password has been set yet.
- •**Registration failed: Disconnected** — usually the transport or port does not match. Check the transport setting, or switch to TCP or UDP on port 5060.
- •**A chirping or Morse-code-like tone when you dial out** — the number was not dialled in a format the network accepts. Try the full number with the area code.

### Before you contact support: a quick checklist

- •A password is set on the line in Voice → Line Manager, and the app uses that password — not your portal password
- •The username is the number (or extension Login) exactly as Line Manager shows it
- •The domain is sip.click2call.com.au and the transport matches the port
- •No other device is using the same credentials
- •Notifications are allowed for the app, and on iPhone Background App Refresh is on
- •You have tried mobile data instead of Wi-Fi, to rule out the office router
- •You have tried a second app (Linphone) with the same details, to rule out the app
Still stuck? Email support@click2call.com.au with your account number, the number or extension, the app and version, your device and operating system, the time of a failed attempt, and a screenshot of any error. Never send your password.

## Registering a Desk Phone

Source: https://www.click2call.com.au/help/how-to-add-desk-phone

Phones & Devices
4 min read

## Adding & Provisioning a Desk Phone

This guide covers two methods for connecting a physical desk phone to your Click2Call account. If you have a Yealink phone, follow the Auto Provisioning steps below for the fastest setup. For all other brands, skip to the Manual SIP Setup section.

### Option 1 — Yealink Auto Provisioning

Recommended for Yealink phones — fastest setup method

Click2Call has a fully automated Yealink device provisioning process to take the hard work out of configuring these phones. Follow the steps below to get your Yealink phone registered and ready to use in minutes.

1

#### Unbox and assemble the phone

When opening your Yealink phone box, you will find the main phone unit, one handset cord, one handset, one phone stand, and one Ethernet cable. Flip the phone over and attach the stand to the back slots above the cable ports. Connect the larger end of the handset cord into the port marked with a phone icon on the unit, and the smaller end into the handset.

2

#### Connect to your network and power on

Plug one end of the Ethernet cable into the port labelled **Internet** on the back of the phone, and the other end into your internet modem or router. Once connected, the phone will power on and display a welcome message on screen.

3

#### Add the phone in the Click2Call portal

Log in to your Click2Call account and navigate to **Voice > Phones**. Click **Add New Phone** and fill in the following details:

- **Phone model:** select your Yealink model from the drop-down menu

- **MAC address:** found on the sticker on the back of the phone

- **Description:** a label to identify this phone line (e.g. Reception, Sales)

- **VLAN ID:** optional — only required if your network uses VLANs

- **Web admin password:** set a password for the phone's web interface. If left blank, the default will be admin (admin) and user (user)

- **Accounts:** assign a phone number from the drop-down. If your Yealink model has multiple line keys, you can also configure speed dials, voicemail buttons, pickup, and transfer keys on the spare keys

Once complete, click **Add New Phone** to save.

4

#### Find the phone's IP address

On the Yealink phone, press **Menu** and then select **Status**. The field labelled **IPv4 Address** shows the phone's current IP address on your network. Note this down — you will need it in the next step.

5

#### Log in to the phone's web interface

Open a web browser on a computer connected to the same network and type the phone's IP address into the address bar (e.g. http://192.168.1.100). You will be redirected to the Yealink login page. Enter admin for both the username and password fields.

6

#### Trigger Auto Provisioning

Once logged in, go to the **Settings** tab and select **Auto Provision**. In the **Server URL** field, enter:

http://yea.nz

Press **Confirm** at the bottom of the page. Once the page reloads, press **Auto Provision Now**. The phone screen will begin the auto-provisioning process. If a firmware upgrade is required, the phone will display a firmware update message.

7

#### Wait for provisioning to complete

The provisioning process may take up to five minutes. The phone may reboot several times during this period — this is normal. **Do not power off the phone during this process.** Once finished, your Yealink handset will be ready to use. If you need to make any changes in future, update your settings in the Click2Call portal and reboot the phone to download the new configuration.

### Yealink cordless (DECT) phones

Yealink cordless systems are set up the same way as desk phones. In **Voice > Phones**, choose the base station model, such as **W56P**, **W60P/W60B**, **W70B** or **W80DM**, and enter the MAC address of the base, not the handset. Give each handset its own account in the form.

To find the base's IP address, press the button on the front of the base. Its address appears on a registered handset. Then follow steps 5 and 6 above to enter http://yea.nz as the Server URL.

Manual SIP Setup — All Brands

### Option 2 — Manual SIP Setup

For any SIP phone you'd rather set up by hand

### SIP Credentials Reference

Enter these values exactly as shown into your phone's SIP account settings.

| Username / Login / User ID | Your Click2Call phone number including country codee.g. 61234567890 |

| Authorisation Name / Display Name | Your Click2Call phone number including country codee.g. 61234567890 |

| Password | The password saved in the Password box on that number’s row in Voice → Line Manager (new numbers have none by default — type one and click Save Changes) |

| Host / Proxy / Domain | sip.click2call.com.au |

| Outbound Proxy | sip.click2call.com.au |

| SIP Transport | UDP, TCP, or TLS — TLS preferred |

| SIP Port | 5060 or 50600 (UDP/TCP)  •  5061 (TLS) |

| DTMF Mode | RFC 2833 (also listed as AVT or Out-of-Band) |

| STUN Server | Not required |

1

#### Connect the phone to your network

Plug the desk phone into your network using an Ethernet cable. If your switch supports PoE (Power over Ethernet), the phone will power on automatically. Otherwise, connect the included power adapter. Wait for the phone to fully boot before proceeding.

Screenshot placeholder — Step 1

2

#### Access the phone's web interface

Find the phone's IP address — this is usually displayed on the phone screen under **Menu > Status > Network**. Open a web browser on a computer on the same network and navigate to that IP address (e.g. http://192.168.1.100). Log in with the phone's admin credentials (default is often admin / admin — check your phone's manual if this does not work).

Screenshot placeholder — Step 2

3

#### Enter your SIP account settings

Navigate to the **Account** or **SIP Account** section in the phone's web interface. Enter the values from the SIP Credentials Reference table above. The field names vary by brand, but the mapping is consistent:

- **Username / User ID / Account Name:** your phone number including country code (e.g. 61234567890)

- **Authorisation Name / Auth ID:** same as username — your phone number including country code

- **Password:** the password saved in the Password box on the number’s row in Voice → Line Manager (new numbers have none by default — type one and click Save Changes)

- **SIP Server / Host / Domain / Proxy:** sip.click2call.com.au

- **Outbound Proxy:** sip.click2call.com.au

- **SIP Port:** 5060 or 50600 (UDP/TCP), or 5061 (TLS)

- **DTMF Mode:** RFC 2833 (also shown as AVT or Out-of-Band)

- **STUN:** leave blank or disabled — not required

Screenshot placeholder — Step 3

4

#### Configure audio codecs

In the codec or audio settings section, enable the following codecs in order of preference. Disable any codecs not listed below to ensure the best call quality.

| Type | Supported Codecs |

| Voice (Audio) | G.711 alaw  •  G.711 ulaw  •  G.722  •  G.729a |

| Video | H.264  •  H.263 |

**Important:** Set the media packet time (ptime) to **20ms**. A ptime of 10ms is not supported and will cause audio issues.

5

#### Save settings and confirm registration

Save the account settings. The phone will reboot and attempt to register with the Click2Call network. A successful registration is confirmed by a **green line key light**, a **Registered** status on the phone screen, or a dial tone when you pick up the handset. This typically takes 30–60 seconds after saving.

Screenshot placeholder — Step 5

6

#### Test a call

Dial another extension on your system or call your own number from a mobile to confirm the phone is working correctly. Check that audio is clear in both directions. If the phone fails to register, see the Firewall Rules section below and verify your credentials are entered exactly as shown.

Screenshot placeholder — Step 6

### Firewall Rules

If your phone sits behind a business firewall or router, allow the following traffic to ensure SIP registration and audio work correctly.

| Direction | Protocol | Port / Range | Purpose |

| Allow all traffic from | UDP | 1024 – 50000 | RTP media (voice audio) |

| Allow all traffic from | TCP | 5060 | SIP signalling (TCP) |

| Allow all traffic from | TCP | 5061 | SIP signalling (TLS) |

Apply these rules for traffic from subnet 52.63.154.234. No STUN server is required.

## Setting Up a Softphone or Mobile App

Source: https://www.click2call.com.au/help/how-to-set-up-softphone

Phones & Devices
5 min read

## Setting Up a Softphone App

Click2Call recommends the **Secure VoIP App** for iPhone, Android, and Windows users, and the **Telephone App** for Mac users. Both apps are free to download and work with your Click2Call phone number and password. Select your platform below to get started.

Last reviewed: August 2026

To find your app download links, log in to the portal, click the **Account** tab, and select **Apps** from the left-hand menu. From here you can download the app for your device and access the installation instructions for each platform.

Your Click2Call login details (all platforms)

You will need the following details to log in to any of the apps below. Your phone number and password are in the Click2Call portal under **Voice → Line Manager**. Use the number exactly as displayed there. New numbers have no password by default: type any password into the **Password** box on the number’s row and click **Save Changes**, then use that password in the app.

| Field | Value |

| Username / Phone Number | Your Click2Call phone number exactly as shown in the portal under Voice → Line Manager (e.g. 61370500989 — no + and no leading 0) |

| Password | The password saved in the Password box on that number’s row in Voice → Line Manager. New numbers have no password by default — type any password into the box and click Save Changes; the eye icon under the Password heading shows or hides it |

| SIP Domain (Mac only) | sip.click2call.com.au |

iPhone / iPad

Android

Windows

Mac

### Setting Up Secure VoIP on iPhone or iPad

App: **Secure VoIP** — Download from the App Store

1

#### Download the Secure VoIP app

On your iPhone or iPad, open the App Store and search for **Secure VoIP**, or tap the link above to go directly to the download page. Install the app and open it.

2

#### Allow permissions

When the app opens for the first time, you will be prompted to allow access to notifications, photo library, camera, and contacts. Select **Allow** for each of these. Granting all permissions is important to ensure all features of the app work correctly.

3

#### Log in with your Click2Call details

Enter your Click2Call phone number and password (see the credentials table above). Tap **Log In** to continue.

4

#### Allow microphone access

On the main dialler screen, tap the button in the bottom right corner with the three dots. In the pop-up that follows, tap the button with the phone icon on the left. This will place a test call to your voicemail to simulate a phone call. When prompted, select **Allow** for microphone access. All permissions are now granted and the app is ready to use.

### Setting Up Secure VoIP on Android

App: **Secure VoIP** — Download from the Play Store

1

#### Download the Secure VoIP app

On your Android device, open the Play Store and search for **Secure VoIP**, or tap the link above to go directly to the download page. Install the app and open it.

2

#### Allow notifications

When the app opens for the first time, select **Allow** for notifications. This is essential — without notification permission, the app will not be able to wake up to alert you of incoming calls.

3

#### Log in with your Click2Call details

Enter your Click2Call phone number and password (see the credentials table above). Tap **Log In** to continue.

4

#### Make a test call and grant remaining permissions

On the main screen, tap the button in the bottom right corner with the three dots. In the pop-up that follows, tap the button with the phone icon on the left to place a test call to your voicemail. Microphone access may be requested at this point depending on your device — select **Allow**. As you navigate to other parts of the app for the first time (such as the Contacts screen), you will be prompted for additional permissions. Always select **Allow** to ensure all features work correctly.

### Setting Up Secure VoIP Micro Edition on Windows

App: **Secure VoIP Micro Edition** — Download the Windows installer (.exe)

1

#### Download and install the app

Click the download link above to download the installer. Once downloaded, double-click the .exe file to begin installation. If Windows shows a warning about running an unrecognised app, click **More Info** and then **Run anyway** to continue. Select your installer language and click **OK**, then click **Next** and follow the prompts to complete the installation. Click **Finish** to launch the app.

2

#### Log in with your Click2Call details

When the app opens, you will be prompted to enter your username and password. Enter your Click2Call phone number exactly as shown under **Voice → Line Manager** (e.g. 61370500989, no + and no leading 0) as the username and your line password. Do not enter your account number — it must be a phone number. Click **Save** to log in.

3

#### Confirm you are online

If your details are correct, the dialler screen will appear and you will see an **Online** indicator in the bottom left corner of the app. You are now ready to make and receive calls.

4

#### Add contacts (optional)

Switch to the Contacts screen to add contacts to your address book. Right-click in the contacts area to add, edit, or import contacts. To synchronise contacts from your Click2Call account automatically, click the three horizontal lines in the top right corner of the app, select **Settings**, and check the **Directory of Users** setting. Internal contacts on your account will show online/offline and busy status in real time.

5

#### Enable multiple calls and transfers (optional)

To handle attended and blind transfers or take multiple incoming calls simultaneously, go to **Settings** and untick **Single Call Mode**. The app will then be able to manage multiple calls at the same time.

### Setting Up the Telephone App on Mac

App: **Telephone** — Download from the Mac App Store

**Note:** The Telephone app connects using SIP UDP by default. UDP is unencrypted and can be blocked by some firewalls. We recommend switching to TLS immediately after setup (see Step 4 below) for a more secure and reliable connection.

1

#### Download and open the Telephone app

Download the **Telephone** app from the Mac App Store using the link above. Open the app once installed.

2

#### Enter your Click2Call SIP account details

When the app opens, you will be presented with an account setup screen. Fill in the following fields:

| Field | Value |

| Full Name | Your name |

| Domain | sip.click2call.com.au |

| User Name | Your Click2Call phone number exactly as shown in the portal under Voice → Line Manager (e.g. 61370500989 — no + and no leading 0) |

| Password | The password saved in the Password box on that number’s row in Voice → Line Manager. New numbers have no password by default — type any password into the box and click Save Changes; the eye icon under the Password heading shows or hides it |

3

#### Save and confirm the account connects

Click **Add Account** (or the equivalent save button). The app will attempt to register using SIP UDP. Once connected, you can make calls by entering a number in the text field and pressing Enter or clicking Call.

4

#### Switch to TLS for a secure connection (recommended)

Go to the **Telephone** menu in the top left of your screen and select **Preferences**. Click the **Accounts** tab and untick **Enable this account** to allow editing. Click the **Network** tab and under **SIP Transport**, select **TLS** instead of UDP. Return to the **Account Information** tab and tick **Enable this account** again. The app will reconnect using the encrypted TLS protocol.

5

#### Adjust audio and call settings (optional)

In **Preferences**, use the **General** and **Sound** sections to select your preferred microphone and speaker or headset. If you do not want to receive a second call while already on a call, untick **Call waiting** in the General section.

### What to do next

The app is working. Here’s what most people do next.

[#### Make your first call

Test a call in and out on your new number](https://www.click2call.com.au/help/how-to-make-your-first-call)
[#### Keep your existing number

Bring it across for $100 inc GST. It keeps working until it moves.](https://www.click2call.com.au/help/how-to-port-number)
[#### Add your team

$25 a user a month ex GST, each with their own number and 300 outbound minutes](https://www.click2call.com.au/help/how-to-add-user)
[#### Have us set it up

Managed setup from $300 ex GST for up to 3 users, done in 1–2 business days](https://www.click2call.com.au/contact/)

## Connecting simPRO to Click2Call

Source: https://www.click2call.com.au/help/how-to-connect-simpro

simPRO Premium has a built-in softphone that can place and answer calls on your Click2Call numbers, with the caller matched to the right customer card. Setup takes about twenty minutes — and hinges on one field that is easy to get wrong.

Last reviewed: September 2026

### The setting that catches everyone
In simPRO’s **Server Address** field, use port **5060**, not 5061:
sip.click2call.com.au:5060
simPRO’s softphone reaches us through a WebRTC gateway that speaks ordinary SIP over UDP or TCP. Port 5061 is our encrypted TLS port, which that gateway does not use, so the connection never completes and the softphone reports Register failed: Disconnected. It looks like a password problem and is not one.

### Setting Up simPRO, Step by Step

1

#### Turn on the VoIP permission in simPRO

VoIP is hidden until your security group allows it. In simPRO go to **System → Setup → Security Groups** and open the relevant group.

- On the **Setup** tab, tick **VoIP** at the bottom of the **Admin** sub-tab.
- On the **Reports** tab, tick **VoIP**.
- Click **Save and Finish**.
If the VoIP menu or the softphone icon is missing later on, this is almost always why.

2

#### Connect simPRO to Click2Call

Go to **System → Setup → VoIP** and switch **Integration** to **ON**. Then fill in four fields:
| Server Address | sip.click2call.com.au:5060The port matters. See the box above. |
| Prefix | Leave blank. Click2Call does not need a code to reach an outside line. |
| Country Code | +61 |
| Area Code | Your local code — 07 for Queensland, 03 for Victoria, and so on. |

Click **Save**. If you run a multi-company build, VoIP has its own sharing setting under **System → Setup → Company** — either share one set of details across all companies, or configure each one separately.

3

#### Get the line password from Click2Call

In the Click2Call portal open **Voice → Line Manager**. Each number has a **Password** column with a **View** control that reveals the SIP password for that line.
**This is not your portal login password.** The password you use to sign in to the Click2Call portal will not register a phone. Each phone number has its own separate SIP password, and that is the one simPRO needs. This trips up nearly everyone the first time.

Treat the line password as a credential. Anyone holding it can register a device as that number and place calls billed to your account.

4

#### Add the credentials to each employee

simPRO stores VoIP credentials per person, not once for the business. For each employee who needs the softphone, go to **People → Employees** (or Contractors), open their card, and select the **Settings** sub-tab.
Under **VoIP Details**:
| Username | The Click2Call phone number in full international format, no spaces and no plus sign — for example 61755501234 for 07 5550 1234. |
| SIP Username | Leave blank. Click2Call uses the number as both the username and the authorisation name. |
| Password | The line password from step 3. |

Click **Save and Finish**.
Each person needs their own Click2Call number or extension. Two people sharing one set of credentials will fight over the registration — whoever logged in last gets the calls.

5

#### Open the softphone and test

Once the integration is on, a phone icon appears in the simPRO system menu for every user who has VoIP details on their card. Click it to open the softphone, then ring the number from a mobile.
The softphone shows the registration state at the top. Anything other than a connected state means it has not registered — the troubleshooting below covers what each message means.

### Troubleshooting

#### Register failed: Disconnected
The **Server Address** is on the wrong port. Change it to sip.click2call.com.au:5060. “Disconnected” means the connection never came up at all, which is a transport problem rather than a credential one — so no amount of changing passwords will fix it.

#### Unauthorized, Forbidden, or a 401 or 403 error
This one is the credentials. Check you have used the **line password** from Line Manager and not your portal login password, and that the username is the full international number with no plus sign and no spaces. Re-type rather than paste — a trailing space is easy to miss.

#### The softphone icon is missing from the menu
Either the integration is off under **System → Setup → VoIP**, the user has no VoIP details on their employee card, or their security group does not have VoIP ticked. Work through those three in order.

#### It does not work in Internet Explorer
simPRO does not support VoIP in Internet Explorer at all. Use Chrome or Edge.

#### It fails in Firefox
Firefox needs an extra component. Open the softphone, close it, and open it again — a prompt to install the **NS Service Plugin** should appear. Install it, click OK in the softphone, then close and reopen the softphone once more.

#### It works from home but not in the office
A restrictive firewall is blocking simPRO’s voice servers. simPRO’s softphone connects through MizuPhone, so your IT administrator may need to allow rtc.mizu-voip.com, www.webvoipphone.com and the related MizuPhone addresses that simPRO publish in their setup guide.

#### Calls connect but there is no audio one way
Almost always the firewall again, blocking the media rather than the signalling. The same MizuPhone addresses need to be reachable, and outbound UDP must not be blocked.

#### You want to use a different softphone inside simPRO
You cannot. simPRO state that the VoIP integration only supports their included softphone and that third-party softphones are not supported. You can of course run [our softphone](https://www.click2call.com.au/help/how-to-set-up-softphone) alongside simPRO on the same number.

### Frequently Asked Questions

#### Why port 5060 and not 5061?
simPRO’s softphone runs in your browser and reaches us through a WebRTC-to-SIP gateway, which converts the browser’s connection into ordinary SIP over UDP or TCP. Port 5061 is our encrypted TLS port and the gateway does not speak it, so the registration never completes. Port 5060 is the one that works.

#### Which password does simPRO need?
The **line password**, found in the Click2Call portal under **Voice → Line Manager** in the Password column. It is not the password you use to log in to the portal — those are two different things, and using the login password is the single most common mistake.

#### What format should the username be in?
The phone number in full international format with no plus sign and no spaces — 61755501234 rather than 07 5550 1234. Leave the optional SIP Username field blank.

#### Do calls through simPRO still get recorded and transcribed?
Yes, provided recording is switched on for that number. Recording is off by default and has to be enabled per number under **Voice** → the line → **Other Settings → Call Recording**. Recordings, AI transcripts and sentiment scores then appear under **Account → Records** alongside every other call. See [viewing call recordings](https://www.click2call.com.au/help/how-to-view-call-recordings). Australian law requires all parties to know the call is being recorded.

#### Does each employee need their own phone number?
Each simultaneous user needs their own number or extension, because the credentials are what register the softphone. Two people sharing one set will knock each other offline. Extensions are the usual way to do this — see [adding an extension](https://www.click2call.com.au/help/how-to-add-extension).

#### Can I use simPRO on my mobile as well?
The simPRO softphone runs in a browser on a computer. For mobile, register [our softphone app](https://www.click2call.com.au/help/how-to-set-up-softphone) on the same number and you will get calls in both places.

#### Do I need a SIP trunk instead of numbers?
No. simPRO registers as a device against each phone number, exactly like a desk phone or a softphone, so ordinary Click2Call numbers are what you want. A SIP trunk is for connecting a physical PBX, which simPRO is not.

## Setting Up Linphone (Free Third-Party Softphone)

Source: https://www.click2call.com.au/help/how-to-set-up-linphone

Phones & Devices
10 min read

## Setting Up Linphone with Click2Call

**Linphone** is a free, open-source SIP softphone available for iPhone, Android, Windows, and Mac. It is more configurable than the standard Click2Call app, which makes it a useful option for users who prefer a different interface, or for testing and troubleshooting SIP connectivity. This guide explains how to download Linphone and connect it to your Click2Call account using your SIP credentials.

Last reviewed: August 2026

When to use Linphone

Linphone is a good choice if you want a highly configurable SIP client, if you are troubleshooting a connection issue and want to rule out the standard app, or if you simply prefer Linphone's interface. It works on all four major platforms and connects to Click2Call using the same SIP credentials as any other softphone.

Before you begin: find your SIP credentials

You will need your phone number and line password from the Click2Call portal. Log in to portal.click2call.com.au, click the **Voice** tab, then select **Line Manager** from the left-hand menu. Your number is listed exactly as you must enter it. If the **Password** box on its row is empty (new numbers have no password by default), type any password and click **Save Changes**; the eye icon under the Password heading shows or hides it.

| Field in Linphone | What to enter |

| Username | Your phone number in E.164 format without the + prefix — e.g. 61287654321 |

| Password | Your line password from Voice → Line Manager in the portal |

| Domain | sip.click2call.com.au |

| Registrar URI | sip:sip.click2call.com.au |

| Transport | TLS |

| Authentication ID | Leave blank |

| Outbound SIP Proxy URI | Leave blank |

iPhone / iPad
Android
Windows
Mac

### Setting Up Linphone on iPhone or iPad

App: **Linphone** — Download from the App Store

1

#### Download and open Linphone

Open the App Store, search for **Linphone**, and install it. Once installed, open the app. You will be taken to the **Connection** screen, which shows a Username field, a Password field, and an orange **Connection** button.

2

#### Tap "Third-party SIP account"

Do **not** enter your details into the Username and Password fields on this screen, and do not tap the orange **Connection** button at the top. Those fields are for a Linphone account, not a SIP account. Scroll down and tap the **Third-party SIP account** button, which appears below the main login form.

3

#### Tap "I understand"

Linphone will display a notice explaining that some of its own features — such as group chat and video conferencing — require a Linphone account and will not be available when using a third-party SIP account. This is expected and does not affect calling. Tap **I understand** to continue to the SIP account setup form.

4

#### Fill in your SIP account details

You will now see the **Third-party SIP account** form. The form has two sections — the main fields on the left and **Advanced parameters** on the right. Fill in the fields as follows:

| Field | Value |

| Username | e.g. 61287654321 |

| Password | Your line password from the portal |

| Domain | sip.click2call.com.au |

| Display name | Any name you choose |

| Transport | TLS |

| Registrar URI (Advanced) | sip:sip.click2call.com.au |

| Auth ID & Outbound Proxy (Advanced) | Leave blank |

The Advanced parameters section is on the right-hand side of the form. Scroll right or expand it to find the Registrar URI field.

5

#### Tap "Connection" to register

Scroll to the bottom of the form and tap the orange **Connection** button. Linphone will attempt to register with the Click2Call SIP server using TLS. If your credentials are correct, the app will return to the main screen and display a green registered status indicator. You are now ready to make and receive calls.

6

#### Allow microphone and notification permissions

When you make or receive your first call, iOS will prompt you to allow microphone access — select **Allow**. Also ensure notifications are enabled for Linphone in your iPhone Settings so that incoming calls can wake the app when it is running in the background.

### Setting Up Linphone on Android

App: **Linphone** — Download from the Play Store

1

#### Download and open Linphone

Open the Play Store, search for **Linphone**, and install it. Once installed, open the app. When prompted, allow notifications — this is essential for receiving incoming calls when the app is running in the background.

2

#### Tap "Third-party SIP account"

On the Connection screen, do **not** use the Username and Password fields at the top — those are for a Linphone account. Scroll down and tap **Third-party SIP account** instead.

3

#### Tap "I understand"

Linphone will show a notice about Linphone-specific features being unavailable with a third-party SIP account. This does not affect calling. Tap **I understand** to proceed to the SIP configuration form.

4

#### Fill in your SIP account details

Complete the form using the values from the credentials table above:

| Field | Value |

| Username | e.g. 61287654321 |

| Password | Your line password from the portal |

| Domain | sip.click2call.com.au |

| Display name | Any name you choose |

| Transport | TLS |

| Registrar URI (Advanced) | sip:sip.click2call.com.au |

5

#### Tap "Connection" to register

Scroll to the bottom of the form and tap the orange **Connection** button. If your credentials are correct, Linphone will register and return to the main screen with a green status indicator. You are now ready to make and receive calls.

### Setting Up Linphone on Windows

App: **Linphone** — Download from linphone.org

1

#### Download and install Linphone

Visit linphone.org/en/download and download the Windows installer. Double-click the .exe file to install. If Windows shows a security warning, click **More info** then **Run anyway**. Follow the prompts to complete installation, then open Linphone.

2

#### Click "Third-party SIP account"

When Linphone opens, you will see the **Connection** screen. Do **not** enter your details into the Username and Password fields at the top. Click the **Third-party SIP account** button below the main login form instead.

3

#### Click "I understand"

Linphone will display a notice about Linphone-only features being unavailable with a third-party SIP account. Click **I understand** to proceed to the SIP configuration form.

4

#### Fill in your SIP account details

Complete the **Third-party SIP account** form. The form has two columns — required fields on the left and Advanced parameters on the right.

| Field | Value |

| Username | e.g. 61287654321 |

| Password | Your line password from the portal |

| Domain | sip.click2call.com.au |

| Display name | Any name you choose |

| Transport | TLS |

| Registrar URI (right column) | sip:sip.click2call.com.au |

| Auth ID & Outbound Proxy (right column) | Leave blank |

5

#### Click "Connection" to register

Click the orange **Connection** button at the bottom of the form. Linphone will register with the Click2Call SIP server. Once connected, a green status indicator will appear in the app. You are now ready to make and receive calls.

### Setting Up Linphone on Mac

App: **Linphone** — Download from linphone.org

1

#### Download and open Linphone

Visit linphone.org/en/download and download the Mac version. Open the downloaded .dmg file, drag Linphone to your Applications folder, and launch it.

2

#### Click "Third-party SIP account"

When Linphone opens, you will see the **Connection** screen. Do **not** use the Username and Password fields at the top. Click the **Third-party SIP account** button below the main login form.

3

#### Click "I understand"

Linphone will display a notice about Linphone-only features being unavailable. Click **I understand** to proceed to the SIP configuration form.

4

#### Fill in your SIP account details

Complete the **Third-party SIP account** form. The form has two columns — required fields on the left and Advanced parameters on the right.

| Field | Value |

| Username | e.g. 61287654321 |

| Password | Your line password from the portal |

| Domain | sip.click2call.com.au |

| Display name | Any name you choose |

| Transport | TLS |

| Registrar URI (right column) | sip:sip.click2call.com.au |

| Auth ID & Outbound Proxy (right column) | Leave blank |

5

#### Click "Connection" to register

Click the orange **Connection** button at the bottom of the form. Linphone will register with the Click2Call SIP server. Once connected, a green status indicator will appear. You are now ready to make and receive calls.

### Troubleshooting

Linphone shows "Registration failed" or "Forbidden"

Double-check your username and password. Your username must be the full E.164 number without a + prefix (e.g. 61287654321, not +61287654321 or 0287654321). Set or view your password in Voice → Line Manager: type it into the Password box on the number’s row and click Save Changes.

Linphone registered but calls are not connecting

Ensure the **Transport** is set to **TLS** and the **Registrar URI** is set to sip:sip.click2call.com.au. UDP connections may be blocked by some firewalls or mobile networks. TLS is the recommended transport for Click2Call.

I accidentally used the wrong login screen

If you entered your details on the main Connection screen (the one with the Username and Password fields at the top), go to Linphone's settings, remove the account that was created, and start again from the **Third-party SIP account** button.

Incoming calls are not ringing on my mobile

Ensure notifications are enabled for Linphone in your device settings. Without notification permission, the app cannot wake up to alert you of an incoming call. On iOS, also check that Background App Refresh is enabled for Linphone in Settings → General → Background App Refresh.

# Call Flows

## Keeping Calls Coming In During an Outage

Source: https://www.click2call.com.au/help/calls-during-power-or-internet-outage

Your phones need power and internet to work. If either goes down, Click2Call can still answer your calls and send them to a mobile or another number, because your phone system runs in the cloud, not in your office.

Last reviewed: October 2026

### Forward calls when your phones are offline

- Go to **Voice → Line Manager** and click your main number.
- From **Incoming Calls**, choose **Call Forwarding**.
- Turn on **Forward when Offline** and enter your mobile number.
- Save.

Now, if your phones lose power or internet, callers are sent to your mobile instead of hearing nothing.

### Ring a mobile at the same time

Another option is a [ring group](https://www.click2call.com.au/help/how-to-create-ring-group) that rings your mobile along with your desk phones. Calls reach you wherever you are, whether or not the office is online.

### If your own phone system (PBX) fails

If you connect your own PBX with a SIP trunk, set call forwarding on the trunk's main number the same way. If the PBX stops answering or goes offline, calls go to the numbers you've chosen. See [Connecting your own PBX with a SIP trunk](https://www.click2call.com.au/help/sip-trunk-pbx-setup).

### Voicemail still works

Voicemail runs in the cloud too. If nobody answers, callers can leave a message and you'll get it by email.

## Parking, Picking Up and Transferring Calls

Source: https://www.click2call.com.au/help/call-parking-pickup-transfers

Click2Call lets your team park a call and pick it up on another phone, answer a colleague's ringing phone, and transfer callers with a few key presses. These features work between phones on the same account and in the same calling group.

Last reviewed: October 2026

### Parking a call

Parking puts a caller on hold in a numbered slot so anyone in your group can pick them up from another phone.

#### Turn parking on

- Go to **Voice → Line Manager** and click any number in the group.
- From **Other Settings**, choose **Call Parking**.
- Tick **Enable Call Parking**. Every phone on the account in the same calling group can then park and retrieve calls.
- Choose the first parking slot number (for example 200), how many slots you want, and how long a call can stay parked.
- Under **Parking Return Destination**, choose whether an unanswered parked call goes back to the person who parked it or to another number. Save.

#### Park and retrieve

| To do this | Dial |
| Park the current call | Transfer the call to *07. You hear the slot number. |
| Park in a specific slot | Transfer to *07 plus the slot, e.g. *07205 |
| Pick up a parked call | *17, then the slot number when asked |
| Pick up from a specific slot | *1 plus the slot, e.g. *1205 |

If your phone has no transfer button, dial `#0` during the call, then `*07#`.

#### Tip: park calls in a queue instead

Parked calls time out and can't be watched from a phone key. For a hold slot you can see, create a spare extension, turn on a call queue for it, and tick **Support BLF monitoring and call pickup directly from the queue**. Program a BLF key for that extension on each phone. Transfer callers to the key to hold them, and press the key on any phone to pick them up. See [Setting up a call queue](https://www.click2call.com.au/help/how-to-set-up-call-queue).

### Picking up a colleague's ringing phone

| To do this | Dial |
| Answer the latest call ringing anywhere in your group | *88 |
| Answer a call ringing on a specific phone | *89, then the number or extension |
| Shortcut for a specific phone | *89 plus the extension, e.g. *8912 |

Pickup is on for every line by default.

### Transferring a call

Most people transfer with their phone's own transfer button. You can also transfer from any phone by dialling during the call:

| Transfer type | Dial | What happens |
| Attended | #0 then the number | You speak to the other person first, and can take the call back if they don't answer |
| Blind | ## then the number | The call goes straight through without an introduction |

These keypad transfers work on incoming calls. To allow them on outgoing calls too, go to **Other Settings → Inband Call Transfers**. You can also turn them off there.

To send an unanswered blind transfer back to you, go to **Outgoing Calls → Transfer Options** and tick **Recall enabled for blind transfers**.

## Hunt Groups: Ringing Phones One After Another

Source: https://www.click2call.com.au/help/hunt-groups

A hunt group rings a list of phones one at a time, in the order you choose, until someone answers. Use it when calls should go to your first choice of person and then move down the list. If you want several phones to ring at once instead, use a [ring group](https://www.click2call.com.au/help/how-to-create-ring-group).

Last reviewed: October 2026

### Setting up a hunt group

- Go to **Voice → Line Manager** and click the number people call.
- From **Incoming Calls**, choose **Hunt Group**.
- Tick **Enable a hunt group for this number**.
- Choose a **Time Schedule** if the group should only run at certain times, for example outside work hours.
- Set **Timeout before hunting**. This is how long the number rings on its own before the group starts.
- Enter up to 10 numbers. Each one rings for its own number of seconds before the call moves to the next.
- Save.

The numbers can be your own Click2Call numbers and extensions, or outside numbers such as mobiles. Click2Call numbers in the group are rung directly, without their own forwarding or voicemail settings.

### If nobody answers

Tick **If the call fails to connect through the hunt group then try ringing the line as normal** to send unanswered calls back to the main number's usual settings, such as voicemail.

### Combining with a ring group

Tick **Connect to the hunt group after ringing the line and any simultaneous rings first** to ring the line and its ring group first, then move through the hunt group.

### Hunt group, ring group or queue?

| Feature | Best for |
| Ring group (Simultaneous Ring) | Ringing several phones at once |
| Hunt group | Ringing people one after another, in a fixed order |
| Call queue | Holding callers with music until an agent is free |

## Do Not Disturb and Call Screening

Source: https://www.click2call.com.au/help/do-not-disturb-and-call-screening

Do not disturb stops your phone ringing and sends callers to voicemail, a busy tone or another number. Call screening asks callers to say their name first, so you can decide whether to take the call.

Last reviewed: October 2026

### Turning on do not disturb

You can switch it on in three ways:

- Press the DND button on your phone, if it has one and was set up through the portal.
- Dial `*78` to turn it on and `*79` to turn it off.
- In the portal, open the number, choose **Incoming Calls → Do not Disturb** and tick **Enable Do not Disturb Service**.

#### Choose where calls go

| Setting | What it does |
| Play Busy Tone | Callers hear busy instead of going to voicemail |
| Do not Disturb Forwarding Number | Sends calls to another number while DND is on |
| Time Schedule | Turns DND on only at certain times |
| Apply DND before all other features | DND also blocks the auto attendant, queues and conferencing on this number |
| Also apply DND when part of a ring group or queue | Stops ring group and queue calls too. By default they still ring |

#### Showing DND on colleagues' phones

When DND is on, BLF keys watching your line turn red. This only works when the time schedule is **At all times**.

You can use this to show forwarding too. Set a DND forwarding number instead of normal call forwarding. Your DND key then turns forwarding on and off, and colleagues see the red light while it's on.

If you set up a phone by hand, set its DND on code to `*78` and off code to `*79` so the light follows the button.

### Screening calls

- Open the number and choose **Incoming Calls → Call Screening**.
- Pick who to screen: anonymous callers, all callers, forwarded calls only, overseas callers, or overseas and anonymous callers.
- Choose a time schedule and save.

Screened callers are asked to say their name. Your phone plays it to you, and you choose to accept or reject the call. You can also dial `*34` to switch between screening anonymous callers, all callers, and off.

## Conference Calls and Dictation

Source: https://www.click2call.com.au/help/conference-calls

Any Click2Call number can become a conference bridge. Callers dial the number, enter a PIN if you've set one, and join the call together. We recommend using a spare extension or number for this, because every call to it goes into the conference.

Last reviewed: October 2026

### Setting up a conference number

- Go to **Voice → Line Manager** and click the number.
- From **Incoming Calls**, choose **Conferencing & Dictation**.
- Under **Select conference type**, choose **Audio conferencing enabled on this line**.
- Set a **Guest PIN** and a **Supervisor PIN** if you want them.
- Choose whether all callers can join, or only the numbers you list (one per line, with area code).
- Save.

### Recordings

Conferences are recorded by default and emailed to you as an MP3 when they end. Tick **Disable conference recordings** to stop this.

### During the conference

| Press | To |
| *1 | Mute or unmute yourself |
| *2 | Lock or unlock the room |
| *3 | Remove the last person who joined |
| *4 / *6 | Turn the conference volume down / up |
| *7 / *9 | Turn your own volume down / up |

### How many people can join?

Each person uses one of your account's channels, so the limit is your channel count. See [Adding channels](https://www.click2call.com.au/help/how-to-add-channels).

### Dictation

Choose **Turn this number into a voice dictation recorder** instead, and callers' messages are recorded for you. You can also dial `*64` from your own phone to record a dictation and get the transcript by email.

## Controlling Outgoing Calls: PIN Codes and Call Assignment

Source: https://www.click2call.com.au/help/outgoing-call-pin-and-call-assignment

You can ask for a PIN before certain calls go out, so only approved people can call overseas or mobiles. On a shared phone, call assignment mode asks for the caller's extension, so each call is billed and reported against the right person.

Last reviewed: October 2026

### Requiring a PIN for outgoing calls

- Go to **Voice → Line Manager** and click the number.
- From **Outgoing Calls**, choose **PIN Code & Call Assignment**.
- Tick **Enable Authorisation PIN code for outbound calls** and set a **PIN Code**.
- Under **Prompt for authorisation PIN code**, choose which calls need it. The choices are listed below.
- Save.

You can require the PIN for:

- all calls
- toll calls only (local calls go straight through)
- mobile and overseas calls
- overseas calls only
- overseas calls except Australia
- expensive overseas destinations

### Call assignment on a shared phone

- Open the shared phone's number. For a PBX on a SIP trunk, use the trunk's main number.
- Choose **Outgoing Calls → PIN Code & Call Assignment**.
- Tick **Call Assignment Mode** and save.

Now, after dialling, the caller is asked for their extension. The call then goes out with that person's caller ID and is billed to them. Their extension must be on the same account and in the same calling group. If their extension has its own PIN, they're asked for it too.

#### One code per person

Tick **Treat the extension as the PIN code during call assignment** to ask for a PIN instead. Create a free extension for each person, and their extension number becomes their personal code.

## Calling Through Your Business Number While Away

Source: https://www.click2call.com.au/help/remote-call-back-and-dial-tone

Remote dial tone and remote call back let you make calls through your Click2Call number from another phone, such as your mobile. The person you call sees your business number, and the call is charged to your Click2Call account at its normal rates instead of your mobile plan.

Last reviewed: October 2026

### Remote dial tone

You call your business number, enter a PIN, and get a dial tone to call out.

#### Set it up

- Go to **Voice → Line Manager**, click the number, and choose **Other Settings → Remote Dial Tone**.
- Tick **Enable remote dial tone service**.
- Choose whether only listed numbers or all callers get dial tone. Listing your mobile is safest.
- Enter your phone numbers, one per line with area code.
- Set a **PIN**. The service doesn't work without one.
- Save.

#### Use it

Call your business number from a listed phone, enter your PIN, wait for the dial tone and dial.

### Remote call back

You call your business number and hang up when it rings. Click2Call calls you back with a dial tone. This saves the cost of your outgoing call, which helps when you're overseas.

#### Set it up

- Open the number and choose **Other Settings → Remote Call Back**.
- Tick **Enable remote call back service**.
- Choose selected callers or all callers. A PIN is required if you allow all callers.
- List the numbers to call back, one per line with area code.
- Optionally set a delay before the call back, or a fixed number to always call back.
- Save.

### Keep it secure

These features place calls billed to your account. Always set a PIN, list only your own numbers, and turn the feature off when you don't need it. See [Stopping ghost and spam calls](https://www.click2call.com.au/help/ghost-and-spam-calls) for more security tips.

## Group Calls and Paging

Source: https://www.click2call.com.au/help/group-call-and-paging

A group call rings up to 20 people at once and joins everyone who answers into one call. Paging mode turns it into an announcement: phones answer on speaker automatically and only one person talks.

Last reviewed: October 2026

We recommend setting this up on a spare extension. Otherwise every call to the number starts a group call.

### Setting up a group call

- Go to **Voice → Line Manager**, click the extension, and choose **Incoming Calls → Group Call or Page**.
- Enter a **Group Name** and up to 20 members.
- Tick **Enable Group Call for all incoming calls to this number**.
- Choose a time schedule if needed, and save.

Now anyone who dials the extension starts the group call. From a phone registered to that number, you can also dial `*48`.

### Setting up paging

Set up the group as above, then also tick:

- **Paging Mode**, so members' phones answer automatically on speaker, if the phone allows it.
- **Mute all users on the call/page except for member 1 and the group call initiator**, so only the speaker is heard. Everyone is disconnected when they hang up.

Set **Member 1** to the person who makes most announcements.

### Other options

| Option | What it does |
| Do not connect the group call initiator | The caller isn't joined to the call and hears "call activated" |
| Follow call flow logic for Group Member 1 only | Uses member 1's settings, for example to play a recorded message to the group |

To control who can start a group call, add a whitelist to the number under **Incoming Calls → Blacklist and Whitelist Options**.

## Hold Music, Caller Tunes and Which Setting Wins

Source: https://www.click2call.com.au/help/hold-music-and-feature-order

You can replace the ringing callers hear with your own music or message, and upload your own music on hold. This guide also explains why one setting can override another on the same number.

Last reviewed: October 2026

### Caller tunes and hold music

- Go to **Voice → Line Manager**, click the number, and choose **Other Settings → Media Options**.
- Choose a **caller tune** to play instead of ringing, or upload your own MP3.
- Adjust the volume of your tune and of the background ringing.
- Upload your own music on hold if you want it.
- Save.

Tick **Disable all caller tunes** to go back to normal ringing, or **Disable all Music on hold** to play simple ringing while callers are on hold. There's no extra charge for either.

### Why one setting overrides another

Each number runs its features in a fixed order, and the first one that applies handles the call. For example, if call blocking and call forwarding are both on, blocking wins.

| Order | Feature |
| 1 | Call rejection (blocked and anonymous callers) |
| 2 | Remote dial tone |
| 3 | Remote call back |
| 4 | Conferencing |
| 5 | Auto attendant |
| 6 | Call queue |
| 7 | Do not disturb |
| 8 | Call screening |
| 9 | Forward all calls |
| 10 | Simultaneous ring |
| 11 | Hunt group |

Do not disturb can be moved above the auto attendant, queues and conferencing with **Apply DND before all other features**. See [Do not disturb and call screening](https://www.click2call.com.au/help/do-not-disturb-and-call-screening).

## Stopping Ghost and Spam Calls

Source: https://www.click2call.com.au/help/ghost-and-spam-calls

If your phone rings and nobody is there, or you get calls from numbers like "100" or "blocked" several times a day, there are two possible causes. Which one you have decides the fix, and the call records tell you which.

Last reviewed: October 2026

### Step 1: check whether the calls came through Click2Call

#### Look in Records

Log in to the portal and open Account → Records. Find the times the ghost calls rang.

#### If the calls are listed

They are real calls from the phone network — usually robocallers or an overseas call centre. Go to the next section.

#### If the calls are NOT listed

Something on the internet is calling your phone directly, bypassing Click2Call. Skip to "Calls that don't appear in Records".

### Calls that appear in Records: block or screen them

- **Block specific numbers**: Voice → Line Manager → click the number → Incoming Calls → Blacklist and Whitelist Options → enter the numbers in Blacklisted or Whitelisted Callers (one per line, with area code; * works as a wildcard), leave Matching Caller Action on Blacklist Applied → Save. From a handset you can also dial *60 followed by the number to block it, and *80 followed by the number to unblock it.
- **Reject anonymous callers**: on the same page, tick Reject all anonymous calls? Star codes: *77 on, *87 off.
- **Other options on the same page**: Reject all calls from overseas?, and Block all mobiles from calling this number? (callers hear a message saying mobiles are blocked). You can also send blocked callers to a forwarding number instead of a busy tone.
- **Screen callers**: Incoming Calls → Call Screening makes callers say their name first, and you choose whether to take the call. Star codes: *32 screen anonymous callers, *33 screen all callers, *34 turn screening off.
- **Persistent nuisance callers**: contact support with the times and numbers and we'll check for you whether they can be blocked at the network level.

### Calls that don't appear in Records: lock down your network

These come from automated scanners on the internet that look for phones listening on ports 5060 and 5061 and try to call them. They mean your phone or PBX is reachable from the internet, usually because of a port-forwarding rule on your router.

#### Why this matters

Besides the nuisance, these scans are attempts to break into a PBX and use it to make expensive international calls at your cost.

#### What to do

- Remove any port-forwarding rules on your router that send ports 5060 or 5061 to a phone or PBX. Click2Call does not need them.
- If your PBX genuinely needs to be reachable (for example, it uses SIP Peering), restrict those ports with a firewall rule so only sip.click2call.com.au can reach them.
- Switch the device to TLS or port 50600 (see [SIP Settings for Desk Phones, Adapters and PBX Systems](https://www.click2call.com.au/help/sip-settings-for-devices-and-pbx)).
- Change the line password in Voice → Line Manager and update your devices.

## Star Codes: Control Your Phone from the Handset

Source: https://www.click2call.com.au/help/star-codes

You can change many settings by dialling a code from any phone on your account, without logging in to the portal. Where you see xxx, enter a phone number (or a number of seconds, where stated).

Last reviewed: October 2026

### Voicemail

| *55 | Open your voicemail |
| *50 | Play your unavailable greeting |
| *58 | Record your unavailable greeting (press # to finish) |
| *59 | Record your busy greeting (press # to finish) |
| *52 | Turn voicemail on |
| *53 | Turn voicemail off |

### Call forwarding and simultaneous ring

| *72xxx | Forward all calls to xxx (*72 alone turns it back on to the last number) |
| *73 | Stop forwarding all calls |
| *92xxx | Forward unanswered calls to xxx |
| *93 | Stop forwarding unanswered calls |
| *90xxx | Forward calls when busy to xxx |
| *91 | Stop forwarding when busy |
| *82[1–6]xxx | Set and turn on saved forward 1–6 |
| *83[1–6] | Turn off saved forward 1–6 |
| *561xxx / *562xxx / *563xxx | Also ring xxx (simultaneous ring 1, 2 or 3) |
| *571 / *572 / *573 | Stop simultaneous ring 1, 2 or 3 |
| *54n | Ring for n seconds before diverting |
| *38 / *39 | Record / remove the message played to whoever you forward a call to. Or tick Play a notification to the callee at the start of the call when the call has been forwarded at the bottom of the Call Forwarding page, and they hear “call-forwarding” before the call connects. |

### Do not disturb, privacy and blocking

| *78 / *79 | Do not disturb on / off |
| *30 / *31 | Hide your caller ID on all calls / show it again |
| *67xxx | Call xxx with your caller ID hidden |
| *65xxx | Call xxx with your caller ID shown |
| *77 / *87 | Reject anonymous callers on / off |
| *60xxx / *80xxx | Block / unblock number xxx |
| *32 / *33 / *34 | Screen anonymous callers / screen all callers / screening off |

### Call queues

| *45 / *46 | Hot desk log in / log out (*45xx to log in as extension xx) |
| *70 | Log in to all your queues |
| *70xx | Log in to queue xx (its extension or number) |
| *71 | Log out of all queues |
| *71xx | Log out of queue xx |

### Auto attendant and AI receptionist

| *22 / *23 | Record / play your auto attendant menu |
| *26 / *25 | Turn the auto attendant on / off |
| *62 / *63 | Record / play your AI receptionist message |

### During a call

| ## | Blind transfer (then dial the number) |
| #0 | Attended transfer (talk first, then hang up to connect) |
| *1 | Start or stop recording this call |
| *3 / *4 | Pause / resume recording |
| *0 | Disconnect |

### Other handy codes

| *69 | Call back your last caller |
| *66 | Redial the last number you called |
| *51 | Hear who last called you |
| *61 / *81 | Call waiting on / off |
| *07 | Park a call (you'll hear the parking slot number) |
| *17 | Pick up a parked call (*1xxx for a specific slot) |
| *88 / *89 | Pick up a call ringing in your group / a specific phone |
| *64 | Record a dictation — the transcript is emailed to you |
| *24 | Talk to the Click2Call AI assistant |

## Ring Your Mobile and Still Get Voicemail

Source: https://www.click2call.com.au/help/call-flow-ring-mobile-then-voicemail

: Why Call Forwarding Breaks It

A common setup that quietly does not work: forward the business number to a mobile, then wonder why voicemail never arrives and why the mobile ring time cannot be changed. Here is what is happening and the setup that does what you want.

Last reviewed: October 2026

### Why a forward loses your voicemail

When a call is forwarded to an external mobile, the call **leaves the Click2Call platform**. From that moment your mobile's own no-answer timer applies, and if nobody picks up it is your mobile carrier's voicemail that answers, not ours.

Two things follow, and both surprise people:

- The **Call Ringing Time** on your line does not control how long the forwarded mobile rings. That setting governs your line, not a call that has already left.

- Adding a voicemail step after the forward does nothing, because the call is gone before it gets there.

If you are trying to build a flow like *ring the app, then ring my mobile, then take a message*, plain Call Forwarding cannot deliver it.

### The setup that works

Use Simultaneous Ring instead. It rings the mobile alongside your app while keeping the call on our platform, so our voicemail can still answer.

- Go to **Voice** then **Line Manager**, and click the number you want to change.

- Open **Incoming Calls** then **Call Forwarding**, and turn off any busy, no-answer or unreachable rules pointing at your mobile. While a no-answer forward is active, unanswered calls go to the mobile instead of voicemail.

- Open **Incoming Calls** then **Simultaneous Ring**. On Simultaneous Ring #1, tick Enable, enter your mobile number, and choose when it applies. You can set a delay in seconds so your app rings first and the mobile joins a few seconds later. Up to ten numbers can ring together.

- Open **Incoming Calls** then **Voice Mail**. Set **Call Ringing Time (in seconds)** to cover the whole ring period you want before voicemail answers, and enter an address in **Send a copy of my voicemail messages to the following email address**.

### Three things worth knowing

Simultaneous Ring gives you one total ring period rather than a separate count for the app and then the mobile. You choose how long everything rings before voicemail takes over, not a precise handover between devices.

Check your mobile's own voicemail delay as well. If your carrier answers after 15 seconds and you have set a 25 second ring time here, your carrier will take the message before our voicemail gets the chance. Either raise the carrier delay or turn its voicemail off.

If you keep a plain forward to your mobile, you can still tell those calls apart from personal ones. Tick **Play a notification to the callee at the start of the call when the call has been forwarded** at the bottom of the Call Forwarding page, and whoever answers hears “call-forwarding” before the call connects. To play your own message instead, dial *38 to record it (*39 removes it).

### Still not behaving?

Email support@click2call.com.au with the number you are working on and what you hear when you test it. We can look at the line configuration directly and tell you what is actually set.

## Setting Up a Call Flow

Source: https://www.click2call.com.au/help/how-to-set-up-call-flow

/ IVR

A call flow (also called an IVR or auto-attendant) is a menu system that greets callers and routes them based on the option they press. For example: 'Press 1 for Sales, Press 2 for Support.' This guide walks you through building one.

Last reviewed: August 2026

### Setting Up a Call Flow, Step by Step

1

#### Log in to the Portal

Navigate to portal.click2call.com.au and sign in with your user credentials.

2

#### Select Your Phone Number or Extension

Click the **Voice** tab in the main navigation. From the left-hand menu, select the specific phone number or user extension you want to configure.

3

#### Choose Auto Attendant for Incoming Calls

In the main settings area for your chosen line, find the **Incoming Calls** dropdown menu and select **Auto Attendant** from the list of options.

4

#### Enable and Program Your Menu Options

Tick the **Enable auto attendant feature on this line** checkbox. Now you can program the call flow by assigning a destination (like an extension or external number) to each digit (1, 2, 3, etc.). Click **Save** at the bottom of the page when you are finished.

5

#### Set Up Your Greeting Message

After saving, go back into the Auto Attendant settings. You will now see options to set up your greeting. You have two main choices:

- **Record manually:** Dial *22 from your handset to record the menu, and *23 to play it back.

- **Upload a file:** Click the button to upload a pre-recorded audio file.

6

#### Uploading a Pre-Recorded Greeting

If you choose to upload a file, you will be taken to the Media page. Ensure you are in the **Auto Attendant** folder, then choose your MP3, WAV, or M4A file and click **Upload File(s)**.

Pro Tip: Use AI Speech to Create Your Greeting

For a professional-sounding message, you can use our built-in **AI Speech** tool (found under the AI menu) to generate a high-quality recording from text. Simply type your message, generate the voice, and download the audio file to upload here.

7

#### Test Your Auto Attendant

Wait a couple of minutes for the settings to apply across the network. Then, call your phone number from an external line (like your mobile) to hear the greeting and test that your menu options route correctly.

## Setting Up a Call Queue

Source: https://www.click2call.com.au/help/how-to-set-up-call-queue

A call queue holds callers while your team is busy, instead of letting the phone ring out or returning an engaged tone. Callers hear your music and your announcements, and are told where they are in the queue. This guide covers enabling a queue on a line, adding agents, and every setting that affects what the caller experiences.

Last reviewed: August 2026

### Setting Up a Call Queue, Step by Step

1

#### Enable the queue on the line

In the portal, open the **Voice** tab and select the number or extension you want the queue to apply to. That opens the **Call Flow** screen for that line.
Open the **Incoming Calls** dropdown and choose **Call Queue**. This is the same menu that holds Voice Mail, Call Forwarding, Simultaneous Ring, Hunt Group, Auto Attendant and AI Attendant — so the queue becomes what that line does with an incoming call, in place of whichever behaviour was set before.

The Call Queue settings open. Tick **Call Queue Enabled on this line**, then set the **Time Schedule** below it. Leave it as At all times for a permanently active queue, or pick a schedule so the queue only runs during opening hours.
A queue is set per line, not per account — your main published number can queue while a direct line rings straight through. Because it is chosen from the Incoming Calls menu, enabling a queue replaces the previous incoming-call behaviour on that line rather than running alongside it.

2

#### Add your agents

Add each team member who should answer queued calls to the numbered agent list. The numbering is the order agents are tried — which matters for every strategy except Ring All, where everyone rings at once.
Leave unused slots as -- Not Set --. You can change the list at any time without affecting callers already waiting.

The dropdown lists your extensions by name and login, along with any voicemail destinations on the account — so a slot can point at a mailbox as well as a person.

3

#### Choose the strategy and ring timers

Pick a **Queue Strategy**. **Ring All** rings every agent simultaneously and is the usual choice for a small team.
Then set the timers:

- **Agent Timeout** — how long each agent’s phone rings, between 5 and 60 seconds. 15 is a sensible default; much longer and callers notice the silence.
- **Retry Timer** — how long before an agent who did not answer is tried again.
- **Wrapup Time** — a pause after a call before that agent can receive another. Useful if staff need a moment to finish notes.
Two further options sit lower down: whether to **send calls to agents even when they are busy** on an existing call, and whether to **report the caller’s hold time to the agent** before connecting them.

4

#### Decide what callers hear

This is the part callers actually experience, so it is worth getting right.

- **Position Announcement** — seconds between telling the caller their place in the queue. Set 0 to turn it off. You can also choose whether it plays at the beginning.
- **Include hold time in position announcements** — adds an estimated wait to that announcement.
- **Announcement Frequency** — how often a short “thank you for holding” message plays between position announcements. 0 turns it off.
Use the upload buttons at the bottom of the page to add your own **Music on Hold** and your own **Queue Announcement**. Both are worth doing — default hold music is the fastest way to sound like everybody else.

5

#### Set limits and the exit path

**Maximum Length** caps how many callers may wait; 0 means unlimited. **Queue Timeout** caps how long any one caller waits; 0 means no limit.
Use **queue exit options** to decide where a caller goes when the timeout is reached — voicemail, another number, or another part of your call flow.
Unlimited length with no timeout is rarely the right choice. A caller who waits eight minutes and then hangs up is a worse outcome than one sent to voicemail after ninety seconds.

6

#### Give the queue a label, then test it

Set a **Queue Identifier** — the text shown in the caller ID so staff can see a call came from the queue rather than direct. The default is QUEUE:.
Then test properly: ring the line from an outside phone while the agents are busy or their phones are unregistered. Confirm you hear your announcement and music, that position announcements play at the interval you set, and that the call is delivered as soon as an agent frees up.

### Frequently Asked Questions

#### What is the difference between a call queue and a ring group?
A ring group rings a set of extensions and, if nobody answers, moves the call to the next step. A queue holds the caller until someone is free. Use a ring group to pass a call along quickly; use a queue when calls arrive faster than the team can answer and you would rather callers waited than got voicemail. See [Creating a Ring Group](https://www.click2call.com.au/help/how-to-create-ring-group).

#### Why is the BLF option not working?
BLF monitoring and call pickup directly from the queue require the **Ring All** strategy. With any other strategy selected the option has no effect.

#### Can a queue run only during business hours?
Yes — set the queue’s **Time Schedule**. Outside those hours the call follows the rest of your call flow instead, normally an after-hours greeting or voicemail. See [Configuring Business Hours](https://www.click2call.com.au/help/how-to-configure-business-hours).

#### What happens when the queue is full?
Callers beyond the **Maximum Length** are not queued and follow the exit path instead. Setting it to 0 makes the queue unlimited.

#### Do queued calls get recorded and transcribed?
Yes. Once answered, a queued call is recorded, transcribed and summarised like any other. While it is waiting it appears in the [live call dashboard](https://www.click2call.com.au/help/how-to-use-live-call-dashboard), with its wait time.

## Using the Live Call Dashboard

Source: https://www.click2call.com.au/help/how-to-use-live-call-dashboard

The Call Activity Dashboard shows live calls, callers waiting in queues and team availability in one place, updating continuously. It answers the question every manager asks mid-morning: is the phone busy right now, and is anyone waiting? This guide covers opening it, reading each panel, and putting it on a screen the team can see.

Last reviewed: August 2026

### Using the Live Call Dashboard, Step by Step

1

#### Open the dashboard

Log in to the portal, open the **Account** tab and choose **Dashboard**. The Call Activity Dashboard opens with live calls, queue activity and team availability on one screen.

2

#### Set the period and filter

Use **Period** to choose what the counters cover — Today is the usual choice — and **Activity** to narrow from All Calls to a single call type.
A **Live updates are on** indicator and a last-updated time sit just below, with a **Refresh** control if you want to force an update.

3

#### Read the counters

The row across the top is the summary for your selected period:

- **Calls** — the total, with **Incoming**, **Outgoing** and **Internal** broken out beside it.
- **Missed** — calls that arrived and were not answered.
- **Total Talk** and **Average Talk** — how much time was spent on calls, and the typical call length.
Missed is the number worth watching. Most businesses have never measured it, and seeing it for the first time is usually what prompts a change to the call flow.

4

#### Watch calls in progress

**Active Calls** lists every call underway: its type, the caller, the callee, when it connected and how long it has been running. Beside it, **Team Status** shows who is available.

5

#### Watch callers waiting

**Queued Calls** shows anyone currently holding — which queue, when they connected, the state of the call, and their wait time.
This panel reads No queues enabled until at least one line has a call queue switched on. See [Setting Up a Call Queue](https://www.click2call.com.au/help/how-to-set-up-call-queue).

6

#### Put it on a screen

Select **Open TV View** for a full-screen version designed for a monitor on the office wall. Live updating continues, so the team can see a queue building without anyone opening the portal.
This works well on a spare monitor or a smart TV browser. Nothing to install.

### Frequently Asked Questions

#### Why does the queued calls panel say “No queues enabled”?
Because no line has a call queue switched on yet — there is nothing to display. Enable a queue and the panel starts showing waiting callers. See [Setting Up a Call Queue](https://www.click2call.com.au/help/how-to-set-up-call-queue).

#### Why is Team Status empty?
Either no users are registered on the account yet, or their devices are not currently registered to the platform. Check that softphones or desk phones are online — see [Setting Up a Softphone](https://www.click2call.com.au/help/how-to-set-up-softphone).

#### Does it update on its own?
Yes. Live updates run automatically while the dashboard is open, and the last updated time is shown. Use **Refresh** to force an immediate update.

#### Can I display it on a TV in the office?
Yes — **Open TV View** gives a full-screen wallboard for a wall monitor, still updating live.

#### How is this different from Reports & Records?
The dashboard is real time — what is happening now, plus totals for the period you select. [Reports & Records](https://www.click2call.com.au/help/how-to-use-reports-and-records) are historical, for filtering and exporting past call and billing data. Use the dashboard to manage the day, Reports to analyse it afterwards.

#### Is there an extra charge?
No. The dashboard and the TV view are included with a standard Cloud PBX user at $25/user/month ex GST — no supervisor licence, analytics add-on or separate tier. More on the [call centre features page](https://www.click2call.com.au/call-centre/).

## Creating a Ring Group

Source: https://www.click2call.com.au/help/how-to-create-ring-group

A ring group allows a single incoming call to ring multiple extensions at the same time (simultaneous ring) or one after another (sequential ring). This is useful for teams like Sales or Support. If you would rather callers waited than moved on when nobody answers, use a [call queue](https://www.click2call.com.au/help/how-to-set-up-call-queue) instead.

Last reviewed: August 2026

### Creating a Ring Group, Step by Step

1

#### Select Your Line and Choose Simultaneous Ring

First, log in to the portal and navigate to the **Voice** tab. Select the extension or phone number you want to set up. From the **Incoming Calls** dropdown menu, choose **Simultaneous Ring**. This feature is also commonly known as a Ring Group.

2

#### Add Numbers and Configure Settings

You can now configure up to 9 numbers to ring at the same time. For each number you want to add, follow these steps:

- **Enable Number:** Tick this checkbox to activate the slot.

- **Number or Extension:** Enter the internal extension or external phone number (e.g., a mobile number) you want to include in the group.

- **Ring this number:** Set a time schedule. For most ring groups, you will leave this as 'At all times'.

- **Seconds delay before ringing:** Enter a number of seconds to wait before this specific number starts ringing. A setting of '0' means it will ring instantly with all other numbers.

- **Direct to handset:** Keep this ticked. This ensures the call connects directly to the user's device. Un-ticking it would send the call to that user's personal voicemail if they don't answer, which is usually not desired in a group setup.

3

#### Save Your Settings

Once you have added all the desired numbers and configured their settings, scroll to the bottom of the page and click the **Save Settings** button.

4

#### Verify the Final Call Flow

After saving, the call flow diagram for your line will update to show the new Simultaneous Ring configuration. You can see all the numbers that will ring at once. Finally, make a test call to the main number to ensure all configured phones ring as expected.

## Configuring Business Hours

Source: https://www.click2call.com.au/help/how-to-configure-business-hours

Business hours rules allow your phone system to behave differently depending on the time of day. During business hours, calls can ring your team; outside hours, they can go to voicemail or an after-hours message.

Last reviewed: August 2026

### Configuring Business Hours, Step by Step

1

#### Navigate to Time Schedules

First, log in to the portal and go to the **Voice** tab. Select the phone number or extension you wish to configure. Then, open the **Other Settings** dropdown menu and click on **Time Schedules**.

2

#### Configure Your Time Schedules

The Time Schedules page provides several pre-named schedules that you can program. Use the 24-hour format (e.g., 09:00 and 17:00). Here’s a breakdown of each schedule type:

**Work Hours:** This is the most commonly used schedule. Set your standard business operating hours here (e.g., Monday to Friday, 9am to 5pm).

**Available Hours:** Can be used for extended hours, such as support availability (e.g., 8am to 10pm, 7 days a week).

**User Defined:** A flexible schedule you can name and use for any specific purpose.

**Custom 1, 2, 3:** Three additional custom schedules for more complex routing needs, such as different weekend hours or team-specific schedules.

3

#### Add Custom Holiday Dates

At the top of the page, you can click the blue button to **add your own custom holiday dates**. These dates will be treated as "outside of hours" in your call flows, ensuring calls are routed correctly on days your business is closed. Enter dates in DD-MM-YYYY format.

4

#### Apply Schedules to Your Call Flow

Once your schedules are saved, you can apply them to various call flow features. For example, you can make a **Simultaneous Ring** group only active 'During Work Hours', or set a **Call Forwarding** rule to send calls to your mobile 'Outside of Work Hours'. This allows for powerful and automated call routing based on time of day.

## Setting Up Voicemail

Source: https://www.click2call.com.au/help/how-to-set-up-voicemail

-to-Email

Voicemail-to-email sends you an email notification with an audio attachment every time someone leaves a voicemail on your extension. This guide shows you how to set it up.

Last reviewed: August 2026

### Setting Up Voicemail-to-Email, Step by Step

1

#### Select Voicemail in Your Call Flow

First, log in to the Click2Call portal. Navigate to the **Voice** tab and select the phone number or extension you want to configure from the Line Manager list. In the main call flow panel, click the **Incoming Calls** dropdown menu and select **Voice Mail**. This tells the system to direct unanswered calls to the voicemail service.

2

#### Configure Your Voicemail Settings

Once you select Voice Mail, the settings panel will appear. Here you can customise how your voicemail service works. We recommend the following at a minimum:

- **Call Ringing Time:** Set how long the phone rings before voicemail answers (e.g., 20 seconds).

- **Voicemail Access PIN:** Set a numeric PIN to access your messages from another phone.

- **Send a copy to email:** Enter one or more email addresses (separated by a semi-colon) to receive voicemail-to-email notifications.

- **Only send an email copy:** Tick this box if you do not want voicemails stored in the portal, only sent to your email. This is a popular option for keeping your mailbox clean.

There are many other advanced options available, such as speech-to-text transcription, SMS alerts, and automatically deleting old messages.

3

#### Set Up Your Voicemail Greeting

Scroll down to find the greeting options. You have two main choices:

- **Record from your handset:** Dial ***58** from your connected phone to record your 'unavailable' message (when you don't answer) or ***59** for your 'busy' message (when you are on another call).

- **Upload a file:** Click the blue buttons to upload a pre-recorded WAV or MP3 file from your computer. This is ideal for professional studio recordings.

**Pro Tip:** You can use our [AI Speech tool](https://www.click2call.com.au/help/how-to-set-up-ai-receptionist) to generate a high-quality, natural-sounding greeting file to upload here.

4

#### Save and Test

Once you are happy with your settings, click the green **Save Settings** button at the bottom. To test, call your number from a different phone (e.g., your mobile), let it ring out, and leave a short message. Within a few minutes, you should receive an email with the audio file attached, along with an AI transcript and summary of the message — so you can read a voicemail at a glance without playing it back.

## Viewing Call Recordings

Source: https://www.click2call.com.au/help/how-to-view-call-recordings

If call recording is enabled on your account, all calls are automatically recorded and stored in the portal. This guide shows you how to find and listen to them.

Last reviewed: August 2026

**Important:** Call recording is disabled by default and must be manually enabled for each phone number or extension you wish to record. All parties must be aware that the call is being recorded to comply with Australian law.

### Part 1: How to Enable Call Recording

1

#### Navigate to Call Recording Settings

Log in to the portal, go to the **Voice** tab, and select the line you want to configure. Click the **Other Settings** dropdown and choose **Call Recording**.

2

#### Configure and Enable Recording

In the Call Recording panel, untick the 'Disable ALL call recording' box. Choose your recording options, such as recording all calls or playing a message to the other party. You can also enter an email address to have a copy of all recordings sent to you automatically. Click **Save Settings** when done.

### Part 2: How to View and Download Recordings

3

#### Navigate to Billing Records

In the portal, click the **Account** tab, then select **Records** from the left-hand menu. This will take you to the Billing Records page where all your call history is stored.

4

#### Find, Play, and Download Your Recording

Use the filters to find the call you're looking for. On the far right of the call log entry, you will see a set of icons. These allow you to manage the recording for that specific call.

Here is what each icon does, from left to right:

- **Smiley Face:** View AI-powered sentiment analysis for the call.

- **Play/Stop:** Listen to the call recording directly in your browser.

- **List Icon:** View the full AI-generated call transcription.

- **Download:** Download the call recording as an MP3 audio file.

- **Trash Can:** Permanently delete the recording.

## Setting Up Microsoft Teams Calling

Source: https://www.click2call.com.au/help/how-to-set-up-microsoft-teams

Connect Microsoft Teams to the Click2Call SBC using Direct Routing so your Teams users can make and receive real phone calls on Australian numbers — no separate softphone required.

Last reviewed: August 2026

Estimated time: 30–45 minutes for a first-time setup
Difficulty: Advanced

Before you begin

You’ll need Global Admin access to your Microsoft 365 tenant, a Microsoft Teams Phone Standard licence (or an E5 licence) for every user that will make calls, and comfort with the Microsoft PowerShell command line for the final step. If you’d rather we handle the setup for you, our [managed setup service](https://www.click2call.com.au/pricing/#managed-setup) covers Teams Direct Routing from end to end.

### What this guide covers

Microsoft Teams doesn’t connect to the public phone network on its own — it needs a Direct Routing provider on the other side of an SBC (Session Border Controller). Click2Call is that provider. This guide walks through the eight steps required to link the two: enabling the Teams profile in the Click2Call portal, adding and verifying the SBC domain in Microsoft 365, creating the trunk user, provisioning your Teams phone numbers, mapping them to users, and running the PowerShell commands that grant each user permission to place calls.

The bulk of the configuration lives in two places: your Click2Call portal at `portal.click2call.com.au` and the Microsoft 365 Admin Centre at `admin.microsoft.com`. Keep both open in side-by-side browser tabs so you can copy values between them.

### Microsoft Teams Direct Routing Setup, Step by Step

1

#### Enable Microsoft Teams on your Click2Call profile

Sign in to portal.click2call.com.au and open **Voice → Profiles**. Either edit the Default profile or create a new one dedicated to Teams. Change the **Connection Type** dropdown to **Microsoft Teams**.

As soon as you save, the portal displays two important values on the profile:

- **Microsoft Teams Domain** — something like `ms{account}.sbc.msteams.nz`. This is the SBC hostname that Microsoft will send calls to and receive calls from. Copy it to your clipboard.

- **Domain TXT Record Value** — a blank field where you’ll paste Microsoft’s verification token in a moment.

2

#### Add the SBC domain in Microsoft 365

Open a new tab, sign in to admin.microsoft.com as a Global Admin, and use the left navigation to open **Settings → Domains**.

Click **Add domain** at the top of the domains list.

Paste the Microsoft Teams Domain you copied in Step 1 into the **Domain name** field, then click **Use this domain**.

3

#### Verify the domain using the TXT record

Microsoft will next ask you to prove ownership of the SBC domain by adding a TXT record to it. You’ll be shown a value that starts with `MS=`. Copy that TXT value.

Switch back to the Click2Call portal, paste it into the **Domain TXT Record Value** field on the Teams profile, and click **Save Default Profile**. The TXT record will be published on the `ms{account}.sbc.msteams.nz` domain within seconds.

Return to Microsoft and click **Verify**. If it fails, wait 30–60 seconds and click it again — DNS propagation is usually near-instant but occasionally lags. When the domain verifies successfully, Microsoft will offer to add online services (Exchange, SharePoint, etc.) to the domain. **Leave every checkbox unticked** — this domain is for Direct Routing only, not for mailboxes. Click **Continue** and then **Finish**.

4

#### Create a trunk user in Microsoft 365

Microsoft won’t attach a Direct Routing licence to a raw domain — it needs a user account on that domain to bind the licence to. The trunk user is a placeholder account that never signs in and never makes calls; its only job is to hold a Teams Phone licence against the SBC domain so Microsoft treats the domain as Teams-enabled.

In the Admin Centre, open **Users → Active users** and click **Add a user**.

Fill in the basics. Any name will do — we use Trunk User / username `tempuser`. Critically, in the **Domains** dropdown on the right, pick the SBC domain you just added (not your regular company domain). Leave Automatically create a password and Require this user to change their password when they first sign in ticked. Click **Next**.

On the **Assign product licenses** screen, choose **Australia** as the location and tick both:

- **Microsoft Teams Phone Standard** — the licence that enables Direct Routing calling.

- A base Office 365 licence such as **Office 365 E1** or higher — required as a companion to Teams Phone Standard.

If you don’t have a spare licence handy, temporarily remove one from an unused account, complete this setup, then reassign it. The trunk user only needs the licences during the initial configuration.

On the **Optional settings** screen leave both sections at their defaults (no admin role, no profile details) and click **Next**.

Review the summary and click **Finish adding**. The trunk user will appear in your Active users list within a few seconds.

5

#### Add Teams phone numbers in the Click2Call portal

Back in the Click2Call portal, open **Account → Numbers** and click **Add a new Number**. For each Teams user you’re setting up, choose **Australia** as the country, pick an Area (Sydney, Melbourne, Brisbane, Perth, Adelaide, etc.), and — the important bit — choose **Microsoft Teams** from the **Line Type** dropdown. Select a Teams plan and confirm the reservation.

If you’re porting existing numbers rather than picking new ones, use the **Port an existing number** button and mark the port request as a Teams line when prompted. See [Porting a number to Click2Call](https://www.click2call.com.au/help/how-to-port-number) for the full porting flow.

Repeat for every Teams user. When you’re done, open **Voice → Line Manager** and confirm each Teams line has a small blue Teams icon next to it. If the icon isn’t showing, edit the line and check that its Profile is set to your Teams-enabled profile from Step 1.

6

#### Map Teams numbers to Teams users

Open **Voice → Microsoft Teams** in the Click2Call portal. You’ll see a table listing every Teams-enabled number on your account, with an **Associated Teams User** field next to each.

For each row, enter the Microsoft 365 email address of the user who should own the number — the same email they use to sign in to Teams (e.g. `joe@yourcompany.com.au`). Then choose a **Call Mode**:

- **Teams Only** — calls ring only in the Teams app. Simplest and recommended for most users.

- **Teams/SIP Twinning** — calls ring in Teams and on a paired SIP device (desk phone or softphone). Useful when a user has both a physical phone and Teams.

Optionally set an **Unavailable Forwarding Number** (where calls go if Teams is offline) and a **Failover Forwarding Number** (a backup like a mobile). Leave **Teams Voicemail** enabled unless the user prefers the Click2Call voicemail system. Click **Save Changes**.

7

#### Run the PowerShell commands

The final piece connects the two sides. Microsoft needs to be told (a) that your SBC exists and is authorised to carry calls, and (b) which users are allowed to route their calls through it. That happens via PowerShell.

Click the orange **Power Shell** button on the Microsoft Teams Lines page. The portal generates the exact commands you need to run, pre-filled with your SBC hostname, each user’s email address, and their assigned phone number in E.164 format.

##### Prepare PowerShell

On a Windows machine, open **Windows PowerShell** as Administrator (right-click → Run as administrator). Then run these four commands one at a time. The first three only need to be run once per machine.

```
Install-Module MicrosoftTeams
Set-ExecutionPolicy RemoteSigned
Import-Module MicrosoftTeams
Connect-MicrosoftTeams
```

When `Connect-MicrosoftTeams` prompts, sign in with your Global Admin credentials. If PowerShell asks about installing from an untrusted repository, press **A** to accept all.

##### Tenant-level commands (run once)

These three commands tell Microsoft that Click2Call’s SBC is a valid PSTN gateway for your tenant. Replace `ms{account}.sbc.msteams.nz` with your actual SBC hostname from Step 1. You only run these once per tenant.

```
Set-CsOnlinePstnUsage -Identity Global -Usage @{Add="VOIP"}

New-CsOnlineVoiceRoute -Identity "VOIP" `
-NumberPattern ".*" `
-OnlinePstnGatewayList "ms{account}.sbc.msteams.nz" `
-Priority 1 `
-OnlinePstnUsages "VOIP"

New-CsOnlineVoiceRoutingPolicy -Identity "VOIP" -OnlinePstnUsages "VOIP"
```

##### Per-user commands (run for each Teams user)

For each user you want to enable calling for, run this block. Replace the email address and phone number with your own values. Numbers must be in full E.164 format — `+61` for Australia, no leading zero, no spaces (so 03 7050 0997 becomes `+61370500997`).

```
Set-CsPhoneNumberAssignment `
-Identity "joe@yourcompany.com.au" `
-PhoneNumber +61370500997 `
-PhoneNumberType DirectRouting

Grant-CsTeamsCallingPolicy `
-PolicyName AllowCalling `
-Identity "joe@yourcompany.com.au"

Grant-CsOnlineVoiceRoutingPolicy `
-Identity "joe@yourcompany.com.au" `
-PolicyName "VOIP"

Set-CsOnlineVoicemailUserSettings `
-Identity "joe@yourcompany.com.au" `
-VoicemailEnabled $false
```

The last command is optional — only include it if the user prefers voicemail to route to Click2Call rather than Teams. Leave it out to keep the standard Teams voicemail.

The exact block for your tenant and users, with values pre-filled, is generated on the **Power Shell** page in the Click2Call portal — copy from there rather than typing by hand.

8

#### Test the setup

Sign in to Teams (desktop or mobile) as one of the configured users. The dialpad should appear under **Calls** in the left sidebar — if it doesn’t, sign out and back in to force Teams to pick up the new voice routing policy. This can take up to 10 minutes after running the PowerShell commands.

Two quick tests:

- **Outbound:** dial an external Australian mobile from the Teams dialpad. Confirm it rings out and the caller ID shown on the receiving phone is the Click2Call number assigned to this user.

- **Inbound:** from a different phone, call the Australian number you assigned to the user. Confirm Teams rings and the call connects when answered.

If both work, you’re done. Repeat Steps 5–7 whenever you add another user.

### Common issues

Domain verification keeps failing

Confirm that you’ve saved the TXT value in the Click2Call portal — nothing gets published until you click **Save Default Profile**. If it’s saved and verification still fails, wait a full minute and retry. The value must include the `MS=` prefix exactly as Microsoft displayed it.

Teams dialpad doesn’t appear for the user

Three things to check: the user has a Teams Phone Standard licence assigned, the `Grant-CsTeamsCallingPolicy` and `Grant-CsOnlineVoiceRoutingPolicy` commands ran without error, and the user has signed out and back in. Policy changes can take up to 10 minutes to propagate in Teams.

Outbound calls fail immediately with a busy tone

Usually this means the Voice Routing Policy didn’t make it to the user. Re-run the two `Grant-` commands from Step 7. If it still fails, check that the PSTN Gateway hostname in `New-CsOnlineVoiceRoute` matches the SBC domain exactly (a typo here is common).

Inbound calls ring the wrong Teams user

The number-to-user mapping lives in the Click2Call portal (**Voice → Microsoft Teams**), not in Microsoft. Re-open that page and confirm the phone number is next to the correct **Associated Teams User** email.

We’re moving from Skype for Business to Teams

The Skype for Business Online service was retired by Microsoft in July 2021. If your tenant still has Skype for Business enabled, complete Microsoft’s Teams upgrade before starting this guide — see Microsoft’s Teams upgrade documentation.

### Related guides

[Microsoft Teams Calling overview](https://www.click2call.com.au/microsoft-teams-calling/)
[Adding a phone number](https://www.click2call.com.au/help/how-to-add-phone-number)
[Porting a number to Click2Call](https://www.click2call.com.au/help/how-to-port-number)

### Prefer we handle the setup?

Our Australian team can complete the whole Teams Direct Routing configuration end-to-end — SBC, licences, PowerShell, testing.

[Managed setup service](https://www.click2call.com.au/pricing/#managed-setup)
Call 1300 884 879

## Forwarding Calls to Your Mobile

Source: https://www.click2call.com.au/help/how-to-forward-calls-to-mobile

, Step by Step

1

#### Check your time zone

Log in to the portal and go to **Voice → Profiles**. Make sure the **Time Zone** on your Default Profile is set to your Australian zone (for example Australia/Brisbane). Every "Work Hours" rule below relies on it.

2

#### Set your work hours

Go to **Voice → Line Manager** and click your business number to open its Call Flow page. In the **Other Settings** dropdown choose **Time Schedules**, then under Work Hours enter your days and times in 24-hour format (for example Monday to Friday 07:00 to 16:00) and save.

3

#### Forward to your mobile during work hours

Back on the line page, open the **Incoming Calls** dropdown and choose **Call Forwarding**. Under Forward Always Rule #1 tick **Enabled**, enter your mobile number, set Time Schedule to **During Work Hours**, and tick **Forward Before all other features** so the divert wins over any other routing. Save. To know when a call has come through your business number, tick **Play a notification to the callee at the start of the call when the call has been forwarded** at the bottom of the Call Forwarding page. Whoever answers hears “call-forwarding” before the call connects. To play your own message instead, dial ***38** to record it (***39** removes it).

4

#### Send after-hours calls to voicemail-to-email

From the **Incoming Calls** dropdown choose **Voice Mail**. In Send a copy of my voicemail messages to the following email address enter your email (separate several with a semicolon) and save. Outside your work hours the forward is inactive, so callers reach voicemail and each message is emailed to you with a text transcript.

5

#### Record a greeting (optional)

Dial ***58** from any phone on your account to record your unavailable greeting, or upload an MP3 on the Voice Mail page. Test by calling your number from another phone inside and outside your work hours.

**Good to know:** During work hours, a diverted call that rings out is answered by your mobile’s own voicemail, not Click2Call’s. If you would rather always use Click2Call voicemail, use [Simultaneous Ring](https://www.click2call.com.au/help/how-to-create-ring-group) instead of Forward Always.

## Setting Up Missed Call Alerts

Source: https://www.click2call.com.au/help/how-to-set-up-missed-call-alerts

, Step by Step

1

#### Open the line

Go to **Voice → Line Manager** and click the number or extension you want alerts for.

2

#### Enable Missed Call Notifications

In the **Incoming Calls** dropdown choose **Missed Call Notifications** and tick **Enable Missed Call Notifications for the Line**. By default alerts go to the account holder’s email; add other recipients one per line if you like.

3

#### Add an SMS alert (optional)

Enter a mobile number in Send me an SMS when I have a missed call to also receive a text. Save, then test by letting a call ring out.

**Good to know:** Pair this with [forwarding to your mobile](https://www.click2call.com.au/help/how-to-forward-calls-to-mobile) or a ring group so fewer calls are missed in the first place. You can also see missed calls live on the [Call Dashboard](https://www.click2call.com.au/help/how-to-use-live-call-dashboard).

## Closing for Holidays

Source: https://www.click2call.com.au/help/how-to-close-for-holidays

, Step by Step

1

#### Open Do Not Disturb

Go to **Voice → Line Manager**, click your business number, and in the **Incoming Calls** dropdown choose **Do not Disturb**.

2

#### Choose what callers get

Tick **Enable Do not Disturb Service**. Leave the busy-tone option unticked so callers go to your voicemail, or enter a Do not Disturb Forwarding Number (for example a mobile) to divert them instead. Tick **Apply DND before all other features** so it overrides menus and queues.

3

#### Add your closure dates

In the dates box enter each closure as DD-MM-YYYY, or a range with a comma, and optionally times, for example `20-12-2026 17:00, 11-01-2027 09:00`. One line per range. Leave the box empty only if you want DND to apply every day.

4

#### Record a holiday greeting (optional)

Dial ***58** from any phone on the account to record an unavailable greeting mentioning your return date, or generate one with [AI Voicemail](https://www.click2call.com.au/help/how-to-set-up-ai-voicemail). Remember to re-record your normal greeting when you are back.

**Good to know:** If your business has set Work Hours, public holidays can also be treated as closed under **Other Settings → Time Schedules**, where you can add custom holiday dates for the whole year.

## Get an Alert When a Phone Goes Offline

Source: https://www.click2call.com.au/help/phone-offline-alerts

Line Monitoring checks every 5 minutes that your desk phone, adaptor or PBX is still connected. If it goes offline, you get an email, and it can also ring a number of your choice to tell you.

Last reviewed: October 2026

### What it can watch

Desk phones, adaptors and PBXs that log in (register) with the number’s SIP details, and registered SIP trunks.

It does not work for the Click2Call smartphone apps, SIP peering (direct IP) trunks, IAX2 connections or Microsoft Teams.

### Turn it on

- Go to **Voice → Line Manager** and click the number.
- Open the **Other Settings** menu and choose **Line Monitoring**.
- Tick **Enable Monitoring for the Line**.
- Alerts go to the account holder’s email. To send them elsewhere, list the addresses in **Alert Email Address recipients**, one per line.
- Optionally, enter a number at **If the phone goes offline then dial out to this number**. It is called and a message says the line has been disconnected.
- Save.

If the number has its own **Message Playback** recording, that recording is played on the call instead of the standard message.

**Good to know:** For an app on a mobile, use [missed call alerts](https://www.click2call.com.au/help/how-to-set-up-missed-call-alerts) instead, so you hear about calls you did not answer.

# Billing & Account

## Why Your Included Minutes Are Not Being Used

Source: https://www.click2call.com.au/help/why-included-minutes-are-not-being-used

A common surprise on the first bill: your plan includes minutes, but calls are still being charged while the allowance sits barely touched. Almost always this is one thing, and it is easy to check.

Last reviewed: September 2026

### Minutes belong to a number, not to your account

An included-minutes allowance is attached to **one specific phone number** on your account. It is not a shared pool that every line draws from.

So if you have more than one number, or a number plus an internal extension, only the line carrying the allowance gets the included minutes. Calls made from any other line are charged per minute, even though it is the same account and the same bill.

### How to check which line has them

- Log in to the portal and go to **Account** then **Plan**.

- Look for a line described as your number followed by **minutes**, for example `61XXXXXXXXX - minutes`. That is the number the allowance sits on.

- Now go to **Account** then **Records** and look at the calls being charged. The **Billed Number** column tells you which line each call was billed to.

If the charged calls show a different number or an extension, that is your answer.

### The most common cause: a divert

When an incoming call is diverted out to another number such as a mobile, the outbound leg is billed to **whichever line performs the divert**. If your call flow hands the call to an internal extension and the extension dials the mobile, the call is billed to the extension, which does not carry your allowance.

The fix is to set the divert on the number that holds the minutes, so the leg is billed there and draws on the allowance.

### What to do next

If the calls are coming from the right line and your allowance still is not being used, send us the account number and one or two example calls with their date and time. We can look at how each call was rated and tell you exactly what happened.

If you have several lines and want the allowance to cover all of them, that is a different product to a per-number allowance. Email support@click2call.com.au and we will go through the options with you.

## Adding Concurrent Call Channels

Source: https://www.click2call.com.au/help/how-to-add-channels

## How to Add More Phone Lines (Channels)

Increase your call capacity by adding more channels to your account, allowing more staff to be on the phone at the same time.

### What are Channels?

Think of a channel as a single phone line. If you have **two channels**, your business can make or receive a maximum of **two calls at the same time**. If a third call comes in while both channels are busy, that caller will go to voicemail or hear a busy signal.

Every Click2Call account comes with **2 free channels** by default. You also receive one extra free channel for every purchased phone number on your account (excluding Inbound Business Numbers).

#### How Many Channels Do I Need?

The number of channels you need depends on how many people will be on the phone simultaneously. A good rule of thumb for a typical office is to have **1 channel for every 3 to 4 users**. For example, a business with 10 staff members would likely need around 3 or 4 channels to avoid congestion.

#### How Much Do They Cost?

If you need more channels than are included with your plan, you can add them at any time. Channels are included with your Cloud PBX User plan. The cost is pro-rated for the first month.

1

#### Navigate to the Plan Page

Log in to the portal, click the **Account** tab, and then select **Plan** from the left-hand navigation menu.

2

#### Select the Channels Tab

On the Plan page, click the **Channels** tab to view your current channel count and make changes.

3

#### Choose the Total Number of Channels

From the dropdown menu, select the **total number of channels** you require for your account. The system will automatically calculate how many new channels are being added and the associated cost.

4

#### Update and Confirm

Review the ongoing and pro-rata costs for the new channels, then click the **Update Channels** button to confirm. The new channels will be active immediately.

## Viewing Account History & Downloading Invoices

Source: https://www.click2call.com.au/help/how-to-view-account-history

Billing & Account
2 min read

## How to View Account History & Download Invoices

The **Account History** page is where you can view every transaction on your Click2Call account and download PDF receipts or invoices for your records. This is useful for bookkeeping, expense claims, and providing proof of payment to your accountant or finance team.

Last reviewed: August 2026

What you will find in Account History

- Every payment, top-up, and charge on your account listed in date order.

- A **Reference number** for each transaction.

- A **PDF download** icon to save a receipt or invoice for each transaction.

- An **Export CSV** option to download your full transaction history as a spreadsheet.

1

### Log in to the portal

Go to portal.click2call.com.au and sign in with your account credentials. You will need to be the account administrator or have a user role with billing access to view transaction history.

2

### Navigate to Account → History

In the left-hand sidebar, click **History** under the Account section. The breadcrumb at the top of the page will show **Account / Account History** confirming you are in the right place.

3

### Understanding the Account History table

The table lists every transaction on your account in reverse chronological order (most recent first). Here is what each column means.

| Column | Description |

| Date | The date the transaction was processed on your account. |

| Transaction Type | A description of what the transaction was — for example, a card payment, a manual top-up, a monthly line fee charge, or a credit adjustment. |

| Amount | The dollar value of the transaction in AUD. Negative values (shown as $ -x.xx) indicate a debit from your account balance. Positive values indicate a credit added to your account. |

| Reference / Download | The unique reference number for the transaction. Click the PDF icon (red) next to the reference to download a receipt as a PDF file. Click the paperclip icon to copy or view the direct link to the receipt. |

| Export CSV | Click this link on any row to download your complete transaction history as a CSV spreadsheet file, suitable for importing into accounting software such as Xero, MYOB, or QuickBooks. |

4

### Download a receipt or invoice

To download a receipt for a specific transaction:

- Locate the transaction in the table using the **Date** and **Transaction Type** columns.

- In the **Reference/Download** column, click the **red PDF icon** on the right-hand side of the reference number.

- Your browser will download the receipt as a PDF file. The file name will include the transaction reference number for easy identification.

**Tip:** If you need to provide invoices to your accountant on a regular basis, use the **Export CSV** option to download all transactions at once rather than downloading individual PDFs.

5

### Export your full transaction history as a CSV

The CSV export gives you a complete record of all transactions on your account in a single file. This is the fastest way to provide a full billing history to your finance team or accountant.

- On the Account History page, click the **Export CSV** link in the last column of any row.

- Your browser will download a `.csv` file containing all transactions.

- Open the file in Microsoft Excel, Google Sheets, or your accounting software to view, filter, and sort the data.

**Note:** The CSV export includes all transactions — there is no date range filter. If you need to filter by date, open the file in a spreadsheet application and use the built-in filter tools.

### Frequently asked questions

Can I download invoices for all my payments?

Yes. Every transaction that appears in the Account History table has a PDF download icon. Click the red PDF icon next to the reference number to download the receipt for that specific transaction.

Do the receipts include GST?

Yes. The PDF receipts are tax invoices and include a GST breakdown. They are issued by Bcom Services Pty Ltd (ABN: 92 636 893 108) and are suitable for BAS reporting and expense claims.

What does a negative amount mean?

A negative amount (e.g. $ -5.00) means that amount was deducted from your account balance. This typically represents a payment made by your account to Click2Call — for example, a monthly line fee charge or a top-up payment processed from your saved card.

How far back does the Account History go?

The Account History page shows all transactions from the date your account was created. There is no limit on how far back the history goes. If you have a large number of transactions, use the Export CSV option to download the full list and sort or filter it in a spreadsheet application.

Can I filter transactions by date or type?

The Account History page does not have built-in date or type filters. To filter your transactions, export the history as a CSV file and open it in Microsoft Excel or Google Sheets, where you can use column filters to view transactions by date range or transaction type.

I cannot see the PDF download icon — what should I do?

The PDF icon appears in the Reference/Download column to the right of the reference number. If you are on a smaller screen, you may need to scroll the table horizontally to see the icon. If the icon is still not visible, try refreshing the page. If the issue persists, contact support at support@click2call.com.au.

Can sub-users view the Account History?

Account History is visible to the account administrator. Sub-users with limited portal access may not see the History section in their sidebar. If a team member needs access to billing records, the account administrator can download and share the PDF receipts or CSV export directly.

A transaction is missing from my history — what should I do?

If you believe a transaction is missing, first try refreshing the page and scrolling to the bottom of the list. If it is still not visible, contact our support team at support@click2call.com.au or call 1300 884 879 and we will investigate.

#### Related articles

[How to Manage Your Subscription
Top up your pre-pay balance](https://www.click2call.com.au/help/how-to-add-account-credit)
[Adding Additional Channels
Increase simultaneous call capacity](https://www.click2call.com.au/help/how-to-add-channels)
[Activating Your Account
First steps after signing up](https://www.click2call.com.au/help/how-to-activate-account)
[Back to Help Centre
Browse all guides](https://www.click2call.com.au/help/)

## Using Reports & Records

Source: https://www.click2call.com.au/help/how-to-use-reports-and-records

Billing & Account
4 min read

## How to Use Reports & Records

The Click2Call portal provides two separate tools for reviewing your call activity: **Reports** and **Records**. Reports give you a summarised view of call activity grouped by line, making them useful for reviewing usage across your team. Records give you a detailed, line-by-line view of every individual call, which is useful for investigating specific calls, verifying charges, or exporting raw data for analysis.

Last reviewed: August 2026

Reports vs Records — which one do you need?

|  | Reports | Records |

| What it shows | Summarised call totals per line | Individual call records |

| Best for | Usage overviews, team reporting | Investigating specific calls, charge verification |

| Export format | CSV | CSV |

| Email scheduling | Yes (daily, weekly, monthly) | No |

### Part 1 — Reports

Account → Reports  •  `portal.click2call.com.au/account/reporting`

1

#### Navigate to Account → Reports

In the left-hand sidebar, click **Reports** under the Account section. The page will load showing the **Call Report by Line** form. The breadcrumb at the top will show **Account / Reports**.

2

#### Configure the report filters

The Reports page contains several filters that control what data is included in your report. Here is a full explanation of every field.

| Field | Description |

| Report type | The type of report to generate. Call Report by Line is the default and shows call activity summarised per phone line or extension. |

| Bill period | The billing period to report on. Defaults to the current billing period. You can select a previous billing period from the dropdown to review historical data. |

| Calendar month | Filter results to a specific calendar month. Select All Months to include all months within the selected bill period. |

| From Date / To Date | Narrow the report to a specific date range within the selected bill period. Enter dates in YYYY-MM-DD format (e.g. 2026-03-01). Leave blank to include all dates in the period. |

| Record Types | Filter by the type of billing record to include. Options include All billing records, inbound calls, outbound calls, or specific call types. Use this to isolate particular types of activity. |

| Search Filter | A free-text search field. Enter a phone number, extension name, or partial string to filter results to matching lines only. |

| Email Call Reports by Line | Set a schedule to automatically email this report. Options include Never, daily, weekly, or monthly. When set, the report will be emailed to the address in the Report Email Recipient field on the selected schedule. |

| Report Email Recipient | The email address to send scheduled reports to. Click Update to save the email address after entering it. |

3

#### Generate or export the report

Once you have configured your filters, use one of the two action buttons:

-

Submit — displays the report results on screen in the table below the form. The table shows each line with columns for Service, Name, Records, Answered, Busy, No Answer, Minutes, and Voice charges.

-

Export — downloads the report as a CSV file without displaying it on screen. Use this when you want to open the data in a spreadsheet application such as Excel or Google Sheets.

**Tip:** The **Totals** row at the bottom of the on-screen report shows the sum of all lines. This is useful for quickly seeing your total call volume and minutes for the selected period.

### Part 2 — Records

Account → Records  •  `portal.click2call.com.au/account/billingrecords`

4

#### Navigate to Account → Records

In the left-hand sidebar, click **Records** under the Account section. The page will load showing the **Billing Records** search form. Unlike Reports, this page shows every individual call as a separate row, giving you a granular view of all activity on your account.

5

#### Configure the search filters

The Billing Records page has a comprehensive set of filters to help you find exactly the calls you are looking for. Here is a full explanation of every field.

| Field | Description |

| Bill Period | The billing period to search within. Defaults to the current period. Select a previous period from the dropdown to search historical records. |

| Call Type | Filter by the type of call — for example, all call types, inbound, outbound, or specific call categories. Useful for isolating inbound-only or outbound-only activity. |

| Calling Number | The number that made the call (the originating number). Enter a full or partial number to search for calls from a specific caller. Format: 6492345678. |

| Called Number | The number that was dialled (the destination number). Enter a full or partial number to search for calls to a specific number. Format: 64289212345. |

| From Date / To Date | Narrow results to a specific date range. Enter dates in YYYY-MM-DD format. Leave blank to search across the entire selected bill period. |

| Calls longer than (seconds) | Filter out very short calls by entering a minimum duration in seconds. For example, entering 30 will only show calls that lasted 30 seconds or longer. Useful for excluding unanswered or very brief calls from your results. |

| Billing Group | If your account uses billing groups to separate lines or departments, select a specific group to filter results to that group only. Defaults to All Groups. |

| Answered Calls | When ticked, only calls that were answered will be included in the results. Untick to include all calls regardless of whether they were answered. |

| Charged Items | When ticked, only calls that incurred a charge will be included. This is useful for reviewing exactly which calls contributed to your bill. |

| Results Limit | The maximum number of records to return per search. Defaults to 10,000. If your account has a very high call volume, you may need to narrow your date range to stay within this limit, or use the Export function to download the full dataset. |

6

#### Search or export billing records

Once you have set your filters, use one of the two action buttons:

-

Search — displays matching call records on screen in a paginated table. Use the **Results per page** dropdown and the **Previous / Next** buttons to navigate through results.

-

Export — downloads the matching records as a CSV file. The export respects all active filters, so you will only receive the records that match your search criteria.

**Note:** If the search returns **No Results Found**, check that the selected **Bill Period** contains activity and that your filters are not too restrictive. Try removing the date range or unchecking the **Answered Calls** and **Charged Items** filters to broaden the search.

### Frequently asked questions

What is the difference between Reports and Records?

Reports provide a summarised view of call activity grouped by phone line or extension — showing totals for answered calls, busy calls, no-answer calls, total minutes, and charges. Records provide a detailed view of every individual call, including the exact calling and called numbers, call duration, date and time, and whether the call was charged. Use Reports for an overview and Records when you need to investigate specific calls.

Can I schedule reports to be emailed automatically?

Yes. On the Reports page, use the **Email Call Reports by Line** dropdown to select a schedule (daily, weekly, or monthly). Enter the recipient's email address in the **Report Email Recipient** field and click **Update** to save. The report will be emailed automatically on the selected schedule. This feature is available on the Reports page only — the Records page does not support scheduled email delivery.

How far back can I search call records?

Both Reports and Records are organised by billing period. You can select any previous billing period from the **Bill Period** dropdown to access historical data. Records are retained from the date your account was created, so you can search as far back as your account history allows.

My search returns No Results Found — what should I check?

First, confirm that the selected **Bill Period** is the correct one — it is easy to accidentally leave it on the current period when you intended to search a previous one. Next, remove any date range filters and uncheck the **Answered Calls** and **Charged Items** checkboxes to broaden the search. If you are searching by phone number, ensure the number is entered in the correct format (e.g. `6492345678` without spaces or dashes).

What does the Calls longer than field do?

This filter lets you exclude very short calls from your results. Enter a duration in seconds — for example, entering `10` will only show calls that lasted more than 10 seconds. This is useful for filtering out unanswered calls, voicemail drops, or very brief accidental calls that would otherwise clutter your results.

Can I export more than 10,000 records at once?

The default results limit is 10,000 records per search. If your account has more than 10,000 calls in a period, narrow the date range using the **From Date** and **To Date** fields and run multiple exports to cover the full period. For example, export the first two weeks of the month, then the second two weeks, and combine the files in a spreadsheet application.

What format are the dates in the exported CSV?

Dates in the exported CSV files are in `YYYY-MM-DD` format and times are in 24-hour format. If you are importing the CSV into accounting software or a reporting tool, you may need to reformat the date column to match the expected format of that application.

Can I see call recordings from the Records page?

The Billing Records page shows call metadata (date, time, numbers, duration, charges) but does not provide access to call recordings. Call recordings, if enabled on your account, are accessible from the **Media** section of the portal.

### Related articles

[Account History & Invoices
Download PDF receipts and transaction history](https://www.click2call.com.au/help/how-to-view-account-history)
[How to Manage Your Subscription
Top up your pre-pay balance](https://www.click2call.com.au/help/how-to-add-account-credit)
[Setting Up a Call Flow
Route inbound calls to the right destination](https://www.click2call.com.au/help/how-to-set-up-call-flow)
[Back to Help Centre
Browse all guides](https://www.click2call.com.au/help/)

## Plans, Numbers and Channels

Source: https://www.click2call.com.au/help/plans-numbers-and-channels

: What You Pay For

You pay for each phone number on its own plan, and extensions are free. Your account also has a number of channels: how many calls can be in progress at once. This guide explains each charge and how to change a number’s plan.

Last reviewed: October 2026

### What each number costs

| Plan | Price | What it’s for |
| Cloud PBX User | $25 + GST a month ($27.50) | A full business line for making and receiving calls, with 300 outbound minutes a month included. |
| Inbound Business Number | $10 + GST a month ($11.00) | A number for receiving calls. It has no included minutes. |
| Microsoft Teams User | $25 + GST a month ($27.50) | A number used for calling inside Microsoft Teams. |
| Internal extension | Free | A short extension on your phone system, for a person, a voicemail box or a feature. |

When you add a number partway through a month, you first pay for the part of the month that is left. After that it is charged in full each month.

### Included minutes belong to one number

The 300 minutes on a Cloud PBX User plan are used only by calls made from that number. Calls made from your other numbers or extensions are charged per minute, even though they are on the same account and the same bill. If your minutes seem unused, check which number the calls were made from.

### See what you are paying for

- **Account → Numbers** lists every number and extension with its line type, line plan, minutes used and monthly cost including GST.
- **Account → Plan → Line Plans** shows the plan on each number.
- **Current Account Details**, at the bottom of the Plan page, lists every monthly charge on the account.

### Change a number’s plan

- Go to **Account → Numbers**.
- Under **Your Numbers**, click **Edit this number** next to the number.
- Choose the new **Line plan**. You can also change the **Line type** to Voice, Web Conference or Microsoft Teams.
- Click **Update Line**.

### Your account plan and bundles

**Account → Plan → Account Plan** shows the base plan for the whole account: its monthly charge and what it includes, such as channels. Account bundles are minute bundles that any number on the account can use. If bundles are available on your account, you will find them under **Account → Plan → Account Bundles**.

### Channels

A channel is one call in progress. Your account includes 2 channels, and some numbers you add bring an extra one. If every channel is busy, the next caller goes to voicemail or hears a busy tone.

Extra channels are $3 + GST each. To add them, go to **Account → Plan → Channels**, choose the total you need, and review the price before you confirm.

**Good to know:** Prices are in Australian dollars. Your call charges and monthly fees come out of your account credit, so keep enough credit on the account or turn on automatic top-ups.

# AI Features

## Setting Up the AI Receptionist

Source: https://www.click2call.com.au/help/how-to-set-up-ai-receptionist

**Not an AI voice agent.** The AI Receptionist is an automated call routing tool — similar to a traditional auto attendant (press 1 for Sales, press 2 for Support), but instead of pressing numbers, callers simply say what they need. The AI matches what the caller says to the department descriptions you configure, then transfers the call to the right number or extension. A real person answers the call. The AI Receptionist does not hold a conversation, answer questions, or act as a virtual agent. If you are looking for an AI voice agent, view the [AI Agents help guide](https://www.click2call.com.au/help/how-to-set-up-ai-agents).

The AI Receptionist answers incoming calls automatically, plays a welcome greeting, listens to the caller's request, and routes the call to the correct department or person. This guide shows you how to set it up.

### Setting Up the AI Receptionist, Step by Step

1

#### Log in to the portal

Navigate to portal.click2call.com.au and sign in with your user
credentials.

2

#### Navigate to AI Receptionist

In the main portal navigation,
click **AI**, then select **AI Receptionist** from the
left-hand menu.

3

#### Configure the Welcome
Message

This is the first message your callers will hear when the AI Receptionist picks up. Enter a short, friendly greeting that tells the caller to say the name of the department or reason for their call. For example: `'Hello, thank you for calling. Please say the name of the department you need, such as Sales, Support, or Accounts.'`

The caller does not need to press any buttons. They simply speak their request and the system matches it to one of your configured departments.

You can also configure the
following settings in this section:

- **AI Voice:** Choose the voice and language for the
receptionist.

- **Replay Message:** The number of times a message will
be replayed if the caller is silent.

- **Silence Timeout:** The seconds of silence to wait
before replaying a message.

- **Total Timeout:** The total seconds of silence before
the call is ended or routed to the default.

- **Hold/Failure Message:** Toggle on or off messages for
hold and call failure scenarios.

4

#### Add Departments

Departments are the core of the AI Receptionist. When a caller speaks their request, the AI compares what they said against each department's description and routes the call to the best match. Think of each department as equivalent to one option on a traditional auto attendant menu — except the caller says what they need rather than pressing a number.

Click the **Add a new Department** button to get started. You can add as many departments as you need — for example, Sales, Support, Accounts, and Reception.

5

#### Create a New Department

Fill in the details for your new
department:

- **Department Name:** A friendly name, e.g.,
'Sales' or 'Support'.

- **Description:** This is the most important field. Write a clear description of what this department handles and include the words or phrases a caller might say when they want to reach it. For example, for a Sales department you might write: 'Sales, new enquiries, quotes, pricing, buying, purchasing, products'. The AI matches the caller's spoken words against this description to decide where to route the call. The more relevant keywords you include, the more accurately calls will be routed.

- **Route to Number:** The phone number or extension where
calls for this department should be sent.

6

#### Configure Call Flow Settings

Finally, define how calls get to
the AI Receptionist and what happens if a department can't be identified.

- **Incoming Call Routing:** Select which of your main
business numbers should be answered by the AI Receptionist.

- **Default Route:** Set a fallback number where the call
will be sent if the AI cannot determine the correct department from the caller's
request.

- **Allow Transfers to User Extensions:** Toggle whether
callers can be transferred directly to a user's extension.

7

#### Test the AI Receptionist

Call one of the numbers you assigned to the AI Receptionist from an external phone. When prompted, say the name of a department or a phrase a real caller might use — for example, 'I'd like to speak to someone about a quote' or just 'Sales'. Confirm that the call transfers to the correct destination. Test each department you have configured. If a call routes incorrectly, update the department description to include more specific keywords.

## Connecting an AI Voice Agent to Your Number

Source: https://www.click2call.com.au/help/how-to-connect-ai-voice-agent

Point an Australian phone number at an AI voice agent. Click2Call has built-in profiles for the major platforms — ElevenLabs, OpenAI, xAI, Retell, VAPI and others — and anything else that speaks SIP connects by registration. This guide covers both, plus the three settings that catch most people out.

Last reviewed: October 2026

### Connecting Your Agent, Step by Step

1

#### Check whether your provider is built in

Open **Voice → Profiles** and open the **Connection Type** list. Click2Call ships ready-made profiles for the major AI voice platforms:
[Eleven Labs AI](https://www.click2call.com.au/help/how-to-connect-elevenlabs)[OpenAI](https://www.click2call.com.au/help/how-to-connect-openai)[xAI](https://www.click2call.com.au/help/how-to-connect-xai)[Retell AI](https://www.click2call.com.au/help/how-to-connect-retell-ai)[VAPI AI Integration](https://www.click2call.com.au/help/how-to-connect-vapi)[Synthflow](https://www.click2call.com.au/help/how-to-connect-synthflow)[LiveKit Cloud](https://www.click2call.com.au/help/how-to-connect-livekit)[Cloudonix](https://www.click2call.com.au/help/how-to-connect-cloudonix)[Twilio Integration](https://www.click2call.com.au/help/how-to-connect-twilio)
If your provider is on that list, select it and Click2Call fills in the SIP route for you. A few profiles ask for one identifier — an OpenAI Project ID, a VAPI Assistant ID, a Twilio or LiveKit subdomain — and the rest need nothing at all. Each name above links to a step-by-step guide covering both ends of the connection.
Not on the list? That is fine — anything that speaks SIP still connects using the generic method in the next step.

2

#### For any other provider, use SIP Registration

Set **Connection Type** to **SIP Registration**. Your AI platform then registers to Click2Call the way a softphone or desk phone does, using the phone number as its username.
This is the step people most often get wrong. It is tempting to pick SIP Peering (Direct IP) because you are joining two platforms — but peering means the two ends trust each other by IP address, with no credentials at all. If you have a username and password, you want registration.

3

#### Get the credentials for the line

Open **Voice → Line Manager**. Each number has a **Password** column with a **View** control that reveals the SIP password for that line. The username is the number itself, in full international format.
Treat the line password as a credential. Anyone holding it can register a device as that number and place calls billed to your account.

4

#### Enter the details on the AI platform

In the platform’s SIP or trunk settings, choose registration-based authentication — some platforms label this “username and password” as opposed to “IP” — then enter the values below.

### SIP Credentials Reference

Enter these values exactly as shown into your phone's SIP account settings.

| Username / Login / User ID | Your Click2Call phone number including country codee.g. 61234567890 |

| Authorisation Name / Display Name | Your Click2Call phone number including country codee.g. 61234567890 |

| Password | Your Click2Call password (set in the Password box on the number’s row in Voice → Line Manager) |

| Host / Proxy / Domain | sip.click2call.com.au |

| Outbound Proxy | sip.click2call.com.au |

| SIP Transport | UDP, TCP, or TLS — TLS preferred |

| SIP Port | 5060 or 50600 (UDP/TCP)  •  5061 (TLS) |

| DTMF Mode | RFC 2833 (also listed as AVT or Out-of-Band) |

| STUN Server | Not required |

5

#### Check the number is on the right profile

Back in **Line Manager**, confirm the **Profile** column for that number points at the profile you configured.
This one catches almost everybody. The default profile applies to every line with no profile assigned, and new numbers land on it automatically — so a number left on Default quietly ignores the profile you just spent your morning setting up.

6

#### Set the time zone on the profile

While you are in the profile, check the **Time Zone**. Every time-based behaviour on the account reads it — business hours, after-hours routing and call queue schedules all follow this setting.
If the phones open and close at the wrong local time, this is almost always why.

7

#### Test it

Ring the number from a mobile. Your agent should answer within a couple of seconds.
If the call reaches Click2Call voicemail instead, work through the troubleshooting below.

### The address to allowlist

When Click2Call delivers a call to an external SIP endpoint — any of the built-in provider profiles, or your own **Inbound SIP URI Route** — the INVITE leaves our switch from:

103.212.52.19

That is the address to put on the provider’s IP allowlist, ACL or access control list. Click2Call cannot present a username and password on an outbound INVITE, so allowlisting is the only way a provider can trust us — if they challenge the call for credentials, it fails.

Some providers only accept individual addresses rather than CIDR ranges. This is a single address, so that is not a problem. Do not allowlist the address that sip.click2call.com.au resolves to — that is the inbound proxy, used when a device registers to us, and it is not where outbound INVITEs come from.

### Guides for Each Built-In Provider

The Click2Call side is much the same for all of them. What differs is what the provider needs at their end — and whether you need to write any code at all.

| Provider | Click2Call field | At the provider end |

| Eleven Labs AI | no extra fields | No code |

| OpenAI | OpenAI Project ID | Needs a webhook |

| xAI | no extra fields | Needs a webhook |

| Retell AI | no extra fields | No code |

| VAPI AI Integration | VAPI Assistant ID | No code |

| Synthflow | no extra fields | No code |

| LiveKit Cloud | Subdomain and Region | Needs an agent worker |

| Cloudonix | no extra fields | Needs a voice application |

| Twilio Integration | Twilio Subdomain | TwiML or Studio Flow |

### Troubleshooting

#### 407 Proxy Authentication Required, over and over
Work out which way the 407 is travelling, because the two causes are opposites.
**The AI platform is being challenged as it registers to Click2Call.** The profile is set to **SIP Peering (Direct IP)** when it should be **SIP Registration**. Peering carries no username or password — the two ends trust each other by IP. If you have credentials, switch to SIP Registration and let the platform register in.
**The provider is challenging our outbound INVITE.** Their end is asking us to authenticate, which means our signalling address is not on their allowlist. Click2Call cannot present a username and password on an outbound INVITE, so this is never fixed with credentials — have the provider allowlist **103.212.52.19**, the address our switch sends INVITEs from. Callers hear “the number you have called is not available from this service” while this is happening.

#### Calls land on Click2Call voicemail instead of the agent
Check three things, in this order. Is the platform actually registered? Is the number assigned to your profile rather than Default? And is an **Inbound SIP URI Route** set on the profile? A URI route overrides delivery to registered endpoints and forces the call to that URI — so never set one on a profile that uses registration.

#### Registration fails, or the platform reports the endpoint unreachable
Make sure the transport matches the port. Port 5061 is TLS only; a platform set to UDP while pointing at 5061 will never connect. Use TLS on 5061, or UDP/TCP on 5060. All three transports are supported — we recommend TLS, but the right choice is whichever the platform at the other end handles well.

#### TLS connects but the platform rejects the certificate
Some SIP clients verify the TLS certificate hostname strictly and drop the connection before authenticating, reporting a certificate or hostname mismatch. Two ways forward. If the platform lets you relax hostname verification, do that and stay on TLS. If it does not, fall back to **TCP on port 5060** — Click2Call accepts UDP, TCP or TLS, so the connection will work, you just lose the encryption on the signalling. Either way it is worth telling [support](https://www.click2call.com.au/support/), because we would rather sort out TLS for you than leave you on TCP.

#### After-hours or queue schedules trigger at the wrong time
The profile **Time Zone** is set to the wrong region. Business hours, after-hours routing and queue schedules all read it. Correct the time zone on the profile and the schedules follow.

#### Everything looks right and the agent still does not answer
Confirm **Call Forward Always** is off on the line, and that no other call flow feature is configured on that number. A queue, ring group or auto-attendant on the same line takes the call before your agent does.

### Frequently Asked Questions

#### Which AI voice platforms are supported?
Ready-made profiles exist for Eleven Labs AI, OpenAI, xAI, Retell AI, VAPI, Synthflow, LiveKit Cloud, Cloudonix and Twilio. Anything else that speaks SIP connects using generic SIP Registration.

#### What happens if my AI platform doesn’t answer?
With a built-in profile (Eleven Labs AI, OpenAI, Retell AI and the others), Click2Call sends the call straight to the platform. If the platform doesn’t answer, the call is **not** failed over to voicemail or another number. If continuity matters, connect the platform with **SIP Registration** instead.

#### What address does my AI provider need to allowlist?
103.212.52.19. That is where outbound INVITEs leave our switch when a call is delivered to an external SIP endpoint. It is not the same as the address sip.click2call.com.au resolves to, which is the inbound proxy used for registration.

#### What username and password does the platform use?
Username and authorisation name are both the phone number in full international format. The password is the line password from Line Manager. Host and outbound proxy are sip.click2call.com.au.

#### Does the call still get recorded and transcribed?
Yes — provided **Recording Enabled** is ticked on the profile, calls answered by an AI agent are recorded, transcribed, summarised and sentiment-scored like any other. Those transcripts are how most customers improve what their agent says. See [AI voice tools](https://www.click2call.com.au/ai-voice-tools/).

#### Can I use my existing business number?
Yes. Port it across first — see [number porting](https://www.click2call.com.au/number-porting/) — then point it at your agent. Or test on a new number and move the main one once you are happy.

## Connecting ElevenLabs to Your Phone Number

Source: https://www.click2call.com.au/help/how-to-connect-elevenlabs

Click2Call has a built-in Eleven Labs AI connection profile, so pointing an Australian number at an ElevenLabs agent takes one dropdown at our end and a number import at theirs. No code, no SIP settings to type.

Last reviewed: September 2026

### At a glance

Mandatory Click2Call fieldNone — just pick the connection type

Where Click2Call sends callssip:sip.rtc.elevenlabs.io:5060;transport=tcp

AuthenticationIP allowlist (ACL) on the ElevenLabs side — add 103.212.52.19

Number format+E.164, set automatically

Code requiredNo — the agent is built in the ElevenLabs dashboard

Provider documentationElevenLabs SIP trunking

### Connecting ElevenLabs, Step by Step

1

#### Build the agent in ElevenLabs

In the ElevenLabs Agents dashboard, create the agent that should answer the phone — its prompt, voice, knowledge and tools. Everything is configured in their dashboard; there is nothing to deploy.

2

#### Import your Click2Call number into ElevenLabs

Open **Phone Numbers** and choose **Import a phone number from SIP trunk**. Fill in:

- **Label** — anything that helps you find it later.
- **Phone number** — in E.164 format, e.g. +61355551234. It has to match exactly.
- **Transport** — TCP, to match what Click2Call sends.
- **Authentication** — choose ACL and allowlist the Click2Call signalling addresses.
Click2Call cannot present a username and password on an outbound INVITE, so the provider has to trust us by **IP allowlist**. Allowlist **103.212.52.19** — that is the address our switch sends INVITEs from. If a provider will only accept authenticated INVITEs, the connection has to run the other way round — the provider registers to Click2Call as the number, which is the generic method in [connecting an AI voice agent](https://www.click2call.com.au/help/how-to-connect-ai-voice-agent).

3

#### Assign the agent to the number

Still in ElevenLabs, attach the agent to the number you just imported. Until an agent is assigned, calls reach ElevenLabs and go nowhere.

4

#### Create the profile in Click2Call

In the Click2Call portal open **Voice → Profiles** and set **Connection Type** to **Eleven Labs AI**.
There are no extra fields to fill in. Click2Call already knows the route — you can see it on the **Inbound SIP URI Route** line as sip:sip.rtc.elevenlabs.io:5060;transport=tcp — and the number format is set to +E.164 automatically.

5

#### Assign your number, then check the time zone

Open **Voice → Line Manager** and set the **Profile** column for your number to the profile you just created.
The Default profile applies to every line with no profile assigned, and new numbers land on it automatically — a number left on Default will ignore everything you just configured. While you are in the profile, set the **Time Zone** to where the business operates: business hours, after-hours routing and queue schedules all read it.

6

#### Test the call

Ring the number from a mobile. The agent should answer. If it does not, work through the checks below.

### Troubleshooting

#### The provider replies 407 Proxy Authentication Required
The provider is challenging our INVITE for a username and password, which means our signalling address is not on their allowlist. Click2Call cannot answer that challenge on an outbound call, so the fix is always at the provider end — allowlist 103.212.52.19 rather than issuing credentials. While this is happening, callers hear “the number you have called is not available from this service”.

#### The call reaches ElevenLabs but no agent answers
Either the number was not imported in exactly the format Click2Call sends (+E.164, with the plus), or no agent is assigned to it. Check both in the ElevenLabs Phone Numbers screen.

#### Calls are rejected before ringing
The ACL on the ElevenLabs side does not include the address Click2Call is signalling from. Ask [support](https://www.click2call.com.au/support/) for the current addresses.

#### Calls go to Click2Call voicemail instead
The number is still on the Default profile rather than your ElevenLabs profile, so it never leaves for ElevenLabs. Check the Profile column in Line Manager.

#### The agent answers but audio is one-way
Almost always a media path problem on the ElevenLabs side. Confirm the media encryption setting on the imported number matches what your trunk sends — Click2Call sends unencrypted media on TCP by default.

### Frequently Asked Questions

#### Do I need to write code?
No. This is one of the no-code providers — the agent is built in the ElevenLabs dashboard, and Click2Call needs one dropdown. Compare that with [OpenAI](https://www.click2call.com.au/help/how-to-connect-openai) and [xAI](https://www.click2call.com.au/help/how-to-connect-xai), which both need a webhook you host.

#### What number format does ElevenLabs expect?
E.164 — +61355551234, not 03 5555 1234. Click2Call sends +E.164 automatically, so import it that way.

#### Are calls still recorded and transcribed?
Yes, provided **Recording Enabled** is ticked on the profile. Recording, transcription, summaries and sentiment all work as normal, stored in Australia and New Zealand. See [AI voice tools](https://www.click2call.com.au/ai-voice-tools/).

#### Can I use my existing business number?
Yes — [port it across](https://www.click2call.com.au/number-porting/) first, then assign it to the profile.

## Connecting OpenAI to Your Phone Number

Source: https://www.click2call.com.au/help/how-to-connect-openai

Click2Call has a built-in OpenAI connection profile: enter your Project ID and calls to your Australian number are routed to the OpenAI Realtime API. This guide covers both ends — what to set up in the OpenAI platform, and what to configure in Click2Call.

Last reviewed: September 2026

### Before you start: this one needs code
OpenAI’s SIP integration is not a no-code setup. When a call arrives, OpenAI sends a realtime.call.incoming event to a webhook you host, and your code has to accept the call before any audio connects. If you want an agent you configure in a dashboard with no server of your own, [ElevenLabs, Retell or Synthflow](https://www.click2call.com.au/help/how-to-connect-ai-voice-agent) are the simpler choices — Click2Call supports those too.

### Connecting OpenAI, Step by Step

1

#### Find your OpenAI Project ID

Sign in at platform.openai.com and open **Settings → Project → General**. The Project ID is shown there and begins with proj_.
Copy it — this is the one value Click2Call needs.

2

#### Set up a webhook that accepts calls

In the OpenAI platform, open **Settings → Project → Webhooks** and register an endpoint you control.
When someone rings your number, OpenAI sends that endpoint a realtime.call.incoming event containing a call_id. Your code accepts the call using that id, and that is also where you give the agent its instructions and context.
This is the step that catches people. Until your webhook accepts the call, the phone will ring and nothing will answer. OpenAI’s own Realtime API with SIP guide has the request format and sample code.

3

#### Create the profile in Click2Call

In the portal open **Voice → Profiles**, set **Connection Type** to **OpenAI**, and paste your Project ID into the **OpenAI Project ID** field.
That field is mandatory — the profile will not save without it. Click2Call then builds the SIP address for you and sets the number format to +E.164 automatically. There is no SIP URI to type.

4

#### Assign your number to the profile

Open **Voice → Line Manager** and set the **Profile** column for your number to the profile you just created.
The default profile applies to every line that has no profile assigned, and new numbers land on it automatically. A number left on Default will ignore everything you just configured.

5

#### Check the time zone, then test

While you are in the profile, confirm the **Time Zone** matches where the business operates — business hours, after-hours routing and queue schedules all read it.
Then ring the number from a mobile. Your webhook should receive the incoming-call event, and the agent answers once your code accepts it.

### Troubleshooting

#### The provider replies 407 Proxy Authentication Required
The provider is challenging our INVITE for a username and password, which means our signalling address is not on their allowlist. Click2Call cannot answer that challenge on an outbound call, so the fix is always at the provider end — allowlist 103.212.52.19 rather than issuing credentials. While this is happening, callers hear “the number you have called is not available from this service”.

#### The profile will not save
The **OpenAI Project ID** field is empty or malformed. It is mandatory, and the value should begin with proj_. Copy it from Settings → Project → General rather than typing it.

#### The phone rings but nothing answers
Almost always the webhook. Either it is not registered in the OpenAI project, it is not reachable from the internet, or it is receiving the event but not accepting the call. Check your endpoint logs for a realtime.call.incoming event.

#### Calls go to Click2Call voicemail instead
The number is still on the Default profile rather than your OpenAI profile, so the call never leaves for OpenAI at all. Check the Profile column in Line Manager.

#### Calls connect but the agent has no context
Context is supplied by your code at the moment it accepts the call, not by Click2Call. Review the accept request in OpenAI’s SIP guide — that is where the session instructions belong.

### Frequently Asked Questions

#### Do I need to write code?
Yes, for OpenAI specifically. The Click2Call side is configuration only, but OpenAI requires a webhook you host to accept each call. If you would rather not run a server, ElevenLabs, Retell and Synthflow are configured entirely in their own dashboards — see [connecting an AI voice agent](https://www.click2call.com.au/help/how-to-connect-ai-voice-agent).

#### Where is my Project ID?
platform.openai.com → Settings → Project → General. It starts with proj_.

#### Are calls still recorded and transcribed?
Yes, provided **Recording Enabled** is ticked on the profile. Recording, transcription, summaries and sentiment all work as normal on the Click2Call side, stored in Australia and New Zealand. See [AI voice tools](https://www.click2call.com.au/ai-voice-tools/).

#### Can I use my existing business number?
Yes — [port it across](https://www.click2call.com.au/number-porting/) first, then assign it to the profile. Most businesses test on a new number and move the main one once the agent behaves.

## Connecting Retell AI to Your Phone Number

Source: https://www.click2call.com.au/help/how-to-connect-retell-ai

Retell does not sell Australian numbers, so bringing your own is the only way to put a Retell agent on a local landline or a 1300 number. Click2Call has a built-in Retell AI connection profile that makes it a one-dropdown job.

Last reviewed: September 2026

### At a glance

Mandatory Click2Call fieldNone — just pick the connection type

Where Click2Call sends callssip:sip.retellai.com;transport=tcp

AuthenticationIP allowlist on the Retell side — add 103.212.52.19

Number format+E.164, set automatically

Code requiredNo — the agent is built in the Retell dashboard

Provider documentationRetell AI custom telephony

### Connecting Retell AI, Step by Step

1

#### Build the agent in Retell

In the Retell AI dashboard, create the agent that should answer the phone — prompt, voice, functions and knowledge base. It is all dashboard configuration; there is nothing to deploy.

2

#### Import your Click2Call number into Retell

Open **Phone Numbers** and import your existing number rather than buying one from Retell. Enter it in E.164 format, e.g. +61355551234 — it has to match what Click2Call sends.
This is the whole reason to use bring-your-own-number: Retell does not sell Australian geographic numbers, so importing a Click2Call number is how you get an AI agent answering a local landline or a 1300 number.

3

#### Assign the agent to the number

Attach the agent you built as the **inbound** agent for that number. Until one is assigned, calls arrive at Retell and are not answered.
Click2Call cannot present a username and password on an outbound INVITE, so the provider has to trust us by **IP allowlist**. Allowlist **103.212.52.19** — that is the address our switch sends INVITEs from. If a provider will only accept authenticated INVITEs, the connection has to run the other way round — the provider registers to Click2Call as the number, which is the generic method in [connecting an AI voice agent](https://www.click2call.com.au/help/how-to-connect-ai-voice-agent).

4

#### Create the profile in Click2Call

In the Click2Call portal open **Voice → Profiles** and set **Connection Type** to **Retell AI**.
There are no extra fields. The **Inbound SIP URI Route** line already shows sip:sip.retellai.com;transport=tcp, and the number format is set to +E.164 automatically.

5

#### Assign your number, then check the time zone

Open **Voice → Line Manager** and set the **Profile** column for your number to the profile you just created.
The Default profile applies to every line with no profile assigned, and new numbers land on it automatically — a number left on Default will ignore everything you just configured. While you are in the profile, set the **Time Zone** to where the business operates: business hours, after-hours routing and queue schedules all read it.

6

#### Test the call

Ring the number from a mobile. The agent should answer, and the call should appear in both the Retell call history and your Click2Call call records.

### Troubleshooting

#### The provider replies 407 Proxy Authentication Required
The provider is challenging our INVITE for a username and password, which means our signalling address is not on their allowlist. Click2Call cannot answer that challenge on an outbound call, so the fix is always at the provider end — allowlist 103.212.52.19 rather than issuing credentials. While this is happening, callers hear “the number you have called is not available from this service”.

#### The call reaches Retell but no agent answers
The number was not imported in the format Click2Call sends (+E.164, with the plus), or no inbound agent is assigned to it. Check both in the Retell Phone Numbers screen.

#### Calls are rejected before ringing
Retell is not accepting traffic from the address Click2Call signals from. Ask [support](https://www.click2call.com.au/support/) for the current addresses and allowlist them.

#### Calls go to Click2Call voicemail instead
The number is still on the Default profile rather than the provider profile, so the call never leaves for the provider at all. Check the Profile column in Line Manager.

#### The agent answers but cannot transfer calls
Warm and cold transfers are configured in the Retell agent, not in Click2Call. If a transfer target is another extension on your account, dial it as a full number rather than an internal extension.

### Frequently Asked Questions

#### Do I need to write code?
No. Retell is one of the no-code providers. Compare with [OpenAI](https://www.click2call.com.au/help/how-to-connect-openai) and [xAI](https://www.click2call.com.au/help/how-to-connect-xai), which both need a webhook you host.

#### Do I have to buy a number from Retell?
No — that is the point of this setup. Retell does not sell Australian geographic numbers, so importing a Click2Call number is how you get an agent on a local landline or a [1300 number](https://www.click2call.com.au/blog/1300-number-providers).

#### Are calls still recorded and transcribed?
Yes, provided **Recording Enabled** is ticked on the profile. Recording, transcription, summaries and sentiment all work as normal on the Click2Call side, stored in Australia and New Zealand. See [AI voice tools](https://www.click2call.com.au/ai-voice-tools/).

#### Can I use my existing business number?
Yes — [port it across](https://www.click2call.com.au/number-porting/) first, then assign it to the profile. Local and mobile numbers typically port in 5 to 10 business days.

## Connecting Synthflow to Your Phone Number

Source: https://www.click2call.com.au/help/how-to-connect-synthflow

Click2Call has a built-in Synthflow connection profile, including their non-standard inbound port, so putting a Synthflow assistant on an Australian number is one dropdown here and a number import there.

Last reviewed: September 2026

### At a glance

Mandatory Click2Call fieldNone — just pick the connection type

Where Click2Call sends callssip:sipin.synthflow.ai:35681;transport=tcp

AuthenticationIP allowlist on the Synthflow side — add 103.212.52.19

Number format+E.164, set automatically

CodecsG.711 recommended, Opus supported — both standard on Click2Call

Code requiredNo — the assistant is built in the Synthflow dashboard

Provider documentationSynthflow SIP integration

### Connecting Synthflow, Step by Step

1

#### Build the assistant in Synthflow

In the Synthflow dashboard, create the assistant that should answer the phone — prompt, voice, actions and knowledge. It is all dashboard configuration.

2

#### Import your Click2Call number into Synthflow

Open **Phone Numbers** and use the **Import Phone Number** form:

- **Number type** — Custom.
- **Phone number** — E.164 format, e.g. +61355551234.
- **Friendly name** — whatever helps you find it later.
Click2Call cannot present a username and password on an outbound INVITE, so the provider has to trust us by **IP allowlist**. Allowlist **103.212.52.19** — that is the address our switch sends INVITEs from. If a provider will only accept authenticated INVITEs, the connection has to run the other way round — the provider registers to Click2Call as the number, which is the generic method in [connecting an AI voice agent](https://www.click2call.com.au/help/how-to-connect-ai-voice-agent).

3

#### Assign the assistant to the number

Attach the assistant to the imported number so inbound calls have somewhere to land.

4

#### Create the profile in Click2Call

In the Click2Call portal open **Voice → Profiles** and set **Connection Type** to **Synthflow**.
There are no extra fields. The **Inbound SIP URI Route** line already shows sip:sipin.synthflow.ai:35681;transport=tcp. The port is non-standard, which is normal for Synthflow, and Click2Call handles it for you.

5

#### Assign your number, then check the time zone

Open **Voice → Line Manager** and set the **Profile** column for your number to the profile you just created.
The Default profile applies to every line with no profile assigned, and new numbers land on it automatically — a number left on Default will ignore everything you just configured. While you are in the profile, set the **Time Zone** to where the business operates: business hours, after-hours routing and queue schedules all read it.

6

#### Test the call

Ring the number from a mobile. The assistant should answer and the call should appear in the Synthflow call log.

### Troubleshooting

#### The provider replies 407 Proxy Authentication Required
The provider is challenging our INVITE for a username and password, which means our signalling address is not on their allowlist. Click2Call cannot answer that challenge on an outbound call, so the fix is always at the provider end — allowlist 103.212.52.19 rather than issuing credentials. While this is happening, callers hear “the number you have called is not available from this service”.

#### The call reaches Synthflow but nothing answers
The number was not imported in +E.164 format, or no assistant is assigned to it. Check both on the Synthflow Phone Numbers screen.

#### Synthflow documentation mentions a different host and port
Synthflow publishes several SIP endpoints, including sip.synthflow.ai:32681 for UDP or TCP and sip.synthflow.ai:32682 for TLS. The built-in Click2Call profile uses their dedicated inbound host, sipin.synthflow.ai:35681, so you do not need to choose — leave it as it is.

#### Calls go to Click2Call voicemail instead
The number is still on the Default profile rather than the provider profile, so the call never leaves for the provider at all. Check the Profile column in Line Manager.

#### The assistant answers but audio is choppy
Check the codec on the Synthflow side. G.711 is the safest choice and is what Click2Call offers by default; Opus works too but is more sensitive to a poor connection.

### Frequently Asked Questions

#### Do I need to write code?
No. Synthflow is one of the no-code providers. [OpenAI](https://www.click2call.com.au/help/how-to-connect-openai) and [xAI](https://www.click2call.com.au/help/how-to-connect-xai) both need a webhook you host.

#### Why is the port so unusual?
Synthflow runs its inbound SIP service on a high port rather than the usual 5060. The built-in profile already points at it, so there is nothing for you to configure.

#### Are calls still recorded and transcribed?
Yes, provided **Recording Enabled** is ticked on the profile. Recording, transcription, summaries and sentiment all work as normal on the Click2Call side, stored in Australia and New Zealand. See [AI voice tools](https://www.click2call.com.au/ai-voice-tools/).

#### Can I use my existing business number?
Yes — [port it across](https://www.click2call.com.au/number-porting/) first, then assign it to the profile. Local and mobile numbers typically port in 5 to 10 business days.

## Connecting Vapi to Your Phone Number

Source: https://www.click2call.com.au/help/how-to-connect-vapi

Vapi is the shortest setup of all the built-in profiles: copy your Assistant ID out of the Vapi dashboard, paste it into Click2Call, assign your number. There is nothing to configure at the Vapi end.

Last reviewed: September 2026

### At a glance

Mandatory Click2Call field**VAPI Assistant ID** — the assistant's UUID

Where Click2Call sends callssip:<assistant_id>@sip.vapi.ai:5060

AuthenticationNone required — Vapi's hosted SIP endpoint does not use registration

Number format+E.164, set automatically

Code requiredNo for call routing; only if you add custom tools to the assistant

Provider documentationVapi SIP introduction

### Connecting Vapi, Step by Step

1

#### Build the assistant in Vapi

In the Vapi dashboard, create the assistant that should answer the phone — prompt, voice, model and any tools it needs.

2

#### Copy the Assistant ID

Open the assistant and copy its **ID**. It is a UUID, shown alongside the assistant in the dashboard and also returned by the GET /assistant API endpoint.
This is the only value Click2Call needs. Vapi identifies the assistant from the user part of the SIP address, so there is no separate phone-number import step at their end and no SIP credentials to exchange.

3

#### Create the profile in Click2Call

In the Click2Call portal open **Voice → Profiles** and set **Connection Type** to **VAPI AI Integration**.
Paste the Assistant ID into the **VAPI Assistant ID** field. It is mandatory — the profile will not save without it. Click2Call then builds the route for you, shown under the field as sip:<assistant_id>@sip.vapi.ai:5060, and sets the number format to +E.164.

4

#### Assign your number, then check the time zone

Open **Voice → Line Manager** and set the **Profile** column for your number to the profile you just created.
The Default profile applies to every line with no profile assigned, and new numbers land on it automatically — a number left on Default will ignore everything you just configured. While you are in the profile, set the **Time Zone** to where the business operates: business hours, after-hours routing and queue schedules all read it.

5

#### Test the call

Ring the number from a mobile. The assistant should answer, and the call should appear in the Vapi call log.

### Troubleshooting

#### The provider replies 407 Proxy Authentication Required
The provider is challenging our INVITE for a username and password, which means our signalling address is not on their allowlist. Click2Call cannot answer that challenge on an outbound call, so the fix is always at the provider end — allowlist 103.212.52.19 rather than issuing credentials. While this is happening, callers hear “the number you have called is not available from this service”.

#### The profile will not save
The **VAPI Assistant ID** field is empty or the value is not a valid assistant UUID. Copy it from the Vapi dashboard rather than typing it.

#### The call connects but Vapi rejects it
Usually the Assistant ID belongs to a deleted assistant, or it was pasted with surrounding whitespace. Re-copy it and save the profile again.

#### Calls go to Click2Call voicemail instead
The number is still on the Default profile rather than the provider profile, so the call never leaves for the provider at all. Check the Profile column in Line Manager.

#### You need calls to terminate in the EU
The built-in profile uses the US host sip.vapi.ai. Vapi also runs sip.eu.vapi.ai. Contact [support](https://www.click2call.com.au/support/) and we will set up a custom SIP route rather than the built-in profile.

### Frequently Asked Questions

#### Where is my Assistant ID?
In the Vapi dashboard, opened against the assistant — it is a UUID. The GET /assistant endpoint returns it too.

#### Do I need to write code?
Not for routing. The assistant is dashboard-configured; code is only needed if you want custom tools. Compare with [OpenAI](https://www.click2call.com.au/help/how-to-connect-openai) and [xAI](https://www.click2call.com.au/help/how-to-connect-xai), where a webhook is mandatory.

#### Do I have to buy a number from Vapi?
No. Vapi does not sell Australian geographic numbers, so bringing a Click2Call number is normally the only way to put a Vapi assistant on a local landline or a [1300 number](https://www.click2call.com.au/blog/1300-number-providers).

#### Are calls still recorded and transcribed?
Yes, provided **Recording Enabled** is ticked on the profile. Recording, transcription, summaries and sentiment all work as normal on the Click2Call side, stored in Australia and New Zealand. See [AI voice tools](https://www.click2call.com.au/ai-voice-tools/).

## Connecting LiveKit Cloud to Your Phone Number

Source: https://www.click2call.com.au/help/how-to-connect-livekit

Click2Call has a built-in LiveKit Cloud connection profile: give it your project subdomain and region and calls to your Australian number land in a LiveKit room. The work is mostly at the LiveKit end — a trunk, a dispatch rule, and an agent to answer.

Last reviewed: September 2026

### Before you start: this one needs code
LiveKit Cloud is real-time media infrastructure, not a hosted agent. Once the call lands in a LiveKit room, something has to join that room and speak to the caller — normally a **LiveKit Agents worker you write and deploy**. If you want an agent you configure in a dashboard with no server of your own, [ElevenLabs](https://www.click2call.com.au/help/how-to-connect-elevenlabs), [Retell](https://www.click2call.com.au/help/how-to-connect-retell-ai) or [Synthflow](https://www.click2call.com.au/help/how-to-connect-synthflow) are the simpler choices.

### At a glance

Mandatory Click2Call fields**LiveKit Subdomain** and **Region**

Where Click2Call sends callssip:<subdomain>.<region>.sip.livekit.cloud:5060;transport=tcp

SubdomainYour project ID without the p_ prefix

Regione.g. us1, eu1

Also needed in LiveKitAn inbound trunk and a dispatch rule

Code requiredYes — an agent must join the room

Provider documentationLiveKit inbound SIP trunks

### Connecting LiveKit Cloud, Step by Step

1

#### Find your subdomain and region

Your SIP subdomain is the LiveKit project ID with the p_ prefix stripped off. Run lk project list --json and read the ProjectId field — a project ID of p_vjnxecm0tjk gives a subdomain of vjnxecm0tjk.
The region is the LiveKit region your project runs in. Region values look like us1 and eu1.

2

#### Create an inbound trunk

In the LiveKit Cloud dashboard open **Telephony → SIP trunks** and create a trunk with direction **Inbound**. List your Click2Call number in E.164 format.
If you leave the numbers list empty, LiveKit requires you to set either a username and password or an allowed-addresses list instead — it will not accept an unauthenticated trunk that matches everything.

Click2Call cannot present a username and password on an outbound INVITE, so the provider has to trust us by **IP allowlist**. Allowlist **103.212.52.19** — that is the address our switch sends INVITEs from. If a provider will only accept authenticated INVITEs, the connection has to run the other way round — the provider registers to Click2Call as the number, which is the generic method in [connecting an AI voice agent](https://www.click2call.com.au/help/how-to-connect-ai-voice-agent).

3

#### Create a dispatch rule

LiveKit will not accept an inbound call without at least one **dispatch rule**, which decides which room the caller is placed into. Putting each caller in their own room is the usual starting point.

4

#### Make sure an agent is running

A LiveKit room with nobody in it is silence. Deploy a LiveKit Agents worker that joins the room and handles the conversation before you test.

5

#### Create the profile in Click2Call

In the Click2Call portal open **Voice → Profiles** and set **Connection Type** to **LiveKit Cloud**.
Enter the subdomain in the first field and the region in the second — both are mandatory and the profile will not save without them. Click2Call joins them into sip:<subdomain>.<region>.sip.livekit.cloud:5060;transport=tcp, shown under the fields.

6

#### Assign your number, then check the time zone

Open **Voice → Line Manager** and set the **Profile** column for your number to the profile you just created.
The Default profile applies to every line with no profile assigned, and new numbers land on it automatically — a number left on Default will ignore everything you just configured. While you are in the profile, set the **Time Zone** to where the business operates: business hours, after-hours routing and queue schedules all read it.

7

#### Test the call

Ring the number from a mobile. The call should appear as a participant in a LiveKit room, and your agent should answer it.

### Troubleshooting

#### The provider replies 407 Proxy Authentication Required
The provider is challenging our INVITE for a username and password, which means our signalling address is not on their allowlist. Click2Call cannot answer that challenge on an outbound call, so the fix is always at the provider end — allowlist 103.212.52.19 rather than issuing credentials. While this is happening, callers hear “the number you have called is not available from this service”.

#### The profile will not save
Both the **Subdomain** and **Region** fields are mandatory. Fill in both, without the p_ prefix on the subdomain and without .sip.livekit.cloud on either.

#### LiveKit rejects the call
Either the inbound trunk does not match — the number is not listed and no authentication is configured — or there is no dispatch rule. LiveKit needs both before it will accept a call.

#### The call connects to silence
The room was created and the caller joined it, but no agent joined. Check that your LiveKit Agents worker is running and registered to the right room pattern.

#### Calls go to Click2Call voicemail instead
The number is still on the Default profile rather than the provider profile, so the call never leaves for the provider at all. Check the Profile column in Line Manager.

### Frequently Asked Questions

#### Where is my subdomain?
It is the project ID minus the p_ prefix. lk project list --json shows it, and so does the dashboard.

#### What region should I use?
Whichever region your LiveKit project runs in — values look like us1 and eu1. Click2Call shows the finished route once both fields are filled.

#### Do I need to write code?
Yes. LiveKit is media infrastructure, so you deploy an agent that joins the room. For a dashboard-only agent use [ElevenLabs](https://www.click2call.com.au/help/how-to-connect-elevenlabs), [Retell](https://www.click2call.com.au/help/how-to-connect-retell-ai) or [Synthflow](https://www.click2call.com.au/help/how-to-connect-synthflow) instead.

#### Are calls still recorded and transcribed?
Yes, provided **Recording Enabled** is ticked on the profile. Recording, transcription, summaries and sentiment all work as normal on the Click2Call side, stored in Australia and New Zealand. See [AI voice tools](https://www.click2call.com.au/ai-voice-tools/).

#### Can I use my existing business number?
Yes — [port it across](https://www.click2call.com.au/number-porting/) first, then assign it to the profile. Local and mobile numbers typically port in 5 to 10 business days.

## Connecting xAI to Your Phone Number

Source: https://www.click2call.com.au/help/how-to-connect-xai

Click2Call has a built-in xAI connection profile, so the routing is one dropdown. The work is at the xAI end: register a bring-your-own-trunk number, host a webhook, and open a WebSocket to answer each call.

Last reviewed: September 2026

### Before you start: this one needs code
xAI’s SIP integration is a developer integration. You register the phone number through their API, host a webhook that receives the realtime.call.incoming event, and open a WebSocket to answer each call. If you want an agent you configure in a dashboard with no server of your own, [ElevenLabs](https://www.click2call.com.au/help/how-to-connect-elevenlabs), [Retell](https://www.click2call.com.au/help/how-to-connect-retell-ai) or [Synthflow](https://www.click2call.com.au/help/how-to-connect-synthflow) are the simpler choices.

### At a glance

Mandatory Click2Call fieldNone — just pick the connection type

Where Click2Call sends callssip:sip.voice.x.ai:5061;transport=tls

AuthenticationIP allowlist (allowed_addresses) on the xAI side — add 103.212.52.19

Number format+E.164, set automatically

Code requiredYes — a webhook plus a WebSocket connection

Provider documentationxAI SIP phone calls

### Connecting xAI, Step by Step

1

#### Register a Direct SIP phone number with xAI

Using the xAI API, create a Direct SIP phone number with origin set to byo_trunk — the number is yours, arriving over your own trunk. Include the webhook URL that should receive incoming-call events.
xAI returns a **signing secret** once and never again. Store it before you close the response; you need it to verify webhook signatures.

2

#### Choose an authentication method

xAI accepts either an IP allowlist, via allowed_addresses, or SIP digest credentials.
Click2Call cannot present a username and password on an outbound INVITE, so the provider has to trust us by **IP allowlist**. Allowlist **103.212.52.19** — that is the address our switch sends INVITEs from. If a provider will only accept authenticated INVITEs, the connection has to run the other way round — the provider registers to Click2Call as the number, which is the generic method in [connecting an AI voice agent](https://www.click2call.com.au/help/how-to-connect-ai-voice-agent).

3

#### Handle the incoming-call webhook

When a call arrives, xAI posts a realtime.call.incoming event to your webhook. Verify the signature with your signing secret, then read the call_id from the payload.

4

#### Open a WebSocket to answer

Connect to wss://api.x.ai/v1/realtime with the call_id and your API key. Send session.update to configure the agent for this call, then response.create when it should start speaking.

5

#### Create the profile in Click2Call

In the Click2Call portal open **Voice → Profiles** and set **Connection Type** to **xAI**.
There are no extra fields. The **Inbound SIP URI Route** line already shows sip:sip.voice.x.ai:5061;transport=tls — note that xAI uses TLS on 5061 rather than plain TCP on 5060 — and the number format is set to +E.164 automatically.

6

#### Assign your number, then check the time zone

Open **Voice → Line Manager** and set the **Profile** column for your number to the profile you just created.
The Default profile applies to every line with no profile assigned, and new numbers land on it automatically — a number left on Default will ignore everything you just configured. While you are in the profile, set the **Time Zone** to where the business operates: business hours, after-hours routing and queue schedules all read it.

7

#### Test the call

Ring the number from a mobile. Your webhook should receive the incoming-call event, and the agent answers once your WebSocket session is established.

### Troubleshooting

#### The provider replies 407 Proxy Authentication Required
The provider is challenging our INVITE for a username and password, which means our signalling address is not on their allowlist. Click2Call cannot answer that challenge on an outbound call, so the fix is always at the provider end — allowlist 103.212.52.19 rather than issuing credentials. While this is happening, callers hear “the number you have called is not available from this service”.

#### The phone rings but nothing answers
Almost always the webhook. Either the Direct SIP number was registered without a webhook URL, the endpoint is not reachable from the internet, or it receives the event but never opens the WebSocket. Check your endpoint logs for a realtime.call.incoming event.

#### Webhook signature verification fails
The signing secret is only returned when the number is created. If it was not stored, register the number again to get a fresh one.

#### xAI rejects the call before it rings
The allowed_addresses list does not include the address Click2Call is signalling from. Ask [support](https://www.click2call.com.au/support/) for the current addresses.

#### Calls go to Click2Call voicemail instead
The number is still on the Default profile rather than the provider profile, so the call never leaves for the provider at all. Check the Profile column in Line Manager.

### Frequently Asked Questions

#### Do I need to write code?
Yes — a webhook and a WebSocket. Same shape as [OpenAI](https://www.click2call.com.au/help/how-to-connect-openai). For a dashboard-only agent, use [ElevenLabs](https://www.click2call.com.au/help/how-to-connect-elevenlabs), [Retell](https://www.click2call.com.au/help/how-to-connect-retell-ai) or [Synthflow](https://www.click2call.com.au/help/how-to-connect-synthflow).

#### What does byo_trunk mean?
That the number is yours and arrives over your own SIP trunk rather than being provisioned by xAI. Provisioning xAI numbers through the API is not supported, so this is how an Australian number reaches a Grok voice agent.

#### Why port 5061 and TLS?
xAI terminates SIP over TLS. The built-in profile already uses sip:sip.voice.x.ai:5061;transport=tls, so there is nothing to change.

#### Are calls still recorded and transcribed?
Yes, provided **Recording Enabled** is ticked on the profile. Recording, transcription, summaries and sentiment all work as normal on the Click2Call side, stored in Australia and New Zealand. See [AI voice tools](https://www.click2call.com.au/ai-voice-tools/).

#### Can I use my existing business number?
Yes — [port it across](https://www.click2call.com.au/number-porting/) first, then assign it to the profile. Local and mobile numbers typically port in 5 to 10 business days.

## Connecting Twilio to Your Phone Number

Source: https://www.click2call.com.au/help/how-to-connect-twilio

If your call logic already lives in Twilio — a Studio Flow, an IVR, a Flex contact centre — but you want an Australian number with local porting and local support, the built-in Twilio Integration profile routes calls straight into your Twilio SIP Domain.

Last reviewed: September 2026

### At a glance

Mandatory Click2Call field**Twilio Subdomain** — the first label only

Where Click2Call sends callssip:<subdomain>.sip.twilio.com:5060;transport=tcp

Twilio productSIP Domain (Programmable Voice) — not Elastic SIP Trunking

AuthenticationIP Access Control List on the Twilio SIP Domain — add 103.212.52.19

Number format+E.164, set automatically

Code requiredNo, if you use a Studio Flow or TwiML Bin

Provider documentationTwilio: sending SIP into Twilio

### Connecting Twilio, Step by Step

1

#### Create a SIP Domain in Twilio

In the Twilio Console open **Voice → Manage → SIP Domains** and create a domain. The name you choose becomes <subdomain>.sip.twilio.com.
SIP domain names are unique across every Twilio account, not just yours, so the obvious short names are long gone. Something like acme-voice-au will usually be free.

2

#### Point the domain at your call logic

Set the domain’s **Voice Configuration** Request URL. Twilio fetches it when a call arrives and executes whatever TwiML comes back.
If you would rather not write code, point it at a **Studio Flow** or a **TwiML Bin** — both produce valid TwiML without a server of your own.

3

#### Secure the domain with an IP Access Control List

Twilio will not accept SIP traffic to a domain that has neither an IP Access Control List nor a Credential List. Create an **IP Access Control List** and add the Click2Call signalling addresses.
Use an IP Access Control List, not a Credential List. Click2Call cannot present a username and password on an outbound INVITE, so a Credential List alone will reject every call. Add **103.212.52.19** to the Access Control List — that is the address our switch sends INVITEs from.

4

#### Create the profile in Click2Call

In the Click2Call portal open **Voice → Profiles** and set **Connection Type** to **Twilio Integration**.
Enter only the first label in the **Twilio Subdomain** field — if your Twilio domain is acme-voice.sip.twilio.com, type acme-voice. The field is mandatory. Click2Call appends the rest and shows the finished route under the field.

5

#### Assign your number, then check the time zone

Open **Voice → Line Manager** and set the **Profile** column for your number to the profile you just created.
The Default profile applies to every line with no profile assigned, and new numbers land on it automatically — a number left on Default will ignore everything you just configured. While you are in the profile, set the **Time Zone** to where the business operates: business hours, after-hours routing and queue schedules all read it.

6

#### Test the call

Ring the number from a mobile. Twilio should fetch your Voice Configuration URL and run the TwiML it returns. The Twilio Console call logs will show the request and any errors.

### Troubleshooting

#### The provider replies 407 Proxy Authentication Required
The provider is challenging our INVITE for a username and password, which means our signalling address is not on their allowlist. Click2Call cannot answer that challenge on an outbound call, so the fix is always at the provider end — allowlist 103.212.52.19 rather than issuing credentials. While this is happening, callers hear “the number you have called is not available from this service”.

#### The profile will not save
The **Twilio Subdomain** field is empty. It is mandatory. Enter only the first label, not the full hostname and not a sip: prefix.

#### Twilio rejects the call with 403 Forbidden
The IP Access Control List on the SIP domain does not include the address Click2Call is signalling from, or the domain has no ACL and no Credential List at all. Twilio requires at least one.

#### Twilio accepts the call but nothing happens
The Voice Configuration Request URL is missing, unreachable, or returning something that is not valid TwiML. The Twilio Console call logs show the exact response Twilio received.

#### You configured Elastic SIP Trunking and it does not work
Elastic SIP Trunking termination uses a host ending in pstn.twilio.com, which is a different product. The Click2Call profile routes to sip.twilio.com, so you need a **SIP Domain** under Voice → Manage.

#### Calls go to Click2Call voicemail instead
The number is still on the Default profile rather than the provider profile, so the call never leaves for the provider at all. Check the Profile column in Line Manager.

### Frequently Asked Questions

#### What goes in the Subdomain field?
Only the first label. For acme-voice.sip.twilio.com, enter acme-voice.

#### SIP Domain or Elastic SIP Trunking?
SIP Domain. Elastic SIP Trunking termination ends in pstn.twilio.com and is for sending calls out to the PSTN; a SIP Domain hands the call to your TwiML, Studio Flow or voice application, which is what you want here.

#### Do I need to write code?
Not necessarily — a Studio Flow or a TwiML Bin returns valid TwiML with no server of your own. You only need code if the call logic has to reach your systems.

#### Are calls still recorded and transcribed?
Yes, provided **Recording Enabled** is ticked on the profile. Recording, transcription, summaries and sentiment all work as normal on the Click2Call side, stored in Australia and New Zealand. See [AI voice tools](https://www.click2call.com.au/ai-voice-tools/).

#### Can I use my existing business number?
Yes — [port it across](https://www.click2call.com.au/number-porting/) first, then assign it to the profile. Local and mobile numbers typically port in 5 to 10 business days.

## Connecting Cloudonix to Your Phone Number

Source: https://www.click2call.com.au/help/how-to-connect-cloudonix

Cloudonix is a programmable layer between the carrier and whatever answers the call. Click2Call has a built-in Cloudonix connection profile, so the routing is one dropdown — the work is the voice application at their end.

Last reviewed: September 2026

### Cloudonix is a layer, not an agent
Cloudonix is programmable SIP middleware. It receives the call, runs a voice application you have written, and hands the call on — often to an AI provider such as Vapi or Retell. If all you want is one AI agent answering one number, connect that provider directly and skip the extra hop: [Vapi](https://www.click2call.com.au/help/how-to-connect-vapi), [Retell](https://www.click2call.com.au/help/how-to-connect-retell-ai), [ElevenLabs](https://www.click2call.com.au/help/how-to-connect-elevenlabs).

### At a glance

Mandatory Click2Call fieldNone — just pick the connection type

Where Click2Call sends callssip:trunk.cloudonix.com:5060;transport=tcp

AuthenticationIP allowlist on the Cloudonix inbound trunk — add 103.212.52.19

Number format+E.164, set automatically

Code requiredYes — a Cloudonix voice application

Provider documentationCloudonix developer resources

### Connecting Cloudonix, Step by Step

1

#### Create a Cloudonix domain

In the Cloudonix portal, create the domain this number belongs to. Each domain gets its own inbound SIP hostname, which appears in the information box at the top of the **Inbound Trunks** section — it looks like <uuid>.sip.cloudonix.net.
You need a separate Cloudonix SIP trunk for each domain, so plan the domain layout before you start wiring numbers up.

2

#### Configure the inbound trunk

In **Inbound Trunks**, set up the trunk that will receive calls from Click2Call and allowlist the Click2Call signalling addresses.
Click2Call cannot present a username and password on an outbound INVITE, so the provider has to trust us by **IP allowlist**. Allowlist **103.212.52.19** — that is the address our switch sends INVITEs from. If a provider will only accept authenticated INVITEs, the connection has to run the other way round — the provider registers to Click2Call as the number, which is the generic method in [connecting an AI voice agent](https://www.click2call.com.au/help/how-to-connect-ai-voice-agent).

3

#### Write the voice application

A Cloudonix voice application is a script that decides what happens to each call. To hand the call to an AI agent platform, use the <Dial><Service> verb.
Until an application is attached to the domain, calls arrive and go nowhere.

4

#### Create the profile in Click2Call

In the Click2Call portal open **Voice → Profiles** and set **Connection Type** to **Cloudonix**.
There are no extra fields. The **Inbound SIP URI Route** line already shows sip:trunk.cloudonix.com:5060;transport=tcp, and the dialled number arrives in +E.164 format for your Cloudonix application to match on.

5

#### Assign your number, then check the time zone

Open **Voice → Line Manager** and set the **Profile** column for your number to the profile you just created.
The Default profile applies to every line with no profile assigned, and new numbers land on it automatically — a number left on Default will ignore everything you just configured. While you are in the profile, set the **Time Zone** to where the business operates: business hours, after-hours routing and queue schedules all read it.

6

#### Test the call

Ring the number from a mobile and watch the Cloudonix call logs. You should see the call arrive and your voice application run.

### Troubleshooting

#### The provider replies 407 Proxy Authentication Required
The provider is challenging our INVITE for a username and password, which means our signalling address is not on their allowlist. Click2Call cannot answer that challenge on an outbound call, so the fix is always at the provider end — allowlist 103.212.52.19 rather than issuing credentials. While this is happening, callers hear “the number you have called is not available from this service”.

#### The call arrives at Cloudonix and stops
No voice application is attached to the domain, or the application is not matching the dialled number. Remember the number arrives in +E.164 format, with the leading plus.

#### Cloudonix rejects the call
The inbound trunk is not accepting traffic from the address Click2Call signals from. Ask [support](https://www.click2call.com.au/support/) for the current addresses and allowlist them.

#### Calls go to Click2Call voicemail instead
The number is still on the Default profile rather than the provider profile, so the call never leaves for the provider at all. Check the Profile column in Line Manager.

#### You are not sure you need Cloudonix at all
If one agent answers one number, you probably do not. Connect the AI provider directly with its own Click2Call profile and remove a hop from the call path.

### Frequently Asked Questions

#### What is Cloudonix for?
Programmable call logic between the carrier and whatever handles the call. It earns its place when routing decisions happen before the agent, when you want to swap AI providers without touching carrier config, or when several services share one number.

#### Do I need it for a single AI agent?
No. Connect the provider directly — [Vapi](https://www.click2call.com.au/help/how-to-connect-vapi), [Retell](https://www.click2call.com.au/help/how-to-connect-retell-ai), [ElevenLabs](https://www.click2call.com.au/help/how-to-connect-elevenlabs) and the rest all have their own built-in profile.

#### Are calls still recorded and transcribed?
Yes, provided **Recording Enabled** is ticked on the profile. Recording, transcription, summaries and sentiment all work as normal on the Click2Call side, stored in Australia and New Zealand. See [AI voice tools](https://www.click2call.com.au/ai-voice-tools/).

#### Can I use my existing business number?
Yes — [port it across](https://www.click2call.com.au/number-porting/) first, then assign it to the profile. Local and mobile numbers typically port in 5 to 10 business days.

## Setting Up AI Agents

Source: https://www.click2call.com.au/help/how-to-set-up-ai-agents

Last reviewed: August 2026

**AI Agents vs AI Receptionist — what is the difference?** The [AI Receptionist](https://www.click2call.com.au/help/how-to-set-up-ai-receptionist) is an automated call routing tool. It listens to what a caller says and transfers the call to the right department — a real person then answers. An **AI Agent** is fundamentally different: it holds a full, two-way conversation with the caller, answers questions, provides information about your business, and can handle entire calls without any human involvement. AI Agents are trained on your own business knowledge base.

AI Agents are conversational AI voice agents that answer incoming calls, greet callers, and respond to their questions in natural language — 24 hours a day, 7 days a week. This guide walks you through creating a Business Profile, configuring your first AI Agent, and assigning it to a phone number.

### How to Set Up an AI Agent, Step by Step

1

#### Log in to the portal

Navigate to portal.click2call.com.au and sign in with your user credentials.

2

#### Navigate to AI Agents

In the top navigation bar, click **AI**. In the left-hand sidebar, click **AI Agents**. You will see the AI Agents overview page, which shows a blue information banner explaining that you can train AI Voice Agents by uploading documents to your Knowledge Base. Before you can create an agent, you must first set up a Business Profile.

3

#### Create your Business Profile

Click the **Create Business Profile** button. The Business Profile is the knowledge base your AI Agent will draw on when answering caller questions. The more detail you provide here, the more accurately and helpfully your agent will respond. The profile is divided into several sections.

Complete each section of the Business Profile:

- **Business Contact Details:** Enter your Business Name, Phone Number, Email, Website, and Physical Address. This information allows the agent to tell callers how to contact your business.

- **Business Category:** Enter your industry type, for example Telecommunications, Accounting, or Retail. This helps the AI understand the context of your business.

- **Business Description:** Write a clear description of your business and any important information you want the agent to share with callers. Include your key services, what makes your business different, and any details callers commonly ask about.

- **Operating Hours:** Enter your Regular Operating Hours (for example, Monday to Friday, 8am to 6pm) and your Public Holiday Hours. The agent can use this information to tell callers when you are open.

- **Products and Pricing:** List the products and services your business offers. You can also include pricing information such as call-out fees or hourly rates, and the payment options you accept (credit card, bank transfer, etc.).

- **Other Information:** This large free-text field (up to 65,535 characters) is where you can add FAQs and any other information you want the agent to know. Format it as question-and-answer pairs for best results — for example: Q: Do you offer after-hours support? A: Yes, emergency support is available 24/7 by calling our after-hours line.

Once all sections are complete, save the Business Profile before proceeding.

4

#### Create a new Agent

Return to the AI Agents page and click **Create a new Agent**. The Create New Agent form will open. At the top right of the form, use the **Enabled** dropdown to set when the agent should be active — for example, At all times, or only during specific hours.

Fill in the **Agent Profile** section:

- **Agent Name:** Give the agent a name that reflects its role, for example Support, Sales, or General Enquiries. This name is used internally in the portal to identify the agent.

- **Welcome Message:** This is the first thing the agent says when a caller connects. Keep it short and natural — for example: Hi, thanks for calling. How can I help you today? The agent will then listen and respond to whatever the caller says.

- **AI Voice Actor:** Choose the voice the agent will use. The default is Alice, which is recommended for conversational speech. The voice selection affects how natural and engaging the agent sounds to callers.

5

#### Configure Agent Call Flow Settings

Scroll down to the **Agent Call Flow Settings** section. This is where you define which phone lines connect to the agent and what happens if a caller asks to speak to a human.

Configure the two panels:

- **Incoming Call Routing:** Select which of your extensions or phone lines should connect directly to this agent. Hold Ctrl (or Command on Mac) and click to select multiple lines. Any call arriving on a selected line will be answered by this AI Agent.

- **If caller asks to speak to a human:** Choose what happens when a caller requests a human. You can keep them connected to the AI, or set a **Default Route** — a phone number or extension where the call will be transferred. Use the **Transfer Availability** dropdown to control when transfers are permitted (for example, only during business hours).

- **Follow call flow for the dialed number:** Toggle this on if you want the agent to follow the existing call flow rules for the dialled number rather than handling the call independently.

When you are satisfied with the settings, click **Create Agent** at the bottom right of the page.

6

#### Test the AI Agent

Call one of the phone lines you assigned to the agent from an external phone. The agent should answer with the Welcome Message you configured. Speak naturally and ask a question that your Business Profile should be able to answer — for example, your business hours, your address, or a question about your services. Verify that the agent responds correctly and sounds natural.

If the agent does not answer a question accurately, return to the Business Profile and add more detail to the relevant section. For frequently asked questions, the **Other Information** field is the most effective place to add specific Q&A pairs. Changes to the Business Profile take effect immediately — no need to recreate the agent.

Also test the human transfer scenario by saying "Can I speak to someone?" or "I'd like to talk to a person" during the call. Confirm the call is handled according to the Agent Transfer Options you configured.

### Frequently Asked Questions About AI Agents

#### What is the difference between an AI Agent and the AI Receptionist?

The AI Receptionist routes calls — it listens to what a caller says and transfers the call to a human in the right department. An AI Agent holds a full conversation with the caller, answers their questions, and can handle the entire call without any human involvement. AI Agents are trained on your Business Profile and knowledge base.

#### Do I need to create a Business Profile before I can set up an AI Agent?

Yes. The Business Profile must be created first. It is the knowledge base the AI Agent uses to answer caller questions. Without a Business Profile, the Create a new Agent button will not be available.

#### How does the AI Agent know what to say to callers?

The agent draws on the information you enter in the Business Profile — your contact details, business description, operating hours, products and pricing, and the Other Information field. The more detail you provide, the more accurately the agent can respond. For specific questions and answers, use the Other Information field and format your content as Q&A pairs.

#### Can I have more than one AI Agent?

Yes. You can create multiple agents, each with a different name, welcome message, voice, and call flow assignment. For example, you might have one agent for general enquiries and another for after-hours support, each assigned to different phone lines.

#### What happens if a caller asks to speak to a human?

This is controlled by the Agent Transfer Options in the Agent Call Flow Settings. You can configure the agent to stay on the call and continue the conversation, or to transfer the caller to a specific phone number or extension. You can also set the Transfer Availability to restrict when transfers are permitted — for example, only during business hours.

#### Can I choose the voice the AI Agent uses?

Yes. When creating the agent, the AI Voice Actor field lets you select from available voices. The default voice (Alice) is recommended for conversational speech. Different voices may suit different business contexts — a professional services firm might prefer a different tone to a casual retail business.

#### How do I update the information the agent uses to answer questions?

Edit your Business Profile at any time from the AI Agents section of the portal. Changes take effect immediately. You do not need to recreate the agent after updating the Business Profile.

#### Can the AI Agent take messages or book appointments?

The AI Agent is designed to answer questions and provide information based on your Business Profile. For more advanced workflows such as appointment booking or CRM integration, contact the Click2Call support team to discuss your requirements.

#### Is the AI Agent available 24/7?

You control when the agent is active using the Enabled dropdown when creating or editing the agent. You can set it to be active at all times, or restrict it to specific hours. This allows you to use the agent for after-hours coverage while routing calls to your team during business hours.

#### What is the character limit for the Other Information field?

The Other Information field in the Business Profile supports up to 65,535 characters. This is sufficient for a comprehensive FAQ document or a detailed knowledge base. For best results, structure the content as question-and-answer pairs so the AI can locate and deliver specific answers accurately.

## Using AI Speech Tools

Source: https://www.click2call.com.au/help/how-to-use-ai-speech

AI Features
3 min read

## Using AI Speech to Create Voice Recordings

AI Speech is Click2Call's text-to-speech tool. Type any message, choose a voice, and the system generates a professional audio recording instantly — ready to use as a voicemail greeting, auto-attendant announcement, after-hours message, or seasonal recording. No microphone, no re-recording, no waiting for someone to find a quiet room.

Last reviewed: August 2026

### What is AI Speech used for?

AI Speech replaces the old way of creating phone system recordings — where someone would dial into a voicemail box and read a script out loud, often with background noise or multiple takes. With AI Speech, you type the message you want callers to hear, and the AI reads it in a natural, professional voice. Common uses include voicemail greetings, auto-attendant welcome messages, out-of-hours announcements, public holiday messages, and seasonal recordings such as Christmas closures.

### How to Create a Recording with AI Speech, Step by Step

1

#### Log in to the portal

Navigate to portal.click2call.com.au and sign in with your user credentials.

2

#### Navigate to AI Speech

In the top navigation bar, click **AI**. In the left-hand sidebar, click **AI Speech**. The Create AI Voice Recording form will load.

3

#### Choose a Gender and Voice Actor

Use the **Gender** dropdown to select Female or Male. Then use the **Voice Actor** dropdown to choose the specific voice you want. The default voice is Alice, which is recommended for conversational speech and works well for most business recordings. Different voices suit different contexts — a warm, friendly voice works well for a welcome greeting, while a clear, measured voice suits an after-hours announcement.

4

#### Type your Recording Text

Type the message you want the AI to speak into the **Recording Text** field. Write it exactly as you want it to sound — the AI will read it word for word. Use commas, full stops, and other punctuation to control the pacing and add natural pauses between phrases. A comma produces a short pause; a full stop produces a longer one.

Below are some example scripts to get you started:

Voicemail Greeting

"You've reached the voicemail of Acme Plumbing. We're unable to take your call right now. Please leave your name, number, and a brief message, and we'll get back to you as soon as possible. Thank you."

After-Hours Message

"Thank you for calling. Our office is currently closed. Our business hours are Monday to Friday, 8am to 5pm. Please call back during business hours, or leave a message and we will return your call the next business day."

Christmas Closure

"Thank you for calling. Our office is closed for the Christmas and New Year period from the 24th of December, and will reopen on the 6th of January. We wish you a wonderful holiday season, and look forward to speaking with you in the new year."

Auto-Attendant Welcome

"Welcome to Acme Plumbing. For Sales, say Sales. For Support, say Support. Or stay on the line and we will connect you to our team."

**Tip:** To add pauses to the voice recording, use commas, full stops, and other punctuation. Reading your script aloud before generating it is a good way to check the pacing feels natural.

5

#### Generate and save the recording

Click the **Generate AI Voice** button. The portal will process your text and produce an audio file. You can preview the recording before saving it. Once you are happy with the result, save it to your account. The recording will then be available to assign to a voicemail box, auto-attendant, call flow, or any other feature in your phone system that plays an audio message to callers.

If the pacing or emphasis does not sound quite right, adjust the punctuation in your script and regenerate. Adding a comma before a key word will cause the AI to pause slightly, giving that word more weight. Splitting a long sentence into two shorter sentences with a full stop between them will also improve the natural flow of the recording.

### Frequently Asked Questions About AI Speech

#### What can I use AI Speech recordings for?

AI Speech recordings can be used anywhere in your phone system that plays a pre-recorded message to callers. Common uses include voicemail greetings, auto-attendant welcome messages, after-hours announcements, on-hold messages, public holiday closures, and seasonal messages such as Christmas and Easter closures.

#### Do I need any special equipment or a microphone?

No. AI Speech is entirely text-based. You type your message in the portal and the AI generates the audio file. There is no need for a microphone, a recording studio, or a quiet room. This makes it easy to update your recordings at any time, from any device.

#### How do I make the recording sound more natural?

Punctuation controls the pacing. Commas create short pauses, full stops create longer pauses, and ellipses (...) can create a deliberate pause for effect. Write your script the way you would naturally speak it, using short sentences and plain language. Read it aloud yourself before generating it — if it sounds awkward when you say it, it will sound awkward when the AI reads it too.

#### Can I choose different voices?

Yes. The Voice Actor dropdown offers a selection of voices across both Female and Male genders. The default voice Alice is recommended for conversational speech. Try a few different voices with your script to find the one that best suits your business's tone.

#### How do I update a seasonal message, like a Christmas greeting?

Simply return to AI Speech, type your new message, generate a new recording, and replace the existing one in your call flow or voicemail settings. Because the process takes only a minute or two, you can update seasonal messages quickly each year without needing to call anyone or book a recording session.

#### Can I generate a recording in a language other than English?

The available languages depend on the voice actors offered in the portal. Type your script in the desired language and select a voice that supports it. Contact the Click2Call support team if you need assistance with a specific language.

#### Where does the generated recording get saved?

Once generated and saved, the recording is stored in your Click2Call account and becomes available to assign within your phone system — for example, as a voicemail greeting, an auto-attendant prompt, or an on-hold message in a call flow.

#### Can I regenerate a recording if I am not happy with it?

Yes. Simply adjust your script text — tweak the punctuation, rephrase a sentence, or try a different voice actor — and click Generate AI Voice again. You can generate as many versions as you need before saving the final result.

#### Is there a character limit on the Recording Text field?

The Recording Text field is suitable for standard phone system messages. For best results, keep recordings concise — callers generally prefer short, clear messages. A typical voicemail greeting or auto-attendant prompt is between 20 and 60 words.

#### How is AI Speech different from the AI Receptionist or AI Agents?

AI Speech is a recording tool — it generates a static audio file from text that you write. The [AI Receptionist](https://www.click2call.com.au/help/how-to-set-up-ai-receptionist) is a live call routing tool that listens to callers and transfers them to the right department. [AI Agents](https://www.click2call.com.au/help/how-to-set-up-ai-agents) are conversational voice agents that hold full, two-way conversations with callers. AI Speech simply creates the audio files that may be used within those and other phone system features.

## Setting Up AI Voicemail

Source: https://www.click2call.com.au/help/how-to-set-up-ai-voicemail

Greetings

AI Voicemail lets you create professional, consistent voicemail greetings for every extension in your organisation — without anyone having to record their own message. You write the script once, choose a voice, and the system automatically personalises the greeting for each person using their name. Every caller hears the same polished, on-brand experience regardless of whose voicemail they reach.

Last reviewed: August 2026

### Why use AI Voicemail instead of recording your own greeting?

The traditional approach — dialling into a voicemail box and recording a message — produces inconsistent results across a team. Some staff record clear, professional greetings; others record theirs in a noisy environment, forget to update them, or never set them up at all. AI Voicemail solves this by letting an administrator set a single script that applies to every extension automatically. The voice is consistent, the wording is consistent, and each greeting is personalised with the individual's name — all from one place in the portal.

### How to Set Up AI Voicemail, Step by Step

1

#### Log in to the portal

Navigate to portal.click2call.com.au and sign in with your user credentials. You will need administrator access to configure AI Voicemail for your account.

2

#### Navigate to AI Voicemail

In the top navigation bar, click **AI**. In the left-hand sidebar, click **AI Voicemail**. The AI Voicemail configuration page will load.

3

#### Enable AI Voicemail

At the top right of the page you will see a toggle switch. Click it to enable AI Voicemail for your account. When the toggle is green and on, AI-generated greetings will be used across your extensions instead of any individually recorded messages.

4

#### Choose a Gender and AI Voice Actor

Under **AI Message Recordings**, use the **Gender** dropdown to select Female or Male, then choose a specific voice from the **AI Voice Actor** dropdown. The default voice is Alice. This voice will be used for all voicemail greetings across your organisation, so choose one that reflects your business's tone — professional, friendly, or neutral.

5

#### Write your Unavailable and Busy messages

There are two message fields to complete:

- **Unavailable Message:** Played when the extension is not answered — for example, when the person is away from their desk or outside business hours. The default script is: "You have reached the voicemail of MAILBOXNAME. Please leave your message after the tone."

- **Busy Message:** Played when the extension is active on another call. The default script is: "MAILBOXNAME is currently busy. Please leave your message after the tone."

**The MAILBOXNAME placeholder:** Wherever you type `MAILBOXNAME` in your script, the system will automatically replace it with the name entered against each extension or line. This means one script covers your entire team — each person hears their own name in the greeting without you needing to create individual recordings.

You can customise both scripts to match your business's style. Keep the wording clear and concise — callers typically hear the greeting for only a few seconds before the tone. Here are some example variations:

Unavailable — Formal

"You have reached the voicemail of MAILBOXNAME. Please leave your name, number, and a brief message, and we will return your call as soon as possible."

Unavailable — Friendly

"Hi, you've reached MAILBOXNAME. I'm not available right now, but leave me a message and I'll get back to you shortly."

Busy

"MAILBOXNAME is on another call at the moment. Please leave a message after the tone and we'll call you back."

6

#### Preview and save your greetings

Click **Preview Voicemail Messages** to hear how both the Unavailable and Busy greetings will sound before applying them. This lets you check the pacing, wording, and voice before your team or callers hear them. If anything sounds off, adjust the script — adding commas or full stops will create natural pauses — then preview again.

When you are satisfied, click **Save Voicemail Greetings** at the bottom right of the page. The AI-generated greetings will immediately apply to all extensions in your account. No individual setup is required per extension — the system handles personalisation automatically using each person's name.

### Frequently Asked Questions About AI Voicemail

#### What is the MAILBOXNAME placeholder and how does it work?

MAILBOXNAME is a special placeholder you include in your voicemail script. When the system generates a greeting for a specific extension or line, it automatically replaces MAILBOXNAME with the name assigned to that extension in the portal. This means you write one script and every person in your organisation gets a personalised greeting with their own name — without any additional setup.

#### What is the difference between the Unavailable Message and the Busy Message?

The Unavailable Message plays when a call is not answered — for example, when the person is away from their desk, outside business hours, or has not picked up within the ring timeout. The Busy Message plays when the extension is already active on another call. Callers hear different greetings depending on the reason their call was not connected, which gives a more professional and informative experience.

#### Does AI Voicemail apply to all extensions automatically?

Yes. Once you save the AI Voicemail greetings, they apply across all extensions in your account. Individual staff members do not need to configure anything themselves. The system uses the name entered against each extension to personalise the greeting automatically.

#### Can individual users still record their own voicemail greeting?

When AI Voicemail is enabled, the AI-generated greetings take precedence. If you need a specific extension to use a custom recording, contact the Click2Call support team to discuss your options.

#### Can I choose a different voice for different departments?

The AI Voicemail configuration applies a single voice across all extensions. If you need different voices for different departments or teams, contact the Click2Call support team to discuss your requirements.

#### How do I make the greeting sound more natural?

Use punctuation to control pacing. Commas create a short pause; full stops create a longer pause. Read your script aloud before saving — if it sounds rushed or awkward when you say it, add punctuation to slow it down. The Preview Voicemail Messages button lets you hear the result before it goes live.

#### What happens if a person's name is not set on their extension?

If no name has been entered against an extension, the MAILBOXNAME placeholder may be read literally or left blank, depending on the system configuration. To ensure every greeting sounds correct, make sure all extensions have a name assigned in the portal before enabling AI Voicemail.

#### Can I update the voicemail script at any time?

Yes. Return to the AI Voicemail page, update the script, preview it, and save again. The new greeting will apply to all extensions immediately. This makes it easy to refresh your voicemail wording without any individual action required from your team.

#### How is AI Voicemail different from AI Speech?

AI Voicemail is specifically designed to manage voicemail greetings across all extensions in your account, with automatic personalisation using each person's name. [AI Speech](https://www.click2call.com.au/help/how-to-use-ai-speech) is a more general text-to-speech tool used to create individual audio recordings for use anywhere in your phone system — such as auto-attendant messages, on-hold announcements, or seasonal recordings.

#### Do I need to set up AI Voicemail for each user individually?

No. AI Voicemail is configured once at the account level by an administrator. The settings apply to all extensions automatically. This is one of the key advantages over the traditional approach of asking each team member to record their own greeting — it requires no action from individual users and ensures a consistent result across the entire organisation.

## Ring First, Then Let the AI Take a Message

Source: https://www.click2call.com.au/help/how-to-set-up-answer-agent

AI Features
5 min read

## How to Ring Your Phone First, Then Let the AI Take a Message

The Answer Agent is a smart replacement for voicemail. Your phone rings first, and if you cannot get to it the AI answers in a natural voice, asks for the caller’s name, number and reason for calling — waiting for each answer — and emails you the details with a transcript. You can write its introduction and questions yourself and pick the voice.

Last reviewed: September 2026

### Setting Up the AI Answer Agent, Step by Step

1

#### Decide how long your phone rings first

Go to **Voice → Line Manager** and click your number to open its Call Flow page. Open the **Incoming Calls** dropdown and choose **Voice Mail**. Set **Call Ringing Time (in seconds)** to how long you want to be able to answer before the AI picks up — the default is 20 seconds. On the same page, tick **Send callers to the AI Answer Agent (instead of voicemail)**, then save.

2

#### Tell it where to email the messages

Still on the **Voice Mail** page, enter your email address in Send a copy of my voicemail messages to the following email address (use a semicolon between several addresses). This is the address your call summaries and transcripts are delivered to. You can also set a per-number address in the **Line Email** column on the Line Manager page.

3

#### Create your business profile

Go to **AI → Answer Agent (Beta)** and click **Create Business Profile**. This holds your business details so the agent can answer simple questions about you. If you only want it to take messages, you can keep the profile brief.

4

#### Choose the mode and the voice

On the General tab, set **Answering mode** to Message only if you just want a smart message-taker, or Answer questions and take messages if it should also answer questions from your business profile. Then pick a **Voice actor** and click **Generate preview** to hear it before you save.

5

#### Write your introduction

The **Welcome message** box is your introduction — replace the default with your own wording, for example: “Hi, you’ve reached Kat at Acme. I’m Maggie, her virtual assistant. Kat can’t get to the phone just now — may I take a few details and she’ll get back to you?” Type `{$biz}` anywhere in the message to have your business name inserted automatically.

6

#### Choose the questions it asks

Under **Fields to Collect**, each row is one question the agent asks, and it waits for an answer before moving on. The defaults are exactly what most businesses want: Full name of the caller, Best contact number, and Message or what they need help with. Edit the wording in the Description box to change how a question is asked, set the Type (Text, Email, Phone or Appointment), tick Required, and use the buttons above the table to add Email Address, Account Number, Company Name, Service Address or a Custom Field.

7

#### Set the closing behaviour and save

Tick **Confirm details before finalising the message** if you want the agent to read the details back to the caller and confirm them before it finishes — this is how the closing works; there is no separate closing script to write. Optionally enable **Appointment Scheduling** further down if you want callers to be able to book a time. Click **Save Details**. Your messages will now arrive by email, and each call is also listed under **AI → Recordings** with its transcript and summary.

**Good to know:** The Answer Agent takes messages. If instead you want callers routed to different people or departments by what they say, that is the [AI Receptionist](https://www.click2call.com.au/help/how-to-set-up-ai-receptionist). Many businesses use the Receptionist during the day and the Answer Agent after hours. Settings can be account-wide or per number — use the Settings Scope dropdown at the top of the Answer Agent page.

**Good to know:** The Answer Agent (Beta) can also book appointments while it takes a call. See [Letting the AI Book Appointments](https://www.click2call.com.au/help/ai-appointment-booking).

## Letting the AI Book Appointments

Source: https://www.click2call.com.au/help/ai-appointment-booking

When it answers a call, the Answer Agent (Beta) can offer the caller times you are free and book an appointment. You set the rules, your hours and your services, and bookings appear in its calendar.

Last reviewed: October 2026

### Before you start

Set up the Answer Agent first, so it answers your calls. See [Setting Up the AI Answer Agent](https://www.click2call.com.au/help/how-to-set-up-answer-agent).

### Turn on booking

- Go to **AI → Answer Agent (Beta)**.
- At **Settings for**, choose **Account defaults**, or one number if only that number should take bookings.
- Open the **Appointments** tab and tick **Enable appointment scheduling**.
- Set the options below, then click **Save changes**.

### Booking settings

| Setting | What it does |
| Appointment mode | Optional takes messages as normal and books only when the caller asks. Required books an appointment with every message. |
| Default duration | How long an appointment lasts, in minutes. The default is 60. |
| Minimum notice | How far ahead a booking must be, in minutes. 1,440 minutes is 24 hours. |
| Slot interval | The spacing between start times: 15, 30 or 60 minutes. |
| Options to offer | How many times the AI suggests. The default is one. |
| Email reminder | How many minutes before the appointment a reminder is set. 0 means no reminder. |

### Set your hours and time zone

Under **Availability**:

- **Timezone** starts on Pacific/Auckland. Change it to your own, for example Australia/Sydney, Australia/Brisbane or Australia/Perth, or appointments will be offered at the wrong times.
- **Working days & hours** start at Monday to Friday, 9am to 5pm.
- **Regular breaks & busy hours** start with a 12:30 to 1:30pm lunch break. Click **+ Add break** for more.
- **Treat NZ public holidays as unavailable** uses New Zealand holidays only. In Australia, leave it off and add your public holidays yourself (see below).

#### Australian public holidays

Add them as custom holiday dates: open the number in **Voice → Line Manager**, choose **Other Settings → Time Schedules**, and click **Click here to add your own custom holiday dates**. You can also block a single day in the calendar with **Add blocked time**.

### Services with different lengths

If your services take different amounts of time, tick **Use service-specific appointment durations** under **Services**. The AI asks the caller which service they want and books the right length.

- Click **Add service** and enter a category, the service name, a short description the AI can say, and its length in minutes. Untick **Active** to hide a service.
- Or click **Import CSV** to load a list. The columns are `category`, `service_name`, `description` and `duration_minutes`.

### The calendar

Click **Open calendar** to see bookings by week or as an agenda.

- **Add appointment** to book one yourself, with the caller’s name and number, notes, and a status: Confirmed, Tentative, Busy or Cancelled.
- **Add blocked time** to stop the AI booking a period, such as a public holiday or a day off.

The calendar shows your available hours, appointments, breaks and blocked time, busy times from an external calendar, and holidays in different colours.

**Good to know:** Check the time zone first. It is the most common reason for appointments offered at the wrong time.
