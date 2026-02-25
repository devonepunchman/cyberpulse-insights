#!/usr/bin/env python3
import re

# Read the index.html file
with open('index.html', 'r') as f:
    content = f.read()

# Fix post card inconsistencies
# Remove any leftover read-time spans and closing divs in post-footer
content = re.sub(r'</div>\s*<span class="read-time">[^<]*<i[^>]*></i>[^<]*</span>\s*(?:</a>)?\s*</div>\s*</div>\s*</article>', 
                 r'</div>\n                    </div>\n                </article>', 
                 content)

# Fix any remaining malformed post-footer divs
content = re.sub(r'<div class="post-footer">\s*<div class="post-tags">(.*?)</div>\s*(?:<[^>]*>)*\s*</div>', 
                 r'<div class="post-footer">\n                        <div class="post-tags">\1</div>\n                    </div>', 
                 content, flags=re.DOTALL)

# Write back to file
with open('index.html', 'w') as f:
    f.write(content)

print("Fixed frontpage inconsistencies!")
