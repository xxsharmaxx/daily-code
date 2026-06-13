import os
import hashlib

def get_file_hash(filepath):
    hasher = hashlib.sha256()

    with open(filepath, "rb") as file:
        while chunk := file.read(4096):
            hasher.update(chunk)

    return hasher.hexdigest()

def find_duplicates(folder):
    hashes = {}
    duplicates = []

    for root, dirs, files in os.walk(folder):

        for file in files:

            filepath = os.path.join(root, file)

            try:
                file_hash = get_file_hash(filepath)

                if file_hash in hashes:
                    duplicates.append((filepath, hashes[file_hash]))
                else:
                    hashes[file_hash] = filepath

            except Exception as e:
                print(f"Error reading {filepath}: {e}")

    return duplicates

folder = input("Enter folder path: ")

duplicates = find_duplicates(folder)

if duplicates:

    print("\nDuplicate Files Found:\n")

    for file1, file2 in duplicates:
        print(f"\nDuplicate:")
        print(file1)
        print(file2)

else:
    print("\nNo duplicate files found.")
