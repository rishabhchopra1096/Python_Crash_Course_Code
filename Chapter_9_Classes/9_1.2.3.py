#9-1:Restaurant:
class Restaurant(object):
    """Building a simple Restaurant"""
    def __init__(self,name,cuisine):
        self.name=name
        self.cuisine=cuisine

    def describe_restaurant(self):
        """Describing the name and cuisine of the restaurant"""
        print("The restaurant, "+self.name.title() + " serves delicious " + self.cuisine + " food.")

    def open_restaurant(self):
        """Informing people that the restaurant is now open"""
        print("The " + self.cuisine + " restaurant, " + self.name.title() + " is now open.")

restaurant=Restaurant('yo china','chinese')
print(restaurant.name)
print(restaurant.cuisine)
restaurant.describe_restaurant()
restaurant.open_restaurant()


#9-2:
restaurant2=Restaurant('punjabi by nature','indian')
print("\n")
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3=Restaurant("spagheti kitchen",'italian')
print("\n")
restaurant3.describe_restaurant()
restaurant3.open_restaurant()

#9-3:
class User(object):
    def __init__(self,first,last,date_of_birth,age):
        self.first=first
        self.last=last
        self.dob=date_of_birth
        self.age=age

    def describe_user(self):
        print("Full Name: " + self.first.title() + " " + self.last.title())
        print("Date of Birth: " + self.dob)
        print("Age: " + str(self.age))

    def greet_user(self):
        print("Hey, " + self.first.title() + "! Good to have you back.")

user1=User('rishabh','chopra','10/10/96',19)
print("\n")
user1.describe_user()
user1.greet_user()







