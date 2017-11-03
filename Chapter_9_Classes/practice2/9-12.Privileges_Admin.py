from User912 import User

class Privileges():
    """Models the privileges of an admin"""
    def __init__(self, privileges):
        # Initializing attributes to describe privileges
        self.privileges = privileges

    def show_privileges(self):
        print("\nThe admin enjoys the following privileges: ")
        for privilege in self.privileges:
            print(privilege)



class Admin(User):
    """Modelling an Admin"""
    def __init__(self,first,last,age,gender):
        """Initializing attributes of parent class,User"""
        super().__init__(first,last,age,gender)
        self.privileges = Privileges(['privilege1','privilege2','privilege3'])

admin = Admin('rishabh','chopra',20,'male')
admin.describe_user()
admin.privileges.show_privileges()