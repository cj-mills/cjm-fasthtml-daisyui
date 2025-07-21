#!/usr/bin/env python3
"""
Script to extract component titles, descriptions, and table data from DaisyUI components pages
"""

import requests
from bs4 import BeautifulSoup
import re
import time
from urllib.parse import urljoin
from tqdm import tqdm
import argparse
import os
from pathlib import Path
from nbdev.config import get_config


def html_table_to_markdown(table):
    """Convert HTML table to Markdown format"""
    rows = []
    
    # Extract headers
    headers = []
    header_row = table.find('thead')
    if header_row:
        for th in header_row.find_all('th'):
            headers.append(th.get_text(strip=True))
    else:
        # Try to find headers in first row
        first_row = table.find('tr')
        if first_row:
            for th in first_row.find_all(['th', 'td']):
                headers.append(th.get_text(strip=True))
    
    if not headers:
        return None
    
    # Create header row
    rows.append('| ' + ' | '.join(headers) + ' |')
    rows.append('|' + '|'.join([' --- ' for _ in headers]) + '|')
    
    # Extract data rows
    tbody = table.find('tbody')
    data_rows = tbody.find_all('tr') if tbody else table.find_all('tr')[1:]  # Skip header if no tbody
    
    for row in data_rows:
        cells = []
        for td in row.find_all(['td', 'th']):
            # Get text and clean it up
            text = td.get_text(strip=True)
            # Escape pipe characters in cell content
            text = text.replace('|', '\\|')
            cells.append(text)
        
        if cells:
            rows.append('| ' + ' | '.join(cells) + ' |')
    
    return '\n'.join(rows) if len(rows) > 2 else None  # Must have at least headers + separator + 1 data row


def extract_html_examples(soup):
    """Extract HTML code examples with their titles from the page"""
    examples = []
    
    # Find all h4 tags with component-preview-title class
    preview_titles = soup.find_all('h4', class_='component-preview-title')
    
    # Debug: print how many titles were found
    if not preview_titles:
        # Try alternative: find all tabs containers and work backwards
        tabs_containers = soup.find_all('div', class_='tabs tabs-lift')
        for container in tabs_containers:
            # Look for previous h4 tag
            prev_h4 = None
            for prev in container.find_all_previous('h4'):
                if 'component-preview-title' in prev.get('class', []):
                    prev_h4 = prev
                    break
            
            title_text = prev_h4.get_text(strip=True) if prev_h4 else "Untitled Example"
            
            # Find the HTML tab input
            html_input = container.find('input', {'aria-label': 'HTML'})
            
            if html_input:
                # Find the associated tab content
                content_div = None
                for sibling in html_input.find_next_siblings():
                    if 'tab-content' in sibling.get('class', []):
                        content_div = sibling
                        break
                
                if content_div:
                    # Find code blocks within the content
                    code_blocks = content_div.find_all('code')
                    
                    for code_block in code_blocks:
                        # Get the text content and clean it up
                        code_text = code_block.get_text()
                        
                        # Skip if it's JSX (contains className instead of class)
                        if 'className=' in code_text:
                            continue
                        
                        # Clean up the code
                        lines = code_text.strip().split('\n')
                        cleaned_lines = []
                        
                        for line in lines:
                            # Remove extra whitespace but preserve indentation
                            if line.strip():
                                # Remove any dollar signs that might be in the class names
                                cleaned_line = line.replace('$$', '').replace('$', '')
                                cleaned_lines.append(cleaned_line)
                        
                        if cleaned_lines:
                            cleaned_code = '\n'.join(cleaned_lines)
                            examples.append({
                                'title': title_text,
                                'code': cleaned_code
                            })
                            break  # Only take the first valid HTML example per container
        
        return examples
    
    for title_tag in preview_titles:
        title_text = title_tag.get_text(strip=True)
        
        # Find the next tabs container after this title
        # Use find_next instead of find_next_sibling to search in all descendants
        tabs_container = title_tag.find_next('div', class_='tabs tabs-lift')
        
        if tabs_container:
            # Find the HTML tab input
            html_input = tabs_container.find('input', {'aria-label': 'HTML'})
            
            if html_input:
                # Find the associated tab content
                content_div = None
                for sibling in html_input.find_next_siblings():
                    if 'tab-content' in sibling.get('class', []):
                        content_div = sibling
                        break
                
                if content_div:
                    # Find code blocks within the content
                    code_blocks = content_div.find_all('code')
                    
                    for code_block in code_blocks:
                        # Get the text content and clean it up
                        code_text = code_block.get_text()
                        
                        # Skip if it's JSX (contains className instead of class)
                        if 'className=' in code_text:
                            continue
                        
                        # Clean up the code
                        lines = code_text.strip().split('\n')
                        cleaned_lines = []
                        
                        for line in lines:
                            # Remove extra whitespace but preserve indentation
                            if line.strip():
                                # Remove any dollar signs that might be in the class names
                                cleaned_line = line.replace('$$', '').replace('$', '')
                                cleaned_lines.append(cleaned_line)
                        
                        if cleaned_lines:
                            cleaned_code = '\n'.join(cleaned_lines)
                            examples.append({
                                'title': title_text,
                                'code': cleaned_code
                            })
                            break  # Only take the first valid HTML example per container
    
    return examples


def extract_component_data(component_url):
    """Extract table and HTML examples from a component page"""
    try:
        response = requests.get(component_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract table
        table_markdown = None
        table_div = soup.find('div', class_=lambda x: x and 'not-prose' in x and 'relative' in x and 'mt-6' in x)
        
        if table_div:
            table = table_div.find('table')
            if table:
                table_markdown = html_table_to_markdown(table)
        
        if not table_markdown:
            # Alternative: look for any table with the specified classes
            table = soup.find('table', class_=lambda x: x and ('table-xs' in str(x) or 'table-sm' in str(x)))
            if table:
                table_markdown = html_table_to_markdown(table)
        
        # Extract HTML examples
        html_examples = extract_html_examples(soup)
        
        return table_markdown, html_examples
            
    except Exception as e:
        print(f"Error extracting data from {component_url}: {e}")
    
    return None, []


def extract_daisyui_components(url="https://daisyui.com/components/"):
    """Extract component titles, descriptions, and links from DaisyUI components page"""
    
    # Fetch the page
    response = requests.get(url)
    response.raise_for_status()
    
    # Parse HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all component cards - they're typically in <a> tags with specific structure
    components = []
    
    # Look for component links that contain title and description
    component_links = soup.find_all('a', class_=lambda x: x and 'card' in x)
    
    # Alternative approach: find by structure
    for link in soup.find_all('a', href=re.compile(r'/components/[^/]+/?$')):
        # Get the href
        href = link.get('href')
        component_url = urljoin(url, href)
        
        # Try to find title and description within the link
        title_elem = link.find(['h2', 'h3', 'div'], class_=lambda x: x and any(c in str(x) for c in ['title', 'heading', 'text-xl', 'font-bold']))
        desc_elem = link.find(['p', 'div'], class_=lambda x: x and any(c in str(x) for c in ['description', 'text-sm', 'opacity']))
        
        if title_elem and desc_elem:
            title = title_elem.get_text(strip=True)
            description = desc_elem.get_text(strip=True)
            if title and description:
                components.append({
                    'title': title,
                    'description': description,
                    'url': component_url
                })
    
    # If the above doesn't work, try a more general approach
    if not components:
        # Look for grid or list container
        container = soup.find(['div', 'main'], class_=lambda x: x and 'grid' in str(x))
        if container:
            for item in container.find_all(['a'], recursive=True):
                href = item.get('href')
                if href and re.match(r'/components/[^/]+/?$', href):
                    component_url = urljoin(url, href)
                    title = None
                    description = None
                    
                    # Find title (usually in larger text)
                    for elem in item.find_all(['h1', 'h2', 'h3', 'div']):
                        text = elem.get_text(strip=True)
                        if text and len(text) < 50 and not title:  # Likely a title
                            title = text
                    
                    # Find description (usually in smaller text after title)
                    for elem in item.find_all(['p', 'div']):
                        text = elem.get_text(strip=True)
                        if text and len(text) > 20 and title and text != title:  # Likely a description
                            description = text
                            break
                    
                    if title and description:
                        components.append({
                            'title': title,
                            'description': description,
                            'url': component_url
                        })
    
    return components


def create_slug(title):
    """Create a URL-friendly slug from a component title"""
    # Convert to lowercase and replace spaces with hyphens
    slug = title.lower().replace(' ', '-')
    # Remove any characters that aren't alphanumeric or hyphens
    slug = re.sub(r'[^a-z0-9-]', '', slug)
    # Remove multiple consecutive hyphens
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')


def save_html_examples_separate(components, output_dir):
    """Save HTML examples for each component to separate files"""
    examples_dir = Path(output_dir) / 'html-examples'
    examples_dir.mkdir(parents=True, exist_ok=True)
    
    for comp in components:
        if 'html_examples' in comp and comp['html_examples']:
            slug = create_slug(comp['title'])
            file_path = examples_dir / f"{slug}.md"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f"# {comp['title']} - HTML Examples\n\n")
                f.write(f"{comp['description']}\n\n")
                
                for example in comp['html_examples']:
                    if isinstance(example, dict):
                        f.write(f"## {example['title']}\n\n")
                        f.write("```html\n")
                        f.write(example['code'])
                        f.write("\n```\n\n")
                    else:
                        f.write("```html\n")
                        f.write(example)
                        f.write("\n```\n\n")
    
    print(f"HTML examples saved to {examples_dir}")


