# file_name = 'alice_in_wonderland.txt'

# with open(file_name) as file_object:
#     contents = file_object.read()
#     print(contents)

file_name = 'alice1.txt'
try:
    with open(file_name) as f_obj:
        contents = f_obj.read()
except IOError:
    msg = "Sorry, the file " + file_name + " does not exist."
    print(msg)

