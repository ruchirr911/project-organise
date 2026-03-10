# AI File Organizer

This **AI-powered file organization tool** that automatically sorts files
in a directory based on a natural language prompt from the user.

The system uses a language model to understand how the user wants files
to be organized and then moves the files into appropriate folders.

This project is currently capable of **sorting files based on their
filenames**.\
A **content-aware renaming system** is currently under development.

------------------------------------------------------------------------

# How to run?

- Insert your personal groq API key in 'main.py' that you can generate from here: https://console.groq.com/keys
- Run the 'run.py' file

------------------------------------------------------------------------

# Project Overview

Many folders become cluttered because files have unclear or inconsistent
names.

This project attempts to solve that problem by combining:

-   Python filesystem automation
-   Large Language Models
-   Natural language prompts

Users can simply describe **how they want their files organized**, and
the system will automatically create folders and move the files
accordingly.

Example user prompt:

    separate screenshots and distribute other types of files accordingly

The program then analyzes the file names and categorizes them
appropriately.

------------------------------------------------------------------------

# Current Features

-   Reads files from a user-specified directory
-   Filters out folders and hidden files
-   Uses an AI model to categorize files
-   Automatically creates folders if they do not exist
-   Moves files into appropriate folders
-   Allows natural language instructions for organization

------------------------------------------------------------------------

# Planned Features

The next major feature currently under development is **AI-based file
renaming**.

Many files have poor names such as:

    IMG_2048.png
    file1.pdf
    Screenshot 2024-01-05.png

The planned system will:

1.  Detect poorly named files
2.  Read a small portion of their content
3.  Generate a meaningful filename using AI
4.  Rename the file before sorting

Example transformation:

    IMG_2048.png

→

    transistor_amplifier_circuit.png

This will significantly improve the quality of the sorting system.

------------------------------------------------------------------------

# Project Structure

    project_organise/
    │
    ├── input.py
    ├── main.py
    ├── run.py
    └── README.md

------------------------------------------------------------------------

# File Explanations

## input.py

This module is responsible for **collecting user input** required to run
the program.

It typically includes:

-   The **path of the folder** to organize
-   The **user prompt** describing how files should be organized

Example responsibilities:

-   Prompt user for directory path
-   Prompt user for sorting instructions
-   Provide these values to other modules

------------------------------------------------------------------------

## main.py

This file contains the **core AI sorting logic**.

The primary function implemented here is:

### sorter()

This function performs the AI-based categorization of files.

Inputs:

-   folder path
-   user prompt

Responsibilities:

1.  Collect the list of files
2.  Send filenames and instructions to the AI model
3.  Receive categorized JSON output
4.  Return structured categories for use by the moving logic

Example expected AI output:

``` json
{
 "Images": ["photo.png", "diagram.jpg"],
 "Documents": ["notes.pdf"],
 "Code": ["script.py"]
}
```

This structured data is then used by the program to move files.

------------------------------------------------------------------------

## run.py

This file acts as the **execution script** of the project.

It performs the physical file system operations.

Responsibilities:

1.  Import user inputs
2.  Call the sorter function
3.  Create folders if needed
4.  Move files into their corresponding folders

Example operations:

    Images/
    Documents/
    Code/

Files are moved using Python's filesystem utilities.

------------------------------------------------------------------------

# Workflow of the System

The current workflow of the program is shown below.

    User Input
        │
        ▼
    input.py
        │
        ▼
    main.py (sorter function)
        │
        │ sends filenames + instructions to AI
        ▼
    AI Model
        │
        │ returns categorized JSON
        ▼
    run.py
        │
        │ creates folders
        │ moves files
        ▼
    Organized Directory

------------------------------------------------------------------------

# Example Execution Flow

Example directory before running the program:

    Downloads/
    │
    ├── IMG_1023.png
    ├── thermodynamics_notes.pdf
    ├── screenshot1.png
    ├── code.py

User prompt:

    separate screenshots and distribute other files accordingly

Directory after execution:

    Downloads/
    │
    ├── Screenshots/
    │   └── screenshot1.png
    │
    ├── Images/
    │   └── IMG_1023.png
    │
    ├── Documents/
    │   └── thermodynamics_notes.pdf
    │
    └── Code/
        └── code.py

------------------------------------------------------------------------

# Future System Workflow (Planned)

Once the **AI renaming feature** is implemented, the workflow will look
like this:

    Scan Directory
         │
         ▼
    Detect Bad Filenames
         │
         ▼
    Extract File Content
         │
         ▼
    AI Rename
         │
         ▼
    AI Categorization
         │
         ▼
    Move Files

This will allow the system to organize files **even when filenames are
poor or unclear**.

------------------------------------------------------------------------

# Technologies Used

-   Python
-   Groq API
-   Large Language Models
-   JSON processing
-   Python filesystem utilities

------------------------------------------------------------------------

# Why This Project Exists

File management is still largely manual and tedious.

This project explores how **AI can automate personal file
organization**, allowing users to describe their intent in natural
language rather than manually sorting files.

------------------------------------------------------------------------

# Current Status

-   Sorting functionality: Complete
-   AI categorization: Working
-   Content-aware renaming: In progress

------------------------------------------------------------------------

# Future Improvements

Potential improvements include:

-   Content-aware renaming
-   OCR support for images
-   PDF content analysis
-   Smart duplicate detection
-   GUI interface
-   Batch processing for large directories

------------------------------------------------------------------------

# Cons

1) Does not work properly for some certain mac files
2) The folder must not contain any subfolder

------------------------------------------------------------------------

# Author

Developed as a learning project exploring **AI-driven automation and
file management systems**.
