# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 3 Module Part 1 Exercise 02
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# In this code, there's an initialization problem that's causing our function to behave incorrectly. Can you find the problem and fix it?

# def count_down(start_number):
#     while (current > 0):
#         print(current)
#         current -= 1
#     print("Zero!")
#
# count_down(3)

def count_down(start_number):
    current = start_number #! <-- The variable current was not initialized beforehand.
    while (current > 0):
        print(current)
        current -= 1
    print("Zero!")

count_down(3)