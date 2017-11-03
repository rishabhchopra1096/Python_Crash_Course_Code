print "You can nest a dictionary inside another dictionary"
print "This can make it complicated"
# A dictionary can also be a value to a key.
# For example, if you have several users
# for a website, each with a unique username, you can use the usernames as the keys in a dictionary.
# You can then store information about each user by using a dictionary as the value associated with their username.
#  In the following listing, we store three pieces of information about each user: their first name, last name, and location.
#   Well access this information by looping through the usernames and the dictionary of information associated with each username:

users={'aeinstein':{ # Defining a dictionary called users.
    'first':'albert',# With 2 keys.
    'last':'einstein',# and each having a value that is a dictionary.
    'location':'princeton',},#the value dictionary each has 3 key-value pairs.
        'mcurie':{ # one for first , one for last and one for location.
        'first':'marie',# Python will store each key in the variable username.
        'last':'curie', # it will store all value dictionaries in the variable user_info
        'location':'paris',},
        }

print users.items()
# will make a list with 2 tuples, 1 for each username:
# each tuple has a 'username' followed by a comma and then
# a dictionary with 3 key value pairs. One for first,one for last and one for
#location.
for username, user_info in users.items():
    print"\nUsername: "+username # Once inside the MainDictionary loop , we print the username.
    full_name=user_info['first']+" "+user_info['last']
    location=user_info['location'].title() # Here , user_info['location'] refers to a string--> therefore .title() is valid.
    print "\tFull Name: "+full_name.title()
    print "\tLocation: "+location

#Notice that the structure of each users dictionary is identical.
#Although not required by Python, this structure makes nested dictionaries easier to work with.
# If each users dictionary had different keys, the code inside the for loop would be more complicated.


