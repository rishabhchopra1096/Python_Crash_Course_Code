magicians = ['magician1','magician2', 'magician3' ,]

# def show_magicians(list_of_magicians):
#     for magician in list_of_magicians:
#         print(magician.title())

# print(show_magicians(magicians))

# def make_great(list_of_magicians):
#     for magician in list_of_magicians:
#         magician = 'The great ' + magician


def make_great(list_of_magicians):
    index = 0
    while index < len(list_of_magicians):
        for magician in list_of_magicians:
            list_of_magicians[index] = "The Great " + magician
            print(list_of_magicians) # Seeing change in list each time.
            index += 1


make_great(magicians)

