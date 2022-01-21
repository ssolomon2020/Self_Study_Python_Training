# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 3 Module Part 1 Exercise 01
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# Can you work out what this function does? Try passing different parameters to the attempts function to see what it does.

def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(5)

# attempt() is called with a parameter of 5.
# When the parameter is passed into the function it is stored in the variable n within the function.
# The variable x is initialized with a value of 1.
# A while loop is initialized to run as long as the condition that x is less than or equal to n is True. Currently it is 1 <= 5 in values.
# As long as the condition remains true, the sequence will print "Attempt " concatenated with the current int/float value of x converted as a string value.
# The sequence will then move on take the value of x, add an increment of 1, then store it back into x. The sequence will then restart.
# As the variable x is stored outside the bounds of the while loop, it will continue to increment by 1 with each loop instance.
# The variable x is therefore serving as a counter for each loop and when the condition of x is more than the value of n, the loop will terminate.
# As the print function is only repeating the value of x, it will not start the iteration of the message at zero attempts.
# Once the while loop has met the conditions to terminate the loop, a print function will output "Done" to the CLI and without further
# instructions, the program will automatically end and return to the normal CLI cursor/prompt.