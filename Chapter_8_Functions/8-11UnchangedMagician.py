magician_name=['eye','chris angel','mindfreak']
print(magician_name)
def show_magicians(magician_name_list):
    for magician in magician_name_list:
        print(magician.title())
#show_magicians(magician_name)
# Eye
# Chris Angel
# Mindfreak


magician_name=['eye','chris angel','mindfreak']
#WAY 1 for 8-10, making a new list for great magicians.
# new_great_list=[]
# def make_great(magician_name_list):
#     for magician in magician_name_list:
#         great_magician='The Great '+magician.title()
#         new_great_list.append(great_magician)
#     print (new_great_list)
# make_great(magician_name)

#Way 2 : Replacing the names in the list itself with "The Great " before their names.

def make_great(magician_name_list):
    index=0
    for magician in magician_name_list:
        magician_name_list[index]="The Great "+magician.title()
        index=index+1
    return (magician_name_list)
#make_great(magician_name) #commented out to make 8-11.
#print (magician_name) # See original list's value changed cause i did not use a copy.

#8-11
great_magicians_list=make_great(magician_name[:])
print (magician_name) # See orginal list unchanged cause i used a copy.
show_magicians(great_magicians_list)
show_magicians(magician_name)

