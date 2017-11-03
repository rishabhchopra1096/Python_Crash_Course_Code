def get_formatted_name(first_name,last_name):
    """Return a full name, neatly formatted"""
    full_name=first_name+' '+last_name
    return full_name.title()

my_name=get_formatted_name('rishabh','chopra')
print(my_name)

def get_formatted_name(first_name,middle_name,last_name):
    """Return a full name, neatly formatted"""
    full_name=first_name+' '+middle_name+' '+last_name
    return full_name.title()

my_name=get_formatted_name('rishabh','WaitforIt','chopra')
print(my_name)

#To Make Middle Name Optional:
def get_formatted_name(first_name,last_name,middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name: #This line means if there is any mention of a middle name:
                    #Also , a non empty string has the value True as a middle name is provided.
                    #An empty string will have the value False.
        full_name=first_name+' '+middle_name+' '+last_name
    else:
        full_name=first_name+' '+last_name
    return full_name.title()

my_name=get_formatted_name('rishabh','chopra')
print (my_name)
#These Two will have the same outut: Rishabh Waitforit Chopra
my_mid_name=get_formatted_name('rishabh','chopra','waitforit') #  The middle name needs to be the last argument passed
print(my_mid_name)
my_mid_name2=get_formatted_name('rishabh','chopra',middle_name='waitforit')#  to match the positional arguments.

print (my_mid_name2)


