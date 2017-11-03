'''Object Oriented Programming: is one of the most effective approaches to writing
software.
In object oriented programming :
You write Classes that represent real-world-things.
When you define a class:
You can define the general behavior that a whole category of objects can have.
Although it is automatically equipped with a general behavior; you can give each object
unique traits you desire. '''
'''Instantiation: Making an object from a class is called instantiation, and you work with
instances of a class'''
'''You can model anything using classes.'''
# You can model almost anything using classes. Lets start by writing a simple class, Dog, that
# represents a dog not one dog in particular, but any dog. What do we know about most pet dogs?
# Well, they all have a name and age.
#  We also know that most dogs sit and roll over.
#  Those two pieces of information (name and age)
#  and those two behaviors (sit and roll over)
#  will go in our Dog class because theyre common to most dogs. This class will tell Python how
#  to make an object representing a dog.
#  After our class is written, well use it to make individual instances, each of which represents
#  one specific dog.
print("Creating the Dog Class")
'''Each instace created from the Dog Class will store a Name and an Age, and we'll give each dog
the ability to sit() and roll_over():'''

# class Dog():
#     """docstring for ClassName"""
#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         self.name=name
'''Fomat=> self.variable_name=parameter'''
#         self.age=age

#     def sit(self):
'''Do not forget to enter self in the parameters of a method for a class'''
#         """Simulate rolling over in response to a command"""
#         print(self.name.title()+ " is not sitting.")
'''self.name is a variable and name is the parameter. self.paramet_name will be used as variables to be used in
methods. '''
#     def roll_over(self):
#         """Simulate rolling over in response to a command"""
#         print(self.name.title()+" rolled over!")

'''A function that is part of a class is called a method.
The _init_ method at 29 is a special method that runs automatically whenever we create a new instance
based on the dog class. '''
'''The self parameter is required in the method definition and it must come first before the other parameters.
It must be included in the definiton as when Python calls this _init_ method later(to ccreate an instance of Dog)
the method will automatically pass the self argument which is a reference to the instance itself ==>
Meaning it gives the individual instace access to attributes and methods in the class. '''
'''When we make an instance of Dog, Python will call the __init__() method from the Dog class. Well pass Dog()
a name and an age as arguments; self is passed automatically, so we dont need to pass it. Whenever we want to make
an instance from the Dog class, well provide values for only the last two parameters, name and age. '''
'''The two variables defined at 31 and 32 each have the prefix self. Any variable prefixed with self is available to
every method in the class, and well also be able to access these variables through any instance created from the class.
self.name = name takes the value stored in the parameter name and stores it in the variable name,
which is then attached to the instance being created. The same process happens with self.age = age.
Variables that are accessible through instances like this are called attributes.'''
'''The Dog class has two other methods defined: sit() and roll_over() y. Because these methods dont need additional information
like a name or age, we just define them to have one parameter, self. The instances we create later will have access to these methods.
In other words, theyll be able to sit and roll over. '''
'''For now, sit() and roll_over() dont do much. They simply print a message saying the dog is sitting or rolling over.
But the concept can be extended to realistic situations: if this class were part of an actual computer game, these methods would
contain code to make an animated dog sit and roll over. If this class was written to control a robot, these methods would direct movements
that cause a dog robot to sit and roll over.'''

print("\nMaking an Instance from a Class")

class Dog():
    """docstring for ClassName"""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name=name
        self.age=age

    def sit(self):
        """Simulate rolling over in response to a command"""
        print(self.name.title()+ " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(self.name.title()+" rolled over!")

my_dog=Dog('lexus',6)
'''Telling Python to create a new dog whose name is 'lexus' and whoseage is 6.
When Python reads this line it calls the _init_() method in Dog with arguments
'lexus' and 6.
The __init__() method creates an instance representing this particular dog and sets
 the name and age attributes using the values we provided.
 The __init__() method has no explicit return statement, but Python automatically
 returns an instance representing this dog. We store that instance in the variable my_dog.
 The naming convention is helpful here: we can usually assume that a capitalized name like Dog
 refers to a class, and a lowercase name like my_dog refers to a single instance created from a class.'''



print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")


#Accessing Attributes:
'''To access attrbutes of an instance, use the dot notation :
at 95, we access the value of my_dog's attribute name by writting:
my_dog.name
Dot notation is used often in Python. This syntax demonstrates how Python finds an attributes value.
Here Python looks at the instance my_dog. and then finds the attribute name associated with my_dog.
This is the same attribute referred to as self.name in the class Dog.
In our first print statement, my_dog.name.title() makes 'willie', the value of my_dogs name attribute,
 start with a capital letter.
  In the second print statement, str(my_dog.age) converts 6, the value of my_dogs age attribute, to a string.'''
#Calling Methods:
'''After we create an instance from the class Dog, we can use dot notation to call any method defined in Dog. '''

my_dog.sit()
my_dog.roll_over()

#Format for calling methods:
'''name_of _instance.method_name_of_ClassName()
When python reads name_of _instance.method_name(), it looks for method method_name in the class ClassName and runs that code.
When python read my_dog.sit(), it looks for method sit() in class Dog and runs that code. '''

'''This syntax is quite useful. When attributes and methods have been given appropriately descriptive names like
name, age, sit(), and roll_over(), we can easily infer what a block of code, even one weve never seen before, is supposed to do.'''


print ("\nCreating Multiple Instances")
your_dog=Dog('mimi',1)

print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")
print("\nYou dog's name is "+your_dog.name.title()+".")
print("Your dog is "+str(your_dog.age)+" year old.")
your_dog.sit()
your_dog.roll_over()



'''Even if we used the same name and age for the second dog,
 Python would still create a separate instance from the Dog class.
  You can make as many instances from one class as you need,
  as long as you give each instance a unique variable name or
  it occupies a unique spot in a list or dictionary.'''




