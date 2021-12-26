# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Student           : Shawn Solomon                                         #
# Date              : 12/26/2021                                            #
# Course            : Scientific Computing with Python: Python For Everyone #
# Instructor        : Chuck Severence                                       #
# Exercise          : #06-05                                                #
# Video             : https://www.youtube.com/watch?v=1bSqHot-KwE           #
# Learning Platform : www.freecodecamp.org                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# The program will start after the script begins its run.
# This script's purpose is to demonstrate how to pull data from a string, turn it into a float, and print it's value.

# Create variable 'str' and set its value to the string 'X-DSPAM-Confidence: 0.8475' for this find function demonstration.
str = 'X-DSPAM-Confidence: 0.8475  '

# Create variable 'ipos' and set its value to the position of ':' with the 'find()' function applied to the 'str' variable. 
ipos = str.find(':')

# Test 'ipos' variable. Remove comment mark below to test.
# print(ipos) 

# Create and set variable 'piece' to the sum of value of 'ipos' and floating point of '2' with in the 'str' variable. Not sure why the colon needs to be there. It just does or the value is '0'.
piece = str[ipos+2:]

# Test 'piece' variable. Remove comment mark below to test.
# print(piece) 

# Test will fail due to concatenation of string and float mismatch Remove comment ark below to Test.
# print(piece+42.0) 

# Create and set the variable 'value' with the floating point of the 'piece' variable.
value = float(piece)
# Print the value of the variable 'value'
print(value)

# Test concatenation of float variable 'value' and 42.0. Remove comment mark below to test.
# print(value+42.0) 

# The program will end and return to the normal CLI cursor.
# End of script.