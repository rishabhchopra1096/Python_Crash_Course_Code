# Recall , remove() funtion used to remove the first value matching to the input from the list.
# Now what if you wanted to delete all instances of a value from the list.
# Say you want to remove all instances of 'cat' from a list of pets.
#Using the while loop.

pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
print (pets)
#This is what i did to remove all metion of cat:
# Using a for loop:
# for pet in pets:
#     if pet=='cat':
#         pets.remove('cat')

# print (pets)

#This is how to do it with a while loop:
while 'cat' in pets:
    pets.remove('cat')

print (pets)

# Now what the while loop does is:
# It looks for the first instance of 'cat'
# it removes that instance.
# It enters the while loop again only if there is another instance of 'cat' is found.
# If no more instances of cat are found. The loop closes.


