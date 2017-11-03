with open('1.pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

print("\nUsing the for loop")
file_name = "1.pi_digits.txt"

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

print("\nStoring the file in a list of lines")
with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

