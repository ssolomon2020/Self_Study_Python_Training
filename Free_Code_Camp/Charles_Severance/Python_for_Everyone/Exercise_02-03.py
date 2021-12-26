# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Student           : Shawn Solomon                               #
# Date              : 12/25/2021                                  #
# Course            : Python For Everyone                         #
# Instructor        : Chuck Severence                             #
# Exercise          : #02-03                                      #
# Video             : https://www.youtube.com/watch?v=wgkC8SxraAQ #
# Learning Platform : www.freecodecamp.org                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# The program will start after script begins run.

# Call the print function to print the string 'Welcome to the Gross Pay Calculator!' in the CLI buffer after run start.
print("Welcome to the Gross Pay Calculator!")
# Create the variable 'p_hours' and set it as an input function. Function will run and print the string 'Please enter the hours worked this pay period: ' in the CLI and wait for user input to set the variable after pressing enter.
p_hours = input("Please enter the hours worked this pay period: ")
# Create the variable 'p_rate' and set it as an input function. Function will run and print the string 'Please enter the hourly rate: ' in the CLI and wait for user input to set the variable after pressing enter.
p_rate =  input("Please enter the hourly rate: ")
#Create the variable 'p_gross' and set it as the product of the variables stored in p_hours and p_rate within the float function to convert the string variables to floating point numerics.
p_gross = float(p_hours) * float(p_rate)
# Call the print function to print the string 'Gross pay: ' with the product contained in the variable 'p_gross' in the CLI buffer.
print("Gross pay: ", p_gross)

# The program will end and return to the normal CLI cursor.
