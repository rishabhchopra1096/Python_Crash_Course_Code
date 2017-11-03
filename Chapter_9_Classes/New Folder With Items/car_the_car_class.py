'''classes represent real world situations. '''
'''Once you write the class, you work with instances created from that class'''
'''1.Modify the attributes asscoiated with a particular instance.
--> You can modify the attributes of an instance directly or
write a methods that update attributes in a specific way.'''

print("Working with Classes and Instances")

class Car():
    """A simple attempt to represent a car"""
    def __init__(self, made_by, model, year):
        """Initializing attributes to describe a car"""
        self.made_by=made_by
        self.model=model
        self.year=year
#'''The init method takes in 3 parameters and store them in the attributes that will
#be asscoiated with instances made from this class'''
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name=str(self.year)+' '+self.made_by+' '+self.model
        return long_name

my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
#Here we added print before calling the method, get_descriptive_name because
#the method does not print anything, it returns long_name.
#So if we just call the function, it will return long_name nut will not show anything
#as it does not print anything.

#To make the class more interesting: Let's add an attribute that changes over time:
print("\nAdding attribute to store car's overall mileage")
class Car():
    """A simple attempt to represent a car"""
    def __init__(self, made_by, model, year):
        """Initializing attributes to describe a car"""
        self.made_by=made_by
        self.model=model
        self.year=year
        self.odometer_reading=0
#This time Python calls the init method to create a new instance, it stores the make, model,
#and year values as attributes like it did in the previous example.
#Then Python create a new attribute called odometer_reading and sets its initial value to 0.
#Lesson: All attributes do not need to derived from parameters. If the are not derived from parameters
#they will need a method to come of some use. Therefore, the method read_odometer that makes it easy
#to read a car's mileage.

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name=str(self.year)+' '+self.made_by+' '+self.model
        return long_name

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print("This car has "+str(self.odometer_reading)+" miles on it. ")

my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

print("Modifying Attribute Values")

'''Here are the 3 ways You can you can modify an attribute'''
#1. change the value directly through an instance.
#2. Set the value through a method
#3. Increment the value through a method.

'''1.The simplest way to modify the value of attribute is to access the attribute directly thougha an instance.'''
print("\nModifying an attribute's value directly")
my_new_car.odometer_reading=23
#We used the dot notation to access the cars odometer_readining attribute and set its value directly.
#This instance tells Python to take the instance my_new_car, find the attribute odometer_reading associated with it,
#and set the value of that attribute to 23.
my_new_car.read_odometer()
#We can do this with other attributes too.
my_new_car.year=2016
my_new_car.made_by='Mercedex'
my_new_car.model='C102'
print(my_new_car.get_descriptive_name())
#Now if we forgot to enter any attribute associated with the method, get_descriptive_name:
#It will use the postional argument entered when making the instance.
#For eg: If i missed out on my_new_car.model--> It will show: 2016 Mercedes a4 because when i made the instance my_new_car
#I wrote: my_new_car=Car('audi','a4',2016)--> In other words the attribute will not get modified.


'''2. Sometimes you might want to set values directly but other times you would want to write a method that updates
the value for you. '''
print("\nModifying an attributes value through a method")
#Instead of accessing the attribute directly, you pass the new value to a method that handles the updating internally.


class Car():
    """A simple attempt to represent a car"""
    def __init__(self, made_by, model, year):
        """Initializing attributes to describe a car"""
        self.made_by=made_by
        self.model=model
        self.year=year
        self.odometer_reading=0

    def update_odometer(self, mileage):
        '''Set the odometer reading to the given value'''
        # self.odometer_reading=mileage #Using this method will set a new value to the attribute self.odometer_reading
                                       #which is by default set to 0.
        if mileage>=self.odometer_reading:#To make sure no one rolls it back. We add if statements.
            self.odometer_reading=mileage# Now if someone enters a number less than the old mileage:
        else:                            #They will get a waring saying:
            print("You cannot roll the odometer back.")


    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name=str(self.year)+' '+self.made_by+' '+self.model
        return long_name

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print("This car has "+str(self.odometer_reading)+" miles on it. ")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
print("Using my_new_car.update_odometer(23):\nWe then use my_new_car.read_odometer(): ")
my_new_car.update_odometer(23) #Here 23 corresponds to the mileage parameter.
my_new_car.read_odometer()
my_new_car.update_odometer(22) #Checking weather it will print "you cannot roll the odometer back" or not.
#Yes, it does print that.

print("\nIncrementing an attributes value through a method")
# Say, we buy a used car. It has 23,500 miles on it. We will have to update that.
#Then after buying and before registering it. We drove it a 100 miles more. Now, we can either
#update the odometer or just add the incremental ammount.

class Car():
    """A simple attempt to represent a car"""
    def __init__(self, made_by, model, year):
        """Initializing attributes to describe a car"""
        self.made_by=made_by
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name=str(self.year)+' '+self.made_by+' '+self.model
        return long_name

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print("This car has "+str(self.odometer_reading)+" miles on it. ")

    def update_odometer(self, mileage):
        '''Set the odometer reading to the given value'''
        # self.odometer_reading=mileage #Using this method will set a new value to the attribute self.odometer_reading
                                       #which is by default set to 0.
        if mileage>=self.odometer_reading:#To make sure no one rolls it back. We add if statements.
            self.odometer_reading=mileage# Now if someone enters a number less than the old mileage:
        else:                            #They will get a waring saying:
            print("You cannot roll the odometer back.")

    def increment_odometer(self, miles):
        '''Adding the given ammount to the odometer.'''
        #self.odometer_reading+=miles #This method just adds the incremented miles to the attribute, self.odometer_reading which
                                    #is initally set to 0.
        if miles>=0:                 #Adding an if statement to refuse negative increments or rolling back the odometer.
            self.odometer_reading+=miles
        else:
            print("You cannot roll the odometer back.")

my_2nd_hand_car=Car('Toyata','camary',2008)
print(my_2nd_hand_car.get_descriptive_name())
my_2nd_hand_car.read_odometer()
my_2nd_hand_car.update_odometer(23500)
my_2nd_hand_car.read_odometer()
my_2nd_hand_car.increment_odometer(100)
my_2nd_hand_car.read_odometer()
my_2nd_hand_car.increment_odometer(-200) #You cannot roll the odometer back.








