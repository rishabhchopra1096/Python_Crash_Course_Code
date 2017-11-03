car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car != 'audi'? I predict False.")
print( car =='audi')

# in not in > < >= <= or and

if 5>4 and 5<=(6-1):
    print("\nYAY!")

numbers = range(1,11)

if 1 in numbers and 11 not in numbers:
    print("\n1 is in numbers and 11 is not in numbers.")

print(1 in numbers)
print(11 not in numbers)

if 1 in numbers or 11 in numbers:
    print("\n1 is in numbers but 11 is not in numbers.")


print("\n5 test true :")
print(5>2)
print(2>=1)
print(1<=2)
print(1<2)
print(1 in numbers)

print("\n5 test resulting false.")
print(2>5)
print(1>=2)
print(2<=1)
print(2<1)
print(3 not in numbers)


print("Testing using lower():")

word1 = 'rIsHaBh'
word2 = 'RishABh'

print(word1 == word2 )
print(word1.lower() == word2.lower())

















