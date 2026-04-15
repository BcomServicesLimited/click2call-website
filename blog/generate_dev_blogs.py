import os
import re
from datetime import datetime

template_path = "/home/ubuntu/click2call/blog/article-template.html"
with open(template_path, "r") as f:
    template = f.read()

blogs = [
    {
        "slug": "cloudflare-worker-phone-system-api",
        "title": "How to Integrate a Phone System into a Cloudflare Worker using the Click2Call API",
        "description": "A step-by-step guide for developers on connecting an Australian phone system to a Cloudflare Worker using the Click2Call API and webhooks.",
        "image": "blog/cloudflare-worker-api-hero",
        "author": "Royce Clark",
        "date": "2026-04-16",
        "content": """
    <p class="text-lg">Serverless computing has changed how we build applications, and Cloudflare Workers are at the forefront of this shift. But what happens when your serverless app needs to interact with the real world—specifically, the telephone network? In this guide, we'll walk through how to integrate a real Australian phone system into a Cloudflare Worker using the Click2Call API.</p>

    <hr class="my-10 border-gray-200">

    <h2 class="text-2xl font-extrabold text-brand-charcoal mt-10 mb-4">Why Connect a Phone System to a Cloudflare Worker?</h2>

    <p>Cloudflare Workers run on the edge, meaning they execute code incredibly fast and close to the user. This makes them perfect for handling real-time events, such as incoming phone calls. By connecting a phone system to a Worker, you can build powerful, low-latency voice applications without managing any servers.</p>

    <p>Common use cases include:</p>
    <ul class="mt-5 space-y-3 text-gray-700">
        <li class="flex items-start gap-3"><span class="mt-1 flex-shrink-0 w-5 h-5 rounded-full bg-green-100 flex items-center justify-center"><svg class="w-3 h-3 text-[#059669]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg></span><span><strong>Dynamic Call Routing:</strong> Route calls based on real-time database lookups or API calls.</span></li>
        <li class="flex items-start gap-3"><span class="mt-1 flex-shrink-0 w-5 h-5 rounded-full bg-green-100 flex items-center justify-center"><svg class="w-3 h-3 text-[#059669]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg></span><span><strong>Automated Logging:</strong> Log every call directly into your CRM or database the moment it ends.</span></li>
        <li class="flex items-start gap-3"><span class="mt-1 flex-shrink-0 w-5 h-5 rounded-full bg-green-100 flex items-center justify-center"><svg class="w-3 h-3 text-[#059669]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg></span><span><strong>AI Voice Agents:</strong> Connect inbound calls to an AI agent hosted on a Worker.</span></li>
    </ul>

    <hr class="my-10 border-gray-200">

    <h2 class="text-2xl font-extrabold text-brand-charcoal mt-10 mb-4">Step 1: Setting Up Your Click2Call Account</h2>

    <p>Before writing any code, you need a Click2Call account. Every Cloud PBX account includes free access to the Developer API. Once you've signed up, navigate to the <strong>API &gt; Getting Started</strong> section in the portal to retrieve your API token.</p>

    <p>You'll also need to configure a webhook. Go to <strong>API &gt; Webhooks</strong> and create a new webhook. Set the URL to your Cloudflare Worker's address (we'll build this next) and select the events you want to listen for, such as "Incoming Calls - Answered Event" or "Incoming Calls - Ended Event".</p>

    <hr class="my-10 border-gray-200">

    <h2 class="text-2xl font-extrabold text-brand-charcoal mt-10 mb-4">Step 2: Creating the Cloudflare Worker</h2>

    <p>Now, let's create the Worker. If you haven't already, install the Wrangler CLI and initialize a new project:</p>

    <pre><code>npm install -g wrangler
wrangler init click2call-worker
cd click2call-worker</code></pre>

    <p>Open the <code>src/index.js</code> file. This is where we'll write the code to handle incoming webhooks from Click2Call.</p>

    <hr class="my-10 border-gray-200">

    <h2 class="text-2xl font-extrabold text-brand-charcoal mt-10 mb-4">Step 3: Handling Webhook Events</h2>

    <p>When a call event occurs, Click2Call sends a POST request to your Worker. Here's a basic example of how to parse that request and log the call details:</p>

    <pre><code>export default {
  async fetch(request, env, ctx) {
    // Only accept POST requests
    if (request.method !== 'POST') {
      return new Response('Method Not Allowed', { status: 405 });
    }

    // Verify the secret token (set this in your Click2Call webhook config)
    const authHeader = request.headers.get('Authorization');
    if (authHeader !== env.WEBHOOK_SECRET) {
      return new Response('Unauthorized', { status: 401 });
    }

    try {
      const payload = await request.json();
      
      // Handle different event types
      if (payload.event === 'call.ended') {
        console.log(`Call ended. Caller: ${payload.caller}, Duration: ${payload.duration}s`);
        // Here you could save the data to a database or send an alert
      }

      return new Response('Webhook received', { status: 200 });
    } catch (error) {
      return new Response('Bad Request', { status: 400 });
    }
  },
};</code></pre>

    <p>Remember to set your <code>WEBHOOK_SECRET</code> in your Cloudflare Worker environment variables to match the secret token you configured in the Click2Call portal.</p>

    <hr class="my-10 border-gray-200">

    <h2 class="text-2xl font-extrabold text-brand-charcoal mt-10 mb-4">Step 4: Making API Calls from the Worker</h2>

    <p>You can also use the Worker to make outbound requests to the Click2Call API. For example, you might want to fetch the transcription of a call after it ends. Here's how you can do that:</p>

    <pre><code>async function getTranscription(uniqueId, apiToken) {
  const response = await fetch('https://portal.click2call.com.au/api/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${apiToken}`
    },
    body: JSON.stringify({
      context: 'ai',
      action: 'Get-Transcription',
      unique_id: uniqueId
    })
  });

  const data = await response.json();
  return data.transcription;
}</code></pre>

    <p>You can call this function from within your webhook handler when you receive a "Recording &amp; AI transcription generation" event.</p>

    <hr class="my-10 border-gray-200">

    <h2 class="text-2xl font-extrabold text-brand-charcoal mt-10 mb-4">Conclusion</h2>

    <p>Integrating a phone system into a Cloudflare Worker is surprisingly straightforward with the Click2Call API. By combining the speed and scalability of Workers with the robust voice infrastructure of Click2Call, you can build powerful, serverless voice applications in minutes.</p>
"""
    },
    {
        "slug": "building-ai-call-agent-claude-click2call",
        "title": "Building an AI Call Agent with Claude and Click2Call",
        "description": "Learn how to build a conversational AI call agent using Anthropic's Claude and the Click2Call Australian VoIP API.",
        "image": "blog/ai-call-agent-claude-hero",
        "author": "Royce Clark",
        "date": "2026-04-16",
        "content": """
    <p class="text-lg">Conversational AI has reached a tipping point. With models like Anthropic's Claude, it's now possible to build AI agents that can hold natural, nuanced conversations over the phone. In this guide, we'll explore how to connect Claude to a real Australian phone number using the Click2Call API.</p>

    <hr class="my-10 border-gray-200">

    <h2 class="text-2xl font-extrabold text-brand-charcoal mt-10 mb-4">The Architecture of an AI Call Agent</h2>

    <p>Building an AI call agent requires three main components:</p>
    <ul class="mt-5 space-y-3 text-gray-700">
        <li class="flex items-start gap-3"><span class="mt-1 flex-shrink-0 w-5 h-5 rounded-full bg-green-100 flex items-center justify-center"><svg class="w-3 h-3 text-[#059669]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg></span><span><strong>The Telephony Provider:</strong> Click2Call provides the phone number, SIP trunking, and API to handle the actual phone calls.</span></li>
        <li class="flex items-start gap-3"><span class="mt-1 flex-shrink-0 w-5 h-5 rounded-full bg-green-100 flex items-center justify-center"><svg class="w-3 h-3 text-[#059669]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg></span><span><strong>The Voice Engine:</strong> A service like ElevenLabs converts text to speech (TTS) and speech to text (STT) in real-time.</span></li>
        <li class="flex items-start gap-3"><span class="mt-1 flex-shrink-0 w-5 h-5 rounded-full bg-green-100 flex items-center justify-center"><svg class="w-3 h-3 text-[#059669]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg></span><span><strong>The Brain:</strong> Claude processes the transcribed text, determines the appropriate response, and generates the text to be spoken back.</span></li>
    </ul>

    <hr class="my-10 border-gray-200">

    <h2 class="text-2xl font-extrabold text-brand-charcoal mt-10 mb-4">The ElevenLabs Shortcut</h2>

    <p>While you can build the entire pipeline from scratch, Click2Call offers a massive shortcut: native ElevenLabs integration. Instead of managing the complex SIP and RTP streams yourself, you can configure your Click2Call phone line to route directly to an ElevenLabs conversational AI agent.</p>

    <p>Here's how to set it up:</p>
    <ol class="mt-5 space-y-3 text-gray-700 list-decimal list-inside">
        <li>Log in to the Click2Call portal.</li>
        <li>Navigate to <strong>Line Preferences</strong> and select the profile for your phone number.</li>
        <li>Change the <strong>Connection Type</strong> to "Eleven Labs AI".</li>
        <li>The system will automatically configure the Inbound SIP URI Route to <code>sip:sip.rtc.elevenlabs.io:5060;transport=tcp</code>.</li>
        <li>Save the profile.</li>
    </ol>

    <p>Now, any call to that number will be routed directly to ElevenLabs.</p>

    <hr class="my-10 border-gray-200">

    <h2 class="text-2xl font-extrabold text-brand-charcoal mt-10 mb-4">Connecting Claude</h2>

    <p>With the telephony handled, you need to connect ElevenLabs to Claude. ElevenLabs provides a Conversational AI platform where you can define the agent's persona and connect it to an LLM.</p>

    <p>In the ElevenLabs dashboard, configure your agent to use Claude as its language model. You can provide Claude with a system prompt that defines its role, such as:</p>

    <blockquote class="not-prose my-8 border-l-4 border-[#059669] pl-6 py-2">
        <p class="text-lg font-medium text-brand-charcoal italic">"You are a helpful customer support agent for an Australian plumbing company. Your goal is to answer basic questions about pricing and availability, and to collect the caller's details to schedule a quote. Be polite, concise, and use Australian English."</p>
    </blockquote>

    <hr class="my-10 border-gray-200">

    <h2 class="text-2xl font-extrabold text-brand-charcoal mt-10 mb-4">Using the Click2Call API for Post-Call Actions</h2>

    <p>The conversation is handled by ElevenLabs and Claude, but what happens after the call ends? This is where the Click2Call API comes back in.</p>

    <p>You can set up a webhook in the Click2Call portal to notify your server when a call ends. When you receive this webhook, you can use the Click2Call API to fetch the call recording and transcription.</p>

    <pre><code>// Example payload from Click2Call webhook
{
  "event": "call.ended",
  "direction": "inbound",
  "number": "+61299999999",
  "caller": "+61411111111",
  "unique_id": "abc123xyz"
}</code></pre>

    <p>You can then pass this transcription back to Claude to extract structured data, such as the customer's name, address, and the reason for calling, and automatically log this information into your CRM.</p>

    <hr class="my-10 border-gray-200">

    <h2 class="text-2xl font-extrabold text-brand-charcoal mt-10 mb-4">Conclusion</h2>

    <p>Building an AI call agent used to require deep expertise in telephony and machine learning. Today, by combining Click2Call's native ElevenLabs integration with Anthropic's Claude, developers can deploy sophisticated, natural-sounding voice agents in a matter of hours.</p>
"""
    },
    {
        "slug": "australian-voip-api-getting-started",
        "title": "Australian VoIP API: Getting Started Guide for AI Developers",
        "description": "A comprehensive guide for developers and AI builders on getting started with the Click2Call Australian VoIP API.",
        "image": "blog/australian-voip-api-hero",
        "author": "Royce Clark",
        "date": "2026-04-16",
        "content": """
    <p class="text-lg">If you're building AI applications, CRM integrations, or custom business software in Australia, you eventually hit a wall: you need to connect your code to the real world. You need a real Australian phone number, the ability to make and receive calls, and access to call data. This is where the Click2Call VoIP API comes in.</p>

    <hr class="my-10 border-gray-200">

    <h2 class="text-2xl font-extrabold text-brand-charcoal mt-10 mb-4">What is the Click2Call API?</h2>

    <p>The Click2Call API is a JSON-based REST API designed specifically for developers and AI builders. It allows you to programmatically control a fully hosted Australian phone system. Unlike complex telecom APIs that require deep knowledge of SIP and RTP, the Click2Call API abstracts the complexity, letting you focus on building your application.</p>

    <p>Key capabilities include:</p>
    <ul class="mt-5 space-y-3 text-gray-700">
        <li class="flex items-start gap-3"><span class="mt-1 flex-shrink-0 w-5 h-5 rounded-full bg-green-100 flex items-center justify-center"><svg class="w-3 h-3 text-[#059669]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg></span><span><strong>Voice Control:</strong> Manage lines, enable recording, and download audio files.</span></li>
        <li class="flex items-start gap-3"><span class="mt-1 flex-shrink-0 w-5 h-5 rounded-full bg-green-100 flex items-center justify-center"><svg class="w-3 h-3 text-[#059669]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg></span><span><strong>AI Functions:</strong> Access transcriptions, sentiment analysis, and text-to-speech (TTS).</span></li>
        <li class="flex items-start gap-3"><span class="mt-1 flex-shrink-0 w-5 h-5 rounded-full bg-green-100 flex items-center justify-center"><svg class="w-3 h-3 text-[#059669]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg></span><span><strong>Webhooks:</strong> Receive real-time HTTP POST events for call activity.</span></li>
    </ul>

    <hr class="my-10 border-gray-200">

    <h2 class="text-2xl font-extrabold text-brand-charcoal mt-10 mb-4">Authentication and Setup</h2>

    <p>Getting started is simple. API access is included free with every Click2Call Cloud PBX account. Once you have an account, log in to the portal and navigate to <strong>API &gt; Getting Started</strong>.</p>

    <p>Here, you will find your Bearer token, which is required for all API requests. The API uses a single endpoint for all requests:</p>

    <pre><code>https://portal.click2call.com.au/api/</code></pre>

    <p>Every request must be a POST request containing a JSON body with a <code>context</code> and an <code>action</code>.</p>

    <hr class="my-10 border-gray-200">

    <h2 class="text-2xl font-extrabold text-brand-charcoal mt-10 mb-4">Making Your First API Call</h2>

    <p>Let's make a simple API call to retrieve the account balance. The context is <code>account</code> and the action is <code>Get-Account-Balance</code>.</p>

    <pre><code>curl -X POST https://portal.click2call.com.au/api/ \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer YOUR_API_TOKEN" \\
  -d '{
    "context": "account",
    "action": "Get-Account-Balance"
  }'</code></pre>

    <p>The API will return a JSON response containing your current balance and account details.</p>

    <hr class="my-10 border-gray-200">

    <h2 class="text-2xl font-extrabold text-brand-charcoal mt-10 mb-4">The "Copy. Paste. Build." Advantage</h2>

    <p>One of the biggest advantages of the Click2Call API is that you don't even need to write the code yourself. The portal includes a complete set of ready-made instructions designed specifically for AI coding tools like Claude, Cursor, and ChatGPT.</p>

    <p>You simply copy the instructions from the portal, paste them into your LLM, and describe what you want to build. For example:</p>

    <blockquote class="not-prose my-8 border-l-4 border-[#059669] pl-6 py-2">
        <p class="text-lg font-medium text-brand-charcoal italic">"Here are the Click2Call API instructions. I want to build a Node.js script that fetches the transcription for a specific call ID and saves it to a text file."</p>
    </blockquote>

    <p>The LLM will generate the complete, working code based on the provided API context, saving you hours of reading documentation and debugging.</p>

    <hr class="my-10 border-gray-200">

    <h2 class="text-2xl font-extrabold text-brand-charcoal mt-10 mb-4">Conclusion</h2>

    <p>The Click2Call API provides a powerful, accessible way for developers to integrate Australian telephony into their applications. With comprehensive features, real-time webhooks, and AI-ready instructions, it's the ideal platform for building the next generation of voice-enabled software.</p>
"""
    },
    {
        "slug": "call-transcriptions-sentiment-data-api-australia",
        "title": "How to Get Call Transcriptions and Sentiment Data via API in Australia",
        "description": "Learn how to automatically retrieve call transcriptions, AI summaries, and sentiment analysis data using the Click2Call API.",
        "image": "blog/transcription-sentiment-api-hero",
        "author": "Royce Clark",
        "date": "2026-04-16",
        "content": """
    <p class="text-lg">Voice calls contain a wealth of business intelligence, but historically, that data has been locked away in audio files. Today, AI can transcribe and analyze calls in real-time, turning spoken conversations into structured, actionable data. In this guide, we'll show you how to automatically retrieve call transcriptions, summaries, and sentiment data using the Click2Call API.</p>

    <hr class="my-10 border-gray-200">

    <h2 class="text-2xl font-extrabold text-brand-charcoal mt-10 mb-4">The Value of Call Data</h2>

    <p>Accessing call data programmatically unlocks numerous possibilities for businesses:</p>
    <ul class="mt-5 space-y-3 text-gray-700">
        <li class="flex items-start gap-3"><span class="mt-1 flex-shrink-0 w-5 h-5 rounded-full bg-green-100 flex items-center justify-center"><svg class="w-3 h-3 text-[#059669]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg></span><span><strong>Automated CRM Logging:</strong> Automatically attach full call transcripts and summaries to customer records in Salesforce or HubSpot.</span></li>
        <li class="flex items-start gap-3"><span class="mt-1 flex-shrink-0 w-5 h-5 rounded-full bg-green-100 flex items-center justify-center"><svg class="w-3 h-3 text-[#059669]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg></span><span><strong>Quality Assurance:</strong> Identify calls with negative sentiment scores to flag them for manager review.</span></li>
        <li class="flex items-start gap-3"><span class="mt-1 flex-shrink-0 w-5 h-5 rounded-full bg-green-100 flex items-center justify-center"><svg class="w-3 h-3 text-[#059669]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg></span><span><strong>Trend Analysis:</strong> Feed transcriptions into an LLM to identify common customer complaints or feature requests.</span></li>
    </ul>

    <hr class="my-10 border-gray-200">

    <h2 class="text-2xl font-extrabold text-brand-charcoal mt-10 mb-4">Step 1: Listening for the Webhook</h2>

    <p>The most efficient way to process call data is to wait for the system to tell you it's ready. Click2Call provides a specific webhook event for this: <strong>"Recording &amp; AI transcription generation"</strong>.</p>

    <p>Configure a webhook in the Click2Call portal to point to your server. When a call ends and the AI processing is complete, your server will receive a POST request containing the <code>unique_id</code> of the call.</p>

    <hr class="my-10 border-gray-200">

    <h2 class="text-2xl font-extrabold text-brand-charcoal mt-10 mb-4">Step 2: Fetching the Transcription</h2>

    <p>Once you have the <code>unique_id</code>, you can use the API's AI Functions to retrieve the transcription. The context is <code>ai</code> and the action is <code>Get-Transcription</code>.</p>

    <pre><code>curl -X POST https://portal.click2call.com.au/api/ \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer YOUR_API_TOKEN" \\
  -d '{
    "context": "ai",
    "action": "Get-Transcription",
    "unique_id": "CALL_UNIQUE_ID"
  }'</code></pre>

    <p>This will return the full text transcription of the conversation, separated by speaker.</p>

    <hr class="my-10 border-gray-200">

    <h2 class="text-2xl font-extrabold text-brand-charcoal mt-10 mb-4">Step 3: Fetching the Summary and Sentiment</h2>

    <p>Reading full transcripts is time-consuming. Click2Call also generates concise summaries and sentiment scores. To retrieve these, use the <code>Get-Transcription-Summary</code> action.</p>

    <pre><code>curl -X POST https://portal.click2call.com.au/api/ \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer YOUR_API_TOKEN" \\
  -d '{
    "context": "ai",
    "action": "Get-Transcription-Summary",
    "unique_id": "CALL_UNIQUE_ID"
  }'</code></pre>

    <p>The response will include a brief summary of the call's outcome and a sentiment analysis score (e.g., Positive, Neutral, Negative), allowing you to quickly gauge customer satisfaction.</p>

    <hr class="my-10 border-gray-200">

    <h2 class="text-2xl font-extrabold text-brand-charcoal mt-10 mb-4">Conclusion</h2>

    <p>By combining webhooks with the Click2Call AI API, developers can build automated workflows that extract immense value from every phone call. Whether you're building a custom CRM integration or a sophisticated business intelligence dashboard, accessing transcriptions and sentiment data has never been easier.</p>
"""
    }
]

