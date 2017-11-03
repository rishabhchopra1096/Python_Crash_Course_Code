rivers = ['ganga','brahmaputra','kaveri']
print(rivers)

print("\nAccessing Element of a list:")
print(rivers[0])

print("\nChanging an Element of the List: ")
rivers[1] = 'nile'
print(rivers)

print("\nAdding a new element to a list:")
rivers.append('godavari')
print(rivers)

print("\nInserting elements into the list:")
rivers.insert(3,'narmada')
print(rivers)

print("\nRemoving Elements from a List Using Index Position")
print("\tRemoving elements using del statement:")

del rivers[0] # Removing ganga
print(rivers)
print("\tRemoving elements using pop")
last_river = rivers.pop()
print(last_river)
print(rivers)

print("Removing Elemts from a List Using Value")
rivers.remove('kaveri')
print(rivers)

print("Recreating rivers to use Sorted() and Sort()")
rivers = ['ganga', 'brahmaputra', 'kaveri']

print("Using Sorted to arrange in alphabetical order, temporarily.")
print(sorted(rivers))
print(rivers)

print("Using Sorted to arrange list in reverse alphabetical order, temporarily.")
print(sorted(rivers , reverse = True))
print(rivers)

print("Using sort to arrange list in alphabetical order , permanently.")
rivers.sort()
print(rivers)

print("Using sort to arrange list in reverse alphabetical order, permanently.")
rivers.sort(reverse = True)
print(rivers)

print("Reversing the order of the current list , permamnently.")
rivers.reverse()
print(rivers)

print("The length of the list is:")
print(len(rivers))

















