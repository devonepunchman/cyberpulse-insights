#!/usr/bin/env python3
import re

# Read the index.html file
with open('index.html', 'r') as f:
    content = f.read()

# Clean up leftover HTML from post cards
# Remove any leftover read-time spans and read-more links in post-footer
content = re.sub(r'<div class="post-footer">\s*<div class="post-tags">.*?</div>\s*<span class="read-time">.*?</span>\s*<a[^>]*>Read Story.*?</a>\s*</div>\s*</div>', 
                 r'<div class="post-footer">\n                        <div class="post-tags">\1</div>\n                    </div>', 
                 content, flags=re.DOTALL)

# Clean up any remaining post-meta-right divs
content = re.sub(r'<div class="post-meta-right">.*?</div>', '', content, flags=re.DOTALL)

# Clean up any remaining read-time spans not in post-meta-info
content = re.sub(r'<span class="read-time">\s*<i class="far fa-clock"></i>\s*[^<]+\s*</span>(?![^<]*</div>)', '', content)

# Write back to file
with open('index.html', 'w') as f:
    f.write(content)

print("Cleaned up post cards successfully!")
