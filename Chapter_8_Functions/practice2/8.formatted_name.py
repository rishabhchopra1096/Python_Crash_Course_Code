# Making an Argument Optional
# people can choose to provide extra information ,
# only if they want to.

def get_formatted_name(first_name,middle_name,last_name):
    """Return a full name , neatly formatted."""
    full_name = first_name + ' ' +  middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jon','lee','hooker')
print(musician)

# Middle names aren't ALWAYS needed.
# If you enter only first and last name in the above function ,
# you will get an error as the function requires 3 arguments.
# Solution ?

def get_formatted_name(first_name,last_name,middle_name=""):
    """Return a full name , neatly formatted."""
    # Make sure the middle name is the last argument
    # entered when function is called.
    if middle_name:
        full_name = first_name + ' '  + middle_name + ' ' + last_name
        return full_name.title()
    else:
        full_name = first_name + ' ' + last_name
        return full_name.title()
print(get_formatted_name('rishabh','chopra'))
print(get_formatted_name('rishabh','chopra','rohan'))

