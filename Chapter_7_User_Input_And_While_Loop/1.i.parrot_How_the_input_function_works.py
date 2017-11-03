# In this chapter youll learn how to accept user input so your program can then work with it.
# When your program needs a name, youll be able
# to prompt the user for a name.
# When your program needs a list of names,
# youll be able to prompt the user for a series of names.
# To do this, youll use the input() function.
#Youll also learn how to keep programs running as long as users want them to,
#  so they can enter as much information as they need to; then, your program can work with
#  that information. Youll use Pythons while loop to keep programs running as long as certain
# conditions remain true.
# The input function along with the while loop will help in writing fully interactive programs.

print "How the input() function works"
#The input function just pauses the program and waits for the user to enter some text.
#Once Python recieves the input , it stores it in a variable to make it convenient for you to work with.
# The following program asks the user to enter some text, then displays that message back to user.
message=input("Tell me something, and i will repeat it back to you:")
print message
# The input() function takes one argument: the prompt, or instructions, that we want to display to the user
# so they know what to do. In this example, when Python runs the first line, the user sees the prompt Tell me something,
# and I will repeat it back to you: . The program waits while the user enters their response and continues after the user presses ENTER.
#  The response is stored in the variable message, then print(message) displays the input back to the user.
# Sublime Text doesnt run programs that prompt the user for input. You can use Sublime Text to write programs that prompt for input, but
# youll need to run these programs from a terminal. See Running Python Programs from a Terminal on page 16.
