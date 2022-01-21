# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 3 Module Part 1 Exercise 03
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# The following code causes an infinite loop. Can you figure out what’s missing and how to fix it?

# def print_range(start, end):
#     # Loop through the numbers from start to end
#     n = start
#     while n <= end:
#         print(n)
# 
# print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 

def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
		n += 1 #! <-- Counter was initialized but it did not increment beforehand.

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 