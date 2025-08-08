#!/usr/bin/env python3
"""
Script to add #| output: false after #| eval: false in code cells.
Uses the execnb.nbio module to read and write Jupyter notebooks.
"""

import argparse
from pathlib import Path
from execnb.nbio import read_nb, write_nb


def process_notebook(notebook_path):
    """Process a single notebook to add #| output: false after #| eval: false."""
    nb = read_nb(notebook_path)
    modified = False
    
    for cell in nb.cells:
        if cell.cell_type == 'code':
            source = cell.source
            lines = source.split('\n')
            
            # Check if first line is #| eval: false
            if lines and lines[0].strip() == '#| eval: false':
                # Check if second line is already #| output: false
                if len(lines) > 1 and lines[1].strip() == '#| output: false':
                    continue  # Already has #| output: false
                
                # Insert #| output: false after #| eval: false
                new_lines = [lines[0], '#| output: false'] + lines[1:]
                new_source = '\n'.join(new_lines)
                
                cell.source = new_source
                modified = True
                print(f"  Modified cell in {notebook_path}")
    
    if modified:
        write_nb(nb, notebook_path)
        print(f"  Saved changes to {notebook_path}")
    
    return modified


def process_directory(directory_path):
    """Recursively process all .ipynb files in the directory."""
    directory = Path(directory_path)
    
    if not directory.exists():
        print(f"Error: Directory {directory} does not exist")
        return
    
    if not directory.is_dir():
        print(f"Error: {directory} is not a directory")
        return
    
    # Get all .ipynb files, excluding those in .ipynb_checkpoints directories
    notebooks = [
        nb for nb in directory.rglob('*.ipynb') 
        if '.ipynb_checkpoints' not in str(nb)
    ]
    
    if not notebooks:
        print(f"No .ipynb files found in {directory}")
        return
    
    print(f"Found {len(notebooks)} notebook(s) to process")
    
    total_modified = 0
    for notebook_path in notebooks:
        print(f"\nProcessing: {notebook_path}")
        if process_notebook(notebook_path):
            total_modified += 1
    
    print(f"\nCompleted: Modified {total_modified} notebook(s)")


def main():
    parser = argparse.ArgumentParser(
        description='Add #| output: false after #| eval: false in code cells'
    )
    parser.add_argument(
        'directory',
        help='Directory path to recursively search for .ipynb files'
    )
    
    args = parser.parse_args()
    process_directory(args.directory)


if __name__ == '__main__':
    main()