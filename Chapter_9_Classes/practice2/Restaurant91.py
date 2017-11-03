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

# restaurant1 = Restaurant("big chill","italian")

# print(restaurant1.name)
# print(restaurant1.cuisine)
# restaurant1.describe_restaurant()


