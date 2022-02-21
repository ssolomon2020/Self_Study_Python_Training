# Specialization: Google IT Automation with Python
# Course 02: Using Python to Interact with the Operating System
# Week 6 Module Part 3 Video Example 03
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# Advanced Command Interaction
# Filename: toploglines.sh

#!/bin/bash

# For every file ending log...
for logfile in /var/log/*log; do
    # Print "Processing log file name"
    echo "Processing: $logfile"
    # The cut command splits lines using a delimiter and print starting with field number 5 and so on.
    # Pipe cut to sort then to uniq to print unique occurrances and count other occurances.
    # Pipe again to sort by number and in reverse order then pipe to head to print the only the first 5 lines and return the stdout. 
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
# Complete the loop after iterations are exhausted.
done