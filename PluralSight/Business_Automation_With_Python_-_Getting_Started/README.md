Course notes by Shawn Solomon

# Business Automation with Python: Getting Started #
- Course on PluralSight | Web Site: http://www.pluralsight.com
- By: Eduardo Freitas | Web Site: https://edfreitas.me


## I. Course Overview ##

Eduardo is a Software Developer, Data Capture, and Business Automation specialist.

Business automation is a form of robotic process automation, which is a technology based on the notion of software robots and scripts. These scripts can allieviate or replace completely the need for human intervention. In traditional workflow tools, a software developer produces a list of actions to automate, and interfaces to the back end system using various API. In contrast, Business Automation scripts and software robots can perform the same task as a human operator, but at a much faster speed, and with higher accuracy.

Python is a powerful and yet still easy enough programming language to use, advanced business users can use it to automate repetitive tasks without having to be software engineers. This way they can reduce costs by using open source software and avoiding costly commercial solutions.

Some of the major topics covered include: core aspects of Business Automation, file automation tasks, PDF data extraction automation, Salesforce data entry automation, and watching the technologies and principles getting applied.

By the end of this course you'll know the basics of Business Automation using Python, and be able to write code that uses it. Before beginning the the course, you should have some basic knowledge in Python and find your way around Visual Studio Code


## II. File Automation Tasks ##

### 01. Introduction ####

Python is an amazing programming language packed with great features and libraries. It is also great for automating repetative tasks. Python is also super easy to learn, so even if you've never used it before, but have some previous programming experience, You'll be able to follow along and apply some of the techniques in this course through your daily work. Automation is all about having the computer to do the work for you rather than the you working for the computer.


### 02. Overview ###

What is covered:
* What is business Automation?
* File Handling Basics in Python
* Reading and Writing Files in Python
* Copying, Moving and Deleting Files and Folders with Python
* Walking a Directory Tree with Python
* Working and Syncing with an FTP Server
* Handling Zip Archives with Python


### 03. What is Business Automation? ###

Business Automation is - a technology-enabled automation of business processes.
- Note: Be aware that business processes may vary.

Why use Python?
* Simple to use, mature, and growing.
    An amazing programming language and is easy to get started with.
    
* Can complete tasks with less lines of code.
    It allows you as a developer to write code in a clean and organized way, requiring fewer lines of code.

* Open source and flexible, with large enthusiastic community.
    
* It provides many built-in libraries which do amazing things.
    Note: Before writing code yourself, check if there's already a Python library that does what you want. You'll likely already find a Python library for it.


With that in mind, it is a great choice for writing scripts that accomplish the same repetitive tasks a person would do manually on a computer. A well designed Python script can reduce manual work tremendously.

### 04. What is File Handling Automation? ###

File Handling Automation is - the capability of handling computer files in an automatic way.
  Files and their content can be manipulated and changed without any manual intervention.

What types of file automation tasks can we carry out with Python?
* Read files.
* Write files.
* Copy Files.
* Move files. <br>
        Move files from folder A to folder B.
* Get and retrieve files from an FTP server.
* Archive files. (Zip)

### 05. File Handling Basics ###

A file is made up of a file path and a file name.
- C:\Folder\File.txt

A file has:
  A root directory location
    C:\
  A directory where the file resides
    \Folder
  A file name
    File.txt

On Windows operating systems, file and folder paths are described using the backslash character.
  '\'

On Mac OS, Linux, and Unix-based operating systems, they are described using the forward slash character.
  '/'

This is the same file path on Mac OS, Linux, or Unix.
  /Folder/File.txt

To manipulate files with Python, the OS library needs to be imported which includes OS related methods.
  import os

For programs to work on all operating systems, don't concatenate strings of the path. Instead, use the join method for the file path which will concatonate based on the OS filesystem.
  os.path.join('C:\\Folder', 'File.txt')

You can also get the current working directory for the program stored in an OS file system.
  os.getcwd()

Sometimes it is necessary to change the current working directory with the chdir method to work with another file.
  os.chdir('C:\\Af\\Bf')

If you need to get a directory name of a path, you can call the dirname method.
  os.path.dirname('C:\\Af\\Bf\\')

If you need a path's dirname and basename together, then call the split method to return a tuple value with of each. i.e.: ('C:\\Af','pr.exe')
  os.path.split('C:\\Af\pr.exe')

You can also join the names of two folders into one path with the join method. *i.e.: returning either \foo\fighter or /foo/fighter*
  os.path.join('foo', 'fighter')

You can also assign paths to variables using the = character as an assignment operator. Remember to use variable naming best practices according to the PEP8 style guide.
  c = 'C:\\Windows\\Systems32\\calc.exe'

With the sep method, you can also determine the correct folder separating slash depending on the operating system we are using.
  os.path.sep()

If you split the string and pass the sep as a parameter, it will return a list of each part without the slashes. i.e.: ['C:', 'Windows', 'System32', 'calc.exe']
  c.split(os.path.sep)

You can also call the split method with the sep method as the paramter to split a string directly. *i.e.: ['','usr','bin']*
  '/usr/bin'.split(os.path.sep)

With that done, we can move on to more advanced methods.


### 06. Checking Files and Listing Folder Contents ###

### 07. Reading and Writing Files ###

### 08. Saving Variables ###

### 09. Demo - Reading and Writing a Config File ###

### 10. Copying, Moving, and Deleting Files ###

### 11. Demo - Inspecting a Directory Structure ###

### 12. Working and Syncing with FTP ###

### 13. Handling Zip Archives ###

### 14. Demo - Configurable Backup Script ###

### 15. Summary ###

## III. PDF Data Extraction Automation ##

### 01. Introduction ###

### 02. Overview ###

### 03. Types of PDF Files ###

### 04. PDF File Handling Basics ###

### 05. Demo - Extracting Text and Combining PDFs ###

### 06. Extract Fields from Form-based PDF Files ###

### 07. Demo - Extracting Fields ###

### 08. Summary ###

## IV. Salesforce Data Entry Automation ##

### 01. Introduction ###

### 02. Overview ###

### 03. Automation with Python and Salesforce ###

### 04. Demo - Salesforce Opportunity Web Form ###

### 05. Demo - Form-based PDF for a Salesforce Opportunity ###

### 06. Demo - Browser Script for Automatic Data Entry ###

### 07. Summary ###
