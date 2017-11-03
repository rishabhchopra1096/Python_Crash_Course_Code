'''If the class you are writing is a specialized version of another class you wrote,
you can use inheritance.'''
'''When one class inherits from another, it automatically takes on all the attributes
and methods of the first class.
The original class is called the parent class,  and the new class is called the child
class. '''
'''The child classs inherits all the attributes and methods of the parent class but its
also free to define new attributes and methods on its own. '''

print("The _init_()Method for a Child Class")
#The first task Python has when creating an instance from a child class is to
#assign values to all attributes in the parent class.
# To do this the _init_() method for a child class needs help from its parent class.
# Creating an ElecticCar class as a child class of the Car class.
# We then have to write attributes and methods specific to only electric cars.

class Car():
    """A simple attempt to represent a car"""
    def __init__(self, made_by, model, year):
        """Initializing attributes to describe a car"""
        self.made_by=made_by
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name=str(self.year)+' '+self.made_by+' '+self.model
        return long_name

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print("This car has "+str(self.odometer_reading)+" miles on it. ")

    def update_odometer(self, mileage):
        '''Set the odometer reading to the given value'''

        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
            print("You cannot roll the odometer back.")

    def increment_odometer(self, miles):
        '''Adding the given ammount to the odometer.'''

        if miles>=0:
            self.odometer_reading+=miles
        else:
            print("You cannot roll the odometer back.")

class ElecticCar(Car): #Defining child class
    """Represents aspects of a cat, specific to electic vehicles."""
    def __init__(self, make, model, year):
        """Initializing attributes of the parent class."""
        super().__init__(make, model, year)

my_tesla= ElecticCar('Tesla','model S',2016)
print(my_tesla.get_descriptive_name())
'''When you create a child class, the parent class must be a part of the file and should
come before the child class in a file. '''
'''When naming an instance of a class, we add the parameters to the respective positional arguments
of the class , but when we create a child class, we write the name of the parent class in the parentheses
after the name of the child class. '''
'''The init method takes in the information required to make a Car instance.'''
'''The super function is a special function that helps in making connections between parent and
child class. This function tells Python to call the _init_() method from ElecticCar's parent class,i.e Car.
The name super refers to calling the parent class a superclass and child class a subclass. '''
'''We test the inheritance by trying to create an electic cars instance with the same kind of information
input as we did with the Car class. '''
''' my_tesla= ElecticCar('Tesla','model S',2016) This line tells Python to call the _init_() function in
ElecticCar which in turn tells Python to class the _init_() method defined in the parent class Car. '''
'''Aside from _init_() which intitialized the attributes of the parent class, there are no attributes or methods
yet that are particular to an electric car. '''
'''Till now, ElecticCar has appropriate Car behaviors.'''
'''Format for creating a child class:
class Child_Class_Name(Parent_Class_Name):
    """Represents aspects of a Parent Class specific to Child Class ."""
    def __init__(self, arg1, arg2, arg3,....):''' # arg refers to the same arguments parent class has.
    #This takes in the information required to create an instance.
#            """Initializing attributes of the parent class."""
       # super().__init__(make, model, year) '''
'''Super()._init_ makes a connection between the parent class and
#the child class. It tell Python to call the _init_ method from parent class.'''


print("\nDefining attributes and methods for a child class.")

class Car():
    """A simple attempt to represent a car"""
    def __init__(self, made_by, model, year):
        """Initializing attributes to describe a car"""
        self.made_by=made_by
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name=str(self.year)+' '+self.made_by+' '+self.model
        return long_name

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print("This car has "+str(self.odometer_reading)+" miles on it. ")

    def update_odometer(self, mileage):
        '''Set the odometer reading to the given value'''

        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
            print("You cannot roll the odometer back.")

    def increment_odometer(self, miles):
        '''Adding the given ammount to the odometer.'''

        if miles>=0:
            self.odometer_reading+=miles
        else:
            print("You cannot roll the odometer back.")

