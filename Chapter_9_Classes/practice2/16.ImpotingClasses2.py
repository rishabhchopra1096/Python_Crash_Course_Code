'''Importing Mulitple Classes from the same module'''
from car_import import Car, ElectricCar

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())


my_tesla = ElectricCar('tesla','model s',2016)
my_tesla.fill_gas_tank()

