#!/usr/bin/env python3
"""Extract DaisyUI documentation pages to Markdown."""

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import re
import sys
from nbdev.config import get_config

def extract_daisyui_page(page_name="config"):
    """Extract documentation from DaisyUI website."""
    url = f"https://daisyui.com/docs/{page_name}/"
    
    # Fetch the page
    response = requests.get(url)
    response.raise_for_status()
    
    # Parse HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the target content div
    content_div = soup.find('div', class_='prose prose-sm lg:prose-h1:text-5xl lg:prose-h2:text-4xl lg:prose-h3:text-3xl md:prose-base w-full max-w-4xl grow pt-10 md:text-sm')
    if not content_div:
        content_div = soup.find('div', class_='prose prose-sm md:prose-base w-full max-w-4xl grow pt-10')


    if not content_div:
        print("Could not find the content div")
        return
    
    # Remove unnecessary elements before conversion
    for element in content_div.find_all(['button', 'svg', 'path']):
        element.decompose()
    
    # Extract content up to the "not-prose" div
    content_parts = []
    for element in content_div.children:
        # Stop if we hit the not-prose div
        if element.name == 'div' and element.get('class') and 'not-prose' in element.get('class', []):
            break
        content_parts.append(str(element))
    
    # Join the content
    html_content = ''.join(content_parts)
    
    # Convert to markdown with better options
    markdown_content = md(html_content, 
                         heading_style="ATX", 
                         code_language="javascript",
                         strip=['a'])
    
    # Clean up the markdown
    # Remove brackets and clean up formatting
    markdown_content = re.sub(r'\[\s*\]', '', markdown_content)  # Remove empty brackets
    markdown_content = re.sub(r'\[\s*!\s*\]', '', markdown_content)  # Remove [!] markers
    markdown_content = re.sub(r'\]\s*\[', '', markdown_content)  # Remove ][ patterns
    markdown_content = re.sub(r'^\s*\]\s*', '', markdown_content, flags=re.MULTILINE)  # Remove lines starting with ]
    markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content)  # Remove excessive newlines
    markdown_content = re.sub(r'^\[\s*', '', markdown_content, flags=re.MULTILINE)  # Remove leading brackets
    markdown_content = re.sub(r'\s*\]$', '', markdown_content, flags=re.MULTILINE)  # Remove trailing brackets
    markdown_content = re.sub(r'\n\s*\n\s*\n', '\n\n', markdown_content)  # Clean up whitespace
    # Final cleanup - preserve code blocks and proper spacing
    lines = markdown_content.split('\n')
    cleaned_lines = []
    in_code_block = False
    skip_next_empty = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Track code blocks
        if line.startswith('```'):
            in_code_block = not in_code_block
            cleaned_lines.append(line)
            continue
            
        # Inside code blocks, preserve formatting
        if in_code_block:
            cleaned_lines.append(line)
            continue
            
        # Skip standalone brackets
        if stripped in [']', '[', '] [']:
            continue
            
        # For regular text
        if stripped:
            # Don't add extra blank lines before headers
            if stripped.startswith('#') and cleaned_lines and cleaned_lines[-1] == '':
                cleaned_lines.pop()
            cleaned_lines.append(stripped)
        elif cleaned_lines and cleaned_lines[-1] != '':
            # Add single blank line between paragraphs
            cleaned_lines.append('')
    
    markdown_content = '\n'.join(cleaned_lines)
    
    cfg = get_config()
    project_dir = cfg.config_path
    save_dir = project_dir/"claude-docs/daisyui/"
    # Save to file
    output_file = save_dir/f"{page_name}.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content.strip())
    
    print(f"Content extracted and saved to {output_file}")

if __name__ == "__main__":
    # Get page name from command line argument or default to 'config'
    page_name = sys.argv[1] if len(sys.argv) > 1 else "config"
    extract_daisyui_page(page_name)