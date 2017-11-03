#Bascially slicing is used to create a subset of the list.
#How to : list_name[starting_index:end_index]
#This slicing creates a sublist of the list.

players=['charles','martina','michael','florence','eli']
print("This the list of all the players: ")
print (players)
print("These are the first 3 players:")
print players[0:3]#prints 1st ,2nd, 3rd element.
print("Player number 2,3,4 are: ")
print players[1:4]#prints 2nd, 3rd, 4th element.
print ("These are the first 4 players on the list: ")
#omitting the first index means that python will automatically start from the beginning.
print players[:4]#prints players 1-4th , without starting index, it starts at the beginning.
print ("Player 3, up till the last name on the list: ")
print players[2:]#prints players 3-till the last element.
print("These are the last 3 names on the list: ")
print players[-3:]#prints the last 3 players in the list.

print "\nLooping Through a Slice"
#Instead of looping through the entire list, python loops through only the first
# 3 names on the list of players.
print "Here are the first three players on my team:"
for player in players[:3]:
    print player.title()
print "Or usin the list comprehension:"
print "here is the list of all players with their names capitalized:"
print [player.title() for player in players]
#See Note:Applications:
# Slicing can be used to show specific parts of a list.
# While rpocessing data: It can be used to process the data into chucks of specific size.
# Web Application : display info in a series of pages with appropriate number of information
# on each page.




