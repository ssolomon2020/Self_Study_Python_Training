# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 4 Module Part 3 - Practice Quiz
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# Scripting examples encountered during the Module Part 3 Practice Quiz:

# 01. The email_list function receives a dictionary, which contains domain names as keys, 
# and a list of users as values. Fill in the blanks to generate a list that contains complete 
# email addresses (e.g. diana.prince@gmail.com).

# def email_list(domains):
#     emails = []
#     for ___:
# 	      for user in users:
# 	          emails.___
# 	  return(emails)
# 
# print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

def email_list(domains):
    emails = []
    for domain, users in domains.items():
        for user in users:
            emails.append(user + "@" + domain)
    return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


# 02. The groups_per_user function receives a dictionary, which contains group names with the 
# list of users. Users can belong to multiple groups. Fill in the blanks to return a dictionary 
# with the users as keys and a list of their groups as values.

# def groups_per_user(group_dictionary):
#     user_groups = {}
#     # Go through group_dictionary
#     for ___:
#         # Now go through the users in the group
#         for ___:
#             # Now add the group to the the list of
# # groups for this user, creating the entry
# # in the dictionary if necessary
# 
#     return(user_groups)
# 
# print(groups_per_user({"local": ["admin", "userA"],
# 		"public":  ["admin", "userB"],
# 		"administrator": ["admin"] }))

def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            # Now add the group to the the list of
            # groups for this user, creating the entry
            # in the dictionary if necessary
            user_groups.update({user:group}) #! <-- Cannot figure this out. It wants me to append to list. Can't point to it in new dictionary.

    return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
        "public":  ["admin", "userB"],
        "administrator": ["admin"] }))


# 05. The add_prices function returns the total price of all of the groceries in the  dictionary. 
# Fill in the blanks to complete this function.

# def add_prices(basket):
# 	# Initialize the variable that will be used for the calculation
# 	total = 0
# 	# Iterate through the dictionary items
# 	for ____:
# 		# Add each price to the total calculation
# 		# Hint: how do you access the values of
# 		# dictionary items?
# 		total += ___
# 	# Limit the return value to 2 decimal places
# 	return round(total, 2)  

# groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
# 	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

# print(add_prices(groceries)) # Should print 28.44


def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for k, v in basket.items():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += v
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44