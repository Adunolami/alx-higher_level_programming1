#!/usr/bin/python3

# 2-print_alphabet.py
"""Print the alphabet in lowercase, not followed by a new line."""
for char in range(97, 123):
    if chr(char) not in ['q', 'e']:
        print(chr(char), end='')
