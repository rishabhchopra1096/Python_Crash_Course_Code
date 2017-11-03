# Keyword Arguments free you up from constantly ordering your
# arguments with repsect to the parameters.

def describe_pet(animal_type,pet_name):
    """Display information about a pet"""
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('dog','lexus')
# Here if i messup the order of the arguments:
# I may end up with : I have a lexus. His name is Dog.
# Now, lets call describe_pet() by using keyword arguments.
# Each of the below will display the same output , no matter the
# order.
describe_pet(animal_type = 'dog',pet_name = 'mimi')
describe_pet(pet_name = 'mimi' , animal_type = 'dog')

