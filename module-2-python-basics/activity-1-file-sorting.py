"""
Module 2 — Activity: File Sorting with os and shutil
Student: [Maristela, John Michael P.]
Date: [September 27, 2026]

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
I made a simple file sorter. It checks the file
type and moves the file to the right folder.


============================================
KEY VOCABULARY
============================================
- os module: used to work with files and folders
- shutil module: used to move files
- file path: the location of a file
- directory: a folder
(add more as needed)


============================================
YOUR SCRIPT
============================================
"""

import os
import shutil

# --- paste your existing code here ---

for file in os.listdir("files"):
    if file.endswith(".jpg"):
        shutil.move("files/" + file, "Images/" + file)
    elif file.endswith(".txt"):
        shutil.move("files/" + file, "Documents/" + file)


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
I need to make sure the folders and file paths
are correct before running the code.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
This can help organize files automatically
instead of moving them one by one.
"""