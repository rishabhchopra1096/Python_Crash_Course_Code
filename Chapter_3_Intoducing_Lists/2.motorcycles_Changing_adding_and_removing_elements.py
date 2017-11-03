#Most lists are dynamic.
# Removing aliens when they get shot down.
# Adding new ones as they enter the screen
# Aliens increase and decrease in length throughout
# the course of the game.

print "CHANGING:"
print "Format for changing: list_name[index_postion]=new_element"
motorcycles=['honda','yamaha','suzuki']
print motorcycles
#changin 1st element to ducati:
motorcycles[0]='ducati'
print motorcycles


print "ADDING:APPENDING:"
# Addig new aliens, new data to a visualization, pr add new registered users to a website.
#The simplest way to add a new element to a list is to append the item to the list
motorcycles=['honda','yamaha','suzuki']
motorcycles.append('ducati')
print motorcycles
#The .append method adds ducati to the end of the list without affecting the other
#elements of the list.
#Building lists this way is very common, because you often wont know the data your users
#want to store in a program until after the program is running. To put your users in control,
# start by defining an empty list that will hold the users values. Then append each new value
# provided to the list you just created.
print "Empty List Appeneded:"
print "format for appending: list_name.append(element_name)"
motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print motorcycles



print "INSERTING:"
#Now what do you do if you want to add an element to a certain position
#in the list?
#Inserting Elements into a List
#You can add a new element at any position in your list by using the insert()
# method. You do this by specifying the index of the new element and the value of the new item.
#This operation shifts every other value in the list one position to the right.
print"format for inserting: list_name.insert(index_postion,new_element_name)"
motorcycles=['honda','yamaha','suzuki']
print motorcycles
motorcycles.insert(0,'ducati')
print motorcycles
#format for inserting: list_name.insert(index_position , 'element_name')
# The insert operation first opens up space at the index and shift every element in the list to the right.
#Next, it inserts the element in the index position .



print "REMOVING:DEL:"
print "Format for removing an element using del: del list_name[index_postion)"
# When a player shoots down an alien, when a user cancels their account on a web application.
#If you know the position of the item you want to remove from a list, you can use the del statement.
# 2 ways to remove an element from a list:
#i)by postion
#ii)by value

motorcycles=['honda','yamaha','suzuki']
print motorcycles
del motorcycles[0] # by postion : Using the del statement.
print motorcycles
motorcycles.remove('yamaha') # by value : Using the remove statement.
print motorcycles
#Note: Once we have removed a value using the del statement, we can no longer access that item.



print "removing an Item Using the pop() Method"
print"Format for popping an item using the pop() method: variable name = list_name.pop()" # This will remove the last item on the list.
#The pop method allows you to remove an item from the list but it lets you work with that
#item after removing it.
# Its like a champagne bottle, you get to pop out the last element.


motorcycles=['honda','yamaha','suzuki']#list defined
print motorcycles#list printed
popped_motorcycles=motorcycles.pop()#pop a value from the list and store it in a variable popped_mototcycles
print motorcycles#shows value removed
print popped_motorcycles#still have access to removed element
#The output shows that the value 'suzuki' was removed from the end of the list and is now stored in the variable popped_motorcycle.
#How might this pop() method be useful? Imagine that the motorcycles in the list are stored in chronological order according
#to when we owned them. If this is the case, we can use the pop() method to print a statement about the last motorcycle we bought.
motorcycles=['honda','yamaha','suzuki']
last_owned="The last motor cycle i owned was a "+motorcycles.pop()+"."
print last_owned
#now -->capitalizing the name suzuki.
motorcycles=['honda','yamaha','suzuki']
last_owned="The last motor cycle i owned was a "+motorcycles.pop().title()+"."
print last_owned
#Lesson: A variable can be subjected to two methods like in the above^pop and title.




print "\nNow , if we try pop with string"
x="Hello , my name is Rishabh chopra"
print x
#my_sur_name=x.pop() #AttributeError: 'str' object has no attribute 'pop'
#print x
#print my_sur_name
#print "My sur name is "+x.pop().title()+"."
#Lesson: pop cannot be applied to strings.
x=["Hello", "," , "my" , "name" ,"is" ,"Rishabh" ,"chopra"]
print x
print x.pop()
#See .pop() works with a list but not strings.
#Lesson : pop , pops out that element and we can use it later.
#if we just use last_owned=motorcycles[2] , last_owned would be equal to suzuki only BUT it
#would still be a part of list->motorcycles.




print "\nPopping Items from any Position in a List"
print "Format for Popping Items from any Position in a List : variable_name = list_name.pop(index_postion)"
#You can actually use pop() to remove an item in a list at any position by including the index of the item you want to remove in parentheses.
motorcycles=['honda','yamaha','suzuki']
first_owned=motorcycles.pop(0)
print 'The first motorcycle i owned was a '+first_owned.title()+'.'
print motorcycles #see honda is popped away and stored in first_owned
#Remember that each time you use pop( ), the item you work with is no longer stored in the list.
#If youre unsure whether to use the del statement or the pop( ) method, heres a simple way to decide:
#when you want to delete an item from a list and not use that item in any way, use the del statement; if you
#want to use an item as you remove it, use the pop() method.

print "\nRemoving an Item by value"
print "Format to remove an item by value: list_name.remove(element_name)"
#When we only know that value and not the index or position of that value.
#for eg: I want to remove 'suzuki' from the list of motorcycles and i don't know that position -->
#i will do this:
motorcycles=['honda','yamaha','suzuki']
print motorcycles
motorcycles.remove('suzuki') # This line tells Python where the element 'suzuki' is and then removes it.
print motorcycles # see 'suzuki' removed.
#You can also use the remove() method to work with a value thats being removed from a list.
#Lets remove the value 'ducati' and print a reason for removing it from the list:
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati' #variable for ducati generated
motorcycles.remove(too_expensive) #you can use a variable also as an iput in a method
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

#The remove() method deletes only the first occurrence of the value you specify.
# If theres a possibility the value appears more than once in the list, youll need
# to use a loop to determine if all occurrences of the value have been removed.
#Youll learn how to do this in Chapter 7.















