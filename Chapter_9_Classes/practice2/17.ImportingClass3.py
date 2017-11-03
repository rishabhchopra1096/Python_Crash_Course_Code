'''Importing an Entire Module'''
'''Access classes in the module by module_name.class_name syntax'''
# import car_import

# my_new_car = car_import.Car('cheverolet','beat',2015)
# print(my_new_car.get_descriptive_name())

# # This requires you to use the dot notation between the module name and class.

# my_tesla = car_import.ElectricCar('tesla','model s ',2016)
# my_tesla.fill_gas_tank()

'''Importing all classes from a module'''
from car_import import *
# Not reccomended for two reasons:
# 1. It is not clear on which classes a program can use.
# 2. With this approach , it is unclear frommwhich module you are using the class.
# You can create a class inside the current module and use that , as well as you can use the classes in the imported module.
# The module_name.class_name syntax is useful and explicit.
# The zen of Python says : Explicit is better than implicit.
# 3. If you accidentally create a class with the same name as a class in the module imported , for eg: you created a Car class in the current module whereas , there is also a Car class in the imported module ==> You will create errors and will lead to confusion.


my_new_car = Car('cheverolet','beat',2016)
print(my_new_car.get_descriptive_name())
