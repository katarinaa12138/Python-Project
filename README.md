# File Organizer
Katarina Wang, Angela Wong

## Table of Contents
- [Descriptions](#descriptions)
- [Dependencies](#dependencies)
- [Instructions](#instructions)
- [Appendix](#appendix)
- [Contributing](#contributing)
 
## Descriptions
File Organizer is a command-line tool for organizing files in a specified directory. It allows users to organize their files based on different criteria, including size, year, and file extension. By using this tool, users can keep their files more organized and easily find what they need.

## Dependencies
This program requires Python 3.x.

There are no external libraries required for this code. However, the code does make use of several Python built-in modules, including os, shutil, datetime, and pathlib. These modules are included in the standard Python distribution, so there is no need to install anything extra.

## Instructions
1. Navigate and download the files 'main.py', 'command_line.py', and 'create_files.py'.
(Note: Make sure you can navigate the file locations after downloaded.)
    <img src="image\Step1.png" width="400"/>

2. [Optional] If you don't have files to organize, you can try our program with sample files. Open "create_files.py" in Visual Studio Code, and run the file. You should see a folder named "Sample_Files" created on you desktop. 
    <img src="image\Optional_Step2.png" width="400"/>

3. Open you Command Prompt Terminal on you personal computer.

4. Navigate to the location where you stored you downloaded files from step 1. 
(Note: use 'cd' to navigate through the file system by changing the current working directory.)
    <img src="image\step4.png" width="400"/>

5. After setting the working directory, type the command, `python command_line.py [Path to Folder You Want to Organize]`.
    Example: 
    ```Python
    python command_line.py C:/Users/cwong3//Desktop/Sample_Files
    ```

6. Follow the prompts in the terminal to organzie your files.
    - You may choose to organize you files by size, year, or file extensions.
        <img src="image\how_to_organize_step.png" width="200"/>

    - You may choose to organize the files one-by-one or move the files all at once. 
        <img src="image\one_by_one.png" width="200"/>

    - If you choose to move one by one, you will go through each file and confirm the move
        <img src="image\undoandconfirm.png" width="200"/>

7. Your files will be organized into predefined folders!


## Appendix
Python Software Foundation. “os — Miscellaneous Operating System Interfaces.” Python 3.10.1 Documentation, 26 Mar. 2023, https://docs.python.org/3/library/os.html.

Python Software Foundation. “shutil — High-Level File Operations.” Python 3.10.1 Documentation, 26 Mar. 2023, https://docs.python.org/3/library/shutil.html.

Python Software Foundation. “pathlib — Object-Oriented Filesystem Paths.” Python 3.10.1 Documentation, 26 Mar. 2023, https://docs.python.org/3/library/pathlib.html.

## Contributing
We welcome contributions to the project. If you find a bug or have a suggestion for improvement, please report it by opening an issue on the project's GitHub page. If you would like to make a change to the code, please fork the repository, make your changes, and submit a pull request. We will review your changes and merge them if they are appropriate.
 

