print("9-6: Ice Cream Stand:")
#9-4: Numbers Served:
class Restaurant(object):
    """Building a simple Restaurant"""
    def __init__(self,name,cuisine):
        self.name=name
        self.cuisine=cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Describing the name and cuisine of the restaurant"""
        print("The restaurant, "+self.name.title() + " serves delicious " + self.cuisine + " food.")

    def open_restaurant(self):
        """Informing people that the restaurant is now open"""
        print("The " + self.cuisine + " restaurant, " + self.name.title() + " is now open.")

    def set_number_served(self, number):
        """Sets the number of customers served"""
        self.number_served = number

    def increment_number_served(self, increment_number):
        """Increases the number of customers served."""
        self.number_served += increment_number

class IceCreamStand(Restaurant):
    """Building a child class of Restaurant"""
    def __init__(self,name,cuisine):
        """Initializing parameter taken in by Restaurant
        Then adds attributes specific to IceCreamStand."""
        super().__init__(name,cuisine)
        self.flavors = ['vanilla','chocolate','mint','blueberry','strawberry']

    def list_out_flavors(self):
        print("\nHere are the flavors:")
        for flavor in self.flavors:
            print(flavor)

ice_cream_stand1=IceCreamStand('mother dairy','ice cream')
ice_cream_stand1.describe_restaurant()
ice_cream_stand1.open_restaurant()
print(ice_cream_stand1.number_served)
#>>0
ice_cream_stand1.set_number_served(1)
print(ice_cream_stand1.number_served)
#>>1
ice_cream_stand1.increment_number_served(4)
print(ice_cream_stand1.number_served)
#>>>5
ice_cream_stand1.list_out_flavors()

print("\n9-7: Admin:")
class User(object):
    def __init__(self,first,last,date_of_birth,age):
        self.first=first
        self.last=last
        self.dob=date_of_birth
        self.age=age
        self.login_attempts = 0

    def describe_user(self):
        print("Full Name: " + self.first.title() + " " + self.last.title())
        print("Date of Birth: " + self.dob)
        print("Age: " + str(self.age))

    def greet_user(self):
        print("Hey, " + self.first.title() + "! Good to have you back.")

    def increment_login_attempts(self):
        """Increments the login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the login attempts to 0"""
        self.login_attempts = 0


class Admin(User):
    """Creating a child class of User"""
    def __init__(self,first,last,date_of_birth,age):
        """Initializing parameters of parent class
        Adding attributes specific to Admin."""
        super().__init__(first,last,date_of_birth,age)
        self.privileges = ["can add post","can delete post","can ban user"]

    def show_privileges(self):
        print("The priveleges of an admin are:")
        for privelege in self.privileges:
            print(privelege)

god=Admin('Tanu','Bhargava','10/10/1975',50)
god.show_privileges()





