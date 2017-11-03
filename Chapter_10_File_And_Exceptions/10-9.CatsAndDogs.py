def read_file(file_name):
    # print(file_name.title() + ":") #So the code below shows which file was not found.
                                    #This line pof code is needed in 10-8 , not in 10-9
                                    # cause we are failing silently.
    with open(file_name) as file_object:
        contents= file_object.read()
        print(contents)

try:
    read_file('cats.txt')
    read_file('dogs1.txt')
except IOError:
    pass

