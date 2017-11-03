# A function can return any kind of value you need it to,
# including more complicated data structures like lists and dictionaries.
# For example, the following function takes in parts of a name and returns a
# dictionary representing a person:

def build_person(first_name,last_name):
    """Return a dictionary of information about a person"""
    person={'first':first_name,'last':last_name}
    return person

my_name=build_person('Rishabh','Chopra')
print(my_name)e