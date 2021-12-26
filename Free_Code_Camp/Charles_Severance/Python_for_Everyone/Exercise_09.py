# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Student           : Shawn Solomon                                         #
# Date              : 12/26/2021                                            #
# Course            : Scientific Computing with Python: Python For Everyone #
# Instructor        : Chuck Severence                                       #
# Exercise          : #09                                                   #
# Video             : https://www.youtube.com/watch?v=PrhZ9qwBDD8           #
# Learning Platform : www.freecodecamp.org                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# This is a demonstration on dictionaries and loops using string data from files using the open() method. 
# File names that can be opened are:
# text_09_clown.txt
# text_09_intro.txt
# text_09_words.txt

# Start of script.
# The program will start after the script begins its run.

# Create the variable 'fname' and assign its value as the user input response to the printed string.
fname = input('Enter File: ')

# Start if statement line.
# If the length of 'fname' is less than the floating point value of '1' as determined by the 'len()' function, assign the string value to 'fname'. 
if len(fname) < 1 : fname = 'text_09_clown.txt'
# End if statement line.

# If 'fname' is the default clown text, print clown string.
if fname == 'text_09_clown.txt' :
    print("It'll be a clown's world today!")

try :
    # Create the variable 'hand' and assign its value as the 'open()' function applied to the variable 'fname'.
    hand = open(fname)
except :
    print('Incorrect file name! Use valid file. Exiting...')
    quit()

# Create the variable 'di' and assign its value as the empty 'dict()' function.
di = dict()

# Start the for loop statement block for 'lin' in 'hand'.
for lin in hand:
    # Set the value of 'lin' with the method of 'rstrip()' applied to it.
    lin = lin.rstrip()
    # Print the string values of 'lin' to confirm the 'rstrip()' method applied correctly. Remove comment mark below to test.
    # print(lin)
    # Create the variable 'wds' and set its value as 'lin' with the method of 'split()' applied to it.
    wds = lin.split()
    # Print the list of string values contained in the variable 'wds' to test. Remove the comment mark below to test.
    # print(wds)
    
    # Start the for loop statement block for 'w' in 'wds' nested within the for loop of 'lin' in 'hand'.
    for w in wds :
        # Within the for loop, print the string '**', the word, and get word and set the key value to '-99'. Remove comment mark below to test.
        # print('**',w,di.get(w,-99))
        
        # Start of if/else statement block. Block is commented out.
        # if w in di :
        #    # If the current word is in the dictionary, then add '1' to the key value and store the new value.
        #    di[w] = di[w] + 1
        #    # Print existing word status during dictionary count. Remove comment mark below to test.
        #    # print('**Existing**')
        # else:
        #    # If the word is NOT in the dictionary, then add word and assign its key value to '1'.
        #    di[w] = 1
        #    # Print new word status during dictionary count. Remove comment mark below to test.
        #    # print('**NEW**')
        # End of if/else statement block.

        # Print to test for loop of 'w' in 'wds' nested within for loop of 'lin' in 'hand'.
        # print(w,di[w])

        # This new block also does the same thing as the previous if/else statement block. Block is commented out.
        # Create the variable 'oldcount' and assign its value as the value for 'w' found by 'get()' within 'di'. If value doesn't exist, create it and set to '0' in the dictionary.
        # oldcount = di.get(w,0)
        # Print the 'oldcount' status.
        # print(w, 'old', oldcount)
        # Create the variable 'newcount' and assign it the value of the variable 'oldcount' and add '1' to it's value.
        # newcount = oldcount + 1
        # Words found in the dictionary are assign the value of  the variable 'newcount'.
        # di[w] = newcount
        # Print the 'newcount' status.
        # print(w, 'new', newcount)

        # This new block is the simplified version of the two previous blocks.
        # This is also referred to as an idiom: retrieve/create/update/counter
        di[w] = di.get(w,0) + 1
        # Print words in dictionary with new status and its key value within the loop.
        # print(w, 'new', di[w])


    # End the for loop statement block of 'w' in 'wds'.
# End the for loop statement block of 'lin' in 'hand'

# print the string and key values stored in the dictionary of the 'di' variable.
# print(di)
# What you should see as you watch the buffer are dictionary values flying up the screen.

# Create the variable 'largest' and assign its value as '1'.
largest = -1
theword = None
# Create for loop examining 'k' and 'v' in the dictionary using the 'items()' method.
for k,v in di.items() :
    # Print the key and value.
    # print(k,v)
    if v > largest :
        largest = v
        theword = k

# Print the most used word and it's total count.
print('Done! The most used word is "',theword, '" with a count of', largest)

# The program will end and return to the normal CLI cursor.
# End of script.