# Day 15: Bulk File Renamer

import os

def rename_files(folder_path, prefix):
    try:
        files = os.listdir(folder_path)

        if not files:
            print("No files found in the folder.")
            return

        count = 1

        for file in files:
            old_path = os.path.join(folder_path, file)

            if os.path.isfile(old_path):
                extension = file.split('.')[-1]
                new_name = f"{prefix}_{count}.{extension}"
                new_path = os.path.join(folder_path, new_name)

                os.rename(old_path, new_path)
                print(f"Renamed: {file} → {new_name}")

                count += 1

        print("\nAll files renamed successfully!")

    except Exception as e:
        print("Error:", e)


# Input
folder = input("Enter folder path: ")
prefix = input("Enter new file prefix: ")

rename_files(folder, prefix)
