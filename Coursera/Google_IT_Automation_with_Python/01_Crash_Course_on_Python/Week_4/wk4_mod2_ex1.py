# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 4 Module Part 2 Exercise 01
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# Using the "split" string method from the preceding lesson, complete the get_word function to return 
# the {n}th word from a passed sentence. For example, get_word("This is a lesson about lists", 4) should 
# return "lesson", which is the 4th word in this sentence. Hint: remember that list indexes start at 0, not 1.

# def get_word(sentence, n):
#     # Only proceed if n is positive 
#     if n > 0:
#         words = ___
#         # Only proceed if n is not more than the number of words 
#         if n <= len(words):
#             return(___)
#     return("")
# 
# print(get_word("This is a lesson about lists", 4)) # Should print: lesson
# print(get_word("This is a lesson about lists", -4)) # Nothing
# print(get_word("Now we are cooking!", 1)) # Should print: Now
# print(get_word("Now we are cooking!", 5)) # Nothing

def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n - 1])
	return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing

