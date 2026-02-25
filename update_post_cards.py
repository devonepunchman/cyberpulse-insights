#!/usr/bin/env python3
import re

# Read the index.html file
with open('index.html', 'r') as f:
    content = f.read()

# Pattern to match each post card
post_pattern = r'(<article class="post-card">.*?</article>)'

def update_post_card(match):
    post_html = match.group(1)
    
    # Extract the post URL from the title link
    url_match = re.search(r'href="([^"]+)"', post_html)
    post_url = url_match.group(1) if url_match else "#"
    
    # Extract author and read time
    author_match = re.search(r'<p class="post-author"><i class="fas fa-user"></i>([^<]+)</p>', post_html)
    author = author_match.group(1).strip() if author_match else ""
    
    read_time_match = re.search(r'<span class="read-time">\s*<i class="far fa-clock"></i>\s*([^<]+)\s*</span>', post_html)
    read_time = read_time_match.group(1).strip() if read_time_match else ""
    
    # Remove the old author line and read-more button section
    # Keep only the post-meta, title, and excerpt
    lines = post_html.split('\n')
    new_lines = []
    
    for line in lines:
        # Skip the old author line and read-more button section
        if 'post-author' in line or 'read-more' in line or 'post-meta-right' in line:
            continue
        new_lines.append(line)
    
    # Reconstruct the post card
    updated_post = '\n'.join(new_lines)
    
    # Insert the new meta-info after the excerpt
    excerpt_end = updated_post.find('</p>', updated_post.find('post-excerpt')) + 4
    meta_info = f'''
                        <div class="post-meta-info">
                            <span class="post-author"><i class="fas fa-user"></i> {author}</span>
                            <span class="read-time"><i class="far fa-clock"></i> {read_time}</span>
                        </div>'''
    
    updated_post = updated_post[:excerpt_end] + meta_info + updated_post[excerpt_end:]
    
    return updated_post

# Update all post cards
updated_content = re.sub(post_pattern, update_post_card, content, flags=re.DOTALL)

# Write back to file
with open('index.html', 'w') as f:
    f.write(updated_content)

print("Updated post cards successfully!")
