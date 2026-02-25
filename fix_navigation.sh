#!/bin/bash

# Fix navigation links in all HTML files
REPO_NAME="cyberpulse-insights"

for file in *.html; do
    echo "Fixing navigation in $file"
    
    # Fix home link
    sed -i "s|href=\"/\"|href=\"/$REPO_NAME/\"|g" "$file"
    
    # Fix anchor links
    sed -i "s|href=\"/#|href=\"/$REPO_NAME/#|g" "$file"
    
    # Fix post links in index.html
    if [ "$file" = "index.html" ]; then
        sed -i "s|href=\"post-|href=\"/$REPO_NAME/post-|g" "$file"
    fi
    
    echo "Fixed $file"
done

echo "All navigation links fixed for GitHub Pages!"
