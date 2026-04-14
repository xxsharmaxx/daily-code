# Day 12: JSON to CSV Converter

import json
import csv

def json_to_csv(json_file, csv_file):
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)

        # Ensure data is a list
        if not isinstance(data, list):
            print("JSON should contain a list of objects")
            return

        # Get headers from keys
        keys = data[0].keys()

        with open(csv_file, 'w', newline='') as output:
            writer = csv.DictWriter(output, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)

        print(f"Data successfully converted to {csv_file}")

    except Exception as e:
        print("Error:", e)


# Example usage
json_file = "data.json"
csv_file = "output.csv"

json_to_csv(json_file, csv_file)
