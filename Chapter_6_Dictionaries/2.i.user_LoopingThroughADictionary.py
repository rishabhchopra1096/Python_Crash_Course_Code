# You can loop through all of a dictionarys
# 1.key-value pairs,
# 2.through its keys,
# 3.or through its values.

print "1. Looping Through All Key Value Pairs"
# Considering a new dictionary designed to store information about a
# a user on a website.
# The following dictionary would store one persons username , first name
# and last name.
user_0={
    'username':'rishabhchopra10',
    'first':'rishabh',
    'last':'chopra',
}
print user_0.items()
#This will return a LIST of the KEY-VALUE PAIRS.
#[('username', 'rishabhchopra10'), ('last', 'chopra'), ('first', 'rishabh')]

for key, value in user_0.items():
    print "\nKey: "+key
    print "Value: "+value
# 1st half:
# okay , so basically what happened above is:
# first we create names for the two variables that will hold the key and
# value in each key-value pair.
# it can be any names :
# it will even work if we would have entered : for kotty, votty in user_0.items()
# 2nd half:
# the .items method returns a list of key-value pairs.
# next , the for loop contains each of the key-value pairs in the two variables
# looping from one pair to another.
# Notice again, the key-value pairs are not returned in the order in which they were
# stored. Python does not care about the order. It tracks only the connections between
# individual keys and their values.

favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }
for name, language in favorite_languages.items():
    print "\nName: "+name.title()
    print "language<3: "+language.title() # .title added later.

#QUESTION: if i do not put .items()--> This error comes:
# ValueError: too many values to unpack
# What does it mean ?
# See , when we target the dictionary is total: There are too many values to fit in
# just 2 variables. When we add .items() ,it helps to form a list of objects-each having
# only two values for the respective 2 variables.
# Now if we put name1 ,language1 , name2 , language2 ...till language4 i think it will print.
# ..as we have 4 names and 4 languages. Let's see.

# for name1, language1, name2, language2, name3, language3, name4, language4, name5, language5 in favorite_languages:
#         print name1
#         print language1
#ValueError: need more than 5 values to unpack



print name # phil cause the last value of the variable name was phil
print language # python as the last value of the variable language was python

print "\n2. Looping thorugh all the keys in a dictionary"
# The key() method is only useful when you have no need of the values in a dictionary.
favorite_languages={
    'jen':'python', # DONT FORGET THE COMMAS
    'sarah':'c', #YOU ALWAYS FORGET THE COMMAS
    'edward':'ruby',
    'phil':'python',
}

#.keys() method makes a list of all names of the keys.
# ['sarah', 'edward', 'jen', 'phil']
print "list of keys:"+str(favorite_languages.keys())

for name in favorite_languages.keys():
    print name.title()

# IMP : Looping through keys is actually the default behaviour when loopoing through a dictionary.
#SO : This will have the same output:
print "Showing default behaviour: "
for name in favorite_languages:
    print name.title()

#Lets print a message to a couple of friends about the languages they chose.
# This is what i did:
for name, language in favorite_languages.items():
    print "Hi "+name.title()+"! I see your favourite language is "+language.title()+"."
#This is what is in the book:
# You printed it for all .. the question was to print it only for your friends.
friends=['phil','sarah']
print "\n"
for name in favorite_languages.keys():
    print name.title()
    if name in friends:
        print "   Hi "+name.title()+"! I see your favourite language is "+favorite_languages[name].title()+"."
    else:
        print "   I don't know you." # i added this.

# We can also find out whether a person took our poll or not:
if 'erin' not in favorite_languages.keys():
    print "\nErin, please take our poll."

# Now , I did this just because it came to my head: Not in the book: See page 106
L=['x','y','z','x','a','z','y','n','y','r','o','c','x']
print_ed=[]
L_without_repetition=[]
all_repeated_letters=[]
for letter in L:
    if letter in print_ed:
        all_repeated_letters.append(letter)
    else:
        L_without_repetition.append(letter)
    print_ed.append(letter)

print L_without_repetition
print sorted(L_without_repetition) # Similar to set(L) and same as sorted(set(L))
print all_repeated_letters
print sorted(all_repeated_letters)
print print_ed

# Now , all you have to do is enter the name of the courses you want to do in the list L,
#dont worry if you can't keep track of your repetition. It will output a list with repeated letters
# and a list with no repeated names. Well Done!
#But python already has a function for this.
# its called set. It will print only unique values.
print set(L)
print sorted(set(L)) # Same as print sorted.(L_without_repetition) above.

#When you wrap set() around a list that contains duplicate items,
# Python identifies the unique items in the list and builds a set from those items.

print "\nLooping Through a Dictionary in Order"
#One way to return items in a certain order is to sort the keys as theyre returned in the for loop.
#You can use the sorted() function to get a copy of the keys in order.
# Just use the sorted function for this.

print favorite_languages
print sorted(favorite_languages.keys()) # Remember , the sorted function sorts the list/dictionary in alphabetical order.
for name in sorted(favorite_languages.keys()):
    print name.title()+", thank you for taking the poll."

print "\nLooping Through all Values in a Dictionary"
# use values() method.

print favorite_languages
print "The following lanuages have been mentioned:"
for language in favorite_languages.values():
    print language.title()

print set(favorite_languages.values())

for language in set(favorite_languages.values()):
    print language

print set(favorite_languages.values())
# A set is similar to a list except that each item in the set must be unique.







