while True:
    try:
        first_number = raw_input("Give me two numbers and i will add them." +
            "\nEnter 'quit' to quit program anytime."+
            "\nFirst Number: ")
        if first_number == 'quit':
            break
        else:
            first_number = int(first_number)
        second_number = raw_input("Second Number: ")
        if second_number == 'quit':
            break
        else:
                second_number = int(second_number)
    except ValueError:
        print("You wrote in a word. Type in a number next time.")
        continue
    else:
        print(first_number + second_number)


'''What the try block does:'''
# First it tells the user what the program will do.
# Next, it tell the use that he/she can quit at anytime.
# Next, It asks for the first number.
# Now if the user enters: 'quit'
# The program will exit/break.
# Till here , if the user has entered a non-integer value except 'quit'..
# The program will go to the first else block(first_number = int(first_number)
# Here, it will catch the error (ValueError) , if there is any.
# Similarly: The process is same for second_number.
# Anytime a ValueError comes due to entering non-integer value(except 'quit'):
# The program shift to the except block.
'''What the except block does'''
# Anytime a ValueError comes due to entering non-integer value(except 'quit'):
# The program shift to the except block.
# 1.the except block displays a friendly message telling the user to enter a number instead
# of a word next time.
# 2. continue: Goes back to the starting of the loop and prompts for first number again.
# Starts the whole program again.
'''What the else block does:'''
# If no error occurs, it prints the sun of the 2 numbers.

# if first_number != 'quit':
#     second_number = raw_input("Second Number: ")
#     if second_number != 'quit':
#         second_number = int(second_number)
#         print(first_number + second_number)
