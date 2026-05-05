import json
import os
from cryptography.fernet import Fernet

# Files
KEY_FILE = "secret.key"
DATA_FILE = "passwords.json"

# Generate key if not exists
def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    return key

key = load_key()
fernet = Fernet(key)

# Load existing data
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Save data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Add password
def add_password():
    site = input("Enter site: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    encrypted = fernet.encrypt(password.encode()).decode()

    data = load_data()
    data[site] = {
        "username": username,
        "password": encrypted
    }

    save_data(data)
    print("✅ Password saved!")

# View password
def view_password():
    site = input("Enter site: ")

    data = load_data()

    if site in data:
        decrypted = fernet.decrypt(data[site]["password"].encode()).decode()
        print(f"\nUsername: {data[site]['username']}")
        print(f"Password: {decrypted}")
    else:
        print("❌ Not found")

# Delete password
def delete_password():
    site = input("Enter site to delete: ")
    data = load_data()

    if site in data:
        del data[site]
        save_data(data)
        print("🗑 Deleted successfully")
    else:
        print("❌ Not found")

# Menu
def menu():
    while True:
        print("\n=== Password Manager ===")
        print("1. Add Password")
        print("2. View Password")
        print("3. Delete Password")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_password()
        elif choice == "3":
            delete_password()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

# Run
menu()
