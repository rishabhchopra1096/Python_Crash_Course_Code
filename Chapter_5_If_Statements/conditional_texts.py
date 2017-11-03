# At the heart of every if statement is an expression that can be evaluated as
# True or False and is called a conditional test. Python uses the values
# True and False to decide whether the code in an if statement should be executed.
# If a conditional test evaluates to True, Python executes the code following
# the if statement. If the test evaluates to False, Python ignores the code
# following the if statement.
car='bmw'
print car=='bmw' #True
# The line checks whether the value of car is 'bmw' using a double equal sign (==).
# This equality operator returns True if the values on the left and right side of
# the operator match, and False if they dont match.
# one equal sign means assignment. it says Set the value of car to bmw.
# double equal sign is an equality operator. It returns only True or False.
# It asks : 'is the value of car equal to bmw?'
# Note : Testing for equality is case sensitive.
car = 'Audi'
print car.lower() == 'audi'
# Websites enforce certain rules for the data that users enter in a manner similar
# to this. For example, a site might use a conditional test like this to ensure
# that every user has a truly unique username, not just a variation on the
# capitalization of another persons username. When some- one submits a new
#  username, that new username is converted to lowercase and compared to the
#  lowercase versions of all existing usernames. During this check, a username
#  like 'John' will be rejected if any variation of 'john' is already in use.

