#Postional Arguments:
def describe_pet(animal_type,pet_name):
    """Display information about a pet"""
    print("\nI have a "+animal_type+".")
    print("\tMy "+animal_type+"'s name is "+pet_name+".")
describe_pet('Labrador','Lexus')
# See we entered the arguments  in the order of the parameters.
# labrador corresponds to animal_type and 'Lexus' corresponds to pet_name.

#Using KEYWORD ARGUEMENTS:
describe_pet(pet_name="Lexus",animal_type='Labrador')
#Now , notice: Eventhogugh you entered the parameters in a different order,
# you assigned them values withing paratheses. So , therefore , you got the same output.

#DEFAULT VALUE
def describe_pet(pet_name,animal_type='dog'):
    print("\nI have a "+animal_type+".")
    print("\tMy "+animal_type+"'s name is "+pet_name+".")

describe_pet('mimi') #for my dog
describe_pet('lexus') #for my dog
describe_pet(animal_type='cat',pet_name='whiskers')#For a cat

