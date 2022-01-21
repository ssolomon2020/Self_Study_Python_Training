# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 3 Module Part 2 Exercise 03
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# The validate_users function is used by the system to check if a list of users is valid or invalid. 
# A valid user is one that is at least 3 characters long. For example, ['taylor', 'luisa', 'jamaal'] 
# are all valid users. When calling it like in this example, something is not right. 
# Can you figure out what to fix?

# def validate_users(users):
#     for user in users:
#         if is_valid(user):
#         print(user + " is valid")
#         else:
#         print(user + " is invalid")
# 
# validate_users("purplecat")

def validate_users(users):
  for user in users:
    if is_valid(user): #! <-- Does not seem to be in the normal Python library. Django maybe?
      print(user + " is valid")
    else:
      print(user + " is invalid")

validate_users(["purplecat"]) #! <-- Need to call function with a list as the input parameter.