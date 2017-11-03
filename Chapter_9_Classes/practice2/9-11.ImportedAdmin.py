from Privileges98 import User , Privileges , Admin

user1 = User('rishabh','chopra',20,'male')
user1.describe_user()
# User class functioning properly.

admin = Admin('rishabh','chopra',20,'male')
admin.privileges.show_privileges()
# Admin and Privileges functioning properly.

