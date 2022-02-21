# Specialization: Google IT Automation with Python
# Course 02: Using Python to Interact with the Operating System
# Week 6 Module Part 3 Video Example 02
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# While Loops in Bash Scripts
# Filename: rename.sh

#!/bin/bash

for file in *HTM; do
    name=$(basename "$file" .HTM)
    # echo mv "$file" "$name.html"
    mv "$file" "$name.html"
done