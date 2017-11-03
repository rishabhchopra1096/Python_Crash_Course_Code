prompt = "What is your age? "
prompt += "\nEnter 'quit' to close program."

age = 0

while True:
    age = raw_input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("The movie ticket is FREE for you.")
        elif 3 <= age < 12:
            print("The movie ticket is $10 for you.")
        elif age >= 12:
            print("The movie ticker is $15 for you.")


