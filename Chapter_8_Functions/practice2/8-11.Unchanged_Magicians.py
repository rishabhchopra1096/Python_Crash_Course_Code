magicians = ['magician1','magician2', 'magician3' ,]
def make_great(list_of_magicians):
    index = 0
    while index < len(list_of_magicians):
        for magician in list_of_magicians:
            list_of_magicians[index] = "The Great " + magician
            print(list_of_magicians) # Seeing change in list each time.
            index += 1
    return(list_of_magicians)

great_magicians = make_great(magicians[:])
print(magicians) # No change to original list.

def show_magicians(list_of_magicians):
    for magician in list_of_magicians:
        print(magician.title())

show_magicians(magicians)
show_magicians(great_magicians)