# I am demonstrating my learning so far in the form of this file organizer project
# file organizer - phase 1
# basic version that organizes files in a folder by their extension
# I have planned this in 2 more phases
# phase 2: show a preview before moving, ask for confirmation, summary of what was moved
# phase 3: will add error handling to this code

import os
from pathlib import Path

# mapping of file extensions to folder names
EXTENSION_MAP = {
    ".jpg": "Images",
    ".png": "Images",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".mp4": "Videos",
    ".mp3": "Music",
    ".py": "Code",
    ".html": "Code",
    ".css": "Code",
    ".xlsx": "Spreadsheets",
    ".csv": "Spreadsheets",
}


def get_folder_name(extension):
    """return the folder name for a given extension, or Other if not mapped"""
    extension = extension.lower()
    if extension in EXTENSION_MAP:
        return EXTENSION_MAP[extension]
    return "Other"


def organize_files(folder_path):
    """move files in the given folder into subfolders based on their extension"""
    path = Path(folder_path)

    files = []
    for item in path.iterdir():
        if item.is_file():
            files.append(item)

    if len(files) == 0:
        print("No files to organize")
        return

    moved = 0
    for file in files:
        folder_name = get_folder_name(file.suffix)
        target_folder = path / folder_name

        if not target_folder.exists():
            os.mkdir(target_folder)
            print(f"Created folder: {folder_name}")

        new_path = target_folder / file.name
        os.rename(str(file), str(new_path))
        print(f"Moved: {file.name} -> {folder_name}/")
        moved = moved + 1

    print(f"\nDone! Moved {moved} files")


def main():
    print("File Organizer")
    folder_path = input("Enter the folder path to organize: ")

    if not os.path.isdir(folder_path):
        print("That folder does not exist")
        return

    print(f"\nOrganizing files in: {folder_path}")
    organize_files(folder_path)


main()
