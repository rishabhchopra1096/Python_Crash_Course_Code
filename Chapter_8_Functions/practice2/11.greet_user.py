def greet_user(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        print("Hello, " + name.title() + "!")

usernames = ['rishabh','rohan','radhika']
greet_user(usernames)

