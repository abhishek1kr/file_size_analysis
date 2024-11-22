Python project scans a directory for files larger than 1GB, generates a PDF report listing the large files, and provides an option to preview the report.

#Features

Recursively scans a selected directory for files larger than 1GB.
Generates a PDF report with the file paths and sizes.
Supports pagination for long reports.
Allows the user to preview the generated PDF.

#Installation
1.Clone the repository
2.Install the required dependencies

#Usage
1.Run the script
2.Follow the GUI prompts to:
-Select a directory to scan.
-Save the generated PDF report.
-Optionally, preview the PDF report.

#How It Works
1.Directory Selection: The program opens a dialog to choose a directory.
2.File Scanning: It searches for files larger than 1GB in the selected directory and its subdirectories.
3.PDF Generation: A PDF report is created listing the large files and their sizes.
4.Report Preview: You can open the PDF in your default viewer.

#Dependencies
Python: Ensure Python 3.6 or later is installed.

Required Libraries:
- tkinter: For GUI dialogs (comes with Python).
- reportlab: For generating PDF reports.
- webbrowser: For previewing the PDF.

#Author

Abhishek Kumar
Feel free to connect.



