# 3-4. Guest List: If you could invite anyone, living or deceased
# , to dinner, who would you invite? Make a list that includes at
#  least three people you’d like to invite to dinner. Then use
#  your list to print a message to each person, inviting them to
#  dinner.



invited = ['one','two','three']

print("Hey, Guest Number: " + invited[0].title() + "! I would like to invite you to dinner.")
print("Hey, Guest Number: " + invited[1].title() + "! I would like to invite you to dinner.")
print("Hey, Guest Number: " + invited[2].title() + "! I would like to invite you to dinner.")


# 3-5. Changing Guest List: You just heard that one of your guests
#  can’t make the dinner, so you need to send out a new set of invitations.
# You’ll have to think of someone else to invite.
# Start with your program from Exercise 3-4.
# Add a print statement at the end of your program stating the
# name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t
# make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person
# who is still in your list.

print("\nShucks! Guest Number: " + invited[2].title() + " will not be able to come.")
invited[2] = 'four'
print("Here is the new list of people who are invited: ")
print(invited)
print("Hey, Guest Number: " + invited[0].title() + "! I would like to invite you to dinner.")
print("Hey, Guest Number: " + invited[1].title() + "! I would like to invite you to dinner.")
print("Hey, Guest Number: " + invited[2].title() + "! I would like to invite you to dinner.")


# 3-6. More Guests: You just found a bigger dinner table, so
# now more space is available. Think of three more guests to
# invite to dinner.
# Start with your program from Exercise 3-4 or Exercise 3-5.
# Add a print statement to the end of your program informing
# people that you found a bigger dinner table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in
# your list.

print("\n3-6:More Guests: ")
print("Hey!Guest Number: " + invited[0].title() + " I found a bigger dinner table!" +
    "So now more people will be coming!")
print("Hey!Guest Number: " + invited[1].title() + " I found a bigger dinner table!" +
    "So now more people will be coming!")
print("Hey!Guest Number: " + invited[2].title() + " I found a bigger dinner table!" +
    "So now more people will be coming!")
invited.insert(3,'five')
print(invited)
invited.insert(2,'six')
print(invited)
invited.append('seven')
print(invited)

print("\nHere are the new invitations: ")
print("Hey, Guest Number: " + invited[0].title() + "! I would like to invite you to dinner.")
print("Hey, Guest Number: " + invited[1].title() + "! I would like to invite you to dinner.")
print("Hey, Guest Number: " + invited[2].title() + "! I would like to invite you to dinner.")
print("Hey, Guest Number: " + invited[3].title() + "! I would like to invite you to dinner.")
print("Hey, Guest Number: " + invited[4].title() + "! I would like to invite you to dinner.")
print("Hey, Guest Number: " + invited[5].title() + "! I would like to invite you to dinner.")


# 3-7. Shrinking Guest List: You just found out that your new
# dinner table won’t arrive in time for the dinner, and you have
# space for only two guests.
#    Start with your program from Exercise 3-6. Add a new line
#    that prints a message saying that you can invite only two people
#     for dinner.
#    Use pop() to remove guests from your list one at a time
#    until only two names remain in your list.
#    Each time you pop a name from your list, print a message
#    to that person letting them know you’re sorry you
#    can’t invite them to dinner.
#    Print a message to each of the two people still on your list,
#    letting them know they’re still invited

print("\n3-7:\n\tUninviting the guest:")
uninvited_1 = invited.pop()
print("Sorry, " + uninvited_1.title() + " I won't be able to invite you.")
uninvited_2 = invited.pop()
print("Sorry, " + uninvited_2.title() + " I won't be able to invite you.")
uninvited_3 = invited.pop()
print("Sorry, " + uninvited_3.title() + " I won't be able to invite you.")
uninvited_4 = invited.pop()
print("Sorry, " + uninvited_4.title() + " I won't be able to invite you.")
print("\tInviting who are left in the list.")
print("Hey, " + invited[0].title() + "! I still want YOU to come!")
print("Hey, " + invited[1].title() + "! I still want YOU to come!")



