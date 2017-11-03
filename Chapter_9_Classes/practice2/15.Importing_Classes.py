# As you add more functionality to your classes , your files can get long , even when you use inheritance properly.
# In keeping with the overall philosphy of Python , you'll want to keeo yout files as uncluttered as possible.
# To help, Python lets you store classes in modules and then import the classes you need into your main program.

'''Importing a single Class from module (car_import) with only one class'''

from car_import import Car

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

print(my_new_car.odometer_reading)
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

'''Importing a single Class from module(car_import) with multiple classes'''
from car_import import ElectricCar
my_tesla = ElectricCar('tesla','model s',2016)
my_tesla.fill_gas_tank()


