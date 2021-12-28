# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Student           : Shawn Solomon                                         #
# Date              : 12/28/2021                                            #
# Course            : Scientific Computing with Python: Python For Everyone #
# Instructor        : Chuck Severence                                       #
# Exercise          : #12-urlinks                                           #
# Video             : https://www.youtube.com/watch?v=g9flPDG9nnY           #
# Learning Platform : www.freecodecamp.org                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# This exercise requires Beautiful Soup. https://pypi.org/project/beautifulsoup4/
# To install the modules type the command below in the python command line:
# pip install beautifulsoup4

# For previous versions of Beautiful Soup: https://pypi.org/project/BeautifulSoup/
# These historic versions have stopped development in 2011 and ended support as of Jan, 1st 2021.
# Please use version 4 unless there is a specific reason you need the previous unsupported versions. 

# Start of script.
# The program will start after the script begins its run.

# import the modules 'request', 'parse', and 'error' from within the module 'urllib' into the current script.
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
# Create the 'ctx' variable and assign it the create_default_context() function from the ssl library module
ctx = ssl.create_default_context()
# Set check host to false.
ctx.check_hostname = False
# set verify mode to no certificate.
ctx.verify_mode = ssl.CERT_NONE

# Create the 'url' variable and assign an 'input()' user query and assign it the user input.
url = input('Enter the URL: - ')
# Create the 'html' variable and assign an open URL request with input 'url' variable and ssl options held with in the 'ctx' variable and apply the read() method to return a large string.
html = urllib.request.urlopen(url, context=ctx).read()
# Create the 'soup' variable and assign it's value as the BeautifulSoup() class reading 'html' and using an html parser to decode.
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all the anchor tags
# Create the variable 'tags' and assign variable 'soup('a')' to parse all a tags.
tags = soup('a')
# Create 'for' loop creating and evaluating the variable 'tag' within 'tags'
for tag in tags :
    # for each loop iteration, print the link with key word 'href' using the 'get()' method on 'tag'
    print(tag.get('href', None))


# The program will end and return to the normal CLI cursor.
# End of script.