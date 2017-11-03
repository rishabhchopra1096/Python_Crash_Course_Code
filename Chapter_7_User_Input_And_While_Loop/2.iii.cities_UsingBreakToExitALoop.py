'''In more complicated programs:There can be more than one reason for a program to end'''
'''If many possible events might occur to stop the prgram, trying to test all these conditions
in one while statement becomes complicated and difficult'''
'''For a program that shyould run only as long as many conditions are true, you can define one
variable that determines whether or not the entire program is active. This variable, called a flag,
acts on a signal to the program'''
'''We can write our prgrams so they run while the flag is set to true. And stop the program when any of the event sets the value of flag to false.
As a result, our overall while statement needs to check only one condition, whether or not our flag is currently true.'''
'''Then, all our other tests (to see if an event has occurred that should set the flag to False) can be neatly organized in the rest of the program.'''

'''To exit a while loop immediately without running any remaining code in the
loop, regardless of the results of any conditional test, use the break statement.
The break statement directs the flow of your program; you can use it to control
which lines of code are executed and which arent, so the program only executes
code that you want it to, when you want it to.'''

prompt="\nPlease enter the name of a city you have visited: "
prompt+="\nEnter 'quit' when you are finished. "

while True: '''A loop that starts with while True will run forever unless it reaches a break statement.'''
    city=input(prompt) # The loop in this program continues asking the user to enter the names of cities theyve been to until they enter 'quit'.
    if city == 'quit':
        break           #When they enter 'quit', the break statement runs, causing Python to exit the loop
    else:
        print ("I'd love to go to "+city.title()+"!")

# Rishabhs-MacBook-Pro:Chapter_7_User_Input_And_While_Loop rishabhchopra$ python cities_UsingBreakToExitALoop.py

# Please enter the name of a city you have visited:
# Enter 'quit' when you are finished. 'hello'
# I'd love to go to Hello!'

# Please enter the name of a city you have visited:
# Enter 'quit' when you are finished. hello
# Traceback (most recent call last):
#   File "cities_UsingBreakToExitALoop.py", line 8, in <module>
#     city=input(prompt) # The loop in this program continues asking the user to enter the names of cities theyve been to until they enter 'quit'.
#   File "<string>", line 1, in <module>
# NameError: name 'hello' is not defined

# Rishabhs-MacBook-Pro:Chapter_7_User_Input_And_While_Loop rishabhchopra$ python cities_UsingBreakToExitALoop.py

# Please enter the name of a city you have visited:
# Enter 'quit' when you are finished. 'new delhi'
# I'd love to go to New Delhi!'

# Please enter the name of a city you have visited:
# Enter 'quit' when you are finished. 'quit'


#You can use the break statement in any of Pythons loops. For example, you could use break to quit a for loop
#thats working through a list or a dictionary.
