def greet_user():
#Display a simple greeting.
    print("Hello!")

greet_user()
#Passing info to a function:
def greet_user(username):
    print("Hello, "+username.title()+"!")

greet_user("rishabh chopra")