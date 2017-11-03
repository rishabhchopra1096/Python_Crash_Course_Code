current_users = ['ris10','rhe24','man22','sam13','ro3']

new_users = ['ris10','ro3','nis26','dj23','ty7']

for user in new_users:
    if user in current_users:
        print(user + " username is not available.")
    else:
        print(user + " username is available.")

