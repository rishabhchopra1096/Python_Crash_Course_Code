prompt = "Please enter the name of a city that you have visited."
prompt += "\nEnter 'quit' to quit the program. "

while True:
    city = raw_input(prompt)
    if city == 'quit':
        break
    else:
        print("I would love to go to " + city.title() + "!")

