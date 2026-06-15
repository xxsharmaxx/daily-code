import pyperclip
import time
import os

HISTORY_FILE = "clipboard_history.txt"

def save_clipboard():
    last_text = ""

    print("Monitoring clipboard... Press Ctrl+C to stop.")

    try:
        while True:
            current_text = pyperclip.paste()

            if current_text != last_text:
                last_text = current_text

                with open(HISTORY_FILE, "a", encoding="utf-8") as file:
                    file.write(current_text + "\n")
                    file.write("-" * 50 + "\n")

                print("Saved:", current_text[:50])

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopped monitoring.")

def view_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            print(file.read())
    else:
        print("No history found.")

def search_history():
    keyword = input("Enter keyword: ")

    if not os.path.exists(HISTORY_FILE):
        print("No history found.")
        return

    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()

    found = False

    for line in lines:
        if keyword.lower() in line.lower():
            print(line.strip())
            found = True

    if not found:
        print("No matches found.")

while True:

    print("\n===== Clipboard History Manager =====")
    print("1. Monitor Clipboard")
    print("2. View History")
    print("3. Search History")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        save_clipboard()

    elif choice == "2":
        view_history()

    elif choice == "3":
        search_history()

    elif choice == "4":
        break

    else:
        print("Invalid option.")
