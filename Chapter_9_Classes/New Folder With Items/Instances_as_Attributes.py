print("\nInstances as Attributes: ")
'''You can break your large class into smaller classes that work together.'''
'''For example, if we continue adding detail to the ElectricCar class, we might notice that were
adding many attributes and methods specific to the cars battery. When we see this happening,
we can stop and move those attributes and methods to a separate class called Battery. Then we can
use a Battery instance as an attribute in the ElectricCar class:'''

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

class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        """Initialize the battery's attribute."""
        self.battery_size=battery_size

    def describe_battery(self):
        """Print a statement describing the battery size. """
        print("This car has a "+str(self.battery_size)+" -kWh battery.")





class ElectricCar(Car):
    """Represents aspects of a cat, specific to electic vehicles."""
    def __init__(self, make, model, year):
        """Initializing attributes of the parent class.
        Then initialize attributes specific to an electic car."""
        super().__init__(make, model, year)
        self.battery=Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()




