# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 3 Module Part 3 - Practice Quiz
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# Scripting examples encountered during the Module Part 3 Practice Quiz:

# 03. Fill in the blanks to make the is_power_of function return whether the number is a 
# power of the given base. Note: base is assumed to be a positive number. 
# Tip: for functions that return a boolean value, you can return the result of a comparison.

# def is_power_of(number, base):
#     # Base case: when number is smaller than base.
#     if number < base:
#     # If number is equal to 1, it's a power (base**0).
#         return __
# 
#     # Recursive case: keep dividing number by base.
#     return is_power_of(__, ___)
# 
# print(is_power_of(8,2)) # Should be True
# print(is_power_of(64,4)) # Should be True
# print(is_power_of(70,10)) # Should be False

def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    if number % base == 1:
      return True
    else:
      return False
  else:
    number = number / base
  # Recursive case: keep dividing number by base.
  return is_power_of(number, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False


# 04. The count_users function recursively counts the amount of users that belong to a group 
# in the company system, by going through each of the members of a group and if one of them 
# is a group, recursively calling the function and counting the members. But it has a bug! 
# Can you spot the problem and fix it?

# def count_users(group):
#     count = 0
#     for member in get_members(group):
#         count += 1
#         if is_group(member):
#             count += count_users(member)
#     return count
# 
# print(count_users("sales")) # Should be 3
# print(count_users("engineering")) # Should be 8
# print(count_users("everyone")) # Should be 18

def count_users(group):
    count = 0
    for member in get_members(group):        #! <-- get_members is not defined in the nomral Python library. Django maybe?
        count += 1
        if is_group(member):                 #! <-- is_group is not defined in the normal Python library. Django again?
            count += count_users(member) - 1 #! <-- Subtract an increment of 1 from the recursion and store in count.
    return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18


# 05. Implement the sum_positive_numbers function, as a recursive function that returns the sum 
# of all positive numbers between the number n received and 1. For example, when n is 3 it should 
# return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15.

# def sum_positive_numbers(n):
#     return 0
# 
# print(sum_positive_numbers(3)) # Should be 6
# print(sum_positive_numbers(5)) # Should be 15

def sum_positive_numbers(n):
    if n < 1:
        return 0
  
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15