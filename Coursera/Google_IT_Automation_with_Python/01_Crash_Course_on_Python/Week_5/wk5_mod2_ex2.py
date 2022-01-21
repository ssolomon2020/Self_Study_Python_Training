# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 5 Module Part 2 Exercise 02
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# Want to see this in action?
# In this code, there's a Person class that has an attribute name, which gets set when constructing 
# the object. Fill in the blanks so that 1) when an instance of the class is created, the attribute 
# gets set correctly, and 2) when the greeting() method is called, the greeting states the assigned name.

# class Person:
#     def __init__(self, name):
#         self.name = ___
#     def greeting(self):
#         # Should return "hi, my name is " followed by the name of the Person.
#         return ___ 

# # Create a new instance with a name of your choice
# some_person = ___  
# # Call the greeting method
# print(some_person.___)

class Person:
  def __init__(self, name):
    self.name = name
  def greeting(self):
    # Should return "hi, my name is " followed by the name of the Person.
    return "hi, my name is {}".format(self.name)

# Create a new instance with a name of your choice
some_person = Person("Nobody")  
# Call the greeting method
print(some_person.greeting())