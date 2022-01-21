# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 4 Module Part 3 Exercise 01
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# The "toc" dictionary represents the table of contents for a book. Fill in the blanks to do the following:
# 1) Add an entry for Epilogue on page 39. 	
# 2) Change the page number for Chapter 3 to 24. 	
# 3) Display the new dictionary contents. 	
# 4) Display True if there is Chapter 5, False if there isn't.

# toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
# ___ # Epilogue starts on page 39
# ___ # Chapter 3 now starts on page 24
# ___ # What are the current contents of the dictionary?
# ___ # Is there a Chapter 5?

toc = {"Introduction": 1, "Chapter 1": 4, "Chapter 2": 11, "Chapter 3": 25, "Chapter 4": 30}
toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
print("Chapter 5" in toc) # Is there a Chapter 5?