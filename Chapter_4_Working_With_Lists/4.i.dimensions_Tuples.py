#Tuples are list that are permanent in nature. They cannot change.
#Format : ( x ,y,5,4,b,6,7,v )->Just like list , except parentheses used
#instead of square brackets.
#this is a tuple that makes sure that the dimensions of rectangle never
#change:
dimensions=(200,50)
print dimensions[0]
print dimensions[1]
#Trying to change an element of tuple:
#dimensions[0]=250  TypeError: 'tuple' object does not support item assignment
print dimensions[0]#still 200
#This is beneficial because we want Python to raise an error when a line
#of code tries to change the dimensions of the rectangle.
print "Looping Through All Values in a Tuple"
for l_or_b in dimensions:
    print l_or_b

print "Writing over a Tuple"
#If you cannot modify a tuple , you can reassign it by changing the value
#of the variable that holds the tuple.
dimensions=(400,100)
print "\nModified dimensions are:"
print dimensions
#overwriting a variable is valid.
#When compared with lists, tuples are simple data structures. Use them when
#you want to store a set of values that should not be changed through- out the
#life of a program.
