import hashlib
import os

def calculate_hash(filepath):
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()

def save_hash():
    filepath = input("Enter file path: ")

    if not os.path.exists(filepath):
        print("File not found!")
        return

    file_hash = calculate_hash(filepath)

    with open("hash_database.txt", "a") as db:
        db.write(f"{filepath}|{file_hash}\n")

    print("\nHash saved successfully!")
    print("SHA-256:", file_hash)

def verify_file():
    filepath = input("Enter file path: ")

    if not os.path.exists(filepath):
        print("File not found!")
        return

    current_hash = calculate_hash(filepath)

    with open("hash_database.txt", "r") as db:
        records = db.readlines()

    for record in records:
        saved_path, saved_hash = record.strip().split("|")

        if saved_path == filepath:

            if current_hash == saved_hash:
                print("\n✅ File is unchanged.")
            else:
                print("\n⚠️ File has been modified!")

            return

    print("No hash record found.")

while True:

    print("\n===== FILE INTEGRITY CHECKER =====")
    print("1. Save File Hash")
    print("2. Verify File")
    print("3. Exit")

    choice = input("Select option: ")

    if choice == "1":
        save_hash()

    elif choice == "2":
        verify_file()

    elif choice == "3":
        break

    else:
        print("Invalid choice.")
