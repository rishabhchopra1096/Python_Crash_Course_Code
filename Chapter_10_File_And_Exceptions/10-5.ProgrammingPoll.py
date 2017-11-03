reason = ""
file_name = "WhyPeopleLikeProgramming.txt"

while reason != 'quit':
    reason = raw_input("Why do you like programming?" +
        "\nEnter 'quit' if you don't like programming / want to quit. ")
    if reason!= 'quit':
        print("We love programming too!")
        with open(file_name , 'a') as file_object:
            file_object.write(reason + "\n")
