''' We can make the program run as long as the user wants to by putting
# most of the program inside the while loop.
# Well define a quit value and then keep the program running as long
# as the user has not entered the quit value.'''

prompt = "\nTell me something, and i will repeat it back to you: "
prompt +="\n Enter 'quit' to end the program."
# First we have entered the two prompts with the two options.
message="" # This will store whatever the value user will enter.
        '''We have defined it as an empty string so that python has something to check
        # for before going into the loop.'''
        #he first time the program runs and Python reaches the while statement, it needs
         # to compare the value of message to 'quit', but no user input has been entered yet.
         # If Python has nothing to compare, it wont be able to continue running the program.
         # To solve this problem, we make sure to give message an initial value. Although its just
         # an empty string, it will make sense to Python and allow it to perform the comparison that
         # makes the while loop work.
         # Note: Nothing has been printed yet.
         # If you comment out the following lines, this program will be blank.
         # In the terminal also.
while message!='quit': '''# First time the loop enters , the message is a blank string.
                        #That is the reason it is able to enter the while loop.'''

    message=input(prompt)#This tells the python interpreter that the variable message stands for #an input value And also gives the first prompt.
    if message!='quit': '''if statement was added later to stop from printing 'quit''''
        print (message)             # This is the first time something is printed in the terminal or build.
'''If you enter any string saying anything , it will repeat what you entered WITHOUT QUOTES. Foreg: 'hello'
# And then it wil go back to the beginning of the while loop. Now the value of message is not a blank string,
# it is 'hello'which is != 'quit' so it will enter the loop again.
# Now if i enter 'quit' , it will print/repeat 'quit' without quotes. Then it will go back to the beginning of the
# while loop. Now the value of message='quit' which is why it will not enter the loop and the program ends.
# To remove the problem of quit being printed , an if statement'''
'''To solve the problem of quit being printed before the program ends, we add a simple if statement. if message!='quit' '''


