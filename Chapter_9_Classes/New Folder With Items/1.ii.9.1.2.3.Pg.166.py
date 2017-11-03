#9-1:'''Fomat=> self.variable_name=parameter'''
class Restaurant():
    """Restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.name=restaurant_name
        self.cuisine=cuisine_type
    def describe_restaurant(self):
        print(self.name.title())
        print(self.cuisine.title())

    def open_restaurant(self):
        print("The "+self.cuisine.title()+" restaurant, "+self.name.title()+" is now open")

restaurant1=Restaurant('MamaGoto','chinese')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

#9-2: Three Restaurants:
print("\n")
restaurant2=Restaurant('south indian','sagar ratna')
restaurant3=Restaurant('thai','wok in the clouds')
restaurant4=Restaurant('mexican','taco bell')
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant4.describe_restaurant()

#9-3: Users:
class User():
    """docstring for ClassName"""
    def __init__(self, first_name, last_name, age, user_name, sex):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.user_name=user_name
        self.sex=sex

    def describe_user(self):
        print("\nHere is some information about the user: ")
        print("First name: "+self.first_name.title())
        print("Last name: "+self.last_name.title())
        print("Age: "+str(self.age))
        print("User name: "+self.user_name)
        print("Sex: "+self.sex.title())

    def greet_user(self):
        print("Hi, "+self.first_name.title()+self.last_name.title()+"!")


user1=User('rishabh','chopra','20','rishabhchopra10','male')
user1.describe_user()
user1.greet_user()








