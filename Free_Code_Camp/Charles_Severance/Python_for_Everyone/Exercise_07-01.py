# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Student           : Shawn Solomon                                         #
# Date              : 12/26/2021                                            #
# Course            : Scientific Computing with Python: Python For Everyone #
# Instructor        : Chuck Severence                                       #
# Exercise          : #07-01                                                #
# Video             : https://www.youtube.com/watch?v=il1j4wkte2E           #
# Learning Platform : www.freecodecamp.org                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# The program will start after the script begins its run.
# This script demonstrates how to store a string in a variable from file and manipulate it with methods in a for loop.

# Create and set variable to the entire string retrieved from file by the 'open()' function.
fh = open('text_07-01.txt')
# Print variable 'fh' to test. Remove comment mark to test.
# print(fh)

# Start for loop of 'lx' in 'fh'
for lx in fh :
    # Create variable 'ly' and set it to the variable 'lx' with the 'rstrip()' method applied.
    ly = lx.rstrip()
    # Print variable 'ly' with the 'upper()' method applied to print in all caps.
    print(ly.upper())

# The program will end and return to the normal CLI cursor.
# End of script.