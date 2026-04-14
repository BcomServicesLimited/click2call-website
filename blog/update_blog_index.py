import re

with open('/home/ubuntu/click2call/blog/index.html', 'r') as f:
    content = f.read()

new_card = """
            <!-- Article Card -->
            <article class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden hover:shadow-md transition-shadow flex flex-col">
                <a href="/blog/ai-receptionist-australia.html" class="block aspect-w-16 aspect-h-9 bg-gray-100">
                    <img src="/assets/images/ai-receptionist-blog.jpg" alt="AI Receptionist Australia" class="object-cover w-full h-full" loading="lazy">
                </a>
                <div class="p-6 flex flex-col flex-grow">
                    <div class="flex items-center gap-3 text-sm text-gray-500 mb-3">
                        <span class="bg-purple-100 text-purple-700 px-2.5 py-0.5 rounded-full font-medium text-xs">AI Voice Tools</span>
                        <span>23 Feb 2026</span>
                    </div>
                    <h2 class="text-xl font-bold text-brand-charcoal mb-2 line-clamp-2">
                        <a href="/blog/ai-receptionist-australia.html" class="hover:text-brand-green-dark transition-colors">AI Receptionist Australia: How Virtual Assistants Are Changing Business</a>
                    </h2>
                    <p class="text-gray-600 text-sm mb-4 line-clamp-3 flex-grow">Discover how an AI receptionist can help your Australian business handle calls 24/7, reduce costs, and improve customer service.</p>
                    <div class="flex items-center justify-between mt-auto pt-4 border-t border-gray-100">
                        <div class="flex items-center gap-2">
                            <img src="/assets/images/royce-clark.webp" alt="Royce Clark" class="w-6 h-6 rounded-full" loading="lazy">
                            <span class="text-sm font-medium text-gray-700">Royce Clark</span>
                        </div>
                        <span class="text-sm text-gray-500">6 min read</span>
                    </div>
                </div>
            </article>
"""

# Insert the new card after the first <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
content = re.sub(r'(<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">)', r'\1\n' + new_card, content, count=1)

with open('/home/ubuntu/click2call/blog/index.html', 'w') as f:
    f.write(content)

