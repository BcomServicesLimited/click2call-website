import re

with open('/home/ubuntu/click2call/blog/cloudflare-worker-phone-system-api.html', 'r') as f:
    content = f.read()

# Update hero image to webp
content = content.replace('cloudflare-worker-api-hero.jpg', 'cloudflare-worker-api-hero.webp')

# Update category and description
content = content.replace('[CATEGORY]', 'Developer API')
content = content.replace('[ARTICLE SUBHEADING / DESCRIPTION]', 'A step-by-step guide for developers on connecting an Australian phone system to a Cloudflare Worker using the Click2Call API and webhooks.')

# Update takeaways
takeaways = """<li><strong>Serverless Voice:</strong> Connect a real Australian phone number directly to a Cloudflare Worker without managing any telecom infrastructure.</li>
                        <li><strong>Real-Time Webhooks:</strong> Trigger Worker functions instantly on incoming calls, answered calls, or ended calls.</li>
                        <li><strong>AI-Ready:</strong> Easily pass call data from your Worker to LLMs like Claude or ChatGPT for instant analysis.</li>
                        <li><strong>Zero Maintenance:</strong> Click2Call handles the SIP trunks and carrier routing; you just write JavaScript.</li>"""
content = re.sub(r'<li>\[Takeaway 1\].*?<li>\[Takeaway 4\]</li>', takeaways, content, flags=re.DOTALL)

# Update body content
body_content = """<p>Building modern business software often means integrating voice capabilities. Whether you're building a custom CRM, an automated support desk, or an AI voice agent, you need a reliable way to connect real phone calls to your code. Traditionally, this meant dealing with complex SIP trunks, PBX hardware, and telecom protocols.</p>
                
                <p>Today, the landscape has changed. Using the Click2Call API and Cloudflare Workers, you can deploy a fully functional, serverless voice integration in an afternoon. This guide walks you through the process of connecting an Australian phone system to a Cloudflare Worker, allowing you to handle calls programmatically with zero infrastructure overhead.</p>

                <h2 class="text-2xl font-bold text-brand-charcoal mt-10 mb-4">Why Cloudflare Workers for Voice?</h2>
                <p>Cloudflare Workers are an ideal environment for handling voice API webhooks. They offer:</p>
                <ul class="list-disc pl-6 mb-6 space-y-2">
                    <li><strong>Ultra-low latency:</strong> Workers run on Cloudflare's global edge network, ensuring your webhook responses are lightning-fast—critical for voice applications where delays are noticeable.</li>
                    <li><strong>Zero cold starts:</strong> Unlike traditional serverless functions, Workers don't suffer from cold starts, meaning the first ring is handled just as quickly as the hundredth.</li>
                    <li><strong>Cost-effective scaling:</strong> You only pay for what you use, making it perfect for unpredictable call volumes.</li>
                </ul>

                <h2 class="text-2xl font-bold text-brand-charcoal mt-10 mb-4">Step 1: Setting Up Your Click2Call Webhook</h2>
                <p>The first step is telling Click2Call where to send data when a call event occurs. In your Click2Call portal, navigate to the <strong>API > Webhooks</strong> section.</p>
                
                <p>Create a new webhook and configure it to point to your Cloudflare Worker URL (e.g., <code>https://voice-handler.yourdomain.workers.dev</code>). You can select which events should trigger the webhook:</p>
                <ul class="list-disc pl-6 mb-6 space-y-2">
                    <li><strong>Incoming Calls:</strong> Ringing, Answered, Ended, Missed</li>
                    <li><strong>Outgoing Calls:</strong> Ringing, Answered, Ended, Unattended</li>
                    <li><strong>AI Analysis:</strong> Recording and AI transcription generation</li>
                </ul>
                <p>For a basic integration, selecting "Ringing Event" and "Ended Event" is a great starting point.</p>

                <div class="bg-gray-900 rounded-lg p-4 my-6 overflow-x-auto">
                    <pre><code class="text-green-400 text-sm">Content-Type: application/json
Authorization: your-secret-token
Content:
{
  "event": "ringing",
  "call_id": "123456789",
  "caller_id": "+61400000000",
  "called_number": "+61280000000",
  "timestamp": "2026-04-16T10:00:00Z"
}</code></pre>
                </div>

                <h2 class="text-2xl font-bold text-brand-charcoal mt-10 mb-4">Step 2: Writing the Cloudflare Worker</h2>
                <p>Now, let's write the Worker code to handle these incoming webhooks. We'll create a simple script that logs the call details and can be easily extended to trigger other actions, like sending a Slack notification or querying a database.</p>

                <div class="bg-gray-900 rounded-lg p-4 my-6 overflow-x-auto">
                    <pre><code class="text-blue-300 text-sm">export default {
  async fetch(request, env, ctx) {
    // Only accept POST requests
    if (request.method !== 'POST') {
      return new Response('Method Not Allowed', { status: 405 });
    }

    // Verify the authorization token
    const authHeader = request.headers.get('Authorization');
    if (authHeader !== env.CLICK2CALL_SECRET) {
      return new Response('Unauthorized', { status: 401 });
    }

    try {
      const payload = await request.json();
      
      // Handle different event types
      switch (payload.event) {
        case 'ringing':
          console.log(`Incoming call from ${payload.caller_id}`);
          // Add your custom logic here (e.g., CRM lookup)
          break;
        case 'ended':
          console.log(`Call ${payload.call_id} ended`);
          break;
        case 'transcription_ready':
          console.log(`Transcription available for ${payload.call_id}`);
          // Send transcription to an LLM for summarization
          break;
      }

      return new Response('Webhook received', { status: 200 });
    } catch (error) {
      console.error('Error processing webhook:', error);
      return new Response('Bad Request', { status: 400 });
    }
  }
};</code></pre>
                </div>

                <h2 class="text-2xl font-bold text-brand-charcoal mt-10 mb-4">Step 3: Extending with the Click2Call API</h2>
                <p>Webhooks are great for receiving data, but what if you want to take action? The Click2Call API allows your Worker to actively manage calls and account settings.</p>
                <p>For example, when a call ends, your Worker could use the API to fetch the call recording or transcription, then pass that data to Claude or ChatGPT to generate a summary and push it to your CRM.</p>
                
                <blockquote class="border-l-4 border-brand-green-dark pl-4 italic text-gray-700 my-6">
                    "By combining Click2Call's robust API with the serverless power of Cloudflare Workers, developers can build enterprise-grade voice applications without touching a single piece of telecom hardware."
                </blockquote>

                <h2 class="text-2xl font-bold text-brand-charcoal mt-10 mb-4">Ready to Build?</h2>
                <p>Integrating a real Australian phone system into your custom software has never been easier. With Click2Call's developer-friendly API and comprehensive webhook support, you can focus on writing code, not managing infrastructure.</p>
                <p>Every Click2Call account includes full API access. <a href="/api" class="text-brand-green-dark hover:underline font-semibold">Explore the Developer API</a> to see what else you can build.</p>"""

