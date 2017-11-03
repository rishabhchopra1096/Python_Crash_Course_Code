#Pg. 50
#3-8:Seeing the World
destinations=['greece','hawai','new zealand','belgium','new york','sydney']
print (destinations) # raw python list
print (sorted(destinations)) # alphabetically arranged, temporarily
print (destinations) # Original list, not affected
print (sorted(destinations,reverse=True)) # reverse alphabetically aranged, temporarily
print (destinations) # Original list, not affected
(destinations.reverse()) # reversing order permanently==>no output in print
print (destinations) # order reversed permanently
(destinations.sort()) # no output in print
print (destinations)
destinations.sort(reverse=True)
print (destinations)

#3-9: Dinner Guests:
# 3-4: contd.
invited=['rohan','ridhi','rhea']
print (len(invited)) # number of people invited, 3
#3-10 Every Function:
my_friends = ['manan','samarth','rishi','rohan','ankit','rhea','ira','ridhi']
#What are all the functions that i learnt:
#1. Changing a name:
my_friends[2]='shourya'
print (my_friends)
#2. Adding a name
my_friends.append('anisha')
print (my_friends)
# 3. Inserting a name
my_friends.insert(0,'dhairya')
print(my_friends)
# 4. Del a name
del my_friends[-1] #deleted 'anisha'
# 5.popping a name and saving it:
ridhi=my_friends.pop()
print (my_friends)
print (ridhi)
# 6. Removing a name
my_friends.remove('ankit')
print (my_friends)
# 7. using sorted to arrange them alphabetically, temporarily:
print (sorted(my_friends))
# 8. using sorted to reverse the alphabetical order , temporarily:
print (sorted(my_friends,reverse=True))
print (my_friends) # Orignal list not affected
#9. reverse method:
my_friends.reverse() # Reversing order of list
print (my_friends) # order reversed permanently
#10. sort() method:
my_friends.sort() # arranging alphabetically permanently
print (my_friends) # arranged alphabetically permanently
#11.len function:
print ("number of friends i have left in the list: ")
print (len(my_friends))














