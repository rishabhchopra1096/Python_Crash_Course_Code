class User():
    """Modelling a user"""
    def __init__(self, first, last,age,gender):
        self.first_name = first
        self.age = age
        self.last_name = last
        self.gender = gender

    def describe_user(self):
        print("Here's some information about the user: ")
        print(
            "\tFirst Name : " + self.first_name.title() +
            "\n\tLast Name: " + self.last_name.title() +
            "\n\tAge: "  + str(self.age) +
            "\n\tGender: " + self.gender.title()
            )

    def greet_user(self):
        full_name = self.first_name.title() + self.last_name.title()
        print("Hello, " + full_name + "!")


user1 = User("rishabh",'chopra',9,'male')
user1.describe_user()
user1.greet_user()

