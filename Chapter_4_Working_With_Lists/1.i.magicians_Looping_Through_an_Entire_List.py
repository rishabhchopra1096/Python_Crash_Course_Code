#Youll often want to run through all entries in a list, performing the same task with each item.
#For example, in a game you might want to move every element on the screen by the same amount,
#or in a list of numbers you might want to perform the same statistical operation on every element.
# Or perhaps youll want to display each headline from a list of articles on a website.
#When you want to do the same action with every item in a list, you can use a for loop.
#Lets say we have a list of magicians names, and we want to print out each name in the list.
#We could do this by retrieving each name from the list individually, but this approach could cause several problems. For one,
#it would be repetitive to do this with a long list of names. Also, wed have to change our code each time the lists length changed.
# A for loop avoids both of these issues by letting Python manage these issues internally.

print "\nUsing the for loop :"
#IMP : #When you want to do the same action with every item in a list, you can use a for loop.

magicians=['alice','david','carolina'] #list defined
for magician in magicians: #this line tells Python to pull a name from the list magicians, and store it in the variable magician.
    print(magician)         #This Line tells Python to print the name it just stored in magician.
#Python then repeats lines and once for each name in the list till there are no more elements in the list.
# Read this code as: Line 15:"For" "every magician" "in" "the list of magicans". Line 16: Print the magician's name.




print "\nA closer look at looping"
#The steps in the for loop are repeated once for each element in the list.
#Any name can be chosen for the temporary variable. Itis wise to choose a meaningful name.
# eg: for singular(shoe) in plural(shoes)
#               print(shoe)




print "\nprinting a message to each magician, telling them that they performed a great trick"
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print magician.title()+", that was a great trick!"
#Every line indented following the for magician in magicians is cosidered INSIDE THE LOOP,
# and each indented line is executed once for each value in the list.
    print "I can't wait to see your next trick, "+magician.title()+".\n"
#Any lines of code after the for loop that are not indented are executed once without repetition. Lets write a thank you to the group of magicians as a whole,
# thanking them for putting on an excellent show. To display this group message after all of the individual messages have been printed, we place the thank you message after the for loop without indentation.
print "Thank you, everyone.That was a great magic show!"
#As the above line is not indented , it is executed only once.

#When youre processing data using a for loop, youll find that this is a good way to summarize an operation that was performed on an entire data set.
# For example, you might use a for loop to initialize a game by running through a list of characters and displaying each character on the screen.
#You might then write an unindented block after this loop that displays a Play Now button after all the characters have been drawn to the screen.

print "AVOIDING INDENTATION ERRORS"
#people sometimes indent blocks of code that dont need to be indented or forget to indent blocks that need to be indented
#EXAMPLE 1: Forgetting to Indent
#magicians = ['alice', 'david', 'carolina']
#for magician in magicians:
#print(magician)
#OUTPUT:
#File "magicians.py", line 3
#       print(magician)
#           ^
#   IndentationError: expected an indented block
#EXAMPLE 2:Forgetting to Indent Additional Lines
#magicians = ['alice', 'david', 'carolina']
#   for magician in magicians:
#   print(magician.title() + ", that was a great trick!")
#print("I can't wait to see your next trick, " + magician.title() + ".\n") #not indented.
#OUTPUT:
#Alice, that was a great trick!
#   David, that was a great trick!
#   Carolina, that was a great trick!
#   I can't wait to see your next trick, Carolina. #since last value of magician was carolina.
#EXAMPLE 3: Indenting Unnecessarily Pg.59
#EXAMPLE 4: Forgeting the colon Pg.60



