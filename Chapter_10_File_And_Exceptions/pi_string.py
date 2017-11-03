filename = '1.pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

filename= 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

birth_date = input("Enter your birth date in the form mmddyy and i'll tell you "+
    "\nIf your birthdate appears in the first million decimal places of pi!")

line_number = 1


if str(birth_date) in pi_string:
    print("Yes , your birthdate appears in the first million decimal places of pi")
else:
    print("No , your birthdate does not appear in the first million decimal places of pi. ")




