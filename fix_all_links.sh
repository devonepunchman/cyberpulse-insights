#!/bin/bash

REPO_NAME="cyberpulse-insights"

# Fix all HTML files
for file in *.html; do
    echo "Processing $file"
    
    # Fix home links
    sed -i "s|href=\"/\"|href=\"/$REPO_NAME/\"|g" "$file"
    
    # Fix anchor links  
    sed -i "s|href=\"/#|href=\"/$REPO_NAME/#|g" "$file"
    
    # Fix back buttons (they point to /)
    sed -i "s|href=\"/\" class=\"back-button\"|href=\"/$REPO_NAME/\" class=\"back-button\"|g" "$file"
    
    # Fix post links in index.html
    if [ "$file" = "index.html" ]; then
        sed -i "s|href=\"post-|href=\"/$REPO_NAME/post-|g" "$file"
    fi
    
    # Fix links between post pages
    sed -i "s|href=\"post-|href=\"/$REPO_NAME/post-|g" "$file"
    
    echo "Fixed $file"
done

echo "All links fixed for GitHub Pages deployment!"
