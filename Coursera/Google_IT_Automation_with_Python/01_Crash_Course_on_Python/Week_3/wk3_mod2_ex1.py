# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 3 Module Part 2 Exercise 01
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# Want to try this out? Let's give it a go!

# Fill in the gaps of the sum_squares function, so that it returns the sum of all the squares
# of numbers between 0 and x (not included). Remember that you can use the range(x) function to
# generate a sequence of numbers from 0 to x (not included).

# def square(n):
#     return n*n
# 
# def sum_squares(x):
#     sum = 0
#     for n in ___:
#         sum += __
#     return __
# 
# print(sum_squares(10)) # Should be 285

def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n) #! <-- Can call other user defined functions within a user defined function.
    return sum

print(sum_squares(10)) # Should be 285