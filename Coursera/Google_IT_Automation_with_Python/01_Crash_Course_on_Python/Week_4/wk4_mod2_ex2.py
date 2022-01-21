# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 4 Module Part 2 Exercise 02
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# The skip_elements function returns a list containing every other element from an input list, 
# starting with the first element. Complete this function to do that, using the for loop to 
# iterate through the input list.

# def skip_elements(elements):
#     # Initialize variables
#     new_list = []
#     i = 0
# 
#     # Iterate through the list
#     for ___
#         # Does this element belong in the resulting list?
#         if ___
#             # Add this element to the resulting list
#             ___
#         # Increment i
#         ___
# 
#     return ___
# 
# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
# print(skip_elements([])) # Should be []


def skip_elements(elements):
    # Initialize variables
    new_list = list()
    i = 0
    # Iterate through the list
    while i <= len(elements):
        if len(elements) < 1:
            return new_list
        new_list.append(elements[i])
        # Increment i
        i += 2
    return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []