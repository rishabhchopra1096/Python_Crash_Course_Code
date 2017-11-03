# the if-elif-else chain is efficient to the extent of one condition as
# As soon as python finds out that one test is true , it skips the rest of the test.
# However , when its important to check for all the conditions to be true , you can just
# add a series of simple if statements with no elif or else block.
# this works only when more than one codition could be true AND you want to act on all the
#True conditions.

requested_toppings = ['mushroom','extra cheese']
if 'mushroom' in requested_toppings:
    print "Adding mushrooms."
if 'peperoni' in requested_toppings:
    print "Adding peperoni."
if 'extra cheese' in requested_toppings:
    print "Adding extra cheese."

print "\nYour pizza is ready."

#Now , this code would have stopped running after the first 'mushroom' test if we had used elif.
# We wanted to print command for all toppings in the list.
# In summary, if you want only one block of code to run, use an if-elif- else chain. If more than
# one block of code needs to run, use a series of independent if statements.

