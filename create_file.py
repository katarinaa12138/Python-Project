import os
import shutil
import random
import string
from faker import Faker
from datetime import datetime, timedelta

# Function to generate random string
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

# Function to generate random date in the past
def generate_random_date():
    days_ago = random.randint(1, 1000)
    return datetime.now() - timedelta(days=days_ago)

# Desktop path
desktop_path = os.path.expanduser("~/Desktop")

# Create a folder on desktop
folder_name = "Sample_Files"
folder_path = os.path.join(desktop_path, folder_name)
os.makedirs(folder_path, exist_ok=True)

# Generate sample files in the folder
fake = Faker()
for file_extension, extension in file_extensions.items():
    for i in range(5): # create 5 files for each extension
        fake_name = fake.file_name(extension=extension)
        file_name = generate_random_string(10) + "_" + fake_name
        file_path = os.path.join(folder_path, file_name)
        file_size = random.randint(1024, 1048576000) # generate file size between 1KB to 1GB
        with open(file_path, 'wb') as file:
            file.write(os.urandom(file_size))  # Write random data to file
        creation_time = generate_random_date().timestamp() # generate random timestamp in the past
        os.utime(file_path, (creation_time, creation_time)) # set file creation time

print("Sample files created successfully in folder: ", folder_path)
