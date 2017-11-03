def make_pizza(size,*toppings):
    """Summarize the pizza we are about to make:"""
    print("Make a "+str(size)+"-inch pizza with the following toppings:")
    for topping in toppings:
        print("-->"+topping)

