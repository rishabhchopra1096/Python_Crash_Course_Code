#6-3:
glossary={'sort() method':'sorts the list in alphabetical order permanently',
    'sorted() function':'sorts the list in alphabetical order temporarily',
    'range() function': 'makes a list of numbers from first parameter to the second parameter-1',
    'tuple':'tuple is just like a listexcept it cannot be modified.',
    'remove() method':'removes an element from the list',
    }

print ("sort() method: "+"\n\t\t"+glossary['sort() method'])
print ("sorted() function: "+"\n\t\t"+glossary['sorted() function'])
print ("tuple: "+"\n\t\t"+glossary['tuple'])
print ("sort() method: "+"\n\t\t"+glossary['sort() method'])
print ("remove() method: "+"\n\t\t"+glossary['remove() method'])



print("\nGlossary 2:")
glossary={'sort() method':'sorts the list in alphabetical order permanently',
    'sorted() function':'sorts the list in alphabetical order temporarily',
    'range() function': 'makes a list of numbers from first parameter to the second parameter-1',
    'tuple':'tuple is just like a listexcept it cannot be modified.',
    'remove() method':'removes an element from the list',
    }

for concept, explanation in glossary.items():
    print (concept+":\n\t"+explanation)

#6-5:Rivers:
rivers={'ganga':'india','nile':'egypt','brahmaputra':'india'}
for river, country in rivers.items():
    print(river.title()+" is in "+country.title())
print("Here are the rivers: ")
for river in rivers.keys():
    print river.title()

print("Here are the countires: ")
for country in rivers.values():
    print country.title()

#6-6: Polling:

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

voters=['rishabh','rohan','manan','jen','sarah']
for voter in voters:
    if voter in favorite_languages.keys():
        print(voter.title()+", Thank you for responding to out poll.")
    else:
        print(voter.title()+", Please take out favourite language poll.")



