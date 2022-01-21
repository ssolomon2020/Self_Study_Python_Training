# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 4 Module Part 2 - Practice Quiz
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# Scripting examples encountered during the Module Part 2 Practice Quiz:

# 01. Given a list of filenames, we want to rename all the files with extension 
# hpp to the extension h. To do this, we would like to generate a new list called 
# newfilenames, consisting of the new filenames. Fill in the blanks in the code 
# using any of the methods you’ve learned thus far, like a for loop or a list comprehension.

# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# # Generate newfilenames as a list containing the new filenames
# # using as many lines of code as your chosen method requires.
# ___  
# 
# print(newfilenames) 
# # Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for file in filenames:
    pos = file.find(".hpp")
    if pos >= 0:
        file = file[0: pos]
        file = file + ".h"
        newfilenames.append(file)
    else:
        newfilenames.append(file)


print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


# 02. Let's create a function that turns text into pig latin: a simple text transformation that 
# modifies each word moving the first character to the end and appending "ay" to the end. For example, 
# python ends up as ythonpay.

# def pig_latin(text):
#     say = ""
#     # Separate the text into words
#     words = ___
#     for word in words:
#         # Create the pig latin word and add it to the list
#         ___
#         # Turn the list back into a phrase
#     return ___
#		
# print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    word = word[1:] + word[0] + "ay "
    say = say + word
    # Turn the list back into a phrase
  return say
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"


# 03. The permissions of a file in a Linux system are split into three sets of three permissions: 
# read, write, and execute for the owner, group, and others. Each of the three values can be expressed 
# as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. 
# Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.
# 
# For example: 
# 640 is read/write for the owner, read for the group, and no permissions for the others; 
# converted to a string, it would be: "rw-r-----"
# 755 is read/write/execute for the owner, and read/execute for group and others; 
# converted to a string, it would be: "rwxr-xr-x"
# Fill in the blanks to make the code convert a permission in octal format into a string format.

# def octal_to_string(octal):
#     result = ""
#     value_letters = [(4,"r"),(2,"w"),(1,"x")]
#     # Iterate over each of the digits in octal
#     for ___ in [int(n) for n in str(octal)]:
#         # Check for each of the permissions values
#         for value, letter in value_letters:
#             if ___ >= value:
#                 result += ___
#                 ___ -= value
#             else:
#                 ___
#     return result
#    
# print(octal_to_string(755)) # Should be rwxr-xr-x
# print(octal_to_string(644)) # Should be rw-r--r--
# print(octal_to_string(750)) # Should be rwxr-x---
# print(octal_to_string(600)) # Should be rw-------

def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for digit in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if digit >= value:
                result += letter
                digit -= value
            else:
                result += "-"
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------


# 05. The group_list function accepts a group name and a list of members, and returns a string with 
# the format: group_name: member1, member2, … For example, group_list("g", ["a","b","c"]) returns 
# "g: a, b, c". Fill in the gaps in this function to do that.

# def group_list(group, users):
#     members = ___
#     return ___
# 
# print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
# print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
# print(group_list("Users", "")) # Should be "Users:"

def group_list(group, users):
  members = ""
  for user in users:
    members = members + user + ", "
  members = members.rstrip(", ")
  return "{} : {}".format(group, members)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"


# 06. The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, 
# and prints the sentence "Guest is X years old and works as __." for each one. 
# For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: 
# Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works 
# as Engineer. Fill in the gaps in this function to do that.

# def guest_list(guests):
#         for ___:
#         ___
#         print(___.format(___))
# 
# guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
# 
# #Click Run to submit code
# """
# Output should match:
# Ken is 30 years old and works as Chef
# Pat is 35 years old and works as Lawyer
# Amanda is 25 years old and works as Engineer
# """

def guest_list(guests):
	for guest in guests:
		name, age, work = guest
		print("{} is {} years old and works as {}".format(name, age, work))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""