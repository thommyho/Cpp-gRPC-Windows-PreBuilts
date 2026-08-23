#!/usr/bin/env python3
"""
Build script for Cpp-gRPC-Docs standalone executable using PyInstaller.
This creates a statically compiled Windows application that opens the documentation website.
"""
import subprocess
import sys
import os

def main():
    """Build the PyInstaller executable."""
    print("Building Cpp-gRPC-Docs executable...")
    print()
    
    # Install PyInstaller if not already installed
    try:
        import pyinstaller
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
    
    # Build the executable with PyInstaller
    print("Building executable...")
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--name", "Cpp-gRPC-Docs",
        "--onefile",
        "--windowed",
        "--add-data", f"site;site",
        "--add-data", f"_assets,_assets",
        "--clean",
        "docs-open.py"
    ]
    
    result = subprocess.run(cmd, check=True)
    
    print()
    print("Build complete!")
    print(f"The executable is located at: dist\\Cpp-gRPC-Docs.exe")
    print()
    print("To run the application, execute: dist\\Cpp-gRPC-Docs.exe")

if __name__ == "__main__":
    main()
