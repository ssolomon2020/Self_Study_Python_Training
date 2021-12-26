# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Student           : Shawn Solomon                                         #
# Date              : 12/26/2021                                            #
# Course            : Scientific Computing with Python: Python For Everyone #
# Instructor        : Chuck Severence                                       #
# Exercise          : #08                                                   #
# Video             : https://www.youtube.com/watch?v=-9TfJF2dwHI           #
# Learning Platform : www.freecodecamp.org                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# The program will start after the script begins its run.
# This script demonstrates how to store a string in a variable from file and manipulate it with methods in a for loop. It also demonstrates how to troubleshoot traceback issues using print statements.

# Create variable 'han' and set its value to the entire string found in file called by the 'open()' function.
han = open('text_08.txt')

# Create for loop and variable 'line' using the 'han' as a reference. 
for line in han:
    # Set the value of variable 'line' to its current value and remove whitespace using the 'rstrip()' method applied to it with default action.
    line = line.rstrip()
    # Print the 'line' variable with string to test. Remove comment mark below to test.
    # print('Line:', line)
 
    # Create variable 'wds' and set its value to the variable 'line' with the default action of the 'split()' method to divide the text by each whitespace. 
    wds = line.split()
    # Print variable 'wds' to test. Remove comment mark below to test.
    # print('Words:', wds)

    # The guardian pattern implemented after traceback regarding the next if statement block. Remove comment marks below on 'if' statement block to test.
    # if len(wds) < 1 :
    #    # Continue with the 'for' loop if length of the value of 'wds' is less than 1 character.
    #    continue

    # Another guardian pattern implemented as an alternative after the first one. Remove comment marks below on the 'if' statement block to test.
    #if line == '' :
    #    # Print string that the blank lin is being skipped.
    #    # print('Skip Blank')
    #    continue

    # Original 'if' statement that created traceback errors.  Remove comment marks below to test.
    # if wds[0] != 'Lorem' :
    #    # Print string 'Ignore:' to test tracebacks and see what was ignored. Remove comment mark below to test.
    #    # print('Ignore:')
    #    # Continue with the 'for' loop.
    #    continue

    # Final guardian pattern implemented in the video to combine first guardian pattern and original 'if' statement as a compound statement using 'or'. Remember to comment mark out the block when testing other iterations.
    if len(wds) < 3 or wds[0] != 'Lorem' :
        # print('Words:', wds)
        continue
        # For loop will continue until interrupted or finite strings are parsed.
    # If the order of the evaluation is switched, the traceback error will fail again due to list index being out of range.

    # Print position defined strings captured in variable 'wds' dictionary. Should print 'Wikipedia'.
    print(wds[2]) # For some reason it is throwing tracebacks on positions after 3. Should look into this later.

# End of 'for' loop statement block.

# The program will end and return to the normal CLI cursor.
# End of script.