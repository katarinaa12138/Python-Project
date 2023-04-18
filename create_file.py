import os
import shutil
import random
import string

# Function to generate random string
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

# Mapping of file extensions to new extensions
file_extensions = {
    'pdf': '.pdf',
    'docx': '.docx',
    'xlsx': '.xlsx',
    'mp4': '.mp4',
    'py': '.py',
    'jpg': '.jpg',
    'R': '.R',
    'mpg': '.mpg',
    'tar': '.tar',
    'mp3': '.mp3',
    'txt': '.txt',
    'csv': '.csv',
    'html': '.html',
    'css': '.css',
    'js': '.js',
    'xml': '.xml',
    'json': '.json',
    'pptx': '.pptx',
    'db': '.db',
    'zip': '.zip',
    'exe': '.exe',
    'md': '.md'
}

# Desktop path
desktop_path = os.path.expanduser("~/Desktop")

# Create a folder on desktop
folder_name = "Sample_Files"
folder_path = os.path.join(desktop_path, folder_name)
os.makedirs(folder_path, exist_ok=True)

# Generate sample files in the folder
for file_type, new_ext in file_extensions.items():
    for i in range(1, 8):
        file_name = f"{file_type}_{i}{new_ext}"
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'wb') as file:
            file.write(os.urandom(i*1024*1024))  # Write random data to file
          
print("Sample files created successfully in folder: ", folder_path)
