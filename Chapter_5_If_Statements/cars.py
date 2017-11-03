# Programming often involves examining a set of conditions and deciding which
# action to take based on those conditions. Pythons if statement allows you to
# examine the current state of a program and respond appropriately
# to that state.
# In this chapter youll learn to write conditional tests, which allow you to
# check any condition of interest. Youll learn to write simple if statements, and
#  youll learn how to create a more complex series of if statements to identify
#  when the exact conditions you want are present. Youll then apply this concept
#  to lists, so youll be able to write a for loop that handles most items in a
#  list one way but handles certain items with specific values in a different way.

cars = ['audi', 'bmw', 'subaru', 'toyota']
#print out name of each car
#names of most cars should be printed in title case
# however , 'bmw' should be printed in uppercase
#trying on my own:
for car in cars:
    if car == 'bmw':
        print car.upper()
    else:
        print car.title()
# The loop in this example first checks if the current value of car is 'bmw' .
# If it is, the value is printed in uppercase. If the value of car is anything
# other than 'bmw', its printed in title case.
#Notice: If you do not provide else , it does not skip 'bmw' in the for loop.
for car in cars:
    if car == 'bmw':
        print car.upper()
    print car.title()
# Audi
# BMW
# Bmw --> It includes 'bmw' in the for loop and does not skip it. Adding else
# applies that condition to 'bmw' and makes sure .title() is not applied.
# normal english buddy.
# Subaru
# Toyota

