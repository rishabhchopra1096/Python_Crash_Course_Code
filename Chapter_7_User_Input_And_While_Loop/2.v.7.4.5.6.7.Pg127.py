#6-7:
prompt="What topping would you like? "
prompt+="\nEnter 'quit' when you finish."
toppings=[]
active=True
while active:
    topping=input(prompt)
    if topping=='quit':
        active=False
    else:
        print ("Ok, "+topping+" will be added on your pizza.")
        toppings.append(topping)


if toppings: #This line means that "execute below code only if there is something in toppings"
    print("So here is the final list of toppings you want: ")
    for topping in toppings:
        print(topping)

#7-5:


