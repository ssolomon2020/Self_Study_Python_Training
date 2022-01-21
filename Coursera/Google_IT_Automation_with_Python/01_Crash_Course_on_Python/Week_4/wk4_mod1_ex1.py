# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 4 Module Part 1 Exercise 01
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# Modify the double_word function so that it returns the same word repeated twice, 
# followed by the length of the new doubled word. For example, double_word("hello") 
# should return hellohello10.

# def double_word(word):
#     return
# 
# print(double_word("hello")) # Should return hellohello10
# print(double_word("abc"))   # Should return abcabc6
# print(double_word(""))      # Should return 0

def double_word(word):
    return word * 2 + str((len(word) * 2))

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0