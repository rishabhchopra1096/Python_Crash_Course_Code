print "Making Numerical Lists: "
# Keep track of positions on each character in a game.
print("Usiung the range function:")
#range() function makes it easy top generate a series of number.
for value in range(1,5):
    print value
#this function starts at the first agrgument and stops aty the last argument so 5 does not get printed.
# The range function makes a list of numbers starting from the first parameter till the second parameter-1.
print "Using range() to Make a List of Numbers"
#Wr can use list() to convert the above set of nummber into a list.
#There is no necessity to use the list function below. As the range function returns a list only.
numbers=list(range(1,5))
print numbers
print range(1,5)
print range(1,5)[1]
print numbers[1]




digits=range(0,10)
print(digits[:4])
print(digits[8:])