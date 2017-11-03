from dog1 import Dog
from Instance2 import my_dog

# We access the attributes of an instance using the dot notation.
print("\n" + my_dog.name.title())
# Here , Python looks at the instance my_dog and the finds the attribute name associated with my_dog.

'''Calling Methods'''
# After we crate an instance from the class Dog, we can use dot notation to call any method defined in Dog.
my_dog.sit()