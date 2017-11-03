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




class Admin(User):
    """Modelling an Admin"""
    def __init__(self,first,last,age,gender):
        """Initializing attributes of parent class,User"""
        super().__init__(first,last,age,gender)
        self.privileges = ['can add post','can delete post','can ban user']

    def show_privelges(self):
        print("The admin, " + (self.first_name + ' ' + self.last_name).title() + " has the following priveleges: ")
        for privilege in self.privileges:
            print(privilege.title())


admin = Admin('rishabh','chopra',20,'male')
admin.describe_user()
admin.show_privelges()


