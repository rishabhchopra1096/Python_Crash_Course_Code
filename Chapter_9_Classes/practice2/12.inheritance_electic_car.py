print("Inheritance")
# You don't always have to star from scratch when writing a class.
# If the class you're writing is a specialized version of another class you wrote, it automatically takes on all the attributed and methods of the first class.
'''Inherits'''# When one class inherits from another , it automatically taken in all the attrbutes and methods of the first class.
'''Parent/Child Class'''#The original class is called the parent class and the new class is called the child class.
# The child class inherits every attribute and method from its parent class but is also free to define its own attrbutes and methods.
print("Making child class ElectricCar from parent class Car:")
class Car():
    """A simple attempt to model a car."""

    def __init__(self,make,model,year):
        """Initialize attributes to describe a car."""
        # Taking in parameters ans storing them in attributes that will be associated with instances made from this class.
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Setting inital value

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + " " + self.model
        return(long_name.title())

    def read_odometer(self):
        """Print a statement showing a car's mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        # Sets the odometer to a given value.
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            print("==>Odometer updated.") # Making sure function executed properly.
        else:
            print("You cannot roll back the odometer.")

    def increment_odometer(self,miles):
        if miles > 0:
            print("===>Odometer incremented by " + str(miles))
            self.odometer_reading += miles
        else:
            print("You cannot roll back an odometer.")

class ElectricCar(Car):
    """Represent aspects of a car , specific to eletric vehicles."""
    def __init__(self,make,model,year):
        """Initializing attributes of the parent class."""
        """Then initializing attributes specific to an electic car."""
        super().__init__(make, model,year)
        self.battery_size = 70 # Adding new attribute and setting initial value to 70.
        # This attribute will only be associated to all instances of ElectricCar but will have no relation to instances of Car class.

    def describe_battery(self):
        """Print a statement descibing the battery size."""
        print("This car has a " + str(self.battery_size)  + "-kwh battery.")


my_tesla = ElectricCar('tesla','model s ',2016)
print(my_tesla.get_descriptive_name())

print("\nDefining attrbutes and methods for a child class. ")
my_tesla.describe_battery()

print("\nOverwriting methods from the parent class - 13.")



print(30%50)

