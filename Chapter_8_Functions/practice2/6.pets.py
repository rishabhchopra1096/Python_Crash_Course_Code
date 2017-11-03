def describe_pet(pet_name , animal_type = 'dog'):
    """Displayt information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type +"'s name is " + pet_name.title() +
     ".")

# Postional , keyword, defautl can all be used together.
# With this definition , an argument always needs to be provided
# for pet_name and this value can be provided using positional
# or keyword format.
'''A dog named Lexus'''
# postional :
describe_pet('lexus')
# keyword :
describe_pet(pet_name = 'lexus')
# If the animal being described is not a dog ,  an argument for
# animal_type must be also included in the call.
# Again this argument can be postional or keyword.
'''A cat named Lexus'''
# Postional:
describe_pet('lexus','cat')
# Keyword
describe_pet('lexus',animal_type = 'cat')


# It does not really matter which calling style you use.
# As long as your function calls produce the output you want.
# Just use the style find easiest to understand.