content = re.sub(r'<p>\[ARTICLE BODY CONTENT.*?<p>\[Section content\]</p>', body_content, content, flags=re.DOTALL)

# Update FAQs
faqs = """<div class="border border-gray-200 rounded-lg overflow-hidden">
                            <button class="w-full text-left px-6 py-4 font-semibold text-brand-charcoal flex justify-between items-center focus:outline-none faq-toggle" aria-expanded="false">
                                <span>Do I need telecom experience to use the Click2Call API?</span>
                                <svg class="w-5 h-5 text-gray-400 faq-icon transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
                            </button>
                            <div class="px-6 pb-4 text-gray-600 hidden">No. The API is designed for modern web developers. It uses standard JSON payloads and RESTful endpoints. If you can write a fetch request in JavaScript, you can integrate our phone system.</div>
                        </div>
                        <div class="border border-gray-200 rounded-lg overflow-hidden">
                            <button class="w-full text-left px-6 py-4 font-semibold text-brand-charcoal flex justify-between items-center focus:outline-none faq-toggle" aria-expanded="false">
                                <span>Is API access included in the standard plan?</span>
                                <svg class="w-5 h-5 text-gray-400 faq-icon transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
                            </button>
                            <div class="px-6 pb-4 text-gray-600 hidden">Yes, full API and webhook access is included free with every Click2Call Cloud PBX account.</div>
                        </div>
                        <div class="border border-gray-200 rounded-lg overflow-hidden">
                            <button class="w-full text-left px-6 py-4 font-semibold text-brand-charcoal flex justify-between items-center focus:outline-none faq-toggle" aria-expanded="false">
                                <span>Can I use Cloudflare Workers for outbound calls?</span>
                                <svg class="w-5 h-5 text-gray-400 faq-icon transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
                            </button>
                            <div class="px-6 pb-4 text-gray-600 hidden">Yes, your Worker can make API requests to Click2Call to initiate outbound calls, manage line preferences, and control call routing programmatically.</div>
                        </div>"""
content = re.sub(r'<div class="border border-gray-200 rounded-lg overflow-hidden">\s*<button.*?</div>\s*</div>\s*</div>', faqs + '\n                    </div>', content, flags=re.DOTALL)

# Update Author Bio
content = content.replace('[AUTHOR BIO - PLACEHOLDER]', 'Royce is a technical writer and developer advocate specializing in cloud communications and AI integrations.')

# Update Related Articles
related = """<li><a href="/blog/building-ai-call-agent-claude-click2call.html" class="text-sm text-brand-green-dark hover:underline">Building an AI Call Agent with Claude</a></li>
                    <li><a href="/blog/australian-voip-api-getting-started.html" class="text-sm text-brand-green-dark hover:underline">Australian VoIP API: Getting Started Guide</a></li>
                    <li><a href="/blog/call-transcriptions-sentiment-data-api-australia.html" class="text-sm text-brand-green-dark hover:underline">How to Get Call Transcriptions via API</a></li>"""
content = re.sub(r'<li><a href="#" class="text-sm text-brand-green-dark hover:underline">\[Related Article 1\].*?\[Related Article 3\]</a></li>', related, content, flags=re.DOTALL)

with open('/home/ubuntu/click2call/blog/cloudflare-worker-phone-system-api.html', 'w') as f:
    f.write(content)

print("Blog 1 rebuilt successfully.")
