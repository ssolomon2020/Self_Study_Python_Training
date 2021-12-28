# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Student           : Shawn Solomon                                         #
# Date              : 12/28/2021                                            #
# Course            : Scientific Computing with Python: Python For Everyone #
# Instructor        : Chuck Severence                                       #
# Exercise          : #12-urllib                                           #
# Video             : https://www.youtube.com/watch?v=8yis2DvbBkI           #
# Learning Platform : www.freecodecamp.org                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Start of script.
# The program will start after the script begins its run.

# import the modules 'request', 'parse', and 'error' from within the module 'urllib' into the current script.
import urllib.request, urllib.parse, urllib.error

# Create the 'fhand' variable and assign the string called with the 'urlopen()' function in the request module to open the URL.
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# Create the 'counts' variable and assign the 'dict()' dictionary class to it.
counts = dict()

# Create 'for' loop creating and evaluating variable 'line' with in the 'fhand' variable.
for line in fhand :
    # Print the 'line' variable using 'decode()' and 'strip()' methods to remove tags and whitespaces.
    print(line.decode().strip())
    # Create the variable 'words' and assign it the 'line' variable as it's value with the 'decode()' and 'split()' methods applied to it.
    words = line.decode().split()
    # Create a nested 'for' loop creating and evaluating the 'word' variable with in the 'words' variable.
    for word in words :
        # Assign to 'word' within 'counts' the value of counts with the get() method applied with key and value adding '1' to the value.
        counts[word] = counts.get(word, 0) + 1
    # Loop will restart until all lines are exhausted and end the loop.
    # Four lines should be extracted and printed from the URL address for the text file.
    # Continue adding words to dictionary until lines are exhausted.
# End of loop statement block.

# Print the dictionary key and values with in the variable 'counts'.
print(counts)

# Create the variable 'largest' and assign its value as '1'.
largest = -1
theword = None
# Create for loop examining 'k' and 'v' in the dictionary using the 'items()' method.
for k,v in counts.items() :
    # Print the key and value.
    # print(k,v)
    if v > largest :
        largest = v
        theword = k
# Print the most used word and it's total count.
print('The first most used word in the text is "',theword, '" with a count of', largest)

# The program will end and return to the normal CLI cursor.
# End of script.