# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 5 Module Part 3 Exercise 01
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# Let’s create a new class together and inherit from it. Below we have a base class called Clothing. 
# Together, let’s create a second class, called Shirt, that inherits methods from the Clothing class. 
# Fill in the blanks to make it work properly.

# class Clothing:
#   material = ""
#   def __init__(self,name):
#     self.name = name
#   def checkmaterial(self):
# 	  print("This {} is made of {}".format(self.___,self.___))
			
# class Shirt(___):
#   material="Cotton"

# polo = Shirt("Polo")
# polo.checkmaterial()

class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name,self.material))
			
class Shirt(Clothing):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()