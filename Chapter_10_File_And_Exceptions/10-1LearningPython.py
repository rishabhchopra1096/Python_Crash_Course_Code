file_name = '10-1.LearningPython.txt'

with open('10-1.LearningPython.txt') as file_object:
    notes = file_object.read()
    print(notes.strip())

with open("10-1.LearningPython.txt") as file_object:
    for line in file_object:
        print(line.strip())

with open("10-1.LearningPython.txt") as file_object:
    notes = file_object.readlines()

for line in notes:
    print (line.strip())
