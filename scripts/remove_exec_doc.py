#!/usr/bin/env python3
"""
Script to remove lines containing #|exec_doc from code cells.
Uses the execnb.nbio module to read and write Jupyter notebooks.
"""

import argparse
from pathlib import Path
from execnb.nbio import read_nb, write_nb


def process_notebook(notebook_path):
    """Process a single notebook to remove #|exec_doc lines."""
    nb = read_nb(notebook_path)
    modified = False
    
    for cell in nb.cells:
        if cell.cell_type == 'code':
            source = cell.source
            lines = source.split('\n')
            
            # Filter out lines containing #|exec_doc
            new_lines = [line for line in lines if '#|exec_doc' not in line]
            
            if len(new_lines) != len(lines):
                new_source = '\n'.join(new_lines)
                cell.source = new_source
                modified = True
                print(f"  Removed #|exec_doc line(s) from cell in {notebook_path}")
    
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
        description='Remove lines containing #|exec_doc from code cells'
    )
    parser.add_argument(
        'directory',
        help='Directory path to recursively search for .ipynb files'
    )
    
    args = parser.parse_args()
    process_directory(args.directory)


if __name__ == '__main__':
    main()