import re

with open('/home/ubuntu/click2call/blog/australian-voip-api-getting-started.html', 'r') as f:
    content = f.read()

# Update hero image to webp
content = content.replace('australian-voip-api-hero.jpg', 'australian-voip-api-hero.webp')

# Update category and description
content = content.replace('[CATEGORY]', 'Developer API')
content = content.replace('[ARTICLE SUBHEADING / DESCRIPTION]', 'A comprehensive getting started guide for developers looking to integrate Australian VoIP capabilities into their AI applications.')

# Update takeaways
takeaways = """<li><strong>Local Infrastructure:</strong> Build with a true Australian VoIP provider for low latency and local compliance.</li>
                        <li><strong>RESTful JSON API:</strong> Interact with your phone system using standard JSON payloads and simple HTTP requests.</li>
                        <li><strong>AI-Ready Instructions:</strong> Copy-paste our pre-written LLM instructions into Claude or Cursor to build integrations instantly.</li>
                        <li><strong>Comprehensive Webhooks:</strong> Get real-time event notifications for ringing, answered, and ended calls.</li>"""
content = re.sub(r'<li>\[Takeaway 1\].*?<li>\[Takeaway 4\]</li>', takeaways, content, flags=re.DOTALL)

# Update body content
body_content = """<p>If you're building software in Australia—whether it's a custom CRM, an AI voice agent, or an automated support desk—you eventually hit a wall: you need to connect your code to the real-world phone network. You need an Australian VoIP API.</p>
                
                <p>While global providers exist, they often route traffic overseas (adding latency) or lack deep integration with Australian telecom standards. Click2Call provides a developer-first API built specifically on Australian infrastructure, designed for modern AI builders and "vibe coders."</p>

                <h2 class="text-2xl font-bold text-brand-charcoal mt-10 mb-4">What Can You Build?</h2>
                <p>The Click2Call API exposes the core functionality of our enterprise Cloud PBX to your custom software. Here are a few examples of what developers are building:</p>
                <ul class="list-disc pl-6 mb-6 space-y-2">
                    <li><strong>AI Voice Agents:</strong> Connect an Australian 1300 number directly to ElevenLabs and Claude for conversational AI.</li>
                    <li><strong>CRM Auto-Logging:</strong> Automatically log every inbound and outbound call, complete with AI-generated transcriptions and summaries.</li>
                    <li><strong>Automated Support Desks:</strong> Trigger a webhook when a call ends to automatically create a support ticket with the caller's details and call sentiment.</li>
                    <li><strong>Custom Dashboards:</strong> Pull real-time call data to build live wallboards for your sales or support teams.</li>
                </ul>

                <h2 class="text-2xl font-bold text-brand-charcoal mt-10 mb-4">The "No Experience Needed" Approach</h2>
                <p>We know that many people building AI tools today aren't traditional telecom engineers. That's why we've optimized our API for LLM-assisted coding.</p>
                
                <p>Inside your Click2Call portal, you'll find a complete set of copy-paste instructions written specifically for AI coding tools like Claude, Cursor, and ChatGPT. You don't need to read pages of API documentation. Just paste our instructions into your LLM, describe what you want to build, and let the AI write the integration code for you.</p>

                <div class="bg-gray-50 p-6 rounded-lg border border-gray-200 my-6">
                    <h3 class="font-bold text-brand-charcoal mb-2">Example LLM Prompt:</h3>
                    <p class="text-gray-600 italic">"I'm building a Cloudflare Worker. Here are the Click2Call API instructions: [PASTE INSTRUCTIONS]. Write a script that listens for the 'Ended Event' webhook, fetches the call transcription using the API, and sends it to my Slack channel."</p>
                </div>

                <h2 class="text-2xl font-bold text-brand-charcoal mt-10 mb-4">Core API Capabilities</h2>
                <p>The API is broken down into several key contexts, all accessible via standard JSON POST requests to <code>https://portal.click2call.com.au/api/</code>.</p>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-8">
                    <div class="bg-white border border-gray-200 p-5 rounded-lg shadow-sm">
                        <h4 class="font-bold text-brand-charcoal text-lg mb-2">Voice Functions</h4>
                        <p class="text-sm text-gray-600">Manage phone lines, enable/disable call recording programmatically, and download voicemail or auto-attendant audio files.</p>
                    </div>
                    <div class="bg-white border border-gray-200 p-5 rounded-lg shadow-sm">
                        <h4 class="font-bold text-brand-charcoal text-lg mb-2">AI Functions</h4>
                        <p class="text-sm text-gray-600">Fetch call transcriptions, retrieve AI-generated call summaries, get sentiment analysis data, and convert text to speech (TTS).</p>
                    </div>
                    <div class="bg-white border border-gray-200 p-5 rounded-lg shadow-sm">
                        <h4 class="font-bold text-brand-charcoal text-lg mb-2">Webhooks</h4>
                        <p class="text-sm text-gray-600">Receive real-time HTTP POST payloads for ringing, answered, ended, and missed calls, plus notifications when AI analysis is complete.</p>
                    </div>
                    <div class="bg-white border border-gray-200 p-5 rounded-lg shadow-sm">
                        <h4 class="font-bold text-brand-charcoal text-lg mb-2">Account Functions</h4>
                        <p class="text-sm text-gray-600">Pull detailed calling records, check account balances, retrieve billing summaries, and manage channel limits.</p>
                    </div>
                </div>

                <h2 class="text-2xl font-bold text-brand-charcoal mt-10 mb-4">Authentication</h2>
                <p>All API queries must be authenticated using a Token-based system. You generate your secret token within the Click2Call portal. This token is passed in the header of your JSON requests, ensuring your data remains secure.</p>
                
                <blockquote class="border-l-4 border-brand-green-dark pl-4 italic text-gray-700 my-6">
                    "Click2Call bridges the gap between traditional Australian telecommunications and modern AI software development."
                </blockquote>

                <h2 class="text-2xl font-bold text-brand-charcoal mt-10 mb-4">Getting Started</h2>
                <p>API access is included free with every Click2Call Cloud PBX account. You don't need a special enterprise plan to start building.</p>
                <p>Sign up for a 30-day free trial, grab your API token from the portal, and <a href="/api" class="text-brand-green-dark hover:underline font-semibold">explore the Developer API</a> to bring your software to life.</p>"""

