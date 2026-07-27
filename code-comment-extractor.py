import os

def extract_comments(file_path):
    if not os.path.exists(file_path):
        print("File not found!")
        return

    comments = []
    total_lines = 0

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            total_lines += 1

            stripped = line.strip()

            if stripped.startswith("#"):
                comments.append(stripped)

    print("\n========== COMMENT REPORT ==========\n")

    print(f"File Name      : {os.path.basename(file_path)}")
    print(f"Total Lines    : {total_lines}")
    print(f"Comments Found : {len(comments)}")

    print("\nComments:\n")

    for i, comment in enumerate(comments, 1):
        print(f"{i}. {comment}")

    with open("comments_report.txt", "w", encoding="utf-8") as report:

        report.write("COMMENT REPORT\n")
        report.write("=" * 40 + "\n\n")

        report.write(f"File Name : {os.path.basename(file_path)}\n")
        report.write(f"Total Lines : {total_lines}\n")
        report.write(f"Comments : {len(comments)}\n\n")

        for i, comment in enumerate(comments, 1):
            report.write(f"{i}. {comment}\n")

    print("\nReport saved as comments_report.txt")


if __name__ == "__main__":

    filename = input("Enter Python file: ")

    extract_comments(filename)
