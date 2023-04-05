import os
from pathlib import Path

# Define a dictionary that maps each file extension to a directory
extensions = {
    ".jpeg": "Pictures",
    ".jpg": "Pictures",
    ".gif": "Pictures",
    ".png": "Pictures",
    ".wmv": "Videos",
    ".mov": "Videos",
    ".mp4": "Videos",
    ".mpg": "Videos",
    ".mpeg": "Videos",
    ".mkv": "Videos",
    ".iso": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    ".rz": "Archives",
    ".7z": "Archives",
    ".dmg": "Archives",
    ".rar": "Archives",
    ".zip": "Archives",
    ".mp3": "Music",
    ".msv": "Music",
    ".wav": "Music",
    ".wma": "Music",
    ".pdf": "PDFs",
}

# Define a function to organize the files in a folder
def organize_files(folder_path):
    # Iterate over each file in the folder
    for file_name in os.listdir(folder_path):
        # Get the file extension
        file_extension = os.path.splitext(file_name)[1].lower()

        # Get the destination directory for this file
        if file_extension in extensions:
            dest_dir = os.path.join(folder_path, extensions[file_extension])
        else:
            dest_dir = os.path.join(folder_path, "Other")

        # Create the destination directory if it doesn't exist
        os.makedirs(dest_dir, exist_ok=True)

        # Move the file to the destination directory
        src_path = os.path.join(folder_path, file_name)
        dest_path = os.path.join(dest_dir, file_name)
        os.rename(src_path, dest_path)

# Example usage:
if __name__ == "__main__":
    folder_path = "C:/Users/xwang2/Documents/temp"
    organize_files(folder_path)
