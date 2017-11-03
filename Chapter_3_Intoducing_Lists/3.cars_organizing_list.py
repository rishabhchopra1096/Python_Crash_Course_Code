#Python provides a number of different ways to organize your lists, depending on the situation.
#Pythons sort() method makes it relatively easy to sort a list. Imagine we have a list of cars
#and want to change the order of the list to store them alphabetically.
print ("SORTING A LIST permanently with sorted() METHOD")
#TAKEAWAY:
#1. sort method : list_name.sort() --> sorts the list in alphabetical order

#2. sort method with input reverse=True : list_name.sort(reverse=True)-->reverse alphabetical order.
##-------------#
cars=['bmw','audi','toyota','subaru']
print cars
cars.sort()
print (cars)
#The sort() method, shown, changes the order of the list permanently.
#You can also sort this list in reverse alphabetical order by passing the argument reverse=True to the sort() method.
cars=['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print (cars)



print "Sorting a List Temporarily with the sorted() FUNCTION"
#TAKEAWAY:
#3. Sorted function: sorted(list_name)--> printing this function with the input as a list:
# arranges it in alphabetical order, temporarily.
#The original list is not affected.
#4. Sorted function used to reverse alphabetical order, temporarily: sorted(list_name,reverse=True)
#-------------#
cars=['bmw','audi','toyota','subaru']
print "Here's the original list:"
print cars
print ("\nHere is the sorted list:")
print sorted(cars) #above we did cars.sort() cause sort is method, here the list is an input of the FUNCTION sorted.
#print cars.sorted #AttributeError: 'list' object has no attribute 'sorted'
print "Here is the original list again:"
print cars
#Notice that the list still exists in its original order after the sorted() function has been used.
#The sorted() function can also accept a reverse=True argument if you want to display a list in reverse alphabetical order.
print sorted(cars ,reverse=True) #since there are 2 arguments , we use a comma.
#Sorting a list alphabetically is a bit more complicated when all the values are not in lowercase.
#There are several ways to interpret capital letters when youre deciding on a sort order, and specifying the exact order can be more complex than
#we want to deal with at this time. However, most approaches to sorting will build directly on what you learned in this section.



print "Printing a List in Reverse Order"
#TAKEAWAY:
# 5. Using reverse method to reverse the order of the elements of a list:
# --> list_name.reverse()
# 6. reverse() takes no keyword arguments. Meaning you can't use reverse=True in
# this method. Anyway, it will just neutralise this method.
# 7. #The reverse() method changes the order of a list permanently, but you can revert to the original order anytime by applying reverse() to the same list a second time.
#-------------#
#To reverse the original order of a list, you can use the reverse() method.
#If we originally stored the list of cars in chronological order according to when we owned them, we could easily rearrange the list into
# reverse chronological order:
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print cars
#cars.reverse(reverse=True)
#print cars

print "Finding the Length of a List"
#TAKEAWAY:
# 8. Used to identify number of aliens you need yo shoot down in a game OR
# determine the ammoung of data OR figure out the number of registered users on the
# website.
# 9. len returns the number of elements in a list or the number of characters in a string.
#-------------#
#using the len FUNCTION-we get the length of the list.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print len(cars)
#Youll find len() useful when you need to identify the number of aliens that still need to be shot down in a game, determine the amount of data you have to manage in
#a visualization, or figure out the number of registered users on a website, among other tasks.

#Note: Index errors: means Python cant figure out the index you requested. If an index error occurs in your program, try adjusting the index youre asking for by one.
#Then run the program again to see if the results are correct.
#Keep in mind that whenever you want to access the last item in a list you use the index -1.
#If an index error occurs and you cant figure out how to resolve it, try printing your list or just printing the length of your list. Your list might look much different
# than you thought it did, especially if it has been managed dynamically by your program. Seeing the actual list, or the exact number of items in your list, can help you sort
#out such logical errors.
#For example:
#cars = ['bmw', 'audi', 'toyota', 'subaru']
#print cars[4]--> there is not 4th index.
#Next example:
#cars=[]
#print cars[-1]-->there is no last index since it is an empty list.

#In this chapter you learned what lists are and how to work with the individual items in a list. You learned how to define a list and how to add and remove elements.
#You learned to sort lists permanently and temporarily for display purposes.
#You also learned how to find the length of a list and how to avoid index errors when youre working with lists.
# Chapter 4 youll learn how to work with items in a list more efficiently.
# By looping through each item in a list using just a few lines of code youl be able to work efficiently, even when your list contains thousands or millions of items.






