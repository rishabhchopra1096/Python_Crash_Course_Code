user_names = ['admin','ris100','man22','sam13','rhe24']

if user_names:
    for user in user_names:
        if user == 'admin':
            print("Hello admin, would you like a status report?")
        else:
            print("Hello " + user + "! Thankyou for logging in again.")
else:
    print("We need to find some users!")
