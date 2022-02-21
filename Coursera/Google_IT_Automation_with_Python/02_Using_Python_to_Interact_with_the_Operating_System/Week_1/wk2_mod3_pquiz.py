# Specialization: Google IT Automation with Python
# Course 02: Using Python to Interact with the Operating System
# Week 2 Module Part 3 - Practice Quiz
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# Scripting examples encountered during the Module Part 3 Practice Quiz:

# 01. We're working with a list of flowers and some information about each one. 
# The create_file function writes this information to a CSV file. The contents_of_file 
# function reads this file into records and returns the information in a nicely formatted 
# block. Fill in the gaps of the contents_of_file function to turn the data in the CSV 
# file into a dictionary using DictReader.

# import os
# import csv
#
# # Create a file with data in it
# def create_file(filename):
#   with open(filename, "w") as file:
#     file.write("name,color,type\n")
#     file.write("carnation,pink,annual\n")
#     file.write("daffodil,yellow,perennial\n")
#     file.write("iris,blue,perennial\n")
#     file.write("poinsettia,red,perennial\n")
#     file.write("sunflower,yellow,annual\n")
#
# # Read the file contents and format the information about each row
# def contents_of_file(filename):
#   return_string = ""
#
#   # Call the function to create the file 
#   create_file(filename)
#
#   # Open the file
#   ___
#     # Read the rows of the file into a dictionary
#     ___
#     # Process each item of the dictionary
#     for ___:
#       return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
#   return return_string
#
# #Call the function
# print(contents_of_file("flowers.csv"))

import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # Read the rows of the file into a dictionary
    for row in csv_reader:
    # Process each item of the dictionary
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
    return return_string

#Call the function
print(contents_of_file("flowers.csv"))


# 02. Using the CSV file of flowers again, fill in the gaps of the contents_of_file 
# function to process the data without turning it into a dictionary. How do you skip 
# over the header record with the field names?

# import os
# import csv
#
# # Create a file with data in it
# def create_file(filename):
#   with open(filename, "w") as file:
#     file.write("name,color,type\n")
#     file.write("carnation,pink,annual\n")
#     file.write("daffodil,yellow,perennial\n")
#     file.write("iris,blue,perennial\n")
#     file.write("poinsettia,red,perennial\n")
#     file.write("sunflower,yellow,annual\n")
#
# # Read the file contents and format the information about each row
# def contents_of_file(filename):
#   return_string = ""
#
#   # Call the function to create the file 
#   create_file(filename)
#
#   # Open the file
#   ___
#     # Read the rows of the file
#     rows = ___
#     # Process each row
#     for row in rows:
#       ___ = row
#       # Format the return string for data rows only
#
#           return_string += "a {} {} is {}\n".format(___)
#   return return_string
#
# #Call the function
# print(contents_of_file("flowers.csv"))

import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename, "r") as csv_file:
    reader = csv.reader(csv_file)
    # Read the rows of the file
    rows = reader
    # Process each row
    for row in rows:
      name, color, typ = row
      # Format the return string for data rows only
      if name != "name":
        return_string += "a {} {} is {}\n".format(color, name, typ)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))