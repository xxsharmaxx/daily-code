import time
from collections import Counter

LOG_FILE = "app.log"

def analyze_logs(lines):
    errors = 0
    warnings = 0
    messages = []

    for line in lines:
        line_lower = line.lower()

        if "error" in line_lower:
            errors += 1
        elif "warning" in line_lower:
            warnings += 1

        messages.append(line.strip())

    return errors, warnings, Counter(messages)


def monitor_logs():
    print("🚀 Real-Time Log Analyzer Started...\n")

    try:
        with open(LOG_FILE, "r") as file:
            file.seek(0, 2)  # move to end of file

            while True:
                line = file.readline()

                if not line:
                    time.sleep(1)
                    continue

                print(f"📄 New Log: {line.strip()}")

    except FileNotFoundError:
        print("❌ Log file not found")


def summary():
    try:
        with open(LOG_FILE, "r") as file:
            lines = file.readlines()

        errors, warnings, counter = analyze_logs(lines)

        print("\n📊 LOG SUMMARY")
        print(f"Errors: {errors}")
        print(f"Warnings: {warnings}")

        print("\n🔥 Top 5 Messages:")
        for msg, count in counter.most_common(5):
            print(f"{msg} ({count} times)")

    except FileNotFoundError:
        print("❌ Log file not found")


def menu():
    while True:
        print("\n=== Log Analyzer ===")
        print("1. View Summary")
        print("2. Monitor Logs (Live)")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            summary()
        elif choice == "2":
            monitor_logs()
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()
