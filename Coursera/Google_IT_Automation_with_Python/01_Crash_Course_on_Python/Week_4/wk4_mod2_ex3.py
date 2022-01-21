# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 4 Module Part 2 Exercise 03
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# Let's use tuples to store information about a file: its name, its type and its size in bytes. 
# Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 
# 2 decimal places.

# def file_size(file_info):
#     ___, ___, ___= file_info
#     return("{:.2f}".format(___ / 1024))
#
# print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
# print(file_size(('Notes', 'txt', 496))) # Should print 0.48
# print(file_size(('Program', 'py', 1239))) # Should print 1.21


def file_size(file_info):
	na, ty, si = file_info          #! <-- The first 2 variables of the tuple are not being accessed.
	return("{:.2f}".format(si / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21