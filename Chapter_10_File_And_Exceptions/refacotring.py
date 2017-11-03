import json

def greet_user():
    """Greet the user by name."""
    file_name = 'username.json'
    try:
        with open(file_name) as file_object:
            username = json.load(file_object)
    except IOError:
        username = raw_input("What is your name? ")
        with open(file_name , 'w') as file_object:
            username = json.dump(username , file_object)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")

greet_user()

# greet_user does too many different tasks.
# Refaacotr greet_user so that it handles less tasks.

print('''\nRefactoring greet_user()''')

def get_stored_username():
    """Retrieves a stored username and Returns the username if found one"""
    """Get stored username if available"""
    # Does only what the except block in the above greet_user does
    # Return a username to be utilised by the if block of greet_user BELOW
    file_name = 'username2.json'
    try:
        with open(file_name) as file_object:
            username = json.load(file_object)
    except IOError:
        return None # This is good practice, a function should ether return the value you are expecting
                    # or return None
    else:
        return username


# def greet_user():
#     """Greet the user by name"""
#     # Print a Welcome Back message to user if the attempt to retrieve a username was successful
#     # If not : Prompt the user for a new username
#     username = get_stored_username()
#     if username: # if block utilises the get_stored_username() like said above
#         print("Welcome back " + username + "!") # username is what get_stored_username() returns
#     else:
#         username = raw_input("What is your name? ")
#         file_name = 'username2.json'
#         with open(file_name , 'w') as file_object:
#             username = json.dump(username , file_object)
#             print("We'll remember you when you come back, " + username + "!")


# greet_user()

print("""\nRefacatoring Further""")

"""For when the username exists: """
def get_stored_username():
    """Retrieves a stored username and Returns the username if found one"""
    """Get stored username if available"""
    # Does only what the except block in the above greet_user does
    # Return a username to be utilised by the if block of greet_user BELOW
    file_name = 'username2.json'
    try:
        with open(file_name) as file_object:
            username = json.load(file_object)
    except IOError:
        return None # This is good practice, a function should ether return the value you are expecting
                    # or return None
    else:
        return username

"""For when the username does not exist"""
def get_new_username():
    username = raw_input("What is your name?")
    file_name = 'username2.json'
    with open(file_name , 'w') as file_object:
        username = json.dump(username,file_object)
    return username

"""Now that we a functions for when the username exist and when it doesnt : """


def greet_user():
    """Greet the user by name"""
    # Print a Welcome Back message to user if the attempt to retrieve a username was successful
    # If not : Prompt the user for a new username
    username = get_stored_username()
    if username: # if block utilises the get_stored_username() like said above
        print("Welcome back " + username + "!") # username is what get_stored_username() returns
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()




