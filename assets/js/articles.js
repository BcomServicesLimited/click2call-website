/**
 * articles.js — Click2Call central help article registry
 * Bcom Services Pty Ltd (ABN: 92 636 893 108)
 *
 * HOW TO ADD A NEW ARTICLE:
 * 1. Create the article HTML file in /help/
 * 2. Add one entry to the HELP_ARTICLES array below
 * 3. Run `python3 scripts/build_help_grid.py` to regenerate the
 *    server-rendered grid in help/index.html (so non-JS crawlers —
 *    including most LLM crawlers — see the new article)
 * 4. /support and the /help JS search pick it up automatically
 *
 * FIELDS:
 *   url      — absolute path to the article (required)
 *   title    — article title shown on cards (required)
 *   desc     — one-sentence description shown on cards (required)
 *   tags     — space-separated search keywords (required)
 *   category — category key, must match one of the HELP_CATEGORIES keys (required)
 *   readTime — estimated read time string, e.g. "3 min read" (required)
 *   featured — true = show in /support article clusters (optional, default false)
 *   pinned   — true = show in /support primary task tiles (optional, default false)
 */

var HELP_ARTICLES = [

  {
    url:      "/help/faxmail",
    title:    "Sending and Receiving Faxes by Email (Faxmail)",
    desc:     "Faxmail replaces a fax machine with email. Faxes sent to your number arrive in your inbox as attachments, and you send a fax by emailing a document.",
    tags:     "fax faxmail email to fax fax to email t.38 pdf fax number",
    category: "phone-numbers",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/sending-sms",
    title:    "Sending SMS from Your Business Number",
    desc:     "You can send text messages from your Click2Call number from the portal, by email, or from your own software. Replies come back to you by email, and you.",
    tags:     "sms text message email to sms send sms replies api 50c",
    category: "phone-numbers",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/call-setup-api",
    title:    "Starting a Call from a Web Link (Call Setup API)",
    desc:     "The call setup API connects two phone numbers with a single web request. Click2Call rings the first number, and when it's answered, dials the second. It's.",
    tags:     "call setup api click to call web request call.php developer integration",
    category: "getting-started",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/webrtc-sip-over-websocket",
    title:    "Browser Calling with WebRTC (SIP over WebSocket)",
    desc:     "You can register a Click2Call number from a web browser, using SIP over a secure WebSocket (WSS). This lets you build calling into your own web app with a.",
    tags:     "webrtc wss websocket browser calling sip.js jssip turn developer",
    category: "getting-started",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/zoho-crm-integration",
    title:    "Connecting Zoho CRM",
    desc:     "Click2Call connects to Zoho CRM so your team can click a number in Zoho to call it, see who's calling before they answer, and keep every call, note and.",
    tags:     "zoho crm integration phonebridge click to dial call logging recordings",
    category: "getting-started",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/call-quality-and-starlink",
    title:    "Call Quality: Codecs, Your Connection and Starlink",
    desc:     "Most call quality problems come from the internet connection, not the phone service. This guide covers the settings that affect quality, what your.",
    tags:     "call quality choppy audio codecs bandwidth qos starlink satellite internet",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/calls-during-power-or-internet-outage",
    title:    "Keeping Calls Coming In During an Outage",
    desc:     "Your phones need power and internet to work. If either goes down, Click2Call can still answer your calls and send them to a mobile or another number.",
    tags:     "power cut outage internet down forward when offline failover pbx backup mobile",
    category: "call-flows",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/which-phones-can-i-use",
    title:    "Which Phones Can I Use? (And Alarm Systems)",
    desc:     "Click2Call works with IP desk phones, the Secure VoIP app on your mobile or computer, and ordinary analogue phones through an adaptor. Back-to-base alarm.",
    tags:     "which phones compatible desk phone existing phone analogue ata alarm system",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/toll-fraud-protection",
    title:    "Protecting Your Account from Toll Fraud",
    desc:     "Toll fraud is when someone breaks into a phone account and uses it to make expensive overseas calls. It's the biggest security risk for any internet phone.",
    tags:     "toll fraud hacking security passwords call barring overseas access control list",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/two-factor-login",
    title:    "Turning On Two-Factor Login",
    desc:     "Two-factor login adds a one-time code to your portal sign-in. Even if someone learns your password, they can't get into your account without the code.",
    tags:     "two factor 2fa login security email verification portal trusted locations",
    category: "getting-started",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/zoiper-setup",
    title:    "Setting Up Zoiper",
    desc:     "Zoiper is a free SIP softphone for Windows, Mac, Linux, iPhone and Android. It works with Click2Call as a standard SIP app. Click2Call recommends its own.",
    tags:     "zoiper softphone sip app windows mac linux iphone android setup",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/bria-teams-setup",
    title:    "Setting Up Bria Teams",
    desc:     "Bria Teams is a paid softphone from CounterPath that lets an administrator set up calling for the whole team from one web dashboard. It connects to.",
    tags:     "bria teams counterpath softphone team dashboard sip setup",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/secure-voip-app-transfers",
    title:    "Transferring Calls in the Secure VoIP App",
    desc:     "You can pass a call to a colleague from the Secure VoIP app in two ways. A blind transfer sends the call straight through. An attended transfer lets you.",
    tags:     "secure voip app transfer attended blind micro edition iphone android windows",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/secure-voip-windows-tips",
    title:    "Secure VoIP on Windows: Clean Reinstall, Default Calling App and Linux",
    desc:     "This guide covers three things for the Secure VoIP Micro Edition app on Windows. You can reinstall it cleanly, make it open when you click a phone number.",
    tags:     "secure voip windows reinstall uninstall appdata default calling app tel callto linux wine",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/secure-voip-android-background-mode",
    title:    "Secure VoIP on Android: Fixing Missed Calls and Battery Saving",
    desc:     "Android phones save battery by putting apps to sleep. The Secure VoIP app is woken by a push notification when a call comes in, but some phones' battery.",
    tags:     "secure voip android battery optimisation background missed calls push notification",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/call-parking-pickup-transfers",
    title:    "Parking, Picking Up and Transferring Calls",
    desc:     "Click2Call lets your team park a call and pick it up on another phone, answer a colleague's ringing phone, and transfer callers with a few key presses.",
    tags:     "call park parking *07 *17 pickup *88 *89 transfer attended blind #0 ## recall",
    category: "call-flows",
    readTime: "3 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/hunt-groups",
    title:    "Hunt Groups: Ringing Phones One After Another",
    desc:     "A hunt group rings a list of phones one at a time, in the order you choose, until someone answers. Use it when calls should go to your first choice of.",
    tags:     "hunt group sequential ring linear hunt ring in order ring group simultaneous ring",
    category: "call-flows",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/do-not-disturb-and-call-screening",
    title:    "Do Not Disturb and Call Screening",
    desc:     "Do not disturb stops your phone ringing and sends callers to voicemail, a busy tone or another number. Call screening asks callers to say their name.",
    tags:     "dnd do not disturb *78 *79 call screening announce name anonymous busy tone",
    category: "call-flows",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/conference-calls",
    title:    "Conference Calls and Dictation",
    desc:     "Any Click2Call number can become a conference bridge. Callers dial the number, enter a PIN if you've set one, and join the call together. We recommend.",
    tags:     "conference call bridge meeting pin supervisor recording dictation",
    category: "call-flows",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/busy-lamp-field-blf",
    title:    "Busy Lamp Field (BLF): Watching Lines, Queues and Voicemail",
    desc:     "A BLF key is a button on a desk phone with a light that shows what another line is doing. Green means free, red means on a call, and flashing red means.",
    tags:     "blf busy lamp field presence line monitoring mailbox monitoring queue monitoring light",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/hot-desking",
    title:    "Hot Desking: Logging In to Any Phone",
    desc:     "Hot desking lets anyone log in to a shared desk phone with their own extension using a short code. The phone reloads with their number and keys, then goes.",
    tags:     "hot desk hot desking shared phone login logout *45 *46",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/extension-numbers-and-groups",
    title:    "Extension Numbers, Calling Groups and Caller Names",
    desc:     "Every line on your account can have a short extension number and a name. Staff dial the extension instead of the full number, callers can enter it at your.",
    tags:     "extension number extension dialling calling group billing group caller name intercom *85",
    category: "extensions",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/outgoing-call-pin-and-call-assignment",
    title:    "Controlling Outgoing Calls: PIN Codes and Call Assignment",
    desc:     "You can ask for a PIN before certain calls go out, so only approved people can call overseas or mobiles. On a shared phone, call assignment mode asks for.",
    tags:     "pin code authorisation outgoing call restriction overseas call assignment smart code",
    category: "call-flows",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/remote-call-back-and-dial-tone",
    title:    "Calling Through Your Business Number While Away",
    desc:     "Remote dial tone and remote call back let you make calls through your Click2Call number from another phone, such as your mobile. The person you call sees.",
    tags:     "remote dial tone remote call back callback dial out from mobile business number overseas",
    category: "call-flows",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/group-call-and-paging",
    title:    "Group Calls and Paging",
    desc:     "A group call rings up to 20 people at once and joins everyone who answers into one call. Paging mode turns it into an announcement: phones answer on.",
    tags:     "group call page paging announcement intercom *48 auto answer",
    category: "call-flows",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/hold-music-and-feature-order",
    title:    "Hold Music, Caller Tunes and Which Setting Wins",
    desc:     "You can replace the ringing callers hear with your own music or message, and upload your own music on hold. This guide also explains why one setting can.",
    tags:     "hold music music on hold caller tunes mp3 call flow priority feature order",
    category: "call-flows",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/distinctive-ring-internal-calls",
    title:    "Different Ringtones for Internal Calls (Yealink and Grandstream)",
    desc:     "You can make your desk phones ring differently when a colleague calls, so you know it's an internal call before you answer. Click2Call tags internal calls.",
    tags:     "distinctive ring ringtone internal calls alert-info yealink grandstream custom configuration",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/fanvil-phones",
    title:    "Setting Up Fanvil Phones",
    desc:     "Click2Call sets up Fanvil desk phones for you. Add the phone in the portal, point it at our provisioning server once, and it downloads your numbers and.",
    tags:     "fanvil x series auto provisioning fanvil.securevoip.nz desk phone encryption key",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/panasonic-sip-phones",
    title:    "Setting Up Panasonic SIP Phones",
    desc:     "Click2Call auto-provisions Panasonic SIP phones, including the KX-HDV, KX-UT, KX-TGP, KX-TPA and KX-HGT ranges. Panasonic's KX-NT phones only work with.",
    tags:     "panasonic kx-hdv kx-ut kx-tgp kx-tpa kx-hgt sip phone auto provisioning standard file url",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/alcatel-lucent-phones",
    title:    "Setting Up Alcatel-Lucent Enterprise H and M Series Phones",
    desc:     "Click2Call auto-provisions Alcatel-Lucent Enterprise H3, H6, M3, M5, M7 and M8 phones. Provisioning keeps the firmware up to date and sets up your lines.",
    tags:     "alcatel lucent enterprise ale h3 h6 m3 m5 m7 m8 auto provisioning desk phone",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/flyingvoice-phones",
    title:    "Setting Up FlyingVoice Phones",
    desc:     "Click2Call auto-provisions several FlyingVoice phones. Add the phone in the portal, enter a few provisioning settings on the phone, and it downloads your.",
    tags:     "flyingvoice fip phone auto provisioning profile rule firmware",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/yeastar-ta-adaptors",
    title:    "Setting Up Yeastar TA Analogue Adaptors",
    desc:     "The Yeastar TA100, TA200, TA400 and TA800 connect ordinary analogue phones to Click2Call. The portal builds the adaptor's settings for you, so you only.",
    tags:     "yeastar ta100 ta200 ta400 ta800 ata analogue phone adapter auto provisioning aes key",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/gigaset-ip-phones",
    title:    "Setting Up Gigaset Cordless IP Phones",
    desc:     "Gigaset IP cordless phones aren't in the portal's auto-provisioning list, so you set them up by hand in the base station's web page. It takes about five.",
    tags:     "gigaset cordless dect ip phone manual sip setup base station",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/fritzbox-phone-port",
    title:    "Setting Up the Phone Port on a FRITZ!Box",
    desc:     "Many FRITZ!Box routers have a built-in phone port. You can register a Click2Call number on it and plug an ordinary analogue phone straight in. This guide.",
    tags:     "fritzbox fritz box avm phone port analogue phone sip manual setup",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/programming-phone-keys",
    title:    "Programming Phone Keys (BLF, Speed Dial, Pickup and More)",
    desc:     "When you add a desk phone under Voice \u2192 Phones, you can also decide what each programmable key on the phone does \u2014 a second line, a busy lamp for a.",
    tags:     "dss keys line keys blf busy lamp speed dial pickup park intercom programmable keys desk phone provisioning hot desk paging",
    category: "devices",
    readTime: "3 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/grandstream-desk-phones",
    title:    "Setting Up Grandstream Desk Phones",
    desc:     "Click2Call can set up most Grandstream desk, cordless and conference phones for you \u2014 GRP, GXP, GXV, GHP, DP and WP models. You add the phone in the.",
    tags:     "grandstream grp gxp gxv ghp dp750 wp810 auto provisioning gs.securevoip.nz desk phone firmware",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/grandstream-ht801-ht802",
    title:    "Connecting an Analogue Phone or Fax with a Grandstream HT801 / HT802",
    desc:     "A Grandstream HT801 or HT802 (an analogue telephone adaptor, or ATA) lets you plug an ordinary home or office phone \u2014 or a fax machine \u2014 into Click2Call.",
    tags:     "grandstream ht801 ht802 ht812 ht814 ata analogue phone adapter fax provisioning",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/polycom-vvx-phones",
    title:    "Setting Up Polycom VVX Phones",
    desc:     "Click2Call can set up Polycom VVX phones (VVX 101 to VVX 601) for you. Add the phone in the portal, point it at Click2Call's provisioning server, and it.",
    tags:     "polycom vvx provisioning polycom.securevoip.nz desk phone firmware admin password 456",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/cisco-spa-phones",
    title:    "Cisco SPA Phones and SPA112 / SPA122 Adapters",
    desc:     "Older Cisco SPA phones (SPA301 to SPA525G) and the SPA112 and SPA122 phone adaptors still work with Click2Call, and the portal can configure them for you.",
    tags:     "cisco spa spa112 spa122 spa504g spa525g ata profile rule provisioning certificate custom ca security",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/sip-trunk-pbx-setup",
    title:    "Connecting Your Own PBX with a SIP Trunk",
    desc:     "If you already have a PBX \u2014 3CX, FreePBX, Asterisk or another SIP-capable system \u2014 you can keep it and use Click2Call for your phone numbers and calls.",
    tags:     "sip trunk pbx own pbx registered sip trunk pilot number ddi peering iax2 profile caller id channels 3cx freepbx asterisk",
    category: "devices",
    readTime: "3 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/asterisk-freepbx-pjsip",
    title:    "Connecting Asterisk or FreePBX (PJSIP)",
    desc:     "Asterisk and systems built on it (FreePBX, Issabel and similar) connect to Click2Call as a Registered SIP Trunk using the PJSIP channel driver. Set up the.",
    tags:     "asterisk freepbx pjsip chan_pjsip trunk config pjsip.conf issabel iax2 sip trunk",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/3cx-sip-trunk",
    title:    "Connecting 3CX",
    desc:     "3CX connects to Click2Call as a Registered SIP Trunk. These steps are for 3CX version 20 and.",
    tags:     "3cx v20 sip trunk pilot number did e164 codec caller id p-asserted-identity",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/sip-settings-for-devices-and-pbx",
    title:    "SIP Settings for Desk Phones, Adapters and PBX Systems",
    desc:     "Any SIP-compatible desk phone, analogue adapter or PBX can connect to Click2Call. Use the settings below for any device we don't have a step-by-step guide.",
    tags:     "sip settings desk phone ata adapter pbx username password proxy server port 5060 50600 5061 tls tcp udp codecs g722 g711 dtmf firewall srtp peering iax2 registration",
    category: "devices",
    readTime: "3 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/sip-alg-one-way-audio",
    title:    "Fixing One-Way Audio and Dropped Registrations (SIP ALG and NAT)",
    desc:     "If calls connect but you can't hear the other person (or they can't hear you), if incoming calls ring but go silent when answered, or if your phone keeps.",
    tags:     "one way audio no audio silence answered sip alg nat router registration dropping tls 50600 firewall port forwarding",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/ghost-and-spam-calls",
    title:    "Stopping Ghost and Spam Calls",
    desc:     "If your phone rings and nobody is there, or you get calls from numbers like \"100\" or \"blocked\" several times a day, there are two possible causes. Which.",
    tags:     "ghost calls silent calls spam robocall blocked anonymous blacklist whitelist reject overseas mobiles call screening port forwarding scanner",
    category: "call-flows",
    readTime: "3 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/dtmf-keypad-presses-not-working",
    title:    "Keypad Presses Not Recognised (DTMF Problems)",
    desc:     "If callers press options in your auto attendant and nothing happens, or you can't enter a PIN or menu option when you call a bank or another business.",
    tags:     "dtmf keypad tones digits ivr menu auto attendant pin rfc2833 sip info inband",
    category: "devices",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/star-codes",
    title:    "Star Codes: Control Your Phone from the Handset",
    desc:     "You can change many settings by dialling a code from any phone on your account, without logging in to the portal. Where you see xxx, enter a phone number.",
    tags:     "star codes feature codes handset voicemail forwarding do not disturb caller id block queue login transfer record park pickup redial",
    category: "call-flows",
    readTime: "3 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/webhooks-and-api-during-your-trial",
    title:    "Using the API and Webhooks on a Trial Account",
    desc:     "The trial includes the full API and webhooks. Set up a webhook, see the call states and fields it sends, and check why one did not arrive.",
    tags:     "api webhook webhooks trial developer integration aianalysis transcript call summary payload state call id endpoint not arriving fired zapier make crm iou limit credit",
    category: "getting-started",
    readTime: "6 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/softphone-setup-and-troubleshooting",
    title:    "Setting Up a Softphone and Fixing Registration Problems",
    desc:     "Supported softphones, where your SIP credentials are, why iPhone apps miss calls in the background, and how to check a line is registering.",
    tags:     "softphone registration registered not registering sip credentials line password line manager tls tcp udp iphone ios background push notifications app closed groundwire linphone zoiper microsip troubleshooting",
    category: "devices",
    readTime: "7 min read",
    featured: true,
    pinned:   false
  },



  {
    url:      "/help/why-included-minutes-are-not-being-used",
    title:    "Why Your Included Minutes Are Not Being Used",
    desc:     "Included minutes belong to one specific number, not the whole account. If calls are charged while your allowance sits untouched, this is why.",
    tags:     "included minutes not used allowance bundle per number billing charged calls divert forwarded extension billed number plan minutes",
    category: "billing",
    readTime: "3 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/call-flow-ring-mobile-then-voicemail",
    title:    "Ring Your Mobile and Still Get Voicemail",
    desc:     "Forwarding to a mobile sends unanswered calls to your carrier's voicemail, not ours. Use Simultaneous Ring so the call stays with us.",
    tags:     "voicemail call forwarding simultaneous ring divert mobile ring time call flow missed calls no voicemail forward to mobile carrier voicemail not working",
    category: "call-flows",
    readTime: "3 min read",
    featured: true,
    pinned:   false
  },

  /* ── Getting Started ── */
  {
    url:      "/help/how-to-activate-account",
    title:    "Activating Your Account",
    desc:     "How to activate your Click2Call account and log in to the portal for the first time.",
    tags:     "activate account setup first time login portal",
    category: "getting-started",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/understanding-your-free-trial",
    title:    "Understanding Your Free Trial",
    desc:     "What the $11 credit covers, what to do in your 7 days, and how to upgrade after the trial ends.",
    tags:     "free trial 7 day credit 11 dollars outbound calls upgrade cloud pbx",
    category: "getting-started",
    readTime: "3 min read",
    featured: true,
    pinned:   true
  },
  {
    url:      "/help/how-to-make-your-first-call",
    title:    "Making Your First Call",
    desc:     "How to add a phone number, register a device (softphone, desk phone, or mobile divert), and make your first outbound call.",
    tags:     "first call outbound call softphone desk phone mobile divert register device caller id test call outbound",
    category: "getting-started",
    readTime: "5 min read",
    featured: true,
    pinned:   true
  },
  {
    url:      "/help/how-to-add-account-credit",
    title:    "Adding Account Credit",
    desc:     "How to load credit onto your account and set up auto top-up.",
    tags:     "add credit top up prepay billing payment auto top-up auto top up automatic payments credit card low balance warning stored card one off payment",
    category: "getting-started",
    readTime: "2 min read",
    featured: true,
    pinned:   true
  },

  /* ── Phone Numbers ── */
  {
    url:      "/help/how-to-add-phone-number",
    title:    "Adding a Phone Number",
    desc:     "How to add a new local or 1300 number to your account.",
    tags:     "add phone number ddi direct dial 1300 local number",
    category: "phone-numbers",
    readTime: "2 min read",
    featured: true,
    pinned:   true
  },
  {
    url:      "/help/how-to-port-number",
    title:    "Porting an Existing Number",
    desc:     "How to transfer your current phone number to Click2Call with no downtime.",
    tags:     "port number transfer porting existing number move porting fee transfer number keep my number bring my number port request",
    category: "phone-numbers",
    readTime: "3 min read",
    featured: true,
    pinned:   false
  },

  /* ── Extensions & Users ── */
  {
    url:      "/help/how-to-add-extension",
    title:    "Adding a New Extension",
    desc:     "How to create a new extension on your Cloud PBX.",
    tags:     "add extension new extension pbx create",
    category: "extensions",
    readTime: "2 min read",
    featured: true,
    pinned:   true
  },
  {
    url:      "/help/how-to-add-user",
    title:    "Adding a New User",
    desc:     "How to add a staff member to your account and assign their credentials.",
    tags:     "add user staff member credentials new user invite extension login sip password seat staff",
    category: "extensions",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-set-outbound-caller-id",
    title:    "Setting Outbound Caller ID",
    desc:     "How to set which number displays when your extensions make outbound calls.",
    tags:     "caller id outbound caller id cli number display cli hide number private *67 show number display number withheld",
    category: "extensions",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-set-up-speed-dials",
    title:    "Setting Up Global Contacts and Speed Dials",
    desc:     "How to save contact names and assign speed dial codes so you can dial contacts quickly from any phone on your account.",
    tags:     "speed dial global contacts external contacts contact name caller name csv import",
    category: "extensions",
    readTime: "3 min read",
    featured: true,
    pinned:   false
  },

  /* ── Devices & Apps ── */
  {
    url:      "/help/how-to-add-desk-phone",
    title:    "Registering a Desk Phone",
    desc:     "How to register a Yealink or compatible SIP desk phone to your extension.",
    tags:     "desk phone register yealink sip phone hardware setup",
    category: "devices",
    readTime: "3 min read",
    featured: true,
    pinned:   true
  },
  {
    url:      "/help/how-to-set-up-softphone",
    title:    "Setting Up a Softphone or Mobile App",
    desc:     "How to install and configure the softphone app on your PC or mobile device.",
    tags:     "softphone mobile app ios android pc desktop download install app iphone android securevoip mobile phone qr code login sip",
    category: "devices",
    readTime: "3 min read",
    featured: true,
    pinned:   true
  },
  {
    url:      "/help/how-to-connect-simpro",
    title:    "Connecting simPRO to Click2Call",
    desc:     "Set up the simPRO Premium VoIP integration so its built-in softphone works on your Click2Call numbers.",
    tags:     "simpro simpro premium voip integration softphone webphone trades field service server address 5060 line password employee card mizuphone job management",
    category: "devices",
    readTime: "6 min read",
    featured: true,
    pinned:   false
  },

  {
    url:      "/help/how-to-set-up-linphone",
    title:    "Setting Up Linphone (Free Third-Party Softphone)",
    desc:     "How to download and configure Linphone on iPhone, Android, Windows, or Mac as a free SIP softphone with Click2Call.",
    tags:     "linphone softphone sip third party free ios android windows mac troubleshooting testing",
    category: "devices",
    readTime: "10 min read",
    featured: true,
    pinned:   false
  },

  /* ── Call Flows & Routing ── */
  {
    url:      "/help/how-to-set-up-call-flow",
    title:    "Setting Up a Call Flow",
    desc:     "How to build a call flow to route incoming calls to the right destination.",
    tags:     "call flow routing inbound ivr auto attendant menu ivr menu press 1 auto attendant options greeting recording *22 phone menu",
    category: "call-flows",
    readTime: "4 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-set-up-call-queue",
    title:    "Setting Up a Call Queue",
    desc:     "How to hold callers in a queue with your own music and position announcements while your team is busy.",
    tags:     "call queue queuing hold music position announcement wait agents ring all wallboard contact centre call centre agents login *70 hold queue strategy",
    category: "call-flows",
    readTime: "5 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-use-live-call-dashboard",
    title:    "Using the Live Call Dashboard",
    desc:     "See live calls, callers waiting in queues and team availability, and put it on a screen in the office.",
    tags:     "dashboard live real time wallboard tv view monitor missed calls talk time active calls queued calls team status supervisor",
    category: "call-flows",
    readTime: "4 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-create-ring-group",
    title:    "Creating a Ring Group",
    desc:     "How to set up a ring group so multiple extensions ring simultaneously.",
    tags:     "ring group hunt group simultaneous ring group call simultaneous ring mobile ring together divert forward hunt multiple phones",
    category: "call-flows",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-configure-business-hours",
    title:    "Configuring Business Hours",
    desc:     "How to set your open and closed hours so calls route correctly after hours.",
    tags:     "business hours after hours time conditions schedule closed work hours open hours opening hours holidays public holidays divert after-hours forward mobile",
    category: "call-flows",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-set-up-voicemail",
    title:    "Setting Up Voicemail",
    desc:     "How to enable voicemail on an extension and configure voicemail-to-email.",
    tags:     "voicemail setup voicemail to email mailbox greeting voicemail to email transcription greeting record *58 message answering machine voice mail after hours",
    category: "call-flows",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-view-call-recordings",
    title:    "Viewing Call Recordings",
    desc:     "How to access and download call recordings from the portal.",
    tags:     "call recordings download listen playback portal record calls recording playback download records",
    category: "call-flows",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-set-up-microsoft-teams",
    title:    "Setting Up Microsoft Teams Calling",
    desc:     "Connect Microsoft Teams to Click2Call Direct Routing — add the SBC domain, create the trunk user, map numbers to Teams users, and run the PowerShell commands.",
    tags:     "microsoft teams direct routing sbc powershell msteams calling office 365 m365 admin centre pstn gateway trunk voice route",
    category: "call-flows",
    readTime: "8 min read",
    featured: true,
    pinned:   false
  },

  /* ── Account & Billing ── */
  {
    url:      "/help/how-to-add-channels",
    title:    "Adding Concurrent Call Channels",
    desc:     "How to increase the number of simultaneous calls your system can handle.",
    tags:     "channels concurrent calls capacity add channels upgrade",
    category: "billing",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-view-account-history",
    title:    "Viewing Account History & Downloading Invoices",
    desc:     "How to view your transactions and download PDF receipts or invoices from the portal.",
    tags:     "account history transactions invoices receipts billing download pdf csv",
    category: "billing",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-use-reports-and-records",
    title:    "Using Reports & Records",
    desc:     "How to run call reports, search individual billing records, and export call data as CSV.",
    tags:     "reports records billing records call report export csv call history usage bill invoice charges usage statement scheduled report email",
    category: "billing",
    readTime: "4 min read",
    featured: true,
    pinned:   false
  },

  /* ── AI Features ── */
  {
    url:      "/help/how-to-set-up-ai-receptionist",
    title:    "Setting Up the AI Receptionist",
    desc:     "How to enable and configure the AI Receptionist to answer calls automatically.",
    tags:     "ai receptionist virtual receptionist auto answer setup configure departments route callers ai attendant answer calls virtual receptionist voice recognition",
    category: "ai",
    readTime: "4 min read",
    featured: true,
    pinned:   true
  },
  {
    url:      "/help/how-to-connect-ai-voice-agent",
    title:    "Connecting an AI Voice Agent to Your Number",
    desc:     "Point a phone number at ElevenLabs, OpenAI, xAI, Retell, VAPI or any SIP voice agent.",
    tags:     "ai voice agent elevenlabs openai xai retell vapi synthflow livekit cloudonix twilio sip registration external endpoint bland connection type profile",
    category: "ai",
    readTime: "6 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-connect-elevenlabs",
    title:    "Connecting ElevenLabs to Your Phone Number",
    desc:     "Point an Australian number at an ElevenLabs voice agent using the built-in profile. No code required.",
    tags:     "elevenlabs eleven labs ai voice agent sip trunk import phone number connection type profile no code",
    category: "ai",
    readTime: "5 min read",
    featured: false,
    pinned:   false
  },
  {
    url:      "/help/how-to-connect-openai",
    title:    "Connecting OpenAI to Your Phone Number",
    desc:     "Enter your OpenAI Project ID, set up the call webhook, and route calls to the Realtime API.",
    tags:     "openai project id realtime api sip webhook realtime.call.incoming voice agent connection type profile",
    category: "ai",
    readTime: "5 min read",
    featured: false,
    pinned:   false
  },
  {
    url:      "/help/how-to-connect-retell-ai",
    title:    "Connecting Retell AI to Your Phone Number",
    desc:     "Bring your own Australian number to a Retell AI agent using the built-in profile. No code required.",
    tags:     "retell retellai ai voice agent bring your own number import custom telephony connection type profile",
    category: "ai",
    readTime: "5 min read",
    featured: false,
    pinned:   false
  },
  {
    url:      "/help/how-to-connect-synthflow",
    title:    "Connecting Synthflow to Your Phone Number",
    desc:     "Import your number into Synthflow and point Click2Call at it with one dropdown. No code required.",
    tags:     "synthflow ai assistant voice agent sip trunk import phone number custom connection type profile",
    category: "ai",
    readTime: "5 min read",
    featured: false,
    pinned:   false
  },
  {
    url:      "/help/how-to-connect-vapi",
    title:    "Connecting Vapi to Your Phone Number",
    desc:     "Paste your Vapi Assistant ID into the profile and calls route straight to the assistant.",
    tags:     "vapi vapi.ai assistant id ai voice agent sip connection type profile bring your own number",
    category: "ai",
    readTime: "4 min read",
    featured: false,
    pinned:   false
  },
  {
    url:      "/help/how-to-connect-livekit",
    title:    "Connecting LiveKit Cloud to Your Phone Number",
    desc:     "Find your project subdomain and region, create an inbound trunk and dispatch rule, and connect.",
    tags:     "livekit cloud sip subdomain region inbound trunk dispatch rule agents worker connection type profile",
    category: "ai",
    readTime: "6 min read",
    featured: false,
    pinned:   false
  },
  {
    url:      "/help/how-to-connect-xai",
    title:    "Connecting xAI to Your Phone Number",
    desc:     "Register a bring-your-own-trunk number with xAI, host the webhook, and route calls to Grok.",
    tags:     "xai x.ai grok voice agent sip byo_trunk webhook websocket realtime connection type profile",
    category: "ai",
    readTime: "6 min read",
    featured: false,
    pinned:   false
  },
  {
    url:      "/help/how-to-connect-twilio",
    title:    "Connecting Twilio to Your Phone Number",
    desc:     "Route an Australian number into a Twilio SIP Domain so your TwiML or Studio Flow answers.",
    tags:     "twilio sip domain twiml studio flow subdomain ip access control list programmable voice connection type profile",
    category: "ai",
    readTime: "6 min read",
    featured: false,
    pinned:   false
  },
  {
    url:      "/help/how-to-connect-cloudonix",
    title:    "Connecting Cloudonix to Your Phone Number",
    desc:     "Route calls into a Cloudonix domain so a voice application can decide what happens next.",
    tags:     "cloudonix domain inbound trunk voice application dial service middleware sip connection type profile",
    category: "ai",
    readTime: "5 min read",
    featured: false,
    pinned:   false
  },
  {
    url:      "/help/how-to-set-up-ai-agents",
    title:    "Setting Up AI Agents",
    desc:     "How to create a conversational AI voice agent that answers calls and responds to questions 24/7.",
    tags:     "ai agent voice agent conversational ai chatbot knowledge base",
    category: "ai",
    readTime: "5 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-use-ai-speech",
    title:    "Using AI Speech Tools",
    desc:     "How to use Click2Call's AI speech synthesis and voice cloning tools.",
    tags:     "ai speech text to speech voice clone tts synthesis",
    category: "ai",
    readTime: "3 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-set-up-ai-voicemail",
    title:    "Setting Up AI Voicemail",
    desc:     "How to enable AI-powered voicemail transcription and smart summaries.",
    tags:     "ai voicemail transcription summary smart voicemail ai greeting voice actor text to speech mailbox",
    category: "ai",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  /* ── Added 2026-09-09 from portal walkthrough ── */
  {
    url:      "/help/how-to-forward-calls-to-mobile",
    title:    "Forwarding Calls to Your Mobile",
    desc:     "Divert your Click2Call number to a mobile during work hours and send after-hours callers to voicemail that is emailed to you, using Call Forwarding, Time Schedules and Voicemail settings.",
    tags:     "divert forward forwarding mobile call forwarding after hours work hours business hours voicemail to email redirect transfer cell phone out of office",
    category: "call-flows",
    readTime: "5 min read",
    featured: true,
    pinned:   true
  },
  {
    url:      "/help/how-to-set-up-missed-call-alerts",
    title:    "Setting Up Missed Call Alerts",
    desc:     "Turn on Missed Call Notifications so Click2Call emails or texts you whenever an incoming call on your number goes unanswered.",
    tags:     "missed call alert notification email sms text unanswered call back lost calls",
    category: "call-flows",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-close-for-holidays",
    title:    "Closing for Holidays",
    desc:     "Use Do Not Disturb with specific dates to send callers to voicemail or a divert number while your business is closed for holidays, without changing your normal call flow.",
    tags:     "holiday closure closed christmas public holiday do not disturb dnd away out of office dates divert voicemail",
    category: "call-flows",
    readTime: "3 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-set-up-answer-agent",
    title:    "Ring First, Then Let the AI Take a Message",
    desc:     "Ring your phone first and have the AI Answer Agent take the caller\u2019s name, number and reason for calling, then email you the details.",
    tags:     "answer agent ai answering service take a message ring first unanswered virtual assistant receptionist script introduction questions voice australian female transcript email appointment booking message taking business profile call flow",
    category: "ai",
    readTime: "5 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-add-portal-logins",
    title:    "Adding Portal Logins for Your Team",
    desc:     "Create additional Click2Call portal logins for staff, bookkeepers or receptionists with the right access level, optional two-factor authentication, and recording-deletion protection.",
    tags:     "login user access staff portal password 2fa two factor administrator read only billing access bookkeeper accountant permissions",
    category: "getting-started",
    readTime: "3 min read",
    featured: true,
    pinned:   false
  }
];

/**
 * HELP_CATEGORIES — ordered list of categories for display
 * Add new categories here when needed.
 */
var HELP_CATEGORIES = [
  { key: "getting-started", label: "Getting Started",      icon: "rocket" },
  { key: "phone-numbers",   label: "Phone Numbers",        icon: "phone" },
  { key: "extensions",      label: "Extensions & Users",   icon: "users" },
  { key: "devices",         label: "Devices & Apps",       icon: "monitor" },
  { key: "call-flows",      label: "Call Flows & Routing", icon: "git-branch" },
  { key: "billing",         label: "Account & Billing",    icon: "credit-card" },
  { key: "ai",              label: "AI Features",          icon: "cpu" }
];
