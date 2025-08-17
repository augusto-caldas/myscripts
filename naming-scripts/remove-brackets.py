import os
import re

def rename_files(directory):
    for filename in os.listdir(directory):
        # Remove brackets and content inside of it
        new_filename = re.sub(r'\[.*?\]|\(.*?\)|<.*?>|{.*?}', '', filename)
        # Remove whitespace before extension
        new_filename = re.sub(r'\s+\.', '.', new_filename)
        new_filename = new_filename.strip()  
        # Only rename if there are changes
        if new_filename != filename:
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            # Print feedback to user
            print(f"{filename} -> {new_filename}")

directory_path = input("Enter directory path >> ")
rename_files(directory_path)
