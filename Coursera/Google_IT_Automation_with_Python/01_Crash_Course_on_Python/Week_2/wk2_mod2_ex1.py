# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 2 Module Part 2 Exercise 01
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# Do you think you can flesh out your own function? I think you can! Let’s give it a go. 

# Flesh out the body of the print_seconds function so that it prints the total amount of seconds given the hours, minutes, and seconds function parameters.
# Remember that there are 3600 seconds in an hour and 60 seconds in a minute.

# def print_seconds(hours, minutes, seconds):
#     print(___)

# print_seconds(1,2,3)

def print_seconds(hours, minutes, seconds):
    print(hours * 3600)
    print(minutes * 60)
    print(seconds)

print_seconds(1,2,3)