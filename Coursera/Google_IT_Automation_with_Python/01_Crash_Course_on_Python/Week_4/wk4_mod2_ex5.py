# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 4 Module Part 2 Exercise 05
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. 
# Fill in the blanks in the function, using list comprehension. 
# Hint: remember that list and range counters start at 0 and end at the limit minus 1.

# def odd_numbers(n):
#     return [x for x in ___ if ___]
# 
# print(odd_numbers(5))  # Should print [1, 3, 5]
# print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
# print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
# print(odd_numbers(1))  # Should print [1]
# print(odd_numbers(-1)) # Should print []

def odd_numbers(n):
	return [x for x in range(1, n + 1) if x %2 == 1 ]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []