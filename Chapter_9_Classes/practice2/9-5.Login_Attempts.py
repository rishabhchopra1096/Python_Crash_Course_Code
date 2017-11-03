class User():
    """Modelling a user"""
    def __init__(self, first, last,age,gender):
        self.first_name = first
        self.age = age
        self.last_name = last
        self.gender = gender
        self.login_attempts = 0

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

    def read_login_attempts(self):
        print(self.first_name.title() + ' ' + self.last_name.title() + ' has attempted to log in ' + str(self.login_attempts) + " times. " )

    def increment_login_attempts(self):
        self.login_attempts += 1
        print("Login attempts incremented by 1.")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("login attempts reset.")


user1 = User('rishabh','chopra',20,'male')
print("Descibing User:")
user1.describe_user()

print("\nGreet User")
user1.greet_user()

print("\n")
user1.read_login_attempts()
print("Incrementing login attempts 3 times")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.read_login_attempts()

print("\nResetting login attempts")
user1.reset_login_attempts()
user1.read_login_attempts()



