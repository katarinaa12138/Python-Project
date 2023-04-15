import argparse
from main import organize_files

# Create the arguement 
parser = argparse.ArgumentParser(description='Organizes files in a folder based on extensions.')

# Add arguement
parser.add_argument("folder_path", help="Path to the folder to organize.")

# Parse the arguments
args = parser.parse_args()

# Calls the organize_files function from main
organize_files(args.folder_path)

