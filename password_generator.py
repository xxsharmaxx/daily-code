# Day 16: Password Generator

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"

    password = "".join(random.choice(characters) for _ in range(length))
    return password


# Input
length = int(input("Enter password length: "))

password = generate_password(length)

print("\nGenerated Password:", password)
