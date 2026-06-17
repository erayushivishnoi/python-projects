# I am demonstrating my learning so far in the form of this file organizer project
# file organizer - phase 3
# now shows a preview of what will happen and asks before moving
# also shows a summary at the end
# added error handling so bad files or permissions don't crash the program

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


def get_files(folder_path):
    """get all files in the folder and return them as a list"""
    path = Path(folder_path)
    files = []
    for item in path.iterdir():
        if item.is_file():
            files.append(item)
    return files


def preview_moves(files):
    """show the user what will happen before moving anything"""
    print("\nPreview:")
    for file in files:
        folder_name = get_folder_name(file.suffix)
        print(f"  {file.name} -> {folder_name}/")


def organize_files(folder_path, files):
    """move files into subfolders based on their extension"""
    path = Path(folder_path)

    # keep track of how many files go to each folder
    summary = {}

    skipped = 0
    for file in files:
        folder_name = get_folder_name(file.suffix)
        target_folder = path / folder_name

        if not target_folder.exists():
            os.mkdir(target_folder)

        new_path = target_folder / file.name

        if new_path.exists():
            print(f"Skipped: {file.name} (already exists in {folder_name}/)")
            skipped = skipped + 1
            continue

        try:
            os.rename(str(file), str(new_path))
        except OSError:
            print(f"Skipped: {file.name} (could not move)")
            skipped = skipped + 1
            continue

        if folder_name in summary:
            summary[folder_name] = summary[folder_name] + 1
        else:
            summary[folder_name] = 1

    # show summary
    print("\nSummary:")
    total = 0
    for folder in summary:
        print(f"  {folder}: {summary[folder]} files")
        total = total + summary[folder]
    print(f"  Total: {total} files moved")
    if skipped > 0:
        print(f"  Skipped: {skipped} files")


def main():
    print("File Organizer")
    folder_path = input("Enter the folder path to organize: ")

    if not os.path.isdir(folder_path):
        print("That folder does not exist")
        return

    files = get_files(folder_path)

    if len(files) == 0:
        print("No files to organize")
        return

    preview_moves(files)

    confirm = input("\nProceed? (y/n): ")
    if confirm != "y":
        print("Cancelled")
        return

    organize_files(folder_path, files)


main()
