import os
import re

related_html = """
<!-- Related Posts Section -->
<div class="mt-16 pt-10 border-t border-gray-200">
  <h3 class="text-2xl font-bold text-gray-900 mb-6">Related Articles</h3>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
    <a href="/blog/cloud-pbx-vs-traditional.html" class="block group">
      <div class="bg-gray-50 rounded-xl p-6 border border-gray-100 group-hover:border-[#3B9C49] group-hover:shadow-md transition-all duration-200 h-full">
        <h4 class="text-lg font-bold text-gray-900 mb-2 group-hover:text-[#3B9C49] transition-colors">Cloud PBX vs Traditional Phone Systems</h4>
        <p class="text-sm text-gray-600">A comprehensive comparison of features, costs, and flexibility for Australian businesses.</p>
      </div>
    </a>
    <a href="/blog/business-phone-system-cost.html" class="block group">
      <div class="bg-gray-50 rounded-xl p-6 border border-gray-100 group-hover:border-[#3B9C49] group-hover:shadow-md transition-all duration-200 h-full">
        <h4 class="text-lg font-bold text-gray-900 mb-2 group-hover:text-[#3B9C49] transition-colors">How Much Does a Business Phone System Cost?</h4>
        <p class="text-sm text-gray-600">A breakdown of the real costs involved in setting up and running a modern VoIP system.</p>
      </div>
    </a>
  </div>
</div>
"""

for filename in os.listdir('.'):
    if filename.endswith('.html') and filename != 'index.html' and filename != 'article-template.html':
        with open(filename, 'r') as f:
            content = f.read()
            
        if 'Related Articles' not in content and 'Related Posts' not in content:
            # Find the end of the article content (usually before the CTA or footer)
            # We'll insert it right before the closing </article> tag
            if '</article>' in content:
                content = content.replace('</article>', related_html + '\n</article>')
                with open(filename, 'w') as f:
                    f.write(content)
                print(f"Added Related Posts to {filename}")
            else:
                print(f"Could not find </article> in {filename}")
