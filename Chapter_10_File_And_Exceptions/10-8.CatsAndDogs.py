with open('cats.txt','w') as file_object:
    file_object.write('Pussy\nTushy\nKhushy')


with open('dogs.txt','w') as file_object:
    file_object.write('Pat\nTyler\nKamina')

def read_file(file_name):
    print(file_name.title() + ":") #So the code below shows which file was not found.
    with open(file_name) as file_object:
        contents= file_object.read()
        print(contents)

try:
    read_file('cats.txt')
    read_file('dogs1.txt')
except IOError:
    print("The file was not found.")

