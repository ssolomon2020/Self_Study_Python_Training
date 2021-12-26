# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Student           : Shawn Solomon                                         #
# Date              : 12/25/2021                                            #
# Course            : Scientific Computing with Python: Python For Everyone #
# Instructor        : Chuck Severence                                       #
# Exercise          : #03-02                                                #
# Video             : https://www.youtube.com/watch?v=KJN3-7HH6yk           #
# Learning Platform : www.freecodecamp.org                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# The program will start after the script begins its run.

# Call the print function to print the string 'Welcome to the Gross Pay Calculator!' in the CLI buffer after run start.
print("Welcome to the Gross Pay Calculator!")
# Create the variable 'p_hours' and set it as an input function. Function will run and print the string 'Please enter the hours worked this pay period: ' in the CLI and wait for user input to set the variable after pressing enter.
p_hours = input("Please enter the hours worked this pay period: ")
# Create the variable 'p_rate' and set it as an input function. Function will run and print the string 'Please enter normal the hourly rate: ' in the CLI and wait for user input to set the variable after pressing enter.
p_rate =  input("Please enter the normal hourly rate: ")

# Try variables as floats.
try :
    float(p_hours)
    float(p_rate)
# If not, run the except statement.
except :
    # Print error message.
    print("Error: Please enter numeric inputs")
    # Quit the program.
    quit()
    # The program will end and return to the CLI cursor.

# If p_hours > 40 is true, then run the if statement for regular and over-time pay calculation.
if float(p_hours) > 40 :
    # Create and set variable to the diffrence of the floating point value of 'p_hours' and 40. 
    op_hours = float(p_hours) - 40
    # Set the variable 'p_hours' to the floating point value of 40.
    p_hours = float(40)
    # Create the variable 'p_gross' and set it as the product of the variables stored in 'p_hours' and 'p_rate' within the float functions to convert the string variables to floating point numerics.
    p_gross = float(p_hours) * float(p_rate)
    # Create the variable 'op_gross' and set it as the product of the variables stored in 'op_hours' and ('op_rate'*1.5) within the float functions to convert the string variables to floating point numerics.
    op_gross = float(op_hours) * (float(p_rate) * 1.5)
    # Call the print function to print the string 'Gross pay with over-time: ' with the sum of the values contained in the variables 'op_gross' and 'p_hours' in the CLI buffer.
    print("Gross pay with over-time: $", op_gross + p_gross)

    print('Regular: $',p_gross , ' Over-time: $', op_gross)

# If p_hours > 40 is false, then run the else statement for regular pay calculation.
else :
    # Create the variable 'p_gross' and set it as the product of the variables stored in 'p_hours' and 'p_rate' within the float functions to convert the string variables to floating point numerics.
    p_gross = float(p_hours) * float(p_rate)
    # Call the print function to print the string 'Gross pay: ' with the product contained in the variable 'p_gross' in the CLI buffer.
    print("Gross pay:", p_gross)

# The program will end and return to the normal CLI cursor.