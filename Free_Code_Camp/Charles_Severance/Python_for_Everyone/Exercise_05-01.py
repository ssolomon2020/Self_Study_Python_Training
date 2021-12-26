# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Student           : Shawn Solomon                                         #
# Date              : 12/25/2021                                            #
# Course            : Scientific Computing with Python: Python For Everyone #
# Instructor        : Chuck Severence                                       #
# Exercise          : #05-01                                                #
# Video             : https://www.youtube.com/watch?v=kjxXZQw0uPg           #
# Learning Platform : www.freecodecamp.org                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# The program will start after the script begins its run.

# Create variable 'num' and set its value to '0'.
num = 0
# Create variable 'tot' and set its value to '0.0'
tot = 0.0

# Create a loop and run indefinately while expression is True to ask for floating point input values.
while True :
    # Create the variable 'sval' and set it to the user input response to the printed string.
    sval = input('Pick a number: ')
    
    # If the variable 'sval' is equal to the string 'done' or 'Done', break the while loop and run the rest of the script.
    if sval == 'done' :
        break
        # Move on to after the end of the while loop block.
    elif sval == 'Done' :
        break
        # Move on to after the end of the while loop block.
    # End if/elif statement block.

    # Begin 'try' statement to evaluate variable.
    try :
        # Create variable 'fval' and set it's value to the floating point of the current value of 'sval'.
        fval = float(sval)
    # If try statement fails evaluation, run the except statement.
    except :
        # Print error message.
        print('Error: Invalid input. NOT a numeric!!')
        # Return to the start of the while loop statement block and continue.
        continue

    # Print the value of 'fval'.
    print(fval)
    # Set num to calculate the sum of its current value and '1' and store the new value.
    num = num + 1
    # Set tot to calculate sum of its current value and the value of 'fval' and store the new value.
    tot = tot + fval
    # Return to the start of the while loop block.

# End of the while loop block.

# Prevent dividing by zero.
# If variable 'tot' is still equal to '0.0', then create and set 'avg' to value of '0.0'
if tot == 0.0 :
    avg = 0.0
# Else create and set value of variable 'avg' to the dividend of variables 'tot' and 'num'.
else :
    avg = tot/num
# End if/else statement block.

# Print the all done status string.
print('ALL DONE! Cooking up some numbers here...')
# Print the Total Sum of Input, Count of Input responses, and the average total per input count.
print('Input Sum:', tot,' Input Count:' , num,'Input Average:' , avg)

# The program will end and return to the normal CLI cursor.
# End of script.