/**
 * articles.js — Click2Call central help article registry
 * Bcom Services Pty Ltd (ABN: 92 636 893 108)
 *
 * HOW TO ADD A NEW ARTICLE:
 * 1. Create the article HTML file in /help/
 * 2. Add one entry to the HELP_ARTICLES array below
 * 3. That's it — both /help and /support update automatically
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

  /* ── Getting Started ── */
  {
    url:      "/help/how-to-activate-account.html",
    title:    "Activating Your Account",
    desc:     "How to activate your Click2Call account and log in to the portal for the first time.",
    tags:     "activate account setup first time login portal",
    category: "getting-started",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-add-account-credit.html",
    title:    "Adding Account Credit",
    desc:     "How to load credit onto your account and set up auto top-up.",
    tags:     "add credit top up prepay billing payment auto top-up",
    category: "getting-started",
    readTime: "2 min read",
    featured: true,
    pinned:   true
  },

  /* ── Phone Numbers ── */
  {
    url:      "/help/how-to-add-phone-number.html",
    title:    "Adding a Phone Number",
    desc:     "How to add a new local or 1300 number to your account.",
    tags:     "add phone number ddi direct dial 1300 local number",
    category: "phone-numbers",
    readTime: "2 min read",
    featured: true,
    pinned:   true
  },
  {
    url:      "/help/how-to-port-number.html",
    title:    "Porting an Existing Number",
    desc:     "How to transfer your current phone number to Click2Call with no downtime.",
    tags:     "port number transfer porting existing number move",
    category: "phone-numbers",
    readTime: "3 min read",
    featured: true,
    pinned:   false
  },

  /* ── Extensions & Users ── */
  {
    url:      "/help/how-to-add-extension.html",
    title:    "Adding a New Extension",
    desc:     "How to create a new extension on your Cloud PBX.",
    tags:     "add extension new extension pbx create",
    category: "extensions",
    readTime: "2 min read",
    featured: true,
    pinned:   true
  },
  {
    url:      "/help/how-to-add-user.html",
    title:    "Adding a New User",
    desc:     "How to add a staff member to your account and assign their credentials.",
    tags:     "add user staff member credentials new user invite",
    category: "extensions",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-set-outbound-caller-id.html",
    title:    "Setting Outbound Caller ID",
    desc:     "How to set which number displays when your extensions make outbound calls.",
    tags:     "caller id outbound caller id cli number display",
    category: "extensions",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  /* ── Devices & Apps ── */
  {
    url:      "/help/how-to-add-desk-phone.html",
    title:    "Registering a Desk Phone",
    desc:     "How to register a Yealink or compatible SIP desk phone to your extension.",
    tags:     "desk phone register yealink sip phone hardware setup",
    category: "devices",
    readTime: "3 min read",
    featured: true,
    pinned:   true
  },
  {
    url:      "/help/how-to-set-up-softphone.html",
    title:    "Setting Up a Softphone or Mobile App",
    desc:     "How to install and configure the softphone app on your PC or mobile device.",
    tags:     "softphone mobile app ios android pc desktop download install",
    category: "devices",
    readTime: "3 min read",
    featured: true,
    pinned:   true
  },

  /* ── Call Flows & Routing ── */
  {
    url:      "/help/how-to-set-up-call-flow.html",
    title:    "Setting Up a Call Flow",
    desc:     "How to build a call flow to route incoming calls to the right destination.",
    tags:     "call flow routing inbound ivr auto attendant menu",
    category: "call-flows",
    readTime: "4 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-create-ring-group.html",
    title:    "Creating a Ring Group",
    desc:     "How to set up a ring group so multiple extensions ring simultaneously.",
    tags:     "ring group hunt group simultaneous ring group call",
    category: "call-flows",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-configure-business-hours.html",
    title:    "Configuring Business Hours",
    desc:     "How to set your open and closed hours so calls route correctly after hours.",
    tags:     "business hours after hours time conditions schedule closed",
    category: "call-flows",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-set-up-voicemail.html",
    title:    "Setting Up Voicemail",
    desc:     "How to enable voicemail on an extension and configure voicemail-to-email.",
    tags:     "voicemail setup voicemail to email mailbox greeting",
    category: "call-flows",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-view-call-recordings.html",
    title:    "Viewing Call Recordings",
    desc:     "How to access and download call recordings from the portal.",
    tags:     "call recordings download listen playback portal",
    category: "call-flows",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },

  /* ── Account & Billing ── */
  {
    url:      "/help/how-to-add-channels.html",
    title:    "Adding Concurrent Call Channels",
    desc:     "How to increase the number of simultaneous calls your system can handle.",
    tags:     "channels concurrent calls capacity add channels upgrade",
    category: "billing",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-view-account-history.html",
    title:    "Viewing Account History & Downloading Invoices",
    desc:     "How to view your transactions and download PDF receipts or invoices from the portal.",
    tags:     "account history transactions invoices receipts billing download pdf csv",
    category: "billing",
    readTime: "2 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-use-reports-and-records.html",
    title:    "Using Reports & Records",
    desc:     "How to run call reports, search individual billing records, and export call data as CSV.",
    tags:     "reports records billing records call report export csv call history usage",
    category: "billing",
    readTime: "4 min read",
    featured: true,
    pinned:   false
  },

  /* ── AI Features ── */
  {
    url:      "/help/how-to-set-up-ai-receptionist.html",
    title:    "Setting Up the AI Receptionist",
    desc:     "How to enable and configure the AI Receptionist to answer calls automatically.",
    tags:     "ai receptionist virtual receptionist auto answer setup configure",
    category: "ai",
    readTime: "4 min read",
    featured: true,
    pinned:   true
  },
  {
    url:      "/help/how-to-set-up-ai-agents.html",
    title:    "Setting Up AI Agents",
    desc:     "How to create a conversational AI voice agent that answers calls and responds to questions 24/7.",
    tags:     "ai agent voice agent conversational ai chatbot knowledge base",
    category: "ai",
    readTime: "5 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-use-ai-speech.html",
    title:    "Using AI Speech Tools",
    desc:     "How to use Click2Call's AI speech synthesis and voice cloning tools.",
    tags:     "ai speech text to speech voice clone tts synthesis",
    category: "ai",
    readTime: "3 min read",
    featured: true,
    pinned:   false
  },
  {
    url:      "/help/how-to-set-up-ai-voicemail.html",
    title:    "Setting Up AI Voicemail",
    desc:     "How to enable AI-powered voicemail transcription and smart summaries.",
    tags:     "ai voicemail transcription summary smart voicemail",
    category: "ai",
    readTime: "2 min read",
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
