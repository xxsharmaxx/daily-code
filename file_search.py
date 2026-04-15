# Day 14: File Search Tool

import os

def search_files(directory, keyword):
    print(f"\nSearching for '{keyword}' in {directory}...\n")

    found = False

    for root, dirs, files in os.walk(directory):
        for file in files:
            if keyword.lower() in file.lower():
                found = True
                print("Found:", os.path.join(root, file))

    if not found:
        print("No matching files found.")


# Input
folder = input("Enter folder path: ")
keyword = input("Enter file name keyword: ")

search_files(folder, keyword)
