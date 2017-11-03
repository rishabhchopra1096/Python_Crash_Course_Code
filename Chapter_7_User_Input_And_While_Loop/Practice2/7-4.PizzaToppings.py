prompt1 = "Which topping would you like on your pizza?"
prompt1 += "\nEnter 'quit' when done."

prompt2 = "What else ? "
prompt2 += "\nEnter 'quit' when done."

add_on = ""
toppings = []

while add_on != 'quit':
    topping = raw_input(prompt1)
    if topping != 'quit':
        toppings.append(topping)
        print(topping.title() + " will be added to your pizza.")
        while True:
            add_on = raw_input(prompt2)
            if add_on != 'quit':
                toppings.append(add_on)
                print(topping.title() + "will be added to your pizza.")
            else:
                break
    else:
        break

print("Here are the topppings you wanted:")
for topping in toppings:
    print(topping.title())






