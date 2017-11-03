#Combining lists with if statements:
# You can watch for special values that need to be treated differently than
#other values in the list.
# manage changing conditions efficiently ->availability of certain ingredients i the restaurant throughout the shift.

print "Checking for special items"

requested_toppings=['mushroom','green peppers','extra cheese']

for requested_topping in requested_toppings:
    print "Adding "+requested_topping+"!"

print"\nFinished making your pizza!"

#But what if the pizzeria runs out of green peppers? An if statement
#inside the for loop can handle this situation appropriately:

for requested_topping in requested_toppings:
    if requested_topping=='green peppers':
        print 'We are out of green peppers right now.'
    else:
        print "Adding "+requested_topping+"!"

print"\nFinished making your pizza!"

print "But how do we keep a track of the number of green peppers or the number of mushroom."
#maybe i have to make 2 interconnected lists-one represents the name and the other the
# of greenpeppers left. Then i would have to apply some if statements....YES THIS WOULD REQUIRE DICTIONARIES.

print " Checking that a list is not empty"
requested_toppings=[] #empty list defined

if requested_toppings: # Now if there is a requested_topping in resquested_toppings ,
#                        this statement evaluates to be true and the following block is executed.
    for requested_topping in requested_toppings:
        print "Adding"+requested_topping+"!"
    print "\nFinished making your pizza!"
#As requested_toppings is a empty list and there in element or requested_topping in it ,the above
#if statement evaluates to False and the following else statement will be executed.
else:
    print "Are you sure you want a plain pizza?"

print "Using Multiple List-What if someone wants an unusual topping?"

available_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings: #As we know in ,is a boolean expression which evaluates to True or
# False. So this line will tell if the requested topping is in available toppings. If not/False , else statement will be executed.
        print "Adding "+requested_topping+"!"
    else:
        print "Sorry , we do not have "+requested_topping+" :'("


# Lesson : Use spacing before and after a comparison operator.




