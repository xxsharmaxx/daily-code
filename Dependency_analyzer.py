import ast
import os
import sys
from collections import Counter


STDLIB = {
    "os", "sys", "json", "math", "time", "re", "random",
    "datetime", "collections", "itertools", "functools",
    "pathlib", "subprocess", "threading", "asyncio",
    "socket", "sqlite3", "logging", "hashlib", "secrets",
    "statistics", "typing", "csv", "urllib", "http",
    "shutil", "glob", "argparse", "configparser",
    "dataclasses", "enum", "queue", "signal"
}


def analyze_file(filename):

    imports = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            tree = ast.parse(file.read(), filename)

    except (SyntaxError, UnicodeDecodeError):
        return imports

    for node in ast.walk(tree):

        if isinstance(node, ast.Import):

            for item in node.names:
                imports.append(item.name.split(".")[0])

        elif isinstance(node, ast.ImportFrom):

            if node.module:
                imports.append(
                    node.module.split(".")[0]
                )

    return imports


def scan_project(folder):

    all_imports = []
    python_files = 0

    for root, _, files in os.walk(folder):

        for filename in files:

            if filename.endswith(".py"):

                python_files += 1

                path = os.path.join(
                    root,
                    filename
                )

                all_imports.extend(
                    analyze_file(path)
                )

    return python_files, all_imports


def main():

    print("=" * 65)
    print("             PYTHON DEPENDENCY ANALYZER")
    print("=" * 65)

    folder = input(
        "\nEnter Python project folder: "
    ).strip()

    if not os.path.isdir(folder):

        print("❌ Folder not found.")
        return

    python_files, imports = scan_project(folder)

    if python_files == 0:

        print("❌ No Python files found.")
        return

    counts = Counter(imports)

    unique = sorted(set(imports))

    standard = []
    external = []

    for library in unique:

        if library in STDLIB:
            standard.append(library)
        else:
            external.append(library)

    print("\n📊 PROJECT SUMMARY")
    print("-" * 65)

    print(f"Python files       : {python_files}")
    print(f"Total imports      : {len(imports)}")
    print(f"Unique dependencies: {len(unique)}")

    print("\n🐍 STANDARD LIBRARY")
    print("-" * 65)

    if standard:

        for library in standard:
            print(
                f"  ✓ {library:<20}"
                f"({counts[library]} imports)"
            )

    else:
        print("  None detected")

    print("\n📦 EXTERNAL DEPENDENCIES")
    print("-" * 65)

    if external:

        for library in external:
            print(
                f"  → {library:<20}"
                f"({counts[library]} imports)"
            )

    else:
        print("  None detected")

    duplicates = {
        name: count
        for name, count in counts.items()
        if count > 1
    }

    print("\n⚠️ FREQUENT IMPORTS")
    print("-" * 65)

    if duplicates:

        for name, count in sorted(
            duplicates.items(),
            key=lambda x: x[1],
            reverse=True
        ):

            print(
                f"  {name:<20} "
                f"{count} times"
            )

    else:

        print("  No repeated imports")

    report = os.path.join(
        folder,
        "dependency_report.txt"
    )

    with open(
        report,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "PYTHON DEPENDENCY REPORT\n"
        )

        file.write("=" * 50 + "\n\n")

        file.write(
            f"Python files: {python_files}\n"
        )

        file.write(
            f"Total imports: {len(imports)}\n"
        )

        file.write(
            f"Unique dependencies: {len(unique)}\n\n"
        )

        file.write(
            "STANDARD LIBRARY\n"
        )

        for library in standard:
            file.write(
                f"- {library}\n"
            )

        file.write(
            "\nEXTERNAL DEPENDENCIES\n"
        )

        for library in external:
            file.write(
                f"- {library}\n"
            )

        file.write(
            "\nFREQUENT IMPORTS\n"
        )

        for name, count in duplicates.items():
            file.write(
                f"- {name}: {count}\n"
            )

    print("\n" + "=" * 65)

    print(
        f"📄 Report created:\n{report}"
    )

    print("\n✅ Analysis completed.")


if __name__ == "__main__":
    main()
