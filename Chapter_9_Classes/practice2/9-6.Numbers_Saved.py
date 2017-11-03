class Restaurant():
    """An attempt to model a restaurant"""

    def __init__(self,restaurant_name,cuisine_type):
        """Initializing name and age attributes"""
        self.name = restaurant_name
        self.cuisine  = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
            # Describes the restaurant name and cuisine
            print(self.name.title() + " serves " + self.cuisine + " food.")

    def open_restaurant(self):
            # Opens the restaurant and welcomes customers.
            print(self.name.title() + " is now Open. \nCome. \nHave some delicious " + self.cuisine + " food.")

    def read_customers_served(self):
        print(self.name.title() + " has served " + str(self.number_served) + " customers as of now.")

    def set_customers_served(self,number):
        self.number_served = number
        print("Number of customers served , Set!")

    def increment_customers_served(self,increment):
        self.number_served += increment
        print("Numbers of customers served , Incremented!")

restaurant1 = Restaurant("big chill","italian")
restaurant1.read_customers_served()

print("\nSetting the number of customers served to 5.")
restaurant1.set_customers_served(5)
restaurant1.read_customers_served()

print("\nIncrementing the number of customers served by 6:")
restaurant1.increment_customers_served(6)
restaurant1.read_customers_served()




