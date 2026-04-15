import re

with open('/home/ubuntu/click2call/blog/call-transcriptions-sentiment-data-api-australia.html', 'r') as f:
    content = f.read()

# Update hero image to webp
content = content.replace('transcription-sentiment-api-hero.jpg', 'transcription-sentiment-api-hero.webp')

# Update category and description
content = content.replace('[CATEGORY]', 'Developer API')
content = content.replace('[ARTICLE SUBHEADING / DESCRIPTION]', 'Learn how to automatically extract call transcriptions, summaries, and sentiment analysis data from Australian phone calls using the Click2Call API.')

# Update takeaways
takeaways = """<li><strong>Automated Extraction:</strong> Pull full call transcriptions and AI-generated summaries via a single API endpoint.</li>
                        <li><strong>Sentiment Analysis:</strong> Instantly know if a call was positive, negative, or neutral without listening to the recording.</li>
                        <li><strong>Webhook Triggers:</strong> Receive real-time notifications the moment AI analysis is complete for a call.</li>
                        <li><strong>CRM Integration:</strong> Push rich call data directly into Salesforce, HubSpot, or your custom database.</li>"""
content = re.sub(r'<li>\[Takeaway 1\].*?<li>\[Takeaway 4\]</li>', takeaways, content, flags=re.DOTALL)

# Update body content
body_content = """<p>Voice calls are a black box for most businesses. Unless a staff member manually types up notes, the contents of a conversation are lost the moment the call ends. For developers building CRMs, support desks, or sales tools, unlocking this voice data is the holy grail.</p>
                
                <p>The Click2Call API changes this by automatically processing every recorded call through our AI engine. Within moments of a call ending, you can extract the full transcription, a concise summary, and sentiment analysis data—all via a simple JSON API.</p>

                <h2 class="text-2xl font-bold text-brand-charcoal mt-10 mb-4">The AI Analysis Workflow</h2>
                <p>Extracting call data is a two-step process: wait for the analysis to finish, then fetch the data.</p>
                
                <div class="bg-gray-50 p-6 rounded-lg border border-gray-200 my-6">
                    <h3 class="font-bold text-brand-charcoal mb-2">How it works:</h3>
                    <ol class="list-decimal pl-6 space-y-2 text-gray-700">
                        <li>A call ends on your Click2Call account (with recording enabled).</li>
                        <li>The Click2Call AI engine automatically transcribes and analyzes the audio.</li>
                        <li>Click2Call fires an "AI Analysis" webhook to your server.</li>
                        <li>Your server makes a GET request to the API to fetch the transcription and sentiment data.</li>
                        <li>Your server pushes the data into your CRM or database.</li>
                    </ol>
                </div>

                <h2 class="text-2xl font-bold text-brand-charcoal mt-10 mb-4">Step 1: The Webhook Payload</h2>
                <p>When you configure a webhook in the Click2Call portal, ensure you check the "Recording and AI transcription generation" box under the AI Analysis section.</p>
                
                <p>When the analysis is complete, your endpoint will receive a payload containing the <code>call_id</code>. This is the unique identifier you'll use to fetch the data.</p>

                <h2 class="text-2xl font-bold text-brand-charcoal mt-10 mb-4">Step 2: Fetching the Data</h2>
                <p>With the <code>call_id</code> in hand, you can query the <strong>AI Functions</strong> context of the API. The most useful endpoint for this is <code>Get-Audio-Transcription-Summary</code>.</p>

                <div class="bg-gray-900 rounded-lg p-4 my-6 overflow-x-auto">
                    <pre><code class="text-green-400 text-sm">// Example API Request Payload
{
  "context": "ai",
  "action": "Get-Audio-Transcription-Summary",
  "call_id": "1713261600.12345"
}</code></pre>
                </div>

                <p>The API will return a rich JSON object containing everything you need to know about the call.</p>

                <div class="bg-gray-900 rounded-lg p-4 my-6 overflow-x-auto">
                    <pre><code class="text-blue-300 text-sm">// Example API Response
{
  "status": "success",
  "data": {
    "transcription": "Speaker 1: Hi, I'm calling about my recent invoice... Speaker 2: Certainly, let me pull that up for you...",
    "summary": "Customer called to query a charge on their April invoice. Agent explained the pro-rata billing. Customer was satisfied and paid over the phone.",
    "sentiment": "positive",
    "sentiment_score": 0.85,
    "duration_seconds": 142
  }
}</code></pre>
                </div>

                <h2 class="text-2xl font-bold text-brand-charcoal mt-10 mb-4">Use Cases for Sentiment Data</h2>
                <p>Having access to sentiment data programmatically opens up powerful automation possibilities:</p>
                <ul class="list-disc pl-6 mb-6 space-y-2">
                    <li><strong>Automated Escalation:</strong> If a call ends with a "negative" sentiment score, automatically trigger a Slack alert to the Customer Success Manager to follow up immediately.</li>
                    <li><strong>Sales Coaching:</strong> Build a dashboard that highlights calls with "positive" sentiment to use as training examples for new sales reps.</li>
                    <li><strong>Churn Prediction:</strong> Feed the sentiment scores into your CRM to identify accounts that have had multiple negative interactions in a single month.</li>
                </ul>
                
                <blockquote class="border-l-4 border-brand-green-dark pl-4 italic text-gray-700 my-6">
                    "By turning unstructured voice conversations into structured JSON data, developers can finally treat phone calls like any other data source in their application stack."
                </blockquote>

                <h2 class="text-2xl font-bold text-brand-charcoal mt-10 mb-4">Start Extracting Data</h2>
                <p>AI transcriptions and summaries are available on all Click2Call Cloud PBX accounts. You can start pulling this data into your applications today.</p>
                <p><a href="/api" class="text-brand-green-dark hover:underline font-semibold">Explore the Developer API</a> to see the full list of AI endpoints and capabilities.</p>"""