content = re.sub(r'<p>\[ARTICLE BODY CONTENT.*?<p>\[Section content\]</p>', body_content, content, flags=re.DOTALL)

# Update FAQs
faqs = """<div class="border border-gray-200 rounded-lg overflow-hidden">
                            <button class="w-full text-left px-6 py-4 font-semibold text-brand-charcoal flex justify-between items-center focus:outline-none faq-toggle" aria-expanded="false">
                                <span>What format does the API use?</span>
                                <svg class="w-5 h-5 text-gray-400 faq-icon transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
                            </button>
                            <div class="px-6 pb-4 text-gray-600 hidden">The Click2Call API is a RESTful service that accepts and returns standard JSON payloads.</div>
                        </div>
                        <div class="border border-gray-200 rounded-lg overflow-hidden">
                            <button class="w-full text-left px-6 py-4 font-semibold text-brand-charcoal flex justify-between items-center focus:outline-none faq-toggle" aria-expanded="false">
                                <span>Where can I find the API documentation?</span>
                                <svg class="w-5 h-5 text-gray-400 faq-icon transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
                            </button>
                            <div class="px-6 pb-4 text-gray-600 hidden">Full documentation, including endpoint details and the AI-ready copy-paste instructions, is available inside the Click2Call customer portal under the API section.</div>
                        </div>
                        <div class="border border-gray-200 rounded-lg overflow-hidden">
                            <button class="w-full text-left px-6 py-4 font-semibold text-brand-charcoal flex justify-between items-center focus:outline-none faq-toggle" aria-expanded="false">
                                <span>Is there a sandbox environment?</span>
                                <svg class="w-5 h-5 text-gray-400 faq-icon transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
                            </button>
                            <div class="px-6 pb-4 text-gray-600 hidden">You can use your standard Click2Call account to test API calls. We recommend setting up a dedicated test extension or phone number within your account for development purposes.</div>
                        </div>"""
content = re.sub(r'<div class="border border-gray-200 rounded-lg overflow-hidden">\s*<button.*?</div>\s*</div>\s*</div>', faqs + '\n                    </div>', content, flags=re.DOTALL)

# Update Author Bio
content = content.replace('[AUTHOR BIO - PLACEHOLDER]', 'Royce is a technical writer and developer advocate specializing in cloud communications and AI integrations.')

# Update Related Articles
related = """<li><a href="/blog/cloudflare-worker-phone-system-api.html" class="text-sm text-brand-green-dark hover:underline">Integrate a Phone System into a Cloudflare Worker</a></li>
                    <li><a href="/blog/building-ai-call-agent-claude-click2call.html" class="text-sm text-brand-green-dark hover:underline">Building an AI Call Agent with Claude</a></li>
                    <li><a href="/blog/call-transcriptions-sentiment-data-api-australia.html" class="text-sm text-brand-green-dark hover:underline">How to Get Call Transcriptions via API</a></li>"""
content = re.sub(r'<li><a href="#" class="text-sm text-brand-green-dark hover:underline">\[Related Article 1\].*?\[Related Article 3\]</a></li>', related, content, flags=re.DOTALL)

with open('/home/ubuntu/click2call/blog/australian-voip-api-getting-started.html', 'w') as f:
    f.write(content)

print("Blog 3 rebuilt successfully.")
