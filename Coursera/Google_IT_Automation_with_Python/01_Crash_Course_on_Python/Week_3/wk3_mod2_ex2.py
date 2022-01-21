# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 3 Module Part 2 Exercise 02
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# In math, the factorial of a number is defined as the product of an integer and all
# the integers below it. For example, the factorial of four (4!) is equal to 1*2*3*4=24. 
# Fill in the blanks to make the factorial function return the right number.

# def factorial(n):
#     result = 1
#     for i in ___:
#         __
#     return result
# 
# print(factorial(4)) # should return 24
# print(factorial(5)) # should return 120

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = i * result
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120