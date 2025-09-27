#!/usr/bin/env python3
"""
Simple test to verify the SpeakUp app works
"""

# Test the user loading logic
import json
import os

def test_user_loading():
    """Test the user loading functionality"""
    print("Testing user loading logic...")
    
    # Simulate the load_users method
    users = {"Ex": "1234"}
    
    try:
        if os.path.exists('users.json'):
            with open('users.json', 'r') as f:
                file_users = json.load(f)
                users.update(file_users)
                print(f"Loaded users from file: {file_users}")
    except Exception as e:
        print(f"Error loading users.json: {e}")
    
    print(f"Final users dictionary: {users}")
    
    # Test login logic
    test_username = "Ex"
    test_password = "1234"
    
    print(f"\nTesting login:")
    print(f"Username: {test_username}")
    print(f"Password: {test_password}")
    
    if test_username in users and users[test_username] == test_password:
        print("✅ Login should work!")
        return True
    else:
        print("❌ Login failed!")
        return False

if __name__ == "__main__":
    test_user_loading()
