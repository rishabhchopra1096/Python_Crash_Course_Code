class Restaurant():
    """An attempt to model a restaurant"""

    def __init__(self,restaurant_name,cuisine_type):
        """Initializing name and age attributes"""
        self.name = restaurant_name
        self.cuisine  = cuisine_type

    def describe_restaurant(self):
            # Describes the restaurant name and cuisine
            print(self.name.title() + " serves " + self.cuisine + " food.")

    def open_restaurant(self):
            # Opens the restaurant and welcomes customers.
            print(self.name.title() + " is now Open. \nCome. \nHave some delicious " + self.cuisine + " food.")

restaurant1 = Restaurant("big chill","italian")

class IceCreamStand(Restaurant):
    """An attempt to model a restaurant , specific to InceCreamStand"""
    def __init__(self,restaurant_name,cuisine_type):
        """Initializing attributes of parent class , Restaurant"""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['vanilla','chocolate','mint','blueberry','strawberry'] #

    def display_flavors(self):
        print("Here is the list of flavors: ")
        for flavor in self.flavors:
            print(flavor)


IceCreamStand1 = IceCreamStand('mother dairy','ice cream')
IceCreamStand1.describe_restaurant()
IceCreamStand1.open_restaurant()
IceCreamStand1.display_flavors()




