#We can also use the range() function to tell Python to skip numbers in a given range.
# For example, heres how we would list the even numbers between 1 and 10:
# FORMAT FOR SKIPPING NUMBERS:
# range(starting_integer,ending_integer,skip_integer)


even_numbers=list(range(2,11,2))
print even_numbers
print "printing list of odd number from 1 to 10"
odd_number=list(range(1,10,2))
print odd_number
#In this example, the range() function starts with the value 2 and then adds 2 to that value.
#It adds 2 repeatedly until it reaches or passes the end value, 11, and produces this result.






