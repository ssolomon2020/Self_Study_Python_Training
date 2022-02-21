# Specialization: Google IT Automation with Python
# Course 02: Using Python to Interact with the Operating System
# Week 6 Module Part 2 Video Example 02
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# Using Variables and Globs

#!/bin/bash
line="------------------------------" # <-- Unlike python, variables are defined without white spaces between the equal signs.
echo "Starting at: $(date)" ;echo $line # <-- the line variable is called with a $ before it. This string will be used to separate the information.

echo "UPTIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "WHO"; who; echo $line

echo "Finishing at: $(date)"