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
    ".xlsx": "Excel Files",
    ".xls": "Excel Files",
    ".docx": "Word Files",
    ".doc": "Word Files",
    ".pptx": "PowerPoint Files",
    ".ppt": "PowerPoint Files",
    ".csv": "CSV Files",
    ".r": "R Files",
    ".py": "Python Files",
}

# # Define a function to organize the files in a folder
# def organize_files(folder_path):
#     # Move all files in subdirectories to folder_path
#     for dirpath, dirnames, filenames in os.walk(folder_path):
#         for filename in filenames:
#             src_path = os.path.join(dirpath, filename)
#             dest_path = os.path.join(folder_path, filename)
#             os.rename(src_path, dest_path)

#     # Delete all empty subdirectories in folder_path
#     for dirpath, dirnames, filenames in os.walk(folder_path, topdown=False):
#         for dirname in dirnames:
#             dir_to_remove = os.path.join(dirpath, dirname)
#             if not os.listdir(dir_to_remove):
#                 os.rmdir(dir_to_remove)

#     # Organize all the files in the folder
#     for file_name in os.listdir(folder_path):
#         # Get the file extension
#         file_extension = os.path.splitext(file_name)[1].lower()

#         # Get the destination directory for this file
#         if file_extension in extensions:
#             dest_dir = os.path.join(folder_path, extensions[file_extension])
#         else:
#             dest_dir = os.path.join(folder_path, "Other")

#         # Create the destination directory if it doesn't exist
#         os.makedirs(dest_dir, exist_ok=True)

#         # Move the file to the destination directory
#         src_path = os.path.join(folder_path, file_name)
#         dest_path = os.path.join(dest_dir, file_name)
#         os.rename(src_path, dest_path)

def move_files(folder_path):
    """
    This function moves all files in subdirectories to folder_path
    """
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            src_path = os.path.join(dirpath, filename)
            dest_path = os.path.join(folder_path, filename)
            os.rename(src_path, dest_path)


def delete_subdirectories(folder_path):
    """
    This function deletes all empty subdirectories in folder_path.
    """
    for dirpath, dirnames, filenames in os.walk(folder_path, topdown=False):
        for dirname in dirnames:
            dir_to_remove = os.path.join(dirpath, dirname)
            if not os.listdir(dir_to_remove):
                os.rmdir(dir_to_remove)


def organize_files_in_folder(folder_path):
    """
    This function organizes all the files in the folder according to file extensions.
    """
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


def organize_files(folder_path):
    """
    This function combines all the previous functions and organizes the files.
    """
    print("Sorting files.....")
    move_files(folder_path)
    delete_subdirectories(folder_path)
    organize_files_in_folder(folder_path)
    print("Sorting Completed")


# Example usage:
if __name__ == "__main__":
    folder_path = "C:/Users/cwong3/Documents/temp"
    organize_files(folder_path)
