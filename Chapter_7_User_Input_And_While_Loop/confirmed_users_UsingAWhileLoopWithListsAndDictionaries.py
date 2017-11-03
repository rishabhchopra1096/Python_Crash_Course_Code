# we have worked with one piece of info.
# To keep track of many users and pieces of information , well need to use
# lists and dictionaries with our while loops.
# We should not use a for loop to modify a list because Python will have trouble keeping track of all
# the items in a list.
# To modify a list as you work through it , use a while loop.

print ("Moving items from one list to another")

# Consider a list of newly registered but unverified users of a website. After
#we verify these users, how can we move them to a separate list of confirmed users?
# One way would be to use a while loop to pull users from the list of unconfirmed users as
#we verify them and then add them to a separate list of confirmed users.

#Starting with the users that need to be verified.
# And an empty list to hold the cofirmed users.

unconfirmed_users=['alice','brian','candace']
confirmed_users=[]

# Aim: Verify each user until there are no more unconfirmed_users.
# Aim: Then move each verified user into the list of confirmed_users.

while unconfirmed_users: # This line means that this loop will run as long as the list is not empty.
    current_user=unconfirmed_users.pop()
    print ("Verifying user: "+current_user.title()) # We simulate confirming each user by printing a verification message
    confirmed_users.append(current_user)          #and then adding them to the list of confirmed users.
#hen the list of unconfirmed users is empty, the loop stops and the list of confirmed users is printed.
#Now, to display all confirmed users:
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print (confirmed_user.title())