def save_components_separate(components, output_dir):
    """Save each component to a separate file"""
    components_dir = Path(output_dir) / 'components'
    components_dir.mkdir(parents=True, exist_ok=True)
    
    for comp in components:
        slug = create_slug(comp['title'])
        file_path = components_dir / f"{slug}.md"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"# {comp['title']}\n\n")
            f.write(f"{comp['description']}\n\n")
            
            if 'table' in comp and comp['table']:
                f.write("## Component Details\n\n")
                f.write(comp['table'])
                f.write("\n\n")
            
            if 'html_examples' in comp and comp['html_examples']:
                f.write("## HTML Examples\n\n")
                for example in comp['html_examples']:
                    if isinstance(example, dict):
                        f.write(f"### {example['title']}\n\n")
                        f.write("```html\n")
                        f.write(example['code'])
                        f.write("\n```\n\n")
                    else:
                        f.write("```html\n")
                        f.write(example)
                        f.write("\n```\n\n")
    
    print(f"Components saved to {components_dir}")


def save_to_markdown(components, output_file="daisyui_components_with_tables.md", include_examples=True):
    """Save extracted components with their tables and optionally HTML examples to a Markdown file"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        title = "DaisyUI Components with Tables"
        if include_examples:
            title += " and Examples"
        f.write(f"# {title}\n\n")
        f.write(f"Extracted {len(components)} components from https://daisyui.com/components/\n\n")
        
        for i, comp in enumerate(components, 1):
            f.write(f"## {i}. {comp['title']}\n\n")
            f.write(f"{comp['description']}\n\n")
            
            if 'table' in comp and comp['table']:
                f.write("### Component Details\n\n")
                f.write(comp['table'])
                f.write("\n\n")
            
            if include_examples and 'html_examples' in comp and comp['html_examples']:
                f.write("### HTML Examples\n\n")
                for example in comp['html_examples']:
                    if isinstance(example, dict):
                        # New format with title
                        f.write(f"#### {example['title']}\n\n")
                        f.write("```html\n")
                        f.write(example['code'])
                        f.write("\n```\n\n")
                    else:
                        # Fallback for old format (just code)
                        f.write("```html\n")
                        f.write(example)
                        f.write("\n```\n\n")
            
            f.write("---\n\n")
    
    print(f"Successfully saved {len(components)} components to {output_file}")


def main():
    """Main function to extract and save DaisyUI components with tables and HTML examples"""
    
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description='Extract DaisyUI component documentation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Save everything to a single file (default)
  python extract_daisyui_components.py
  
  # Save to a specific folder
  python extract_daisyui_components.py --output-dir ./claude-docs/daisyui
  
  # Save HTML examples to separate files
  python extract_daisyui_components.py --output-dir ./claude-docs/daisyui --separate-examples
  
  # Save components to separate files
  python extract_daisyui_components.py --output-dir ./claude-docs/daisyui --separate-components
  
  # Save both components and examples to separate files
  python extract_daisyui_components.py --output-dir ./claude-docs/daisyui --separate-components --separate-examples
  
  # Save main file without HTML examples (just tables)
  python extract_daisyui_components.py --output-dir ./claude-docs/daisyui --no-examples
        '''
    )
    
    parser.add_argument(
        '--output-dir', '-o',
        type=str,
        default='.',
        help='Output directory for saving files (default: current directory)'
    )
    
    parser.add_argument(
        '--separate-examples', '-e',
        action='store_true',
        help='Save HTML examples to separate files in html-examples/ subdirectory'
    )
    
    parser.add_argument(
        '--separate-components', '-c',
        action='store_true',
        help='Save each component to a separate file in components/ subdirectory'
    )
    
    parser.add_argument(
        '--no-combined', '-n',
        action='store_true',
        help='Do not create the combined markdown file (only works with --separate-examples or --separate-components)'
    )
    
    parser.add_argument(
        '--no-examples', '-x',
        action='store_true',
        help='Exclude HTML examples from the main combined markdown file'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.no_combined and not (args.separate_examples or args.separate_components):
        parser.error('--no-combined requires either --separate-examples or --separate-components')
    
    print("Extracting DaisyUI components...")
    
    try:
        # First extract components with their URLs
        components = extract_daisyui_components()
        
        if components:
            print(f"Found {len(components)} components. Now extracting data from each component page...")
            
            # Extract tables and HTML examples from each component page with progress bar
            for comp in tqdm(components, desc="Extracting data", unit=" component"):
                # Add small delay to be respectful to the server
                time.sleep(0.5)
                
                table_markdown, html_examples = extract_component_data(comp['url'])
                comp['table'] = table_markdown
                comp['html_examples'] = html_examples
                
                # Update progress bar description
                status_parts = []
                if table_markdown:
                    status_parts.append("✓ Table")
                if html_examples:
                    status_parts.append(f"✓ {len(html_examples)} example(s)")
                
                if status_parts:
                    tqdm.write(f"  {comp['title']}: {', '.join(status_parts)}")
                else:
                    tqdm.write(f"  {comp['title']}: No data found")
            
            # Create output directory if it doesn't exist
            cfg = get_config()
            project_dir = cfg.config_path
            output_dir = project_dir/args.output_dir
            output_dir.mkdir(parents=True, exist_ok=True)
            
            # Save based on user preferences
            if args.separate_components:
                save_components_separate(components, output_dir)
            
            if args.separate_examples:
                save_html_examples_separate(components, output_dir)
            
            if not args.no_combined:
                output_file = output_dir / "daisyui_components_with_tables.md"
                save_to_markdown(components, output_file, include_examples=not args.no_examples)
            
            # Print summary
            tables_found = sum(1 for comp in components if comp.get('table'))
            examples_found = sum(1 for comp in components if comp.get('html_examples'))
            total_examples = sum(len(comp.get('html_examples', [])) for comp in components)
            
            print(f"\nSummary:")
            print(f"- Total components: {len(components)}")
            print(f"- Components with tables: {tables_found}")
            print(f"- Components with HTML examples: {examples_found}")
            print(f"- Total HTML examples: {total_examples}")
            
        else:
            print("No components found. The page structure might have changed.")
            print("Please check the website manually.")
            
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()