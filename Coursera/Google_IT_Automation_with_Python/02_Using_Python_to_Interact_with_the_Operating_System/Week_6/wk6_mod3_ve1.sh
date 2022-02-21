# Specialization: Google IT Automation with Python
# Course 02: Using Python to Interact with the Operating System
# Week 6 Module Part 3 Video Example 01
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# While Loops in Bash Scripts
# Filename: retry.sh

#!/bin/bash

n=0
command=$1
while ! $command && [ $n -le 5 ]; do
    sleep $n
    ((n=n+1))
    echo "Retry #$n"
done;