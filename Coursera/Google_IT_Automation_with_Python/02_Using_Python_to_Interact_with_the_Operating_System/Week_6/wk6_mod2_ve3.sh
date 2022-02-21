# Specialization: Google IT Automation with Python
# Course 02: Using Python to Interact with the Operating System
# Week 6 Module Part 2 Video Example 03
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# Conditional Execution in Bash
# Filename: 

#!/bin/bash

if grep "127.0.0.1" /etc/hosts; then
        echo "Everything ok"
else
        echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi # <-- fi ends the if/else block in bash.