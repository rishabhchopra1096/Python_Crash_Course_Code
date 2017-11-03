my_pizzas = ['margherita','peri-peri','golden delight']

friend_pizzas = my_pizzas[:]

my_pizzas.append('chicken tikka')
friend_pizzas.append('hawain pizza')

print("My favourite pizzas are:")
for pizza in my_pizzas:
    print(pizza.title())

print("My friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())
