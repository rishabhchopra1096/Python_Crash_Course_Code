print("Instances as Attributes:")
# When modelling somthing from the real world in code, you may find that you're adding more and more details to a class.
# You'll find that you have a gwoing list of attributes and methods.
# You'll find that your files are becoming too lengthy.
'''In these situations you may realise that part of a class can be written as a separate class.'''
'''You can break your large class into smaller classes that work together'''
# For example, if we keep adding details to the ElectricCar class , we might notice that we're adding many attributes and method specific to car's battery.
# When we see this happening, we can stop and move those attributes and methods to a separate class called Battery.
'''Then we can use Battery instance as an attribute in the ElectricCar class.'''
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



class Battery():
    #Defining a new class called battery that does not inherit from any other class.
    """A simple attempt to model a battery for an electric car."""
    def __init__(self,battery_size = 70):
        # Optional parameter provided that automatically sets the battery_size to 70 , if no value is provided.
        """Initializing the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range that this battery provides"""
        if self.battery_size < 70:
            print("I cannot calculate the range of battery size lower that 70-kwh")
        elif self.battery_size == 70:
            range = 240
        else:
            # self.battery_size = 85:
            # range = 270
            range = 240 + (self.battery_size - 70)*2
            message = "This car can go approximately " + str(range) + " miles on full charage "
            print(message)


class ElectricCar(Car):
    """Represent aspects of a car , specific to eletric vehicles."""
    def __init__(self,make,model,year):
        """Initializing attributes of the parent class."""
        """Then initializing attributes specific to an electic car."""
        super().__init__(make, model,year)
        self.battery = Battery(60)
        # This line tells Python to create a new instance called of Battery)with a default size of 70, because we're not specifying a value.
        # This line stores the instance in the attribute self.battery.
        # This will happen every time the __init__ method is called:
        # The __init__ method of the ElectricCar in turn calls the __init__ method of the parent class , Car , then creates a Battery instance automatically.


    def describe_battery(self):
        """Print a statement descibing the battery size."""
        print("This car has a " + str(self.battery_size)  + "-kwh battery.")

    def fill_gas_tank(self):
        """Electric Cars do not have gas tanks"""
        print(self.make.title() + " does not need a gas tank!")
my_tesla = ElectricCar('tesla','model s',2016)

print(my_tesla.get_descriptive_name())
# 2016 Tesla Model S
my_tesla.battery.describe_battery()
# This line tells Python to look at the instance , my_tesla, find its battery attribute , and call the method describe_battery() that's associated with the Battery instance stored in the attribute.
# >>> This car has a 70-kWh battery.

'''This looks like a lot of work but now we can define the battery in as much detail as we want to without cluttering the ElectricCar class'''
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()












