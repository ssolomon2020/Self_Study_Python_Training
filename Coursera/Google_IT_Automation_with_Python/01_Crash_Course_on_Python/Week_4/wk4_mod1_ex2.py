# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 4 Module Part 1 Exercise 02
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# Want to give it a go yourself? Be my guest! Modify the first_and_last function so that it returns 
# True if the first letter of the string is the same as the last letter of the string, False if 
# they’re different. Remember that you can access characters using message[0] or message[-1].
# Be careful how you handle the empty string, which should return True since nothing is equal to nothing.

# def first_and_last(message):
#     return False
# 
# print(first_and_last("else"))
# print(first_and_last("tree"))
# print(first_and_last(""))

def first_and_last(message):
    if message == "":
        return True
    elif message[0] == message[3]:
        return True
    else:
        return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))