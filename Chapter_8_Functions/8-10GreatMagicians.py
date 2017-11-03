magician_name=['eye','chris angel','mindfreak']
def show_magicians(magician_name_list):
    for magician in magician_name_list:
        print(magician.title())

show_magicians(magician_name)

def make_great(magician_name_list):
    for magician in magician_name_list:
        print("The Great "+magician.title())

make_great(magician_name)

