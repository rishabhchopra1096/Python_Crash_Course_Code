#Learning C:
file_name = "10-1.LearningPython.txt"

with open(file_name) as file_object:
    notes = file_object.readlines()

print(notes)
replacingPython = ""
print(replacingPython)
for line in notes:
    replacingPython += line
print("Before Replacing:")
print(replacingPython)
replacingPython = replacingPython.replace('Python',"C")
print(replacingPython)
