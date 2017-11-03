# Sometimes , you'll want to spread out your classes over several modules.
# When you store you classes in several modules , you may find that a class in one module depends on a class in another module.
# When this happens, you can import the rquired class into the current module.
from car_import import Car # If we forget this line , Python will raise an error that NameError: name 'Car' is not defined
from ElectricCar import ElecticCar , Battery

my_new_car = Car('x','y',3)
print(my_new_car.get_descriptive_name())
# my_tesla = ElectricCar('tesla','model s ',2016)
# my_tesla.battery.get_range()
