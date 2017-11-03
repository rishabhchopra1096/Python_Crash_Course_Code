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

    def fill_gas_tank(self):
        if self.odometer_reading % 50 == 0:
            print("Fill gas tank! ")
        elif self.odometer_reading % 50 != 0:
            print("You still have " + str(50 - (self.odometer_reading%50)) + "km left till you have to fill the gas tank.")

my_car = Car('audi','a4',1996)
my_car.update_odometer(5000)
my_car.fill_gas_tank()


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

    def fill_gas_tank(self): # Notice , no self argument is passed , as we are overwriting a method in the Parent Class.
        """Electric Cars do not have gas tanks"""
        print(self.make.title() + " does not need a gas tank!")
    # Now , if someone tries to fill gas tank() with an electric car, Python will ignore the fill_gas_tank() in Car and run this code instead. When you use inheritance , you can make your child classes retain what you need and override anything you don't need from the parent class.


my_tesla = ElectricCar('tesla','model s ',2016)
print(my_tesla.get_descriptive_name())

# print("\nDefining attrbutes and methods for a child class. ")
# my_tesla.describe_battery()

print("\nOverwriting methods from the parent class")
# Define a method in the child class with the same name as the method you want to overwrite.
# Python will disregard the parent class method and only pay attention to the method you define in the child class.
'''Added fill_gas_tank to the parent class , Car'''
'''overwrote the code of fill_gas_tank in child clas, Electric Car'''
my_tesla.fill_gas_tank()

print("Instances as Attributes:")
# When modelling somthing from the real world in code, you may find that you're adding more and more details to a class.
# You'll find that you have a gwoing list of attributes and methods.
# You'll find that your files are becoming too lengthy.
'''In these situations you may realise that part of a class can be written as a separate class.'''
'''You can break your large class into smaller classes that work together'''
# For example, if we keep adding details to the ElectricCar class , we might notice that we're adding many attributes and method specific to car's battery.
# When we see this happening, we can stop and move those attributes and methods to a separate class called Battery.
'''Then we can use Battery instance as an attribute in the ElectricCar class.'''


















