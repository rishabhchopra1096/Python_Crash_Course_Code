#4-3
print (range(1,21))
for number in range(1,21):
    print (number)

# #4-4:One Million
one_million_numbers=list(range(1,1000001))
# for number in one_million_numbers:
#     print (number) #7.5 seconds

#4-5: Summing a million

print (min(one_million_numbers)) #0.2 sec
print (max(one_million_numbers))#0.2 sec
print("this is the summ of a million numbers: ")
print (sum(one_million_numbers)) # 0.2 seconds 500000500000

#4-6:Odd numbers:
print("\nThese are odd numbers: ")
odd_numbers=list(range(1,20,2))
for odd_number in odd_numbers:
    print (odd_number)

#4-7:Threes
print("\nThese are threes:")
multiples_of_3=list(range(3,33,3))
for multiples in multiples_of_3:
    print (multiples)

#4-8: Cubes:
print("\nThese are cubes")
cubes=[value**3 for value in range(1,11)]
for cube in cubes:
    print (cube)

#4-9: Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
#ALready did in 4-8:
cubes=[value**3 for value in range(1,11)]
print (cubes)






