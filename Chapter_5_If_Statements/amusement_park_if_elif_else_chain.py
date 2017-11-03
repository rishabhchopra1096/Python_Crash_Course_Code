# if-elif-else chain
# Python executes only one block in an if elif else chain.
# an if-elif-else chain evaluates more than two situations.
# it will run each test to see which one passes first.
# but when a test passes , python skips the rest of the tests.
# For example, consider an amusement park that charges different rates for different age groups:
# Admission for anyone under age 4 is free.
# Admission for anyone between the ages of 4 and 18 is $5.
# Admission for anyone age 18 or older is $10.

print "How can we use an if statement to determine a persons admission rate?"
age=18

if age<4:
    print "Your entry is Free!"
elif age<18: #Notice, we did not write age<18 and age>4 cause if the first block is not true ,
            #then only will python come to the elif.
    print "Your entry fee is $5"
else: # else does not have any condition. it is the last alternative.
    print "Your entry fee is $10"

# The if test tests whether a person is under 4 years old. If the test passes, an appropriate message
#  is printed and Python skips the rest of the tests. The elif line  really another if test, which runs
#   only if the previous test failed. At this point in the chain, we know the person is at least
# 4 years old because the first test failed. If the person is less than 18, an appropriate message
# is printed and Python skips the else block. If both the if and elif tests fail, Python runs the code
#  in the else block
# In this example the if and elif test evaluates to False, so its code block is not executed.
# Hence , the python interpreter comes to the last alternative -->The else statement.

# It would be more consise to set the price inside the if-elif-else chain rather the whole message.
#we can print the message just once.

age=12
if age<4:
    price = 0
elif age<18:
    price = 5
else:
    price = 10

print "Your entry fee is $"+str(price)+"."
#Here we use str() cause we can contenate strings with strings but cannot concatenate strings with integers or
#variable values equal to integers.
#To change the text of the output message, you would need to change only one print statement rather than
#three separate print statements.

print "Using Multiple elif Blocks "
# elif blocks are the way you can use to implement new conditions -> they are a way to enter multiple if statements.
# make sure elif comes before else. Else is the conclusion , the last alternative.
age=65
if age<4:
    price = 0
elif age<18:
    price = 5
elif age>=65:
    price = 5
else:
    price = 10

print "Your entry fee is $"+str(price)+"."
# OR:
# age = 12
#    if age < 4:
#        price = 0
#    elif age < 18:
#        price = 5
# uelif age < 65: price = 10
# v else:
# price = 5
#    print("Your admission cost is $" + str(price) + ".")


print "Omitting the else Block"
# Python does not require an else block at the end of an ifelif chain.
# Sometimes an else block is useful; sometimes it is clearer to use an
# additional elif statement that catches the specific condition of interest.
age=65
if age<4:
    price = 0
elif age<18:
    price = 5
elif age>=65:
    price = 5
elif age>=18:
    price = 10


print "Your entry fee is $"+str(price)+"."
#Lesson : always check the order of your elif statments to check if your chain derives
#the results you want it to derive.
#Lesson :An extra elif statement is always better than an else statement as it specifies
#what you want to in your results. Using elif creates greater confidence and produces errors
# if any malicious data appears as an input.
# for example , if i enter an alphabet in age , with the else statement , it will say that i
# have to pay $10 eventhough i did not enter an actual number as my age.



