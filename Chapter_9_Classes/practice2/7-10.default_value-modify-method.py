print('''Setting Default Value for Phython''')
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



my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

print('''\nModifying an attribute's value directly''')
# Accessing attribute directly through an instance.
# Here we set the odometer_reading to 23 directly.
print(my_new_car.odometer_reading)
my_new_car.odometer_reading = 23
print(my_new_car.odometer_reading)
my_new_car.read_odometer()

print("""\nModifying an attribute through a Method""")
# Added update_odometer
my_new_car.update_odometer(0)
my_new_car.read_odometer()
my_new_car.update_odometer(23)
my_new_car.read_odometer()

print("\nMaking sure no one rolls back the odometer.")
# Added logic if-else chain in update_odometer.
my_new_car.read_odometer() # 23
my_new_car.update_odometer(22)
# You cannot roll back the odometer.
my_new_car.update_odometer(23) # mileage = self.odometer_reading

print("Incrementing an attribute's value through a method""")
# in 12.Incrementing













