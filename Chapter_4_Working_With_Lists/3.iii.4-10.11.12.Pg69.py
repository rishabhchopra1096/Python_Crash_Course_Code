#4-10: Slices:
laptop=['macintosh','dell','HP','alienware','acer','samsung']
print("The first 3 items in the list are: ")
print (laptop[:3])
print("Three items from the middle of the list are: ")
print (laptop[1:4])
print("The last 3 items on the list are: ")
print (laptop[-3:])

#4-11:My Pizzas,Your Pizzas:

my_pizza=['cheese','spicy chicken','golden delight','loaded','farmhouse']
friend_pizza=my_pizza[:]
my_pizza.append('onion')
friend_pizza.append('capsicum')
print("My favourite pizzas are: ")
for pizza in my_pizza:
    print(pizza.title())
print("My friend's favourite pizza are: ")
for pizza in friend_pizza:
    print(pizza.title())

#4-12:More Loops:
my_foods=['pizza','falafel','carrot cake']
friends_foods=my_foods[:]#copy made

print ("My favourite foods are:")
print (my_foods)
print ("\nMy friend's favourite foods are:")
print (friends_foods)
my_foods.append('canoli')
print("\nMy new favourite foods are:")
print (my_foods)
friends_foods.append('ice cream')
print ("\nMy friend's new favourite foods are:")
print (friends_foods)
print("\tUsing for loop:")
print ("\n\tMy new favourite foods are:")
for food in my_foods:

    print (food)
print ("\n\tMy friend's new favourite foods are:")
for food in friends_foods:

    print (food)


