#In the earlier example of favorite programming languages,
#if we were to store each persons responses in a list, people could choose more than one
#favorite language. When we loop through the dictionary, the value associated with each person
#would be a list of languages rather than a single language.
#Inside the dictionarys for loop,
#we use another for loop to run through the list of languages associated with each person.

favourite_languages={
    'jen':['python','ruby'], # Jen likes python and ruby
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
    }
for name, languages in favourite_languages.items():
    #print "Hi"+name.title()+"! I see your favourite languages are:"+language.title() # now language is a
    #list so i don't know if .title will be directly applied to each element in the list?
    #let's see. NO! AttributeError: 'list' object has no attribute 'title'
    #print "Hi"+name.title()+"! I see your favourite languages are:"+language
    #TypeError: cannot concatenate 'str' and 'list' objects
    #print "Hi "+name.title()+"! I see your favourite languages are:"+str(language)
    #Hi Edward! I see your favourite languages are:['ruby', 'go']
    # Now what if i do not want a list at the end of the sentence , i dont want any square bracket or quotes/
    # Seems like i only want the elements on the list
    #so i will use another for loop within this for loop:
    if len(languages)==1: # This if and elif was added after the explanation given below.
        print "Hi "+name.title()+"! I see your favourite language is: "
    elif len(languages)>1:
        print "Hi "+name.title()+"! I see your favourite languages are:"
    for language in languages:
        print language.title()
    print "\n"
    # And that's how we use a for loop within a for loop.
# Lets revise:
# We started by putting values of keys(names of people) in a list.
# Then the for loop stored all the keys in variable name.
# and store all the values,i.e the list of languages in variable languages.
# before the for loop could end and go back to save next key in name and next value in variable:
# There is a for loop : That states: for for language in languages: meaning its refering to individual
# elements in the list of languages. Then it says: print language.title()
# which prints the first language in the variable "languages" storing a list of languages.
# then it goes back to the line for language in languages IF and ONLY IF there is another language.
# Or else it ends this for loop and goes back at the top to the BIGGER for loop and starts storing the
#next key in name and the next value,i.e the list of languages in the variable languages.
# at last we enter an if and elif block to differ is/are.
# NOTE :You should not nest lists and dictionaries too deeply. If youre nesting items much deeper than what you
# see in the preceding examples or youre working with someone elses code with significant levels of nesting,
# most likely a simpler way to solve the problem exists.




