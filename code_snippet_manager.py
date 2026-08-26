import json
import os
from datetime import datetime

FILE = "snippets.json"


def load_snippets():
    if not os.path.exists(FILE):
        return {}

    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


def save_snippets(snippets):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(snippets, f, indent=4)


def add_snippet(snippets):
    title = input("Snippet title: ").strip()

    if not title:
        print("Title cannot be empty.")
        return

    if title in snippets:
        print("A snippet with this title already exists.")
        return

    language = input("Programming language: ").strip()

    print("\nEnter your code.")
    print("Type END on a new line when finished.\n")

    lines = []

    while True:
        line = input()

        if line == "END":
            break

        lines.append(line)

    code = "\n".join(lines)

    snippets[title] = {
        "language": language,
        "code": code,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    save_snippets(snippets)

    print("\n✓ Snippet saved successfully.")


def list_snippets(snippets):
    if not snippets:
        print("\nNo snippets found.")
        return

    print("\n========== SNIPPETS ==========")

    for index, (title, data) in enumerate(
        snippets.items(), start=1
    ):
        print(
            f"{index}. {title} "
            f"[{data['language']}]"
        )

    print("===============================")


def view_snippet(snippets):
    title = input("Enter snippet title: ").strip()

    if title not in snippets:
        print("Snippet not found.")
        return

    snippet = snippets[title]

    print("\n========== SNIPPET ==========")
    print(f"Title    : {title}")
    print(f"Language : {snippet['language']}")
    print(f"Created  : {snippet['created_at']}")
    print("\nCode:")
    print("-" * 30)
    print(snippet["code"])
    print("==============================")


def search_snippets(snippets):
    keyword = input(
        "Search title or programming language: "
    ).lower().strip()

    results = []

    for title, data in snippets.items():

        if (
            keyword in title.lower()
            or keyword in data["language"].lower()
        ):
            results.append((title, data))

    if not results:
        print("\nNo matching snippets found.")
        return

    print("\n========== RESULTS ==========")

    for title, data in results:
        print(
            f"- {title} [{data['language']}]"
        )

    print("==============================")


def delete_snippet(snippets):
    title = input("Enter snippet title to delete: ").strip()

    if title not in snippets:
        print("Snippet not found.")
        return

    confirm = input(
        f"Delete '{title}'? (y/n): "
    ).lower()

    if confirm == "y":
        del snippets[title]
        save_snippets(snippets)

        print("✓ Snippet deleted.")

    else:
        print("Deletion cancelled.")


def export_snippet(snippets):
    title = input("Enter snippet title: ").strip()

    if title not in snippets:
        print("Snippet not found.")
        return

    snippet = snippets[title]

    filename = (
        title.lower()
        .replace(" ", "_")
        + ".txt"
    )

    try:
        with open(filename, "w", encoding="utf-8") as f:

            f.write(f"Title: {title}\n")
            f.write(
                f"Language: {snippet['language']}\n"
            )
            f.write(
                f"Created: {snippet['created_at']}\n\n"
            )
            f.write(snippet["code"])

        print(
            f"✓ Exported to {filename}"
        )

    except OSError as error:
        print(f"Export failed: {error}")


def show_statistics(snippets):
    if not snippets:
        print("\nNo snippets available.")
        return

    languages = {}

    for data in snippets.values():

        language = data["language"].lower()

        languages[language] = (
            languages.get(language, 0) + 1
        )

    print("\n========== STATISTICS ==========")
    print(f"Total snippets: {len(snippets)}")

    print("\nLanguages:")

    for language, count in sorted(
        languages.items(),
        key=lambda x: x[1],
        reverse=True
    ):
        print(f"- {language}: {count}")

    print("================================")


def menu():
    print("""
╔══════════════════════════════════╗
║      CODE SNIPPET MANAGER       ║
╠══════════════════════════════════╣
║ 1. Add Snippet                  ║
║ 2. List Snippets                ║
║ 3. View Snippet                 ║
║ 4. Search Snippets              ║
║ 5. Delete Snippet               ║
║ 6. Export Snippet               ║
║ 7. Statistics                   ║
║ 8. Exit                         ║
╚══════════════════════════════════╝
""")


def main():
    snippets = load_snippets()

    print("\nWelcome to Code Snippet Manager!")

    while True:

        menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_snippet(snippets)

        elif choice == "2":
            list_snippets(snippets)

        elif choice == "3":
            view_snippet(snippets)

        elif choice == "4":
            search_snippets(snippets)

        elif choice == "5":
            delete_snippet(snippets)

        elif choice == "6":
            export_snippet(snippets)

        elif choice == "7":
            show_statistics(snippets)

        elif choice == "8":
            print("\nGoodbye! 👋")
            break

        else:
            print("\nInvalid choice.")


if __name__ == "__main__":
    main()
