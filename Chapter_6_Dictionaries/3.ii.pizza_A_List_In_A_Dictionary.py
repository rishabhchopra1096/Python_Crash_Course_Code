print "A List in a Dictionary"
# Rather than putting a dicitonary inside a list , its sometime useful to put a
#list inside a dictionary.
# A list can store the kinds of pizza toppings.
# with a dictionary , a list of toppings can be only one aspect of the pizzza yo are describing.
# In the following example, two kinds of information are stored for each pizza.
# A type of crust and a list of toppings.
# The list of toppings is a value of the key:'toppings'.
# Yes , a value can be a list.
print "Question: Can a key be a list? "
print "I dont think so cause keys are like variables"
print "Don't forget to check."
#https://wiki.python.org/moin/DictionaryKeys

pizza={'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
    }
# Let's revise how to print values of keys in a dictionary:
# Format: print name_of_dictionary['name_of_key']
print "\nHere are the values of the keys in pizza:"
print pizza['crust']
print pizza['toppings']
print "\n"
print "You order a "+pizza['crust']+" crust pizza with the following toppings:"
for topping in pizza['toppings']:
    print "\t"+topping #"\t" added later and i forgot to put the + sign between "\t" and topping-->SyntaxError

# Lesson: You can nest a list inside a dictionary any time you want more than one value
# to be associated with a single key in a dictionary.

