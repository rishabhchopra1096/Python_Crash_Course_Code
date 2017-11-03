#10-3: Guest:
guest_name = raw_input("Hey there! Welcome to the Partyy! What's your name? ")

file_name = "guest.txt"

with open(file_name , 'a') as file_object:
    file_object.write(guest_name)

