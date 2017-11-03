favourite_fruits = ['apple','orange','mango']
all_fruits = ['apple','orange','mango','banana','guava','pear']

for fruit in all_fruits:
    if fruit in favourite_fruits:
        print("You really like " + fruit.title() + "!")
    else:
        print("You are not a fan of " + fruit.title() + ".")


