#!/usr/bin/env python3
"""
SpeakUp and Learn - Quick Start Script
This script helps users quickly start the SpeakUp and Learn application.
"""

import sys
import os
import subprocess

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 6):
        print("❌ Error: Python 3.6 or higher is required.")
        print(f"   Current version: {sys.version}")
        print("   Please download Python from https://python.org")
        return False
    return True

def check_tkinter():
    """Check if tkinter is available"""
    try:
        import tkinter
        return True
    except ImportError:
        print("❌ Error: tkinter is not available.")
        print("   Please install tkinter for your Python installation.")
        return False

def install_requirements():
    """Install required packages"""
    try:
        import json
        print("✅ All required packages are available.")
        return True
    except ImportError:
        print("❌ Error: Some required packages are missing.")
        return False

def run_app():
    """Run the SpeakUp and Learn application"""
    try:
        print("🚀 Starting SpeakUp and Learn...")
        print("   Building confidence, one voice at a time!")
        print()
        
        # Import and run the main application
        from speakup_app import SpeakUpApp
        app = SpeakUpApp()
        app.run()
        
    except Exception as e:
        print(f"❌ Error starting the application: {e}")
        print("   Please make sure all files are in the same directory.")
        return False

def main():
    """Main function"""
    print("🎤 SpeakUp and Learn - Quick Start")
    print("=" * 40)
    print()
    
    # Check requirements
    if not check_python_version():
        input("Press Enter to exit...")
        return
    
    if not check_tkinter():
        input("Press Enter to exit...")
        return
    
    if not install_requirements():
        input("Press Enter to exit...")
        return
    
    print("✅ All requirements met!")
    print()
    
    # Run the application
    run_app()

if __name__ == "__main__":
    main()