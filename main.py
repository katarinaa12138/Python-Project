import os
from pathlib import Path
import os
import shutil
from datetime import datetime

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


def move_files(folder_path):
    """
    This function moves all files in subdirectories to folder_path.
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

        user_confirmation = False
            
        while not user_confirmation:
            # Prompt users to confirm file move
            confirm = input(f"Confirm to move {file_name} (y/n):")
            if confirm.lower() == 'y':
                # Move the files if user input y
                os.rename(src_path, dest_path)
                user_confirmation = True

                # Check if users want to undo file move 
                undo_file = input("Undo previous file move? (y/n)")
                if undo_file.lower() == 'y':
                    # Move file back to its original place
                    os.rename(dest_path, src_path)
                    print(f"Moved {file_name} back to original place.")
                elif undo_file.lower() == 'n':
                    print(f"{file_name} moved to new folder.")
                else:
                    print("Invalid Input: please input y or n.")

            elif confirm.lower() == 'n':
                # Do not move files if users input n
                user_confirmation = True
            else:
                # If users input anything other than y or n
                print("Invalid Input. Please input y or n.")


def organize_files_by_size(folder_path):
    """
    This function organizes all files in the folder according to their sizes.
    """
    files = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
    # Get the sizes of all files in the folder
    file_sizes = [(file, os.path.getsize(os.path.join(folder_path, file))) for file in files]

    # Sort files by their size
    file_sizes.sort(key=lambda x: x[1])

    # Create size ranges
    size_ranges = [(0, 1024), (1024, 1024**2), (1024**2, 1024**3), (1024**3, float("inf"))]
    size_range_names = ["Small", "Medium", "Large", "Very Large"]

    # Create a dictionary that maps each file size range to a directory
    size_range_to_dir = {size_range_names[i]: os.path.join(folder_path, size_range_names[i]) for i in range(len(size_range_names))}

    # Create the directories if they don't exist
    for dir_name in size_range_to_dir.values():
        os.makedirs(dir_name, exist_ok=True)

    # Prompt user to choose between manual or automatic file organization
    manual_sort = False
    while not manual_sort:
        user_input = input("Do you want to organize the files one by one? (y/n): ")
        if user_input.lower() == 'y':
            manual_sort = True
        elif user_input.lower() == 'n':
            manual_sort = False
            break
        else:
            print("Invalid Input. Please input y or n.")

    # Move files to their corresponding directories
    for file, size in file_sizes:
        for i, size_range in enumerate(size_ranges):
            if size >= size_range[0] and size < size_range[1]:
                src_path = os.path.join(folder_path, file)
                dest_dir = size_range_to_dir[size_range_names[i]]
                dest_path = os.path.join(dest_dir, file)

                if manual_sort:
                    user_confirmation = False

                    while not user_confirmation:
                        # Prompt users to confirm file move
                        confirm = input(f"Confirm to move {file} (y/n):")
                        if confirm.lower() == 'y':
                            # Move the files if user input y
                            os.rename(src_path, dest_path)
                            user_confirmation = True

                            # Check if users want to undo file move 
                            undo_file = input("Undo previous file move? (y/n)")
                            if undo_file.lower() == 'y':
                                # Move file back to its original place
                                os.rename(dest_path, src_path)
                                print(f"Moved {file} back to original place.")
                            elif undo_file.lower() == 'n':
                                print(f"{file} moved to {dest_dir}.")
                            else:
                                print("Invalid Input: please input y or n.")

                        elif confirm.lower() == 'n':
                            # Do not move files if users input n
                            user_confirmation = True
                        else:
                            # If users input anything other than y or n
                            print("Invalid Input. Please input y or n.")
                else:
                    # If automatic sorting is chosen, move the file without confirmation
                    os.rename(src_path, dest_path)
                    print(f"{file} moved to {dest_dir}.")


def organize_files_by_date(folder_path):
    """
    This function organizes all the files in the folder according to their creation dates.
    """
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        # Get the creation time of the file
        creation_time = os.path.getctime(file_path)
        creation_date = datetime.fromtimestamp(creation_time).date()
        
        # Create a directory with the name of the date if it doesn't exist
        date_dir = os.path.join(folder_path, str(creation_date))
        if not os.path.exists(date_dir):
            os.mkdir(date_dir)
            
        # Move the file to the date directory
        dest_path = os.path.join(date_dir, file_name)
        shutil.move(file_path, dest_path)
        
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
# if __name__ == "__main__":
    # folder_path = "C:/Users/xwang2//Desktop/Sample_Files"
    # # folder_path = "C:/Users/cwong3//Desktop/Sample_Files"
    # organize_files_by_size(folder_path)

    # organize_files(folder_path)

