# Day 6: File Organizer

import os
import shutil

def organize_files(directory):
    print(f"\nOrganizing files in: {directory}")

    if not os.path.exists(directory):
        print("Directory not found!")
        return

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        if os.path.isfile(file_path):
            extension = file.split('.')[-1]

            folder_name = extension.upper() + "_files"
            folder_path = os.path.join(directory, folder_name)

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            shutil.move(file_path, os.path.join(folder_path, file))

    print("Files organized successfully!")


