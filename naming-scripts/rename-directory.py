import os
import shutil

def rename_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Extract file name without extension
            file_name, file_ext = os.path.splitext(file)
            if file_ext in ['.mp4', '.mkv', '.avi', '.mov']:
                # Construct the new folder path
                new_folder_path = os.path.join(directory, file_name)
                os.makedirs(new_folder_path, exist_ok=True)
                # Get file paths
                current_file_path = os.path.join(root, file)
                new_file_path = os.path.join(new_folder_path, file)
                print(f"Processing file: {current_file_path}")
                # Move the file to the new folder
                shutil.move(current_file_path, new_file_path)
                # Remove the old empty directory
                if not os.listdir(root):
                    os.rmdir(root)

rename_directory("./")
