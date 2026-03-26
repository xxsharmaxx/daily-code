import os
import random

def password_generator():
    chars = "abcdefghijklmnopqrstuvwxyz123456789!@#"
    password = "".join(random.choice(chars) for _ in range(8))
    print("Generated Password:", password)

def calculator():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum:", a + b)

def main():
    while True:
        print("\n=== Developer Toolkit ===")
        print("1. Password Generator")
        print("2. Calculator")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            password_generator()
        elif choice == "2":
            calculator()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

main()