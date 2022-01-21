# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 2 Module Part 3 Exercise 03
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# The number_group function should return "Positive" if the number received is positive,
# "Negative" if it's negative, and "Zero" if it's 0. Can you fill in the gaps to make that happen?

# def number_group(number):
#     if ___:
#         return "Positive"
#     elif ___:
#         return ___
#     else:
#         ___
# 
# print(number_group(10)) #Should be Positive
# print(number_group(0)) #Should be Zero
# print(number_group(-5)) #Should be Negative

def number_group(number):
    if number > 0:
        return "Positive"
    elif number == 0:
        return "Zero"
    else:
        return "Negative"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative