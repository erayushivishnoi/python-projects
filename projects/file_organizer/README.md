# File Organizer

Automation script to organize files by type using the os module and pathlib.

## What it does (Phase 2)

- Ask the user for a folder path
- Scan the folder for files
- Show a preview of what will be moved and where
- Ask the user to confirm before moving anything
- Move each file into a subfolder based on its extension (e.g., .jpg goes to Images/, .py goes to Code/)
- Supports 6 categories: Images, Documents, Videos, Music, Code, Spreadsheets
- Files with unknown extensions go to Other/
- Create subfolders automatically if they don't exist
- Show a summary of how many files went to each folder

## Planned for later

- Phase 3: add error handling

## How to run

```
python main.py
```

## Built with

- Python standard library only (os, pathlib)
- Dictionary for mapping extensions to folder names
- Functions, loops, conditionals, f-strings

## What I learned building this

### Phase 1
- Importing and using os and pathlib modules
- Using Path objects to work with files and directories
- Iterating over files in a directory with Path.iterdir()
- Checking if something is a file with is_file()
- Getting a file extension with Path.suffix
- Creating directories with os.mkdir()
- Moving files with os.rename()
- Using a dictionary to map values to categories

### Phase 2
- Splitting logic into smaller functions (get_files, preview_moves, organize_files)
- Building a preview by looping through data without changing it
- Asking for user confirmation before doing something destructive
- Using a dictionary to count and summarize results
