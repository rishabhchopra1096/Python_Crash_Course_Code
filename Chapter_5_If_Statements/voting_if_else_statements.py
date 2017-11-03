#If Statements:
#Several number of if statements exists and your choice of which to use
#depends on the number of conditions you need to test.
print "Format for simplest kind of if statement :"
print "if conditional_test:"
print "   do something"
#You can put any conditional test in the first line and just about any action in the indented block following the test.
# If the conditional test evaluates to True, Python executes the code following the if statement.
#If the test evaluates to False, Python ignores the code following the if statement.

age=19
if age>=18: # YOU ALWAYS FORGET THE COLON. DONT FORGET THE COLON.
    print "You are old enough to vote!"
#You can have as many lines of code as you want in the block following the if statement.
# Lets add another line of output if the person is old enough to vote, asking if the individual
#has registered to vote yet:
    print "Have you registered your vote, yet?"

print "If-else Statements:"
print "This is used when we want one action when a test passes and a different action in all other cases."
print "The else allows you to define an action or a set of actions that are executed when the conditional test fails."

age=17
if age>=18:
    print "You are old enough to vote!"
    print "Have you registed your vote, yet?"
else:
    print "Sorry, you are too young to vote."
    print "Please register to vote as soon as you're 18."
# If the conditional test passes, the first block of indented print statements is executed. If the test evaluates to False,
# the else block is executed. Because age is less than 18 this time, the conditional test fails and the code in the else block
# is executed.



