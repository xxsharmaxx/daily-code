import ast

class CodeReviewer:

    def __init__(self, filename):
        self.filename = filename
        self.issues = []

    def check_long_lines(self):

        with open(self.filename, "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines, start=1):
            if len(line) > 80:
                self.issues.append(
                    f"Line {i}: Line exceeds 80 characters."
                )

    def check_variable_names(self):

        with open(self.filename, "r") as file:
            tree = ast.parse(file.read())

        for node in ast.walk(tree):

            if isinstance(node, ast.Name):

                if len(node.id) == 1:
                    self.issues.append(
                        f"Poor variable name: '{node.id}'"
                    )

    def check_long_functions(self):

        with open(self.filename, "r") as file:
            tree = ast.parse(file.read())

        for node in tree.body:

            if isinstance(node, ast.FunctionDef):

                start = node.lineno
                end = node.end_lineno

                length = end - start

                if length > 20:
                    self.issues.append(
                        f"Function '{node.name}' is too long ({length} lines)"
                    )

    def generate_report(self):

        self.check_long_lines()
        self.check_variable_names()
        self.check_long_functions()

        with open("report.txt", "w") as report:

            report.write("=== AI CODE REVIEW REPORT ===\n\n")

            if not self.issues:
                report.write("No issues found.\n")
            else:
                for issue in self.issues:
                    report.write(issue + "\n")

        print("✅ Review completed.")
        print("Report saved as report.txt")


filename = input("Enter Python file name: ")

reviewer = CodeReviewer(filename)

reviewer.generate_report()

def test():

    a = 10
    b = 20
    c = a + b

    print(c)

    for i in range(50):
        print(i)
