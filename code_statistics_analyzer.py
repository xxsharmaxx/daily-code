import ast
import os

def analyze_python_file(file_path):
    if not os.path.exists(file_path):
        print("File not found!")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    lines = source.splitlines()

    total_lines = len(lines)
    blank_lines = sum(1 for line in lines if not line.strip())
    comment_lines = sum(1 for line in lines if line.strip().startswith("#"))

    tree = ast.parse(source)

    functions = []
    classes = 0
    imports = 0

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):
            length = node.end_lineno - node.lineno + 1
            functions.append((node.name, length))

        elif isinstance(node, ast.ClassDef):
            classes += 1

        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            imports += 1

    print("\n===== CODE STATISTICS =====")

    print(f"File            : {os.path.basename(file_path)}")
    print(f"Total Lines     : {total_lines}")
    print(f"Blank Lines     : {blank_lines}")
    print(f"Comment Lines   : {comment_lines}")
    print(f"Classes         : {classes}")
    print(f"Functions       : {len(functions)}")
    print(f"Imports         : {imports}")

    if functions:
        avg = sum(length for _, length in functions) / len(functions)
        print(f"Average Function Length : {avg:.2f} lines")

        print("\nFunctions:")
        for name, length in functions:
            print(f" - {name} ({length} lines)")

    with open("analysis_report.txt", "w", encoding="utf-8") as report:
        report.write("CODE STATISTICS REPORT\n\n")
        report.write(f"File: {os.path.basename(file_path)}\n")
        report.write(f"Total Lines: {total_lines}\n")
        report.write(f"Blank Lines: {blank_lines}\n")
        report.write(f"Comment Lines: {comment_lines}\n")
        report.write(f"Classes: {classes}\n")
        report.write(f"Functions: {len(functions)}\n")
        report.write(f"Imports: {imports}\n")

    print("\nReport saved as analysis_report.txt")


if __name__ == "__main__":
    filename = input("Enter Python file: ")
    analyze_python_file(filename)
