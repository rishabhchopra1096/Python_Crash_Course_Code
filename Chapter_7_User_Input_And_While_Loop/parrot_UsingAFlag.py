'''In more complicated programs:There can be more than one reason for a program to end'''
'''If many possible events might occur to stop the prgram, trying to test all these conditions
in one while statement becomes complicated and difficult'''
'''For a program that shyould run only as long as many conditions are true, you can define one
variable that determines whether or not the entire program is active. This variable, called a flag,
acts on a signal to the program'''
'''We can write our prgrams so they run while the flag is set to true. And stop the program when any of the event sets the value of flag to false.
As a result, our overall while statement needs to check only one condition, whether or not our flag is currently true.'''
'''Then, all our other tests (to see if an event has occurred that should set the flag to False) can be neatly organized in the rest of the program.'''




prompt = "\nTell me something, and i will repeat it back to you: "
prompt +="\n Enter 'quit' to end the program."

active=True


#while message!='quit':
while active: #True --> in other words #while True #As long as the active variable remains True, the loop will continue running.
    message=input(prompt) # Tells message will prompt
    if message =='quit': # True/False depending on message
        active = False
    else:
        print (message)

#As long as the variable active remains True , the loop will keep running.
# If the user enters 'quit' , we set active to False and the while loop storps.
# If the user enters anything other than 'quit' , we print their input as message.
# Now , my question is that what does while active mean?
# I think it would be better if it would be --> while active == True:
# Cause now , even if we enter 'quit' --> The value of active becomes false but
# the condition to enter the while loop is while active: , which is not substantial information ;
# what does it mean? Does it mean while active==True? or while active?What?
# I think , False means the program will not go on.
# Even when i replace the first active value to False and the second to true ,the program does not run:
# This could mean that if the condition=false , the program will not run.