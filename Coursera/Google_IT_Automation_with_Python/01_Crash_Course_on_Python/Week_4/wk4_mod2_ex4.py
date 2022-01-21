# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 4 Module Part 2 Exercise 04
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements 
# function to return every other element from the list, this time using the enumerate function to 
# check if an element is on an even position or an odd position.

# def skip_elements(elements):
#     # code goes here
#
#     return ___
#
# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

def skip_elements(elements):
	new_list = []
	for index, item in enumerate(elements):
		if index % 2 == 0:
			new_list.append(item)
		elif index % 2 >= 1:
			continue
	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']