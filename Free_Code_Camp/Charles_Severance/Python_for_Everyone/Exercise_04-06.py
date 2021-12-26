# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Student           : Shawn Solomon                                         #
# Date              : 12/25/2021                                            #
# Course            : Scientific Computing with Python: Python For Everyone #
# Instructor        : Chuck Severence                                       #
# Exercise          : #04-06                                                #
# Video             : https://www.youtube.com/watch?v=ksvGhDsjtpw           #
# Learning Platform : www.freecodecamp.org                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# The program will start after the script begins its run.

# Defining a new function called 'computepay()' with new variables created for 'hours' and 'rate'.
def computepay(hours, rate) :
    # Call the print function to repeat the input variables of 'hours' and 'rate' in the human readable string.
    print("You have entered", hours, "hours at a rate of $", rate, "per hour")
    # If the value of the variable 'hours' is greater than '40', run the 'if' statement. Otherwise run the 'else' statement.
    if hours > 40 :
        # Create variable 'otp' under the 'if' statement and set the value as the product of the difference of over-time in 'hours' multiplied by 1.5 times the 'rate'.
        otp = (hours - 40) * (rate * 1.5)
        # Reset the 'hours' variable to '40'.
        hours = 40
        # Create variable 'reg' under the 'if' statement and set the value to the product of the variables 'hours' and 'rate'.
        reg = hours * rate
        # Create variable 'pay' under the 'if' statement and set the value to the sum of the variables 'otp' and 'reg'.
        pay = otp + reg
        # Call the print function to print arbitrary status string under the 'if' statement.
        print("Calculating amounts...")
        # Print regular and over-time pay values in string under the 'if' statement.
        print("Regular Pay: $", reg, "  Over-time Pay: $", otp)
    # If the value of variable 'hours' is not greater than or equal to '40', run this 'else' statement.
    else :
        # Create variable pay under the 'else' statement and set the value as the product of the variables 'hours' and 'rate'.
        pay = hours * rate
    
    # Print arbitrary status string for calculating gross outside and after the 'if/else' block within the function.
    print("Calculating total gross...")
    # Return the value of the variable 'pay' outside the function.
    return pay
# new function 'computepay()' will now be stored in memory for later.

# End of defined functions

# CLI interaction begins here.

# Print the welcome message string.
print("Welcome to the Gross Pay Calculator!")

# Create the variable 'ihr' and set its value as the input response to this printed string. 
ihr = input("Please enter hours worked this pay period: ")
# Create the variable 'irt' and set its value as the input response to this printed string. 
irt = input("Please enter the normal rate of pay: ")

# Run the 'try' statement to test the string of the user input responses.
try :
    # Create the variable fhr and set it's value as the floating point of the 'ihr' string variable.
    fhr = float(ihr)
    # Create the variable frt and set its value as the floating point of the 'irt' string variable.
    frt = float(irt)
# If the variables cannot be converted to floating point numerics, run the 'except' statement. 
except :
    # Print arbitrary error/debug messages. Print quit message. 
    print("User Error: Please enter numerics.")
    print("Quitting Program... Please run the application again")
    # Quit script.
    quit()
    # The program will end here and return to the normal CLI cursor.
# End of the 'try/except' statement block.

# Create the variable 'cpay' and set its value to call upon the function 'computepay()' to return the value of the 'pay' variable. Set the 'hours' variable to the value of 'fhr' and the 'rate' variable to the value of 'frt' within the function. 
cpay = computepay(fhr, frt)

# Print the human readable string with the value of 'cpay' for the gross total this pay period.
print("You have earned a gross total of $", cpay, "this pay period!")

# The program will end and return to the normal CLI cursor.
# End of script.