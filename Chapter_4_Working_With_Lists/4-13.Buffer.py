basic_foods = ('tea','coffee','biscuit','bread','omelette')

for food in basic_foods:
    print(food)

# basic_foods[4] = 'jam' #Rejected
# TypeError: 'tuple' object does not support item assignment
basic_foods = ('tea','coffee','rusk','bread','jam')
print(basic_foods)
