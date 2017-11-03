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


class ElectricCar(Car):
    """Represent aspects of a car , specific to eletric vehicles."""
    def __init__(self,make,model,year):
        """Initializing attributes of the parent class."""
        """Then initializing attributes specific to an electic car."""
        super().__init__(make, model,year)
        # self.battery = Battery(60)
        # This line tells Python to create a new instance called of Battery)with a default size of 70, because we're not specifying a value.
        # This line stores the instance in the attribute self.battery.
        # This will happen every time the __init__ method is called:
        # The __init__ method of the ElectricCar in turn calls the __init__ method of the parent class , Car , then creates a Battery instance automatically.


    # def describe_battery(self):
    #     """Print a statement descibing the battery size."""
    #     print("This car has a " + str(self.battery_size)  + "-kwh battery.")

    def fill_gas_tank(self):
        """Electric Cars do not have gas tanks"""
        print(self.make.title() + " does not need a gas tank!")


