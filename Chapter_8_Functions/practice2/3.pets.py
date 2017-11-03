def describe_pet(animal_type,pet_name):
    """Display information about a pet"""
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('dog','lexus')


#Calling function multiple times is an efficeint way to work.
# Anytime you want to describe a new pet, you have this function.
# Just 1 line of calling the function is required.

