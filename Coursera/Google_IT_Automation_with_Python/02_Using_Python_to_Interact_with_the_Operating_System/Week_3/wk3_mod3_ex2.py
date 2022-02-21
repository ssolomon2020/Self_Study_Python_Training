# Specialization: Google IT Automation with Python
# Course 02: Using Python to Interact with the Operating System
# Week 3 Module Part 3 Exercise 02
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# The long_words function returns all words that are at least 7 characters. Fill in 
# the regular expression to complete this function.

# import re
# def long_words(text):
#   pattern = ___
#   result = re.findall(pattern, text)
#   return result
#
# print(long_words("I like to drink coffee in the morning.")) # ['morning']
# print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
# print(long_words("I never drink tea late at night.")) # []

import re
def long_words(text):
  pattern = r"\w{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []