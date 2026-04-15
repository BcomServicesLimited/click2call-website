import re

with open('/home/ubuntu/click2call/blog/building-ai-call-agent-claude-click2call.html', 'r') as f:
    content = f.read()

# Update hero image to webp
content = content.replace('ai-call-agent-claude-hero.jpg', 'ai-call-agent-claude-hero.webp')

# Update category and description
content = content.replace('[CATEGORY]', 'Developer API')
content = content.replace('[ARTICLE SUBHEADING / DESCRIPTION]', 'Learn how to build a conversational AI call agent using Anthropic\'s Claude and the Click2Call Australian VoIP API with native ElevenLabs integration.')

# Update takeaways
takeaways = """<li><strong>Native Integration:</strong> Click2Call offers native SIP integration with ElevenLabs, bypassing complex audio streaming setups.</li>
                        <li><strong>Low Latency:</strong> Direct SIP connections ensure conversational latency remains under 500ms for natural interactions.</li>
                        <li><strong>Claude Intelligence:</strong> Use Claude to power the agent's logic, decision-making, and conversation flow.</li>
                        <li><strong>Australian Numbers:</strong> Give your AI agent a real Australian 02, 03, 07, 08, or 1300 number instantly.</li>"""
content = re.sub(r'<li>\[Takeaway 1\].*?<li>\[Takeaway 4\]</li>', takeaways, content, flags=re.DOTALL)

# Update body content
body_content = """<p>Building a conversational AI agent that can answer phone calls used to require a team of engineers and months of development. You had to handle SIP protocols, manage real-time audio streaming, integrate speech-to-text (STT), connect an LLM, and pipe it all back through text-to-speech (TTS) with low enough latency to feel natural.</p>
                
                <p>Today, the stack has been radically simplified. By combining Anthropic's Claude for intelligence, ElevenLabs for conversational voice, and Click2Call for the Australian telecom infrastructure, you can deploy a fully functional AI call agent in hours.</p>

                <h2 class="text-2xl font-bold text-brand-charcoal mt-10 mb-4">The Architecture</h2>
                <p>The beauty of this setup is its simplicity. Click2Call handles the complex telecom routing and provides a native SIP connection directly to ElevenLabs. ElevenLabs handles the STT and TTS, and Claude provides the conversational brain.</p>
                
                <div class="bg-gray-50 p-6 rounded-lg border border-gray-200 my-6">
                    <h3 class="font-bold text-brand-charcoal mb-2">How a call flows:</h3>
                    <ol class="list-decimal pl-6 space-y-2 text-gray-700">
                        <li>Customer dials your Click2Call Australian phone number.</li>
                        <li>Click2Call routes the call via SIP directly to your ElevenLabs agent.</li>
                        <li>ElevenLabs transcribes the caller's speech in real-time.</li>
                        <li>The transcription is sent to Claude (via your backend or ElevenLabs' native integration).</li>
                        <li>Claude generates a response based on your custom prompt and knowledge base.</li>
                        <li>ElevenLabs synthesizes Claude's text into lifelike speech.</li>
                        <li>The audio is streamed back through Click2Call to the caller.</li>
                    </ol>
                </div>

                <h2 class="text-2xl font-bold text-brand-charcoal mt-10 mb-4">Step 1: Configure the Click2Call SIP Trunk</h2>
                <p>The biggest hurdle in building voice AI is usually connecting the phone network to the AI platform. Click2Call solves this with native ElevenLabs support.</p>
                
                <p>In your Click2Call portal, navigate to <strong>Line Preferences</strong> and create a new profile:</p>
                <ul class="list-disc pl-6 mb-6 space-y-2">
                    <li>Set the <strong>Connection Type</strong> to "Eleven Labs AI".</li>
                    <li>The system will automatically configure the Inbound SIP URI Route to <code>sip:sip.rtc.elevenlabs.io:5060;transport=tcp</code>.</li>
                    <li>Assign this profile to your chosen Australian phone number.</li>
                </ul>

                <h2 class="text-2xl font-bold text-brand-charcoal mt-10 mb-4">Step 2: Set Up the ElevenLabs Agent</h2>
                <p>Next, head over to ElevenLabs and create a new Conversational AI agent. You'll need to configure the SIP settings to accept calls from Click2Call.</p>
                
                <p>In the ElevenLabs agent settings, navigate to the SIP configuration and generate your SIP credentials. You'll enter these credentials back in the Click2Call portal to authenticate the connection.</p>

                <h2 class="text-2xl font-bold text-brand-charcoal mt-10 mb-4">Step 3: Prompting Claude</h2>
                <p>The personality, knowledge, and capabilities of your agent are defined by the system prompt you provide to Claude. A good prompt for a voice agent is different from a text chatbot prompt—it needs to account for spoken language nuances.</p>

                <div class="bg-gray-900 rounded-lg p-4 my-6 overflow-x-auto">
                    <pre><code class="text-blue-300 text-sm">You are an AI receptionist for Bcom IT Solutions, an IT support company on the Gold Coast.
Your goal is to answer basic questions, take messages, and book support tickets.

CRITICAL VOICE GUIDELINES:
- Keep responses short and conversational (1-2 sentences max).
- Do not use bullet points, markdown, or complex formatting.
- If you don't know the answer, say "I'll need to get one of our techs to look into that for you. Can I grab your name and number?"
- Speak naturally, using occasional filler words like "Sure," "Okay," or "Let me check that."

BUSINESS INFO:
- Hours: 9am to 5pm, Monday to Friday.
- Location: Southport, Gold Coast.
- Services: Managed IT, Cloud PBX, Network Security.</code></pre>
                </div>

                <h2 class="text-2xl font-bold text-brand-charcoal mt-10 mb-4">Step 4: Handling Post-Call Actions</h2>
                <p>A conversation is only useful if you capture the data. Using Click2Call's webhooks, you can trigger actions the moment the call ends.</p>
                
                <p>Set up a webhook in Click2Call to fire on the "Ended Event". Your backend (e.g., a Cloudflare Worker) can receive this webhook, fetch the call recording and transcription via the Click2Call API, and push a summary into your CRM or ticketing system.</p>
                
                <blockquote class="border-l-4 border-brand-green-dark pl-4 italic text-gray-700 my-6">
                    "The combination of Click2Call's native SIP routing and Claude's conversational intelligence allows developers to build AI agents that are indistinguishable from human receptionists."
                </blockquote>

                <h2 class="text-2xl font-bold text-brand-charcoal mt-10 mb-4">Start Building</h2>
                <p>Ready to build your own AI call agent? You can get started with a real Australian phone number and full API access today.</p>
                <p><a href="/api" class="text-brand-green-dark hover:underline font-semibold">Explore the Developer API</a> to learn more about our webhooks and integrations.</p>"""

