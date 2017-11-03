#TAKEAWAY:
#1. Dictionaries: connect pieces of related information.
#2. for eg: A dictionary representing a person and then store as much information as
# you want about that person.
# Like profression, age, height ,etc.
#3. A dictionary is a collection of key-value pairs. Each key is connected to a value
# you can use the key to access the value stored in that key. Kind of like how a variable stores a value.
#4.In python , a dictionary is wrapped in braces {}, with a seies of key-value pairs inside the braces:

# 5.alien_0={'color' : 'green' , 'points' : 5}
# A key-value pair is a set of values associated with each other.
#A keys value can be a number, a string, a list, or even another dictionary.
# When you provide a key ,Python returns the value associated with that key.
# Every key is connected to its value by a colon , and individual key-value pairs are
# separated by commas. You can store as many key-values as you want in a dictionary.
#To get the value associated with a key , give the name of the dictionary and then place the key
#inside a set of square brackets.
# FORMAT FOR ACCESSING A VALUE ASSOCIATED TO A KEY:
#print name_of_dictionary[key_name]
#You can have an unlimited ammount of key-value pairs in a dictionary.

#6.Dictionaries are dynamic structures. You can add new key-values at any time.
#Format to add new key-value pairs : name_of_dictionary['new_key']=value
##The order differs here as python does not care about the order in which
#you added key-value pairs. It only cares about the connection between the
#key:value. In contrast, lists are ordered.

#7. To modify , give the name of the dictionary with the key in square brackets and then the value you want
# associated with it.
# So format for modifying a key: name_of_dictionary['existing_key_name']=new_value

#8.# Use the del statement to completely remove a key-value pair.
# format :del name_of_dictionary['key_name']
# format for lists: del name_of_list[index_postion]
# del removes the element permanently.

#like we used index in list, we use key_name in dictionary.

alien_0={'color' :'green'}
print ("The colour of the alien is : ")
print alien_0['color']
alien_0={'color' : 'green' , 'points' : 5}
new_points = alien_0['points']
print "\nYou just earned "+str(new_points)+" points! :D"
#If you run this code every time an alien is shot down, the alien's point
# value will be retrieved.

print "\nAdding New Key-Value Pairs"
#Dictionaries are dynamic structures. You can add new key-values at any time.
#Format to add new key-value pairs : name_of_dictionary['new_key']=value
# Adding alien's x and y coordinates :
alien_0={'color' : 'green' , 'points' : 5}
print alien_0
alien_0['x position']=0
alien_0['y position']=25
print alien_0
#The order differs here as python does not care about the order in which
#you added key-value pairs. It only cares about the connection between the
#key:value. In contrast, list have order.


print "\nStarting with an Empty Dictionary"
print "It's often convenient to start from a empty dictionary and then adding elements into it."

alien_0={}
print alien_0
alien_0['color']='green' #Do not forget to put the value in quots as you know,Python does not accept plain text.
alien_0['points']=5
print alien_0



print "\nModifying Values in a Dictionary"
# To modify , give the name of the dictionary with the key in square brackets and then the value you want
# associated with it.
# So format for modifying a key: name_of_dictionary['existing_key_name']=new_value
print alien_0
print ("The alien is "+alien_0['color']+" in color.")
alien_0['color']='yellow'
print alien_0
print("Now, the alien is "+alien_0['color']+" in color.")
print("\nFor a more interesting example, lets track the position of an alien that can move at different speeds.")
print("Well store a value representing the aliens current speed and then use it to determine how far to the right ")
print("the alien should move:")

alien_0={'x_position':0 ,'y_position':25 ,'speed':'medium'}
print (alien_0)
print "\norginal x-position: "+str(alien_0['x_position']) #Don't forget to put the quotes around key.
print "Move the alien to the right."
#Determine how far to move the alien based on its current speed.

if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed'] == 'medium':
    x_increment=2
elif alien_0['speed'] == 'fast':
    x_increment=3
alien_0['x_position']=alien_0['x_position']+x_increment
print "New x-position: "+str(alien_0['x_position'])




print "Removing Key-Value Pairs"
# Use the del statement to completely remove a key-value pair.
# format :del name_of_dictionary['key_name']
# format for lists: del name_of_list[index_postion]

print alien_0
del alien_0['speed']
print alien_0
# del removes that key-value pair permanently.





