# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 4 Module Part 3 Exercise 03
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# In Python, a dictionary can only hold a single value for a given key. To workaround this, 
# our single value can be a list containing multiple values. Here we have a dictionary called 
# "wardrobe" with items of clothing and their colors. Fill in the blanks to print a line for 
# each item of clothing with each color, for example: "red shirt", "blue shirt", and so on.

# wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
# for __:
#     for __:
#         print("{} {}".format(__))

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for item, colors in wardrobe.items():
	for color in colors:
		print("{} {}".format(color, item))