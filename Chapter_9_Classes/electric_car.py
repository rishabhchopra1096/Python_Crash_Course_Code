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




my_car=Car('audi','a4',2016)
print(my_car.odometer_reading)
my_car.update_odometer(60)
my_car.read_odometer()
my_car.fill_gas_tank()

class ElecticCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initalize attributes specific to an electic car."""
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Prints a statement describing the battery size."""
        print("This car has " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank.")



my_tesla = ElecticCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()



























