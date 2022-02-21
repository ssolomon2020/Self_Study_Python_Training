# Specialization: Google IT Automation with Python
# Course 02: Using Python to Interact with the Operating System
# Week 3 Module Part 3 Exercise 01
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# Fix the regular expression used in the rearrange_name function so that it can match 
# middle names, middle initials, as well as double surnames.

# import re
# def rearrange_name(name):
#   result = re.search(r"^(\w*), (\w*)$", name)
#   if result == None:
#     return name
#   return "{} {}".format(result[2], result[1])
#
# name=rearrange_name("Kennedy, John F.")
# print(name)

import re
def rearrange_name(name):
  result = re.search(r"^(\w*), ([\w \.]*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)