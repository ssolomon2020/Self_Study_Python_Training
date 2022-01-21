# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 5 Module Part 2 Exercise 01
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# OK, now it’s your turn! Have a go at writing methods for a class.
# Create a Dog class with dog_years based on the Piglet class shown before (one human year is about 7 dog years).

# class Dog:
#   years = 0
#   __
# 
# fido=Dog()
# fido.years=3
# print(fido.dog_years())

class Dog:
    years = 0
    def dog_years(self):
        dy = self.years * 7
        return dy
    
fido=Dog()
fido.years=3
print(fido.dog_years())