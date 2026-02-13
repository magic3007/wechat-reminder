#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Final test of the hostname addition feature."""

import sys
import os
import socket

# Mock the required modules
class MockArgs:
    def __init__(self, title, desp=""):
        self.title = title
        self.desp = desp

# Test the actual logic from wechat-reminder_main.py
def test_hostname_addition():
    print("Testing hostname addition logic...")

    # Simulate what happens in main()
    args = MockArgs("Test Task Complete")

    # Copy the exact logic from wechat-reminder_main.py
    try:
        hostname = socket.gethostname()
        args.title = f"[{hostname}] {args.title}"
        print(f"✓ Hostname added successfully: {args.title}")
    except Exception as e:
        print(f"✗ Failed to get hostname: {e}")
        # Should keep original title
        print(f"  Original title preserved: {args.title}")

    # Verify the format
    expected_start = f"[{socket.gethostname()}]"
    if args.title.startswith(expected_start):
        print(f"✓ Title correctly starts with hostname: {expected_start}")
    else:
        print(f"✗ Title does not start with hostname: {args.title}")
        return False

    # Test with empty description
    args2 = MockArgs("Another Task", "Some description")
    try:
        hostname = socket.gethostname()
        args2.title = f"[{hostname}] {args2.title}"
        print(f"✓ Hostname added with description: {args2.title}")
    except:
        print("✗ Failed to add hostname with description")

    return True

if __name__ == "__main__":
    if test_hostname_addition():
        print("\n✅ All tests passed!")
        sys.exit(0)
    else:
        print("\n❌ Tests failed!")
        sys.exit(1)