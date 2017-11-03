# The value a function reurns is called a return value.

def get_formatted_name(first_name,last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# 1. NO OUTPUT
get_formatted_name('jimi','hendrix')

# 2. PRINTED OUTPUT directly from function.
print(get_formatted_name('jimi','hendrix'))

# 3. PRINTED OUTPUT by saving return value in variable.
musician = get_formatted_name('jimi','hendrix')
print(musician)

