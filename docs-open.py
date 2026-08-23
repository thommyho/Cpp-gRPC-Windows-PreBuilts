#!/usr/bin/env python3
"""
Standalone script to open the static documentation website.
This can be bundled with PyInstaller to create a standalone executable.
"""
import webbrowser
import sys
import os

def main():
    """Open the main documentation page in the default browser."""
    # Get the base path (site directory) - use site from the same directory as this script
    base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site')
    
    # Open index.html in the default browser
    url = f"file://{os.path.join(base_path, 'index.html')}"
    webbrowser.open(url)
    
    print(f"Opening {url} in your default browser...")

if __name__ == "__main__":
    main()
