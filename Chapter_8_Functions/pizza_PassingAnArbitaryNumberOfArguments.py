
# def make_pizza(*toppings):
#     "Print the list of toppings that have been requested"
#     print(toppings)


# make_pizza('mushroom')
# make_pizza('tomato','onion,''capsicum')
# Output:
# ('mushroom',)
# ('tomato', 'onion,capsicum')

#Now if i want to loop through the aruments:
# def make_pizza(*toppings):
#     """Make a summary of the pizza"""
#     print("Make a pizza with the following toppings")
#     for topping in toppings:
#         print("-->"+topping)

# make_pizza('mushroom')
# make_pizza('tomato','onion,','capsicum')

# Output:
# Make a pizza with the following toppings
# -->mushroom
# Make a pizza with the following toppings
# -->tomato
# -->onion,
# -->capsicum

#Mixing Positional and Arbitary Arguments:
#If the function make_pizza needs to take in a size for the pizza, that
#parameter must come before the parameter *toppings:

def make_pizza(size,*toppings):
    """Make a summary of the pizza"""
    print("Make a "+str(size)+"-inch pizza with the following toppings")
    for topping in toppings:
        print("-->"+topping)

make_pizza(21,'mushroom')
make_pizza(40,'tomato','onion,','capsicum')


