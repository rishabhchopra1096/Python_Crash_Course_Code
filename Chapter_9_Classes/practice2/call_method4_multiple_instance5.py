class Dog():
    """A simple attempt to model a dog"""

    def __init__(self,name, age):
        """Initializing name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate rolling over in repsonse to a command"""
        print(self.name.title() + " is not sitting.")

    def roll_over(self):
        """Simulate rolling over in repsose to a command"""
        print(self.name.title() + " rolled over.")

my_dog = Dog('lexus',6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()


your_dog = Dog('mimi',1)
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " year old.")
your_dog.sit()
your_dog.roll_over()

# Even if we used the same name and age for the second dog ,Python would still create a separate instance from the Dog class: provided we used a different variable name.

# As long as you choose a unique variable name for new instance, a new instance will be created.
# You can overwrite an instance too.


