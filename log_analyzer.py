# Day 19: Log Analyzer

def analyze_log(file_path):
    error = 0
    warning = 0
    info = 0

    try:
        with open(file_path, 'r') as file:
            for line in file:
                if "ERROR" in line:
                    error += 1
                elif "WARNING" in line:
                    warning += 1
                elif "INFO" in line:
                    info += 1

        print("\n=== Log Analysis Result ===")
        print("Errors:", error)
        print("Warnings:", warning)
        print("Info:", info)

    except FileNotFoundError:
        print("Log file not found!")


# Input
file_path = input("Enter log file path: ")
analyze_log(file_path)
