import json
# Load the username, if it has been stored previously.
# Otherwise , prompt for the username and store it.

file_name = 'username.json'
# with open(file_name , 'w') as file_object:
#     json.dump(username, file_object)
#     print("We'll remember you when you come back, "+ username.title() + "!")

try: # to open the file_name , read if it exists and Go To else Block
    with open(file_name) as file_object:
        username = json.load(file_object)
except IOError: # when file not found , so we prompt for user's name and write it in the fileng json.dump()
    username = raw_input("What is your name? ")
    with open(file_name , 'w') as file_object:
        json.dump(username, file_object)
        print("We'll remember you when you come back, "+ username.title() + "!")
else: # if try block succeeds in reading the file, We greet the user!
    print("Welcome back, " + username + "!")

''' The first time the program runs: '''
# >>> What is your name? Eric
# >>> We'll remember you when you come back, Eric!

'''Otherwise: '''
# Welcome back, Eric!

'''Output:'''
# Rishabhs-MacBook-Pro:Chapter_10_File_And_Exceptions rishabhchopra$ python remember_me.py
# What is your name? rishabh
# Well remember you when you come back, Rishabh!
# Rishabhs-MacBook-Pro:Chapter_10_File_And_Exceptions rishabhchopra$ python remember_me.py
# Welcome back, rishabh!
# Rishabhs-MacBook-Pro:Chapter_10_File_And_Exceptions rishabhchopra$