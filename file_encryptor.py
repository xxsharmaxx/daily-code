# Day 23: File Encryption & Decryption Tool

from cryptography.fernet import Fernet

KEY_FILE = "secret.key"

# Generate key (run once)
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    print("Key generated and saved.")

# Load key
def load_key():
    return open(KEY_FILE, "rb").read()

# Encrypt file
def encrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted = f.encrypt(data)

    with open(filename, "wb") as file:
        file.write(encrypted)

    print("File encrypted successfully!")

# Decrypt file
def decrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    decrypted = f.decrypt(data)

    with open(filename, "wb") as file:
        file.write(decrypted)

    print("File decrypted successfully!")


def main():
    print("\n=== File Encryptor ===")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    print("4. Exit")

    while True:
        choice = input("\nEnter choice: ")

        if choice == "1":
            generate_key()

        elif choice == "2":
            file = input("Enter filename: ")
            encrypt_file(file)

        elif choice == "3":
            file = input("Enter filename: ")
            decrypt_file(file)

        elif choice == "4":
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
