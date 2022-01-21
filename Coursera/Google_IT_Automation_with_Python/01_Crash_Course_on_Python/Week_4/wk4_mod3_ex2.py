# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 4 Module Part 3 Exercise 02
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# Now, it's your turn! Have a go at iterating over a dictionary!
# Complete the code to iterate through the keys and values of the cool_beasts dictionary. 
# Remember that the items method returns a tuple of key, value for each element in the dictionary.

# cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
# for ___ in cool_beasts.items():
#     print("{} have {}".format(___))

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for k, v in cool_beasts.items():
    print("{} have {}".format(k, v))