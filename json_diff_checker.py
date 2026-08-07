import json
import sys


def load_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"❌ File not found: {filename}")
        sys.exit()

    except json.JSONDecodeError:
        print(f"❌ Invalid JSON: {filename}")
        sys.exit()


def compare(old, new, path=""):
    changes = []

    if isinstance(old, dict) and isinstance(new, dict):

        old_keys = set(old.keys())
        new_keys = set(new.keys())

        for key in old_keys - new_keys:
            changes.append(
                f"REMOVED: {path}{key} = {old[key]}"
            )

        for key in new_keys - old_keys:
            changes.append(
                f"ADDED: {path}{key} = {new[key]}"
            )

        for key in old_keys & new_keys:
            changes.extend(
                compare(
                    old[key],
                    new[key],
                    f"{path}{key}."
                )
            )

    elif isinstance(old, list) and isinstance(new, list):

        max_length = max(len(old), len(new))

        for i in range(max_length):

            if i >= len(old):
                changes.append(
                    f"ADDED: {path}[{i}] = {new[i]}"
                )

            elif i >= len(new):
                changes.append(
                    f"REMOVED: {path}[{i}] = {old[i]}"
                )

            else:
                changes.extend(
                    compare(
                        old[i],
                        new[i],
                        f"{path}[{i}]."
                    )
                )

    elif old != new:

        changes.append(
            f"CHANGED: {path[:-1]}\n"
            f"         OLD: {old}\n"
            f"         NEW: {new}"
        )

    return changes


def main():

    print("=" * 55)
    print("           JSON DIFF CHECKER")
    print("=" * 55)

    old_file = input("Enter OLD JSON file: ")
    new_file = input("Enter NEW JSON file: ")

    old_data = load_json(old_file)
    new_data = load_json(new_file)

    changes = compare(old_data, new_data)

    print("\n" + "=" * 55)
    print("RESULT")
    print("=" * 55)

    if not changes:
        print("✅ No differences found.")

    else:
        print(f"⚠️ {len(changes)} change(s) found:\n")

        for change in changes:
            print(change)
            print("-" * 55)

    with open("json_diff_report.txt", "w", encoding="utf-8") as report:

        report.write("JSON DIFF REPORT\n")
        report.write("=" * 55 + "\n\n")

        if not changes:
            report.write("No differences found.\n")

        else:
            for change in changes:
                report.write(change + "\n")
                report.write("-" * 55 + "\n")

    print("\n📄 Report saved as json_diff_report.txt")


if __name__ == "__main__":
    main()
