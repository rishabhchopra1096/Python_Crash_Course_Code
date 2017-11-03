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
        self.battery = Battery(70)
        # This line tells Python to create a new instance called of Battery)with a default size of 70, because we're not specifying a value.
        # This line stores the instance in the attribute self.battery.
        # This will happen every time the __init__ method is called:
        # The __init__ method of the ElectricCar in turn calls the __init__ method of the parent class , Car , then creates a Battery instance automatically.


    def describe_battery(self):
        """Print a statement descibing the battery size."""
        print("This car has a " + str(self.battery_size)  + "-kwh battery.")

