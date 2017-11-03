from dog1 import Dog

# Think of a class as a set of instructions on how to make an instance.
# The class Dog is a set of instruction that tells Python how to make individual instances representing specific dogs.

my_dog = Dog('willie',6)

print("My dog's name is " + my_dog.name.title())
print("My dog is " + str(my_dog.age) + " years old.")

# We tell Python to create a Dog whose name is Willie and whose age is 6.
# When Python reads this line , it calls __init__ function.
# The __init__ function intializes / creates spaces in memory for a new instance of the Class.
# __init__() method creates an instance representing this particular dog and sets the name and age attributes using the values we provided (self.name OR self.age)
# Once name becomes equal to self.name , it can be accessed by any mehtod in the Class.
# Once nage becomes equal to self.age , it can be accessed by any method in the class.
# We store that instance in the variable my_dog.

