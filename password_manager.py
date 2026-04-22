# Day 22: Simple Password Manager

import os

FILE = "passwords.txt"

def save_password(site, username, password):
    with open(FILE, "a") as f:
        f.write(f"{site},{username},{password}\n")
    print("Password saved successfully!")

def view_passwords():
    if not os.path.exists(FILE):
        print("No passwords saved yet.")
        return

    with open(FILE, "r") as f:
        print("\nSaved Accounts:")
        for line in f:
            site, username, password = line.strip().split(",")
            print(f"Site: {site} | Username: {username} | Password: {password}")

def search_password(site_name):
    if not os.path.exists(FILE):
        print("No passwords found.")
        return

    with open(FILE, "r") as f:
        for line in f:
            site, username, password = line.strip().split(",")
            if site.lower() == site_name.lower():
                print(f"\nFound:\nUsername: {username}\nPassword: {password}")
                return

    print("Site not found!")


def main():
    while True:
        print("\n==== Password Manager ====")
        print("1. Add Password")
        print("2. View All")
        print("3. Search by Site")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            site = input("Enter site: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            save_password(site, username, password)

        elif choice == "2":
            view_passwords()

        elif choice == "3":
            site = input("Enter site to search: ")
            search_password(site)

        elif choice == "4":
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