class ElecticCar(Car): #Defining child class
    """Represents aspects of a cat, specific to electic vehicles."""
    def __init__(self, make, model, year):
        """Initializing attributes of the parent class.
        Then initialize attributes specific to an electic car."""
        super().__init__(make, model, year)
        self.battery_size=70

    def describe_battery(self):
        """Print a describing the battery size."""
        print("This car has a "+str(self.battery_size)+" -kWh battery.")

my_tesla=ElecticCar('Tesla','model S',2016)
print(my_tesla.get_descriptive_name()) #Checking if it can use a method of parent class.
my_tesla.describe_battery() # Describing the electric cars battery.

'''
There’s no limit to how much you can specialize the ElectricCar class. You can add as many
attributes and methods as you need to model an electric car to whatever degree of accuracy you need.
An attribute or method that could belong to any car, rather than one thats specific to an electric
car, should be added to the Car class instead of the ElectricCar class. Then anyone who uses the Car
class will have that functionality available as well, and the ElectricCar class will only contain code
for the information and behavior specific to electric vehicles.'''


print ("\nOveriding Methods from the Parent Class")
#To overide:
# Create amethod in the child class with the sam naem as the method you want to override in the parent class.
#Say the class Car had a method called fill_gas_tank(). This method is meaningless for an all-electric vehicle,
#so you might want to override this method.


class Car():
    """A simple attempt to represent a car"""
    def __init__(self, made_by, model, year):
        """Initializing attributes to describe a car"""
        self.made_by=made_by
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name=str(self.year)+' '+self.made_by+' '+self.model
        return long_name

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print("This car has "+str(self.odometer_reading)+" miles on it. ")

    def update_odometer(self, mileage):
        '''Set the odometer reading to the given value'''

        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You cannot roll the odometer back.")

    def increment_odometer(self, miles):
        '''Adding the given ammount to the odometer.'''

        if miles>=0:
            self.odometer_reading+=miles
        else:
            print("You cannot roll the odometer back.")

    def fill_gas_tank(self):
        if self.odometer_reading%50==0:
            print("It's time to fill the gas tank.")
        else:
            print("You have some gas left in the tank.")


class ElecticCar(Car):
    """Represents aspects of a cat, specific to electic vehicles."""
    def __init__(self, make, model, year):
        """Initializing attributes of the parent class.
        Then initialize attributes specific to an electic car."""
        super().__init__(make, model, year)
        self.battery_size=70

    def describe_battery(self):
        """Print a describing the battery size."""
        print("This car has a "+str(self.battery_size)+" -kWh battery.")

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

print("Printing out all methods of Car including fill_gas_tank")
my_normal_car=Car('Audi','A4',2016)
print(my_normal_car.get_descriptive_name())
my_normal_car.read_odometer()
my_normal_car.update_odometer(90)
my_normal_car.fill_gas_tank()
my_normal_car.increment_odometer(10)
my_normal_car.read_odometer()
my_normal_car.fill_gas_tank()
#Assuming the normal car needs to fill gas after every 50 miles:
# So first we started with a normal car with 0 miles on it.
# Then i updated the odometer to 90, not divisible by 50, therefore, when i called the method
# fill_gas_tank it said: You have some gas left in the tank.
# Then using increment_odometer i added 10 miles to the odometer, now it read_odometer as:
# This car has 100 miles on it.
# 100 is divisible by 50, therefore, when i called the method fill_gas_tank again, it said:
# Its time to fill the gas tank.
print("\nTrying to fill gas in the Tesla: ")
my_tesla=ElecticCar('Tesla','model S', 2016)
my_tesla.fill_gas_tank()

print("\nInstances as Attributes: ")
'''You can break your large class into smaller classes that work together.'''
'''For example, if we continue adding detail to the ElectricCar class, we might notice that were
adding many attributes and methods specific to the cars battery. When we see this happening,
we can stop and move those attributes and methods to a separate class called Battery. Then we can
use a Battery instance as an attribute in the ElectricCar class:'''





