print "Checking whether a value is not in a list "
# Other times, its important to know if a value does not appear in a list.
#  You can use the keyword not in this situation. For example, consider a
#  list of users who are banned from commenting in a forum. You can check whether
#   a user has been banned before allowing that person to submit a comment.

banned_users=['andrew','carolina','david']
user='marie'
if user not in banned_users:
    print(user.title()+", you can post a comment if you wish.")

print "What are Boolean Expressions?"
print " Boolean expression=Conditional tests-->It is either True or False"
# Boolean values are often used to keep track of certain conditions, such as whether
# a game is running or whether a user can edit certain content on a website:
#             game_active = True
#             can_edit = False
# Boolean values provide an efficient way to track the state of a program or a
# particular condition that is important in your program.

