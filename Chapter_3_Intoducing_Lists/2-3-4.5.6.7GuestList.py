# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list
# that includes at least three people youd like to invite to dinner. Then use your list to print a message to
# each person, inviting them to dinner.
invited=['rohan','ridhi','rhea']
print ("Hey, "+invited[0].title()+"! I am thowing a party and i would love it if you'd come. ")
print ("Hey, "+invited[1].title()+"! I am thowing a party and i would love it if you'd come. ")
print ("Hey, "+invited[2].title()+"! I am thowing a party and i would love it if you'd come. ")

# 3-5. Changing Guest List: You just heard that one of your guests cant make the dinner, so you need to send out a
# new set of invitations. Youll have to think of someone else to invite.
#  Start with your program from Exercise 3-4. Add a print statement at the end of your program stating the name of
#  the guest who cant make it.
#  Modify your list, replacing the name of the guest who cant make it with the name of the new person you are inviting.
#  Print a second set of invitation messages, one for each person who is still in your list.
print ("\n"+invited[1].title()+" will not be able to come. How sad.")
print ("I am going to call Manan instead of Ridhi")
invited[1]='manan'
print('The new list of people coming to the party is:')
print (invited)
print ("And here are their invatations!")
print ("Hey, "+invited[0].title()+"! Party's Still On! ")
print ("Hey, "+invited[1].title()+"! I am thowing a party and i would love it if you'd come. ")
print ("Hey, "+invited[2].title()+"! Party's Still On! ")

# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to
# invite to dinner.
# Start with your program from Exercise 3-4 or Exercise 3-5. Add a print statement to the end of your program informing people
# that you found a bigger dinner table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.

print ("\nHey, "+invited[0].title()+"! I found a bigger table!")
print ("Hey, "+invited[1].title()+"! I found a bigger table! ")
print ("Hey, "+invited[2].title()+"! I found a bigger table! ")

invited.insert(0,'rishi')
invited.insert(2,'samarth')
invited.append('dhairya')
print ("So,The final list of all the people invited is: ")
print (invited)
print("And here are the final invitations: ")
print("Hey, "+invited[0].title()+"! We'll all be there by 7. Don't be late.")
print("Hey, "+invited[1].title()+"! We'll all be there by 7. Don't be late.")
print("Hey, "+invited[2].title()+"! We'll all be there by 7. Don't be late.")
print("Hey, "+invited[3].title()+"! We'll all be there by 7. Don't be late.")
print("Hey, "+invited[4].title()+"! We'll all be there by 7. Don't be late.")



print("\nIt's a disaster. I don't have place for more than 3 people including me.")
#Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list,
# print a message to that person letting them know youre sorry you cant invite them to dinner.
popping_invite1=invited.pop()
print("I'm sorry "+popping_invite1.title()+". Tonight's plans would not be possible.")
popping_invite2=invited.pop()
print("I'm sorry "+popping_invite2.title()+". Tonight's plans would not be possible.")
popping_invite3=invited.pop()
print("I'm sorry "+popping_invite3.title()+". Tonight's plans would not be possible.")
popping_invite4=invited.pop()
print("I'm sorry "+popping_invite4.title()+". Tonight's plans would not be possible.")
print("So, now i'm inviting only these 2 people:")
print(invited)
print("Hey "+invited[0].title()+", others will not be able to make it. I want you to come as i have place for only 2 more people.")
print("Hey "+invited[1].title()+", others will not be able to make it. I want you to come as i have place for only 2 more people.")
#Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty
#list at the end of your program.
del invited[0]
print ('\n')
print (invited)
del invited[0]
print(invited)






