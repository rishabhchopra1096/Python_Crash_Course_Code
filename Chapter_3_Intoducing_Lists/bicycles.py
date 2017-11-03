#1.What is a list?
# A list is a collection of items in a particular order.
# It should have a plural name such as letter, digits, names.
#In Python, square brackets indicate a list, and individual elements in the list are separated by commas.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)



#2.Because this isnt the output you want your users to see, lets learn how to access the individual items in a list.
#To access an element in a list, write the name of the list followed by the index of the item enclosed in square brackets.
# To access an element in a list : name_of_list[index_postion].
print bicycles[0]
#When we ask for a single item from a list, Python returns just that element without square brackets or quotation marks.


#3. We can use the sting methods such as title,upper,lower,etc. on individual elemements in the list.
print bicycles[0].title() #prints the 1st element of the list , with first letter uppercase


#4.index positions star at 0,not 1-->
#index postion= original position-
# From the left , index starts from 0,
# From the right, index starts from -1.
print bicycles[-1]
print bicycles[-2]#second last and so on ..

#Now , How to use individual values of a list for a message? Simple:
message="My first bicycle was a "+bicycles[0].title()+"."
print message
#At 17, we build a sentence using the value at bicycles[0] and store it in the variable message.



