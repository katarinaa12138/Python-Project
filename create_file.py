import os
import shutil
import random
import string

# Function to generate random string
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

# Mapping of file extensions to purpose-based names
file_extensions = {
    'pdf': {'name': 'life', 'ext': '.pdf'},
    'word': {'name': 'entertainment', 'ext': '.docx'},
    'excel': {'name': 'study', 'ext': '.xlsx'},
    'video': {'name': 'life', 'ext': '.mp4'},
    'python': {'name': 'study', 'ext': '.py'},
    'picture': {'name': 'entertainment', 'ext': '.jpg'},
    'r_codes': {'name': 'study', 'ext': '.R'},
    'mpg': {'name': 'entertainment', 'ext': '.mpg'},
    'tar': {'name': 'study', 'ext': '.tar'},
    'music': {'name': 'entertainment', 'ext': '.mp3'},
    'text': {'name': 'study', 'ext': '.txt'},
    'csv': {'name': 'study', 'ext': '.csv'},
    'html': {'name': 'entertainment', 'ext': '.html'},
    'css': {'name': 'entertainment', 'ext': '.css'},
    'javascript': {'name': 'study', 'ext': '.js'},
    'xml': {'name': 'study', 'ext': '.xml'},
    'json': {'name': 'study', 'ext': '.json'},
    'powerpoint': {'name': 'entertainment', 'ext': '.pptx'},
    'database': {'name': 'study', 'ext': '.db'},
    'compressed': {'name': 'study', 'ext': '.zip'},
    'executable': {'name': 'study', 'ext': '.exe'},
    'markdown': {'name': 'study', 'ext': '.md'}
}

# Desktop path
desktop_path = os.path.expanduser("~/Desktop")

# Create a folder on desktop
folder_name = "Sample_Files"
folder_path = os.path.join(desktop_path, folder_name)
os.makedirs(folder_path, exist_ok=True)

# Generate sample files in the folder
for file_type, file_info in file_extensions.items():
    file_name = file_info['name'] + '_' + generate_random_string(10) + file_info['ext']
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'wb') as file:
        file.write(os.urandom(1024))  # Write random data to file

print("Sample files created successfully in folder: ", folder_path)
