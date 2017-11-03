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
        """Add the given ammount to the odometer reading"""
        if miles > 0 :
            self.odometer_reading += miles
            print("==>Odometer incremented by " + str(miles))
        else:
            print("You cannot roll back an odometer.")

my_used_car = Car('subaru','outback',2013)
print("getting descriptive name:")
print(my_used_car.get_descriptive_name())
my_used_car.read_odometer()
my_used_car.update_odometer(10)
my_used_car.read_odometer()
print("\nIncrementing odometer:")
my_used_car.increment_odometer(5)
my_used_car.read_odometer()
print("\nTrying to roll back the odometer by entering a negative increment.")
my_used_car.increment_odometer(-5)







