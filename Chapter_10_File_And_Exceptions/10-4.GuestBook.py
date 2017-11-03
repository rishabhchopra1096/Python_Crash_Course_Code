file_name= "guest_book1.txt"
guest_name = ""

while guest_name != 'quit':
    guest_name = raw_input("Hey there! Welcome to the party! What's your name? "+
    "\nEnter 'quit' if you don't want to attend the party. ")
    if guest_name != 'quit':
        print("Hey there, " + guest_name.title() + "! Your name is added to the guest book.")
        with open(file_name , 'a') as file_object:
            file_object.write(guest_name + "\n")



