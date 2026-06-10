import random
import string
import json
import os

DATABASE = "urls.json"

# Load existing URLs
def load_data():
    if os.path.exists(DATABASE):
        with open(DATABASE, "r") as file:
            return json.load(file)
    return {}

# Save URLs
def save_data(data):
    with open(DATABASE, "w") as file:
        json.dump(data, file, indent=4)

# Generate short code
def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# Shorten URL
def shorten_url():
    url = input("Enter long URL: ")

    data = load_data()

    code = generate_code()

    while code in data:
        code = generate_code()

    data[code] = url
    save_data(data)

    print(f"\n✅ Short URL: {code}")

# Retrieve URL
def retrieve_url():
    code = input("Enter short code: ")

    data = load_data()

    if code in data:
        print(f"\n🌐 Original URL: {data[code]}")
    else:
        print("\n❌ URL not found")

# View all URLs
def view_all():
    data = load_data()

    if not data:
        print("\nNo URLs stored.")
        return

    print("\nStored URLs:")
    for code, url in data.items():
        print(f"{code} -> {url}")

# Main menu
while True:
    print("\n===== URL SHORTENER =====")
    print("1. Shorten URL")
    print("2. Retrieve URL")
    print("3. View All")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        shorten_url()

    elif choice == "2":
        retrieve_url()

    elif choice == "3":
        view_all()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
