# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 2 Module Part 3 - Practice Quiz
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# Scripting examples encountered during the Module Part 3 Practice Quiz:

# 02. Complete the script by filling in the missing parts. The function receives a name,
# then returns a greeting based on whether or not that name is "Taylor".

# def greeting(name):
#     if ___ == "Taylor":
#         return "Welcome back Taylor!"
#     ___:
#         return "Hello there, " + name
# 
# print(greeting("Taylor"))
# print(greeting("John"))

def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))


# 05. If a filesystem has a block size of 4096 bytes, this means that a file comprised of only 
# one byte will still use 4096 bytes of storage. A file made up of 4097 bytes will use 4096*2=8192
# bytes of storage. Knowing this, can you fill in the gaps in the calculate_storage function below,
# which calculates the total number of bytes needed to store a file of a given size?

# def calculate_storage(filesize):
#     block_size = 4096
#     # Use floor division to calculate how many blocks are fully occupied
#     full_blocks = ___
#     # Use the modulo operator to check whether there's any remainder
#     partial_block_remainder = ___
#     # Depending on whether there's a remainder or not, return
#     # the total number of bytes required to allocate enough blocks
#     # to store your data.
#     if partial_block_remainder > 0:
#         return ___
#     return ___
#
# print(calculate_storage(1))    # Should be 4096
# print(calculate_storage(4096)) # Should be 4096
# print(calculate_storage(4097)) # Should be 8192
# print(calculate_storage(6000)) # Should be 8192

def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    # full_blocks = filesize // block_size #! <-- This is unneeded to at the moment.
    # print(full_blocks) # test output
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = block_size % filesize
    # print(partial_block_remainder) # Test output
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size * 2
    return block_size

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096 #! <-- Need to figure out what is causing it to use 8192
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192