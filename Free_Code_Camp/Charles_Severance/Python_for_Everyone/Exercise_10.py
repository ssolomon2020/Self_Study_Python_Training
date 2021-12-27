# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Student           : Shawn Solomon                                         #
# Date              : 12/27/2021                                            #
# Course            : Scientific Computing with Python: Python For Everyone #
# Instructor        : Chuck Severence                                       #
# Exercise          : #10                                                   #
# Video             : https://www.youtube.com/watch?v=EhQxwzyT16E           #
# Learning Platform : www.freecodecamp.org                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# This is a continuation of the demonstration from exercise 09 on dictionaries and loops using string data from files, but using the sort() method instead. 
# File names that can be opened are:
# text_09_clown.txt
# text_09_intro.txt
# text_09_words.txt

# Start of script.
# The program will start after the script begins its run.

print("Files that can be opened are: 'text_09_clown.txt', 'text_09_intro.txt', and 'text_09_words.txt'")
# Create the variable 'fname' and assign its value as the user input response to the printed string.
fname = input('Enter File: ')

# Start if statement line.
# If the length of 'fname' is less than the floating point value of '1' as determined by the 'len()' function, assign the string value to 'fname'. 
if len(fname) < 1 : fname = 'text_09_clown.txt'
# End if statement line.

# If 'fname' is the default clown text, print clown string.
if fname == 'text_09_clown.txt' :
    print("It'll be a clown's world today!")

# This try/except block will prevent invalid user input from being processed and exit program.
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

        # This is also referred to as an idiom: retrieve/create/update/counter
        di[w] = di.get(w,0) + 1
        # Print words in dictionary with new status and its key value within the loop.
        # print(w, 'new', di[w])


    # End the for loop statement block of 'w' in 'wds'.
# End the for loop statement block of 'lin' in 'hand'

# Printing the string and key values stored in the dictionary of the 'di' variable. Remove comment mark below to test.
# print('Unsorted Dictionary listing Key, Value:',di)
# # What you should see as you watch the buffer are dictionary values flying up the screen.

# Demonstration of the 'sorted()' method. Remove comment marks below to test.
# # Create variable 'x' and assign its value as the value of 'di' with the 'items()' method and then 'sorted()' method applied creating a list of tuples defaulting to key alphabetical order. 
# x = sorted(di.items())
# # Print the string with variable 'x'.
# print('Sorted Tuples:', x)
# # Print the tuple stored in position '5' of the list.
# print('Specific Listed Tuple:', x[5])

# Create variable 'tmp' and assign it's value to 'list()'.
tmp = list()
# Create 'for' loop evaluating keys and values in dictionary 'di' with the 'items()' method applied.
for k, v in di.items() :
    # print(k, v)
    # Create variable 'newt' and assign it's value as the tuple 'v, k' in the dictionary 'di'.
    newt = (v, k)
    # Apply the 'append()' method to variable 'tmp' using the variable 'newt'
    tmp.append(newt)

# print('Generated List of tuples with flipped to Value, Key: ', tmp)

# Re-assign its value as sorted method applied to the value in the 'tmp' variable and set reverse as 'True'.
tmp = sorted(tmp, reverse=True)
# print('List of tuples is now sorted by value then key: ', tmp)
# print('Specific listed tuple: ', tmp[5])

print('Listing 5 sorted key values line by line:')
for v, k in tmp[:5] :
    print(k,v)

# The program will end and return to the normal CLI cursor.
# End of script.