import os
import shutil
import random
import string

# Function to generate random string
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

# List of file extensions
file_extensions = {
    'pdf': '.pdf',
    'word': '.docx',
    'excel': '.xlsx',
    'video': '.mp4',
    'python': '.py',
    'picture': '.jpg',
    'r_codes': '.R',
    'mpg': '.mpg',
    'tar': '.tar',
    'music': '.mp3',
    'text': '.txt',
    'csv': '.csv',
    'html': '.html',
    'css': '.css',
    'javascript': '.js',
    'xml': '.xml',
    'json': '.json',
    'powerpoint': '.pptx',
    'database': '.db',
    'compressed': '.zip',
    'executable': '.exe',
    'markdown': '.md'
}

# Desktop path
desktop_path = os.path.expanduser("C:/Users/xwang2//Desktop")

# Create a folder on desktop
folder_name = "Sample_Files"
folder_path = os.path.join(desktop_path, folder_name)
os.makedirs(folder_path, exist_ok=True)

# Generate sample files in the folder
for file_type, file_ext in file_extensions.items():
    file_name = generate_random_string(10) + file_ext
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'wb') as file:
        file.write(os.urandom(1024))  # Write random data to file

print("Sample files created successfully in folder: ", folder_path)
