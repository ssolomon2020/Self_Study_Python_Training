# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 3 Module Part 2 - Practice Quiz
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# Scripting examples encountered during the Module Part 2 Practice Quiz:

# 02. Fill in the blanks to make the factorial function return the factorial of n. 
# Then, print the first 10 factorials (from 0 to 9) with the corresponding number. 
# Remember that the factorial of a number is defined as the product of an integer 
# and all integers before it. For example, the factorial of five (5!) is equal to 
# 1*2*3*4*5=120. Also recall that the factorial of zero (0!) is equal to 1.

# def factorial(n):
#     result = 1
#     for x in range(1,___):
#         result = ___ * ___
#     return ___
# 
# for n in range(___,___):
#     print(n, factorial(n+___))

def factorial(n):
    result = 1
    for x in range(1, n):
        result = x * result
    return result

for n in range(0, 10):
    print(n, factorial(n+1))


# 03. Write a script that prints the first 10 cube numbers (x**3), starting with 
# x=1 and ending with x=10.

# for __ in range(__,__):
#     print(__)

for x in range(1,11):
    print(x**3)


# 04. Write a script that prints the multiples of 7 between 0 and 100. Print one 
# multiple per line and avoid printing any numbers that aren't multiples of 7. 
# Remember that 0 is also a multiple of 7.

# print()

for n in range(0, 100, 7):
    print(n)


# 05. The retry function tries to execute an operation that might fail, it retries 
# the operation for a number of attempts.  Currently the code will keep executing 
# the function even if it succeeds. Fill in the blank so the code stops trying after 
# the operation succeeded.

# def retry(operation, attempts):
#     for n in range(attempts):
#         if operation():
#             print("Attempt " + str(n) + " succeeded")
#             ___
#         else:
#             print("Attempt " + str(n) + " failed")
# 
# retry(create_user, 3)
# retry(stop_service, 5)

def retry(operation, attempts):
    for n in range(attempts):
        if operation():
            print("Attempt " + str(n) + " succeeded")
            break
        else:
            print("Attempt " + str(n) + " failed")
            continue

retry(create_user, 3)  #! <-- The operation input parameter is undefined. Not part of the standard library. Django maybe?
retry(stop_service, 5) #! <-- Another operation input parameter is undefined. Not part of the standard library. Another Django maybe?