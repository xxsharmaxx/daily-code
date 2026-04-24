# Day 24: CSV Data Analyzer

import csv

def analyze_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)

            if not data:
                print("Empty CSV file!")
                return

            print("\n=== CSV Analysis ===")

            # Total rows
            print("Total Rows:", len(data))

            # Column names
            columns = data[0].keys()
            print("Columns:", list(columns))

            # Find numeric columns
            numeric_cols = {}
            for col in columns:
                try:
                    numeric_cols[col] = [
                        float(row[col]) for row in data if row[col]
                    ]
                except:
                    continue

            # Calculate averages
            print("\nAverages:")
            for col, values in numeric_cols.items():
                if values:
                    avg = sum(values) / len(values)
                    print(f"{col}: {round(avg, 2)}")

    except FileNotFoundError:
        print("File not found!")


# Input
file_path = input("Enter CSV file path: ")
analyze_csv(file_path)
