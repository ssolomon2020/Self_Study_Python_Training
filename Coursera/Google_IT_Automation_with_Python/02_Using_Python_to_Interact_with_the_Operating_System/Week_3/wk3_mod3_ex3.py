# Specialization: Google IT Automation with Python
# Course 02: Using Python to Interact with the Operating System
# Week 3 Module Part 3 Exercise 03
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# Add to the regular expression used in the extract_pid function, to return the 
# uppercase message in parenthesis, after the process id.

import re
def extract_pid(log_line):
    regex = r"\[([0-9]+)\]: ([A-Z]+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)
