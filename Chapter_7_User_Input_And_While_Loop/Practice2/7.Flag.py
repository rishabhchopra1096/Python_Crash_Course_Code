# One variable that determines weather or not the entire progam
# is active

# When Flag is set to True ==> Program will run.
# When Flag is set to False ==> Program will stop.
# Advantage : Our while statement needs to check only one condition.

prompt = "Tell me something and i will repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "

active = True # Flag


while active: # Meaning while active == True.
    message = raw_input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)


