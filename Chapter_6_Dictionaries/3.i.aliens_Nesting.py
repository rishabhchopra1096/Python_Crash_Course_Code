print("A list of dictionaries")
# Sometimes youll want to store a set of dictionaries in a list
# or a list of items as a Value in a dictionary.
# This is called nesting.
# you can nest a set of dictionaries inside a list , a list of items inside a dictionary
# or even a dictionary inside a dictionary.
# Nesting is a powerful feature.

# Before we just wrote about one alien , whose colour was green and if you shot him , you get
# 5 points.

alien_0={'color':'green', 'points':5}
alien_1={'color':'yellow', 'points':10}
alien_2={'color':'red', 'points':15}
aliens=[alien_0, alien_1, alien_2]
# aliens={alien_0, alien_1, alien_2}
#TypeError: unhashable type: 'dict'
#This happens as you cannot use a mutable object sucha s a distionary,variable or lists as a key
#in a dictionary.
print("Here is the list aliens with 3 dictionaries in it:")
print aliens

# So here what we did is , we created 3 different dictionaries for 3 different colored aliens with different points
# for killing each. Then we nested these 3 dictionaries in one list.
print("Here are the dictionaries: ")
for alien in aliens:
    print alien
# Finally we loop throgh a list , and we print out the details of each alien.







# A more realistic example would involve more than three aliens with code that automatically generates each alien.
#In the following example we use range() to create a fleet of 30 aliens.
#Making an empty list for storing aliens.
print"Making 30 aliens"
# This one is simple, just making an empty list with dictionaries appended to it with the for loop
#30 times using the range function.
aliens2=[]

#Make 30 green aliens.
# Range: Makes it easier to create a list of numbers:
print range(0,10) # will make a list of numbers from 1 till 9
print range(10) # If you do not enter the starting number , the method range print from 0 till (the input number-1)
#therefore ,range(0,10)=range(10)

for alien_number in range(30): # range returns a set of numbers, which just tells Python how many times we want the loop to repeat
    new_alien={'color':'green', 'points':5, 'speed':'slow'}
    aliens2.append(new_alien) #  Each time the loop runs we create a new alien and then append each new alien to the list aliens.

print("printing the the first 5 aliens.")
for alien in aliens2[:5]:
    print alien
print"................"

print("Show how many aliens you created:")
print len(aliens2)






#These aliens all have the same characteristics, but Python considers each one a separate object,
# which allows us to modify each alien individually.
# How might you work with a set of aliens like this? Imagine that one aspect of a game has some aliens changing color and moving faster as the game progresses.
# When its time to change colors, we can use a for loop and an if statement to change the color of aliens.
# For example, to change the first three aliens to yellow, medium speed aliens worth 10 points each, we could do this:
print "\nChanging the colour and speed of aliens:"
#Make an empty list for storing aliens
aliens2=[]
#Make 30 green aliens
for alien_number in range(30):# alien_number is just put in for the sake of it showing for how many aliens or time will the loop go on
    new_alien={'color':'green','points':5, 'speed':'slow'}
    aliens2.append(new_alien)




#Now,ACTUALLY TO CHANGE THE COLOUR :
for alien in aliens2[0:3]:
    if  alien['color']=='green': #True
         alien['color']='yellow'#-->Re-assignment of key->'color'
         alien['speed']='medium'
         alien['points']=10
    elif alien['color']=='yellow':
        alien['color']='red'
        alien['speed']='fast'
        alien['points']=15

for alien in aliens2[:5]:
    print alien
print".............."

# Now let's change aliens a little to use the elif block above that converts yellow aliens to red..and so on.
# aliens2=[]
# for alien_number in range(0,10,2):
#     new_alien={'color':'green', 'speed':'slow','points':5}
#     aliens2.append(new_alien)#At every even place , we will have a green alien.
# for alien_number in range(1,10,2):
#     new_alien={'color':'yellow','speed':'medium','points':10}
#     aliens.append(new_alien)# atevery odd place we will have a yellow alien.

print "\nMy own experiment with green and yellow aliens:"
# print aliens

# #i want to put a green alien every eve place
# L=['h','e','l','l','o','!']

#The above did not work.
# Now first i will append all 20 green aliens
#and then using the while loop i will replace every green alien at an odd index to
#a yellow alien.
# The above method di not work because range(0,10,2) has the value 5 , that it means it loops
# 5 times instead of what i thought. I thought it will loop at alternate indeces but that is not how it works.
# 2ndly, below i have first appended 20 aliens and then replaces them with yellow because i was not able to add
# green aliens to all even indeces for a blank list: IndexError was coming as there was nothing to replace in a blank list.
# So therefore i first filled the list and then replaces every alternate index after 1 to a yellow alien.
aliens=[]
for alien_number in range(20):
    new_alien={'color':'green', 'speed':'slow','points':5}
    aliens.append(new_alien)
index=1
while index<20:
    new_alien={'color':'yellow','speed':'medium','points':10}
    aliens[index]=new_alien
    index=index+2 #Every odd index will have a yellow alien

print aliens




