animals = ['dogs','cats','rats']

for animal in animals:
    print(animal)

for animal in animals:
    index_after = animals.index(animal) + 1
    if index_after <= 2:
        print(animal.title() + " run after " + animals[index_after])
    else:
        print(animal.title() + " run after food.")
print("Any of these animals would make a good pet.")


