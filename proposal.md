# Project Proposal for "File Organizer"
## The Big Idea
The "File Organizer'' project is designed to address the common problem of file clutter and disorganization on personal computers. The program uses Python to develop a command-line interface to automate the process of organizing files into predefined categories, such as pictures, documents, and video files. By recognizing file types through their extensions, the program streamlines the task of file organization for users, ultimately saving them time and effort. 

To achieve this functionality, the project will explore various topics in Python, such as file handling, directory management, and regular expressions. These topics will be leveraged in conjunction with libraries like os and shutil to move files to appropriate folders based on their types. Additionally, the program will include a user interface that simplifies the process of selecting which files to organize and where to move them. 

The minimum viable product for this project will include a functional program capable of recognizing and organizing files into pre-defined categories. However, there are several stretch goals that could enhance the program's usability and effectiveness. For example, one stretch goal could be to classify documents into sub-folders based on their content, such as work-related or personal documents. Another stretch goal could be to provide the option for users to confirm or undo file moves, further enhancing the user experience. 

Overall, the "File Organizer" project is intended to provide a practical solution for file organization using Python, giving users greater control over their digital files. By automating the process of file organization, the program saves users time and effort while also exploring several relevant topics in Python and offering a range of features to enhance the user experience.

***
## Learning Objectives
Through this project, our group wants to explore several Python skills and topics, such as file handling, directory management, and regular expressions. These topics are relevant to our project as they provide the foundation for our program’s functionality, which can be used to automate the process of file organization. In addition, we would also like to gain a better understanding of how to use the os and shutil libraries in Python, which can be used for file management. These libraries allow us to handle files and manage directories on computers. They also provide a range of functions, such as creating and deleting directories, copying and moving files, and listing directory contents. Thus, we would be able to enhance our knowledge of those topics by implementing and exploring these concepts and libraries in our project. 
***
## Implementation Plan
### Implement File Recognition and Organization Logic
>Identify File Extensions and Types
>>To automate the process of file organization, it is necessary to identify file extensions and types. This can be done using Python's mimetypes module, which maps filename extensions to MIME types. A list of file extensions can be defined for each file type, allowing the program to recognize and categorize files based on their extensions.

>Define Categories for File Organization
>>The next subtask is to define categories for file organization. This involves creating pre-defined categories for organizing files, such as pictures, documents, and video files. The os.path module can be used to create directories and subdirectories for each category. Additionally, the configparser module can be used to allow users to create custom categories.

>Write Logic to Move Files to Appropriate Categories
>>Once the file extensions and categories have been defined, it is necessary to write logic to move files to appropriate categories. This can be done using Python's os and shutil modules, which provide functions for moving files and directories. For example, the os.rename() function can be used to move files to a new directory, while shutil.copyfile() can be used to make a copy of a file in a different directory.

### Improve User Experience
After accomplishing the basic functionality of our program, we will implement the following stretch goals(note: due to time limit, we cannot ensure all the stretched goals will be met.):
>Add Ability to Confirm or Undo File Moves
>>To enhance the user experience, it may be helpful to add the ability to confirm or undo file moves. This allows users to preview file moves before they are executed, and to undo moves if necessary. Python's input() function can be used to prompt users to confirm or undo file moves, while the os.rename() function can be used to undo a file move.

>Stretch Goal: Classify Documents into Sub-Folders Based on Content
>>As a stretch goal, it may be possible to classify documents into sub-folders based on their content. This involves using machine learning algorithms to analyze the content of documents and classify them into categories such as work-related or personal documents. Python's scikit-learn, pandas, and NumPy libraries can be used to build and train machine learning models for document classification.

### Testing and Debugging
>Test Program with Various File Types and Folder Structures
>>To ensure that the "File Organizer" program works as intended, it is important to test it with various file types and folder structures. This involves creating test cases for different types of files, such as pictures, documents, and video files, and testing the program's ability to recognize and categorize them correctly. The unittest and pytest modules can be used to create and run test cases.

>Debug Any Issues That Arise During Testing
>>During testing, it is possible that issues may arise that require debugging. For example, the program may fail to recognize a particular file type, or it may move files to the wrong category. Python's logging module can be used to log errors and debug messages, making it easier to identify and fix issues.

### Documentation
>Write Clear and Concise Documentation for Program 
>>To make the "File Organizer" program accessible to users, it is important to write clear and concise documentation for its functionality. This involves documenting the program's features and usage, as well as providing examples of input/output and expected results. Tools such as Sphinx, MkDocs, and Read the Docs can be used to generate documentation in various formats, such as HTML and PDF. In addition to documenting the program's functionality, it is important to provide instructions for its use. This includes creating a user guide or manual that explains how to install and run the program, as well as how to use its various features. Sphinx, MkDocs, and Read the Docs can also be used to generate user guides or manuals. To help users understand how to use the "File Organizer" program, it is helpful to provide examples of usage and expected results. This can be done using tools such as doctest, unittest, and pytest, which allow developers to create test cases and examples of usage that can be included in documentation.
## Project Schedule
Once our project proposal gets approved, we will begin our project. We will have roughly 3.5 weeks to accomplish this project. The timeline of our project will follow the implementation plan we provided in the above section. 

Our project schedule is as follows:
- Week 1: Develop file organizer with baseline functionalities, which is to organize files based on file extensions.
- Week 2: Implement the strech goal of organizing documents based on the content. 
- Week 3: Write README files for instruction purposes. Improve user interface and experience, implement other stretch goals if time permits

Testing and debugging, documentation, and website formation will be done throughout the three weeks.
***
## Collaboration Plan
As this is a team project, it is important that all members of the team understand the goal as well as the implementation of the program. It is also important for both of us to be responsible and accountable for accomplishing the required or pre-defined tasks. We will be dividing and accomplishing the work relatively evenly. Additionally, we will also communicate regularly and effectively to avoid any confusion and to keep each other updated on the progress. We believe that this will ensure an effective team collaboration. 

Detailed work distribution:
Week1: Katarina will give the first draft of the project with baseline functionlaities. Angela and Katarina will be elborating on the first draft.

Week2: Katarina is responsible for identifying documents for work purposes; Angela is responsible for identifying documents for entertainment purposes.

Week3: Katarina and Angela together works on the README file and see how the user interface can be improved if time permits.
***
## Risks and Limitations
The most significant threat to this project’s success would be learning the various Python libraries and tools that are necessary for this project. Since this is a relatively new topic and concept to both of us, it would require a lot of research in order to successfully implement all the functionalities in our program. In addition, the time that is available for us to accomplish this project is also very limited as we only have roughly about 3.5 weeks to complete the program as well as the project website. The process of classifying documents based on their content is forseen to be difficult and take longer time to accomplish. 
***
## Additional Course Content
The most crucial topic for our project would be os and shutil, which are important libraries for working with files and directories on computers. In addition, various machine-learning libraries would also be helpful, which would aid us in implementing the function to classify documents based on their content. 