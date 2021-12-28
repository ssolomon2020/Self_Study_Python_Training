# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Student           : Shawn Solomon                                         #
# Date              : 12/28/2021                                            #
# Course            : Scientific Computing with Python: Python For Everyone #
# Instructor        : Chuck Severence                                       #
# Exercise          : #12-socket1                                           #
# Video             : https://www.youtube.com/watch?v=dWLdI143W-g           #
# Learning Platform : www.freecodecamp.org                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Start of script.
# The program will start after the script begins its run.

# Import the socket library.
import socket

# Create the 'mysock' variable and assign Address family INET and the socket kind STREAM with in the 'socket()' class from the imported library.
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Apply the 'connect()' method referencing a tuple of the hostname and port to the 'mysock' variable.
mysock.connect(('data.pr4e.org', 80))
# Create the 'cmd' variable and assign the 'GET' request to the url in HTTP 1.0 with carriage returns and new lines within a string and apply the 'encode()' method to it. The return carriage was added from the code snippet on the exercise website to correct a bad request 400 error.
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# Apply the 'send()' method referencing the variable 'cmd' to the variable 'mysock' to send request.
mysock.send(cmd)

# Create 'while' loop that runs as long as it is True.
while True:
    # Create the 'data' variable and assign the variable 'mysock' with the 'recv()' method applied to limit data to '512' bytes.
    data = mysock.recv(512)
    # Print 'data' before if statement to test.
    # print(data)
    # If the length of data is less than one.
    if len(data) < 1 :
        # Break the while loop.
        break
    # Print the variable 'data' with the decode() method applied. the 'end' parameter adds a whitespace instead of a new line.
    print(data.decode(),end='')
# Apply the close method to mysock to terminate the connection.
mysock.close()

'''
# For some reason the copy paste version below is formating correctly while the one that was hand typed above and corrected is still formatting incorrectly.
# As it turns out, I added comments to the above code and the weird aberation resolved itself.
# I hypothesize that VSCode held the aberant code in the buffer after corrections were made and until the lines had changed, the corrective changes did not take place for the debugger.
# This is not the first time VSCode has decided to produce the same results despite changes within the line being automatically and manually saved before the debug terminal run.

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True :
    data = mysock.recv(512)
    if len(data) < 1 :
        break
    print(data.decode(),end='')
mysock.close()
'''

# The program will end and return to the normal CLI cursor.
# End of script.