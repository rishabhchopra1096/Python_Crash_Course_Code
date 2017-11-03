number_of_people = raw_input("How many people are in your dinner group? ")
number_of_people = int(number_of_people)

if number_of_people > 8:
    print("Sorry guys , you will have to wait for your table.")
else:
    print("Your table is ready.")
