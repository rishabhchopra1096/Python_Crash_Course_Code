# Sometimes you'll want to accept an arbitary number of
# argument but you won't know ahead of time
# what kind of information will be passed to the
# function.

# Write a function that accepts as many key-value pairs as the
# calling statement provides.

# Example : Building user profiles.
# You're sure that you'll get information about the user but
# you're not sure that what kind of information will be
# given to you.

# The function build_profile() taken in the first and the last
# name but also takes in an arbitrary number of keyword
# arguments.

def build_profile(first,last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    profile = {}
    profile['First name' ] = first
    profile['Last name'] = last
    print(user_info)
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert','einstein',
    location = 'princeton', field = 'physics')

print(user_profile)


