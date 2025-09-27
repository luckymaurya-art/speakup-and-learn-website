#!/usr/bin/env python3
"""
Quick test script to verify the login functionality
"""

import json
import os

def test_users():
    """Test the user loading functionality"""
    print("Testing user loading...")
    
    # Test default users
    default_users = {"Ex": "1234"}
    print(f"Default users: {default_users}")
    
    # Check if users.json exists
    if os.path.exists('users.json'):
        print("users.json file exists")
        try:
            with open('users.json', 'r') as f:
                users = json.load(f)
                print(f"Loaded users: {users}")
        except Exception as e:
            print(f"Error loading users.json: {e}")
    else:
        print("users.json file does not exist - will use default users")
    
    # Test login logic
    test_username = "Ex"
    test_password = "1234"
    
    print(f"\nTesting login with:")
    print(f"Username: {test_username}")
    print(f"Password: {test_password}")
    
    if test_username in default_users and default_users[test_username] == test_password:
        print("✅ Login should work!")
    else:
        print("❌ Login failed!")
        
    # Test wrong password
    wrong_password = "wrong"
    print(f"\nTesting with wrong password: {wrong_password}")
    if test_username in default_users and default_users[test_username] == wrong_password:
        print("❌ This should not work!")
    else:
        print("✅ Correctly rejected wrong password")

if __name__ == "__main__":
    test_users()
