# Specialization: Google IT Automation with Python
# Course 02: Using Python to Interact with the Operating System
# Week 3 Module Part 2 Exercise 03
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# The repeating_letter_a function checks if the text passed includes the letter "a" 
# (lowercase or uppercase) at least twice. For example, repeating_letter_a("banana") 
# is True, while repeating_letter_a("pineapple") is False. Fill in the code to make 
# this work. 

# import re
# def repeating_letter_a(text):
#   result = re.search(r"___", text)
#   return result != None
#
# print(repeating_letter_a("banana")) # True
# print(repeating_letter_a("pineapple")) # False
# print(repeating_letter_a("Animal Kingdom")) # True
# print(repeating_letter_a("A is for apple")) # True

import re
def repeating_letter_a(text):
  result = re.search(r"[aA]+.*[aA]+", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True