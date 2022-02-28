#! /usr/bin/env python3
import os
import requests

# # # # # # # # # # # # # # # # # # # # # #
# POST request exercise:                  #
# Taking non-keyed structured text files  #
# and accessing the REST API of a Django  #
# web application for posting customer    #
# feedback.                               #
# # # # # # # # # # # # # # # # # # # # # #

# Source path for iterating files.
srcpath = input("Source path? ") # Should be something like this: "/data/feedback"

# Set dictionary keys and key list for lines being iterated and copied from non-keyed structured/ordered text files.
feed_dict = {"title": None, "name": None, "date": None, "feedback": None}
keylist = ["title", "name", "date", "feedback"]

print()
# POSTMORTEM: URL requires a backslash at the end to successfully POST. Certain hosts may also need a specific port.
url = input("URL? ") # Should be something like this: "http://127.0.0.1/feedback/" or "http://127.0.0.1:80/feedback/"
for file in os.listdir(srcpath): 
  count = 0
  with open(os.path.join(srcpath, file), mode="r", encoding="UTF-8") as fhand:
    # print(fhand) # <-- Echo filepath, mode, and encoding for text wrapper as test.
    for line in fhand:
      # POSTMORTEM: Count was out of range as a list slice variable without an immediate discernable cause. Had to check with conditional instead.
      if count == 0:
        feed_dict[keylist[0]] = line.rstrip("\n")
      # print(keylist[0], ":", line) # <-- Test key and line being written to dictionary.
      elif count == 1:
        feed_dict[keylist[1]] = line.rstrip("\n")
      # print(keylist[1], ":", line) # <-- Test key and line being written to dictionary.
      elif count == 2:
        feed_dict[keylist[2]] = line.rstrip("\n")
        # print(keylist[2], ":", line) # <-- Test key and line being written to dictionary.
      elif count == 3:
        feed_dict[keylist[3]] = line.rstrip("\n")
      # print(keylist[3], ":", line) # <-- Test key and line being written to dictionary.
      count += 1

  # print(feed_dict) # <-- Test dictionary for correct data output.
  
  # Create a variable to hold the post method.
  r = requests.post(url, json=feed_dict)
  # Post
  print(r.request.body)
  
  # print(r.url) # <-- Test echo of URL being used in the POST request. 
  # print(r.status_code) # <-- Test request status code being recieved.
  # print(r.status_code == requests.codes.ok) # <-- Test request status code is within range.