content = re.sub(r'<p>\[ARTICLE BODY CONTENT.*?<p>\[Section content\]</p>', body_content, content, flags=re.DOTALL)

# Update FAQs
faqs = """<div class="border border-gray-200 rounded-lg overflow-hidden">
                            <button class="w-full text-left px-6 py-4 font-semibold text-brand-charcoal flex justify-between items-center focus:outline-none faq-toggle" aria-expanded="false">
                                <span>What is the latency like for AI voice agents?</span>
                                <svg class="w-5 h-5 text-gray-400 faq-icon transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
                            </button>
                            <div class="px-6 pb-4 text-gray-600 hidden">By using Click2Call's direct SIP integration with ElevenLabs, you bypass intermediate streaming layers. This typically results in conversational latency of 500-800ms, which feels natural to callers.</div>
                        </div>
                        <div class="border border-gray-200 rounded-lg overflow-hidden">
                            <button class="w-full text-left px-6 py-4 font-semibold text-brand-charcoal flex justify-between items-center focus:outline-none faq-toggle" aria-expanded="false">
                                <span>Can I use a different LLM instead of Claude?</span>
                                <svg class="w-5 h-5 text-gray-400 faq-icon transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
                            </button>
                            <div class="px-6 pb-4 text-gray-600 hidden">Yes. While this guide focuses on Claude due to its excellent conversational nuances, the architecture supports any LLM (like OpenAI's GPT-4o) that can integrate with your voice platform.</div>
                        </div>
                        <div class="border border-gray-200 rounded-lg overflow-hidden">
                            <button class="w-full text-left px-6 py-4 font-semibold text-brand-charcoal flex justify-between items-center focus:outline-none faq-toggle" aria-expanded="false">
                                <span>Do I need to host my own SIP server?</span>
                                <svg class="w-5 h-5 text-gray-400 faq-icon transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
                            </button>
                            <div class="px-6 pb-4 text-gray-600 hidden">No. Click2Call acts as your fully hosted SIP provider. We handle the carrier connections and route the SIP traffic directly to your AI agent endpoint.</div>
                        </div>"""
content = re.sub(r'<div class="border border-gray-200 rounded-lg overflow-hidden">\s*<button.*?</div>\s*</div>\s*</div>', faqs + '\n                    </div>', content, flags=re.DOTALL)

# Update Author Bio
content = content.replace('[AUTHOR BIO - PLACEHOLDER]', 'Royce is a technical writer and developer advocate specializing in cloud communications and AI integrations.')

# Update Related Articles
related = """<li><a href="/blog/cloudflare-worker-phone-system-api.html" class="text-sm text-brand-green-dark hover:underline">Integrate a Phone System into a Cloudflare Worker</a></li>
                    <li><a href="/blog/australian-voip-api-getting-started.html" class="text-sm text-brand-green-dark hover:underline">Australian VoIP API: Getting Started Guide</a></li>
                    <li><a href="/blog/call-transcriptions-sentiment-data-api-australia.html" class="text-sm text-brand-green-dark hover:underline">How to Get Call Transcriptions via API</a></li>"""
content = re.sub(r'<li><a href="#" class="text-sm text-brand-green-dark hover:underline">\[Related Article 1\].*?\[Related Article 3\]</a></li>', related, content, flags=re.DOTALL)

with open('/home/ubuntu/click2call/blog/building-ai-call-agent-claude-click2call.html', 'w') as f:
    f.write(content)

print("Blog 2 rebuilt successfully.")
