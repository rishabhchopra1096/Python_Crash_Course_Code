# Sometimes you don't know how many items does a fraction
# need to accept.

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)


make_pizza(make_pizza("peperoni"))
# Python will pass theargument in a tuple eventhough only one
# arguent is given.
make_pizza(make_pizza("mushroom",'green peppers','extra cheese'))

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)

# def make_pizza(*toppings):
#     """Summarize the pizza we are about to make."""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + str(topping))


print(make_pizza("peperoni"))
# Python will pass theargument in a tuple eventhough only one
# arguent is given.
print(make_pizza("mushroom",'green peppers','extra cheese'))



