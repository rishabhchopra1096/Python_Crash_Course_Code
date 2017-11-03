# Object oriiented programming is one of the most effective
# approaches to writing soft-ware.

# In object oriented programming , you write classes that represent real world things and situations.

# You create objects based on these classes.

# When you write a class,  you define the general behavior that a whole category of objects can have.

#You can then give each object whatever unique traits you desire.

# Making an object from a class is called instantiation.

print("Creating and using a class: ")
# Most dog sit and roll over : These are two behaiors that will go in out dog class.
# This class will tell Python how to make an object representing a dog.
# After this , we'll use it to make individual instances , each of which represents one specific dog.

class Dog():
    """A simple attemprt to model a dog."""

    def __init__(self,name,age):
        """Initialise name and age attributes"""
        self.name = name
        self.age = age

        def sit(self):
            """Simulate a dog sitting in response to a command"""
            print(self.name.title() + " is now sitting.")

        def roll_over(self):
            """Simulate rolling over in repsonse to a command"""
            print(self.name.title() + " rolled over!")



