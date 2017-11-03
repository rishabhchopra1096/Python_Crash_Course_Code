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


restaurant=Restaurant('yo china','chinese')
print(restaurant.number_served)
restaurant.set_number_served(10)
print(restaurant.number_served)
restaurant.increment_number_served(3)
print(restaurant.number_served)



#9-5:
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

user1=User('rishabh','chopra','10/10/96',19)
print(user1.login_attempts)
#>>>0
user1.increment_login_attempts()
print(user1.login_attempts)
#>>>1
user1.increment_login_attempts()
print(user1.login_attempts)
#>>>2
user1.increment_login_attempts()
print(user1.login_attempts)
#>>>3
user1.increment_login_attempts()
print(user1.login_attempts)
#>>>4
user1.increment_login_attempts()
print(user1.login_attempts)
#>>>5





