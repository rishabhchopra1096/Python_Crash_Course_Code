print "make a list of the first 10 square numbers (that is, the square of each integer from 1 through 10). In Python, two asterisks (**) represent exponents."
one_to_ten=list(range(1,11)) # Making a list of numbers from 1 to 10.
square_one_to_ten=[] #making an empty list to append the squares in later.
for number in one_to_ten: #OR for value in range(1,11)-->for loops work on ranges too.
    square=number**2 # for the first time, number=1, square =number**2 ==> 1=1**2
    square_one_to_ten.append(square) #appending sqaured number.
#Now it will keep squaring the numbers till 10.
# each time the variable square will represent the value of the square og the next number in the list.
#And that value stored in square will be appended to square_one_to_ten list
#Once the loop has no more values after 10, it will shift to the next command in python.
#Which will be to print the list appended with all the sqaured values.

print square_one_to_ten

# Note: ** represents exponents. So the same program can be used to write
# a list of cubic values from 1 to 10.

#SEE explanation at page 62.
#Now , how can we make the code shorter ?
#squares = []
#   for value in range(1,11):
#       squares.append(value**2)
#print(squares)

#You can use either of the two approaches when making complex lists.
# Sometimes , a temporary variable(square in the first way) is useful to make code
#easy to read. In other case it just makes the code unnecessarily long.
# ALWAYS FOCUS ON WRITING THE CODE THAT YOU UNDERSTAND CLEARLY,WHICH DOES WHAT YOU
#WANT IT TO DO. THEN , FOCUS ON HOW TO MAKE IT SHORTER, MORE EFFICIENT.