content = re.sub(r'<p>\[ARTICLE BODY CONTENT.*?<p>\[Section content\]</p>', body_content, content, flags=re.DOTALL)

# Update FAQs
faqs = """<div class="border border-gray-200 rounded-lg overflow-hidden">
                            <button class="w-full text-left px-6 py-4 font-semibold text-brand-charcoal flex justify-between items-center focus:outline-none faq-toggle" aria-expanded="false">
                                <span>How long does the AI analysis take?</span>
                                <svg class="w-5 h-5 text-gray-400 faq-icon transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
                            </button>
                            <div class="px-6 pb-4 text-gray-600 hidden">Analysis typically completes within 1-3 minutes after the call ends, depending on the length of the recording. The webhook ensures you don't have to poll the API while waiting.</div>
                        </div>
                        <div class="border border-gray-200 rounded-lg overflow-hidden">
                            <button class="w-full text-left px-6 py-4 font-semibold text-brand-charcoal flex justify-between items-center focus:outline-none faq-toggle" aria-expanded="false">
                                <span>Does the transcription identify different speakers?</span>
                                <svg class="w-5 h-5 text-gray-400 faq-icon transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
                            </button>
                            <div class="px-6 pb-4 text-gray-600 hidden">Yes, the AI engine performs speaker diarization, separating the audio into "Speaker 1" (usually the caller) and "Speaker 2" (the agent).</div>
                        </div>
                        <div class="border border-gray-200 rounded-lg overflow-hidden">
                            <button class="w-full text-left px-6 py-4 font-semibold text-brand-charcoal flex justify-between items-center focus:outline-none faq-toggle" aria-expanded="false">
                                <span>Can I disable sentiment analysis?</span>
                                <svg class="w-5 h-5 text-gray-400 faq-icon transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
                            </button>
                            <div class="px-6 pb-4 text-gray-600 hidden">Yes, you can disable transcriptions, summaries, or sentiment analysis on a per-line basis within the Click2Call portal under Line Preferences.</div>
                        </div>"""
content = re.sub(r'<div class="border border-gray-200 rounded-lg overflow-hidden">\s*<button.*?</div>\s*</div>\s*</div>', faqs + '\n                    </div>', content, flags=re.DOTALL)

# Update Author Bio
content = content.replace('[AUTHOR BIO - PLACEHOLDER]', 'Royce is a technical writer and developer advocate specializing in cloud communications and AI integrations.')

# Update Related Articles
related = """<li><a href="/blog/cloudflare-worker-phone-system-api.html" class="text-sm text-brand-green-dark hover:underline">Integrate a Phone System into a Cloudflare Worker</a></li>
                    <li><a href="/blog/building-ai-call-agent-claude-click2call.html" class="text-sm text-brand-green-dark hover:underline">Building an AI Call Agent with Claude</a></li>
                    <li><a href="/blog/australian-voip-api-getting-started.html" class="text-sm text-brand-green-dark hover:underline">Australian VoIP API: Getting Started Guide</a></li>"""
content = re.sub(r'<li><a href="#" class="text-sm text-brand-green-dark hover:underline">\[Related Article 1\].*?\[Related Article 3\]</a></li>', related, content, flags=re.DOTALL)

with open('/home/ubuntu/click2call/blog/call-transcriptions-sentiment-data-api-australia.html', 'w') as f:
    f.write(content)

print("Blog 4 rebuilt successfully.")
