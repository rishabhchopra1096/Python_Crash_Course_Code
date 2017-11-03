#FORMAT TO COPY A LIST:
# list_to_be_copied=['a','b','c']
# new_list=list_to_be_copied[:]


my_foods=['pizza','falafel','carrot cake']
friends_foods=my_foods[:]#copy made

print "My favourite foods are:"
print my_foods
print "\nMy friend's favourite foods are:"
print friends_foods
#both list will contain the same food
#The point of copying the list by slicing it without any indeces is that:
#when you copy a list, they both become independent of each other.
#Now , if i append an item to 1 list, it won't affect the other list.
#for example:
my_foods.append('canoli')
print("\nMy new favourite foods are:")
print
print "\nMy friend's favourite foods are:"
print friends_foods#will still remain the same , will not append canoli to it.
print "if you do not copy a list , x=y and y also gets appended:"
print"\notherwise if i do this:"
x=['pizza','falafel','carrot cake']
y=x
x.append('canoli')
print x
print y
print "Though we did not append'canoli' to y , it was added to y as x=y."

print "In python , = means assignment. So instead of copying the list , y was assigned to x."

#So if you do want to make a copy of a list without affecting that list:
#make a copy of that list by slicing it from beginning to end.
