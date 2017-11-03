# You can use classes to represent many real world situations.
# Once you write a class  you'll spend most of your time working with many instances created from that class.

# One of the first tasks that yo would wna t to do is :
'''Modify the attributes asscoiated with a particular instance'''
# You can modify the attirbutes of an instance directly
# OR , you can write methods that update attributes in specific ways.

class Car():
    """A simple attempt to model a car."""

    def __init__(self,make,model,year):
        """Initialize attributes to describe a car."""
        # Taking in parameters ans storing them in attributes that will be associated with instances made from this class.
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + " " + self.model
        return(long_name.title())

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())













