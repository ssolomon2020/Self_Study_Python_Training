# Specialization: Google IT Automation with Python
# Course 02: Using Python to Interact with the Operating System
# Week 6 Module Part 2 Video Example 01
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# Creating Bash Scripts

#!/bin/bash

echo "Starting at: $(date)" # <-- # Linux shell command echo prints to the CLI output
echo # <-- Empty echo commands creates an empty new line in the CLI output

echo "UPTIME"
uptime # <-- Linux shell command uptime for system uptime metrics
echo

echo "FREE"
free # <-- Linux shell command free for memory usage metrics
echo

echo "WHO"
who # <-- Linux shell command who for users logged in.
echo

echo "Finishing at: $(date)" # <-- $() calls a shell command within the string. The shell command date displays todays date and time.


# New lines can also be represented by semi-colons as shown below in the commented example.

# echo "Starting at: $(date)" ;echo
#
# echo "UPTIME"; uptime; echo
#
# echo "FREE"; free; echo
#
# echo "WHO"; who; echo
#
# echo "Finishing at: $(date)"