for blog in blogs:
    html = template
    html = html.replace("[ARTICLE TITLE]", blog["title"])
    html = html.replace("[ARTICLE DESCRIPTION]", blog["description"])
    html = html.replace("[ARTICLE-SLUG]", blog["slug"])
    html = html.replace("[ARTICLE-IMAGE]", blog["image"])
    html = html.replace("[AUTHOR NAME]", blog["author"])
    html = html.replace("2026-02-23", blog["date"])
    html = html.replace("23 Feb 2026", "16 Apr 2026")
    
    # Replace the body content
    # Find the start of the article body (after the hero)
    body_start_marker = '<!-- Article Body -->'
    body_end_marker = '<!-- Sidebar -->'
    
    start_idx = html.find(body_start_marker)
    end_idx = html.find(body_end_marker)
    
    if start_idx != -1 and end_idx != -1:
        # We need to keep the div structure
        prefix = html[:start_idx + len(body_start_marker)]
        suffix = html[end_idx:]
        
        new_body = f"""
        <div class="lg:col-span-2">
            <div class="prose prose-lg max-w-none text-gray-700 leading-relaxed">
                <figure class="not-prose my-8 rounded-xl overflow-hidden shadow-md">
                    <img src="/assets/images/{blog['image']}.webp" alt="{blog['title']}" class="w-full object-cover" loading="eager" width="1200" height="675">
                </figure>
                {blog['content']}
            </div>
        </div>
        """
        html = prefix + new_body + suffix
        
    # Remove noindex
    html = html.replace('<meta name="robots" content="noindex, nofollow">', '<meta name="robots" content="max-image-preview:large, max-snippet:-1, max-video-preview:-1">')
    
    # Write the file
    file_path = f"/home/ubuntu/click2call/blog/{blog['slug']}.html"
    with open(file_path, "w") as f:
        f.write(html)
    print(f"Generated {file_path}")
