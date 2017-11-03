responses = {}

while True:
    name = raw_input("Welcome to the favourite language poll." +
        "\nWhat is you name?" +
         "\nEnter 'quit' to quit poll. ")
    if name != 'quit':
        name = name.title()
        fav_lang = raw_input("Hello " + name + "! Which is your favourite language? " +
            "\nEnter 'quit' to quit poll. ")
        if fav_lang != 'quit':
            fav_lang = fav_lang.title()
            responses[name] = fav_lang
            repeat = raw_input("Would anyone else like to respond?(yes/no) ")
            if repeat == 'yes':
                continue
            else:
                for key , value in responses.items():
                    print(key + "'s favourite language is " + value + ".")
        else: # In case a person says 'yes' to repeat , enters name , but then 'quit'.
            if responses: # If responses containes at least 1 ket value pair.
                for key , value in responses.items():
                    print(key + "'s favourite language is "+ value + ".")
                break
            else:
                break
    else: # In case a person says 'yes' to repeat , but enters 'quit' when asked for name.
        if responses: # If responses containes at least 1 ket value pair.
            for key , value in responses.items():
                print(key + "'s favourite language is "+ value + ".")
            break
        else:
            break


