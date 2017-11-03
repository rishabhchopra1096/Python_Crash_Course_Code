#In Python, square brackets indicate a list, and individual elements in the list are separated by commas.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
#Because this isnt the output you want your users to see, lets learn how to access the individual items in a list.
#To access an ele- ment in a list, write the name of the list followed by the index of the item enclosed in square brackets.
print bicycles[0]
#When we ask for a single item from a list, Python returns just that element without square brackets or quotation marks:
print bicycles[0].title() #prints the 1st element of the list
#index positions star at 0,not 1-->
#subtract 1 from actual position to get index position.
#To check from the right side of a list or the lasr element
#of the list--> start with -1 index position-->will return last element
print bicycles[-1]
print bicycles[-2]#second last and so on ..

#Now , How to use individual values of a list for a message? Simple:
message="My first bicycle was a "+bicycles[0].title()+"."
print message
#At 17, we build a sentence using the value at bicycles[0] and store it in the variable message.



