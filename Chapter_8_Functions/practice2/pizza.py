# If you want a function to accept several different
# kinds of arguments , the parameter that accepts the arbitrary
# number of arguments , must be placed last.

# Python matches postional and keyword arguments first.
# And then , collects any remaining arguments ion the final
# parameter.

def make_pizza(size,*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
     "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16,'peeroni')



