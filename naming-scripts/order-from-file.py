import os

# Path to the text file with episode information
text_file_path = './'

# Directory where the files to be renamed are located
root_dir = './'

# Read the text file and create a dictionary mapping episode titles to their season and episode numbers
episode_dict = {}
with open(text_file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if ' - ' in line:
            code, title = line.split(' - ', 1)
            episode_dict[title.strip()] = code.strip()

# Walk through all directories and files
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(".avi", ".mkv", ".mp4", ".mov"):
            episode_name = filename[:-4]
            if episode_name in episode_dict:
                new_filename = f"{episode_dict[episode_name]} - {filename}"
                old_file_path = os.path.join(dirpath, filename)
                new_file_path = os.path.join(dirpath, new_filename)
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {old_file_path} -> {new_file_path}")
            else:
                print(f"Skipping: {filename} (No matching episode found)")
