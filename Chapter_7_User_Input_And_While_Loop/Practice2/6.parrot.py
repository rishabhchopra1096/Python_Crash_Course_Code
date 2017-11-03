prompt = "Tell me something and i will repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "

message = "" # Just so the while loop is entered.


while message != 'quit':
    message = raw_input(prompt)
    if message != 'quit':
        print(message)


# When we want ask question repeatedly unless some condition is True,
# We use the raw_input function INSIDE THE WHILE LOOP.