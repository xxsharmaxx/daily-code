# Safe Login Protection Demo

MAX_ATTEMPTS = 3
USERNAME = "admin"
PASSWORD = "Secure123"

failed_attempts = 0
locked = False

while not locked:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == USERNAME and password == PASSWORD:
        print("Login successful ✅")
        break
    else:
        failed_attempts += 1
        remaining = MAX_ATTEMPTS - failed_attempts
        print("Invalid credentials ❌")

        if failed_attempts >= MAX_ATTEMPTS:
            locked = True
            print("Account locked due to too many failed attempts 🔒")
        else:
            print(f"Attempts remaining: {remaining}")
