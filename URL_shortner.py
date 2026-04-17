# Day 18: Simple URL Shortener

import string
import random

url_map = {}

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def shorten_url(long_url):
    short_code = generate_short_code()
    url_map[short_code] = long_url
    return short_code

def get_original_url(short_code):
    return url_map.get(short_code, "URL not found")

# Example usage
print("=== URL Shortener ===")

while True:
    print("\n1. Shorten URL")
    print("2. Retrieve URL")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        long_url = input("Enter long URL: ")
        short = shorten_url(long_url)
        print("Short URL:", short)

    elif choice == '2':
        code = input("Enter short code: ")
        print("Original URL:", get_original_url(code))

    elif choice == '3':
        break

    else:
        print("Invalid choice")
