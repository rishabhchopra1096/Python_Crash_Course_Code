class Car(object):
    """A simple attempt to represent a car"""

    def __init__(self,make,model,year):
        """Initialize attributes to describe a car"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name=str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to given value.
        Reject the change if anyone tries to roll the odometer back."""
        if self.odometer_reading <= mileage:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self , increment_mileage):
        self.odometer_reading += increment_mileage

    def fill_gas_tank(self):
        check = self.odometer_reading % 50
        if check == 0:
            print("It's time to fill the gas tank.")
        else:
            print("Fill gas after " + str(50 - check) + " miles.")

class Battery(object):
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can approximately " + str(range)
        message += " miles on full charge."
        print(message)


class ElecticCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initalize attributes specific to an electic car."""
        super().__init__(make, model, year)
        self.battery_size = 70
        self.battery = Battery(battery_size=85)


    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank.")


my_tesla=ElecticCar('testla','model s',2016)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()





