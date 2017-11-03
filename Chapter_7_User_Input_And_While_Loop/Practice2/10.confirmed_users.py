# List of unverified , new users :
unconfirmed_users = ['alice','brian','candace']
# List of confirmed users:
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop(0)
    print("User: " + current_user + " is being verified.")
    confirmed_users.append(current_user)
    print(current_user + " is verified and shift to confirmed_users.")

# Displaying all confirmed_users:
print("\nThe following users have been confirmed: ")
for user in confirmed_users:
    print(user)
