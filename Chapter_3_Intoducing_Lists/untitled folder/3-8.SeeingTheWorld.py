# 3-8. Seeing the World: Think of at least five places in the
# world you’d like to visit.
# Store the locations in a list. Make sure the list is not
# in alphabetical order.

destinations = ['new zealand','paris' ,'new york','london','hawaii']

# Print your list in its original order. Don’t worry about
# printing the list neatly, just print it as a raw Python
# list.
print(destinations)

# Use sorted() to print your list in alphabetical order without
# modifying the actual list.
print(sorted(destinations))

#Show that your list is in original order by printing it.
print(destinations)

# Use sorted() to print your list in reverse alphabetical order
# without changing the order of the original list.
print(sorted(destinations , reverse = True))

#Show that your list is still in its original order by
# printing it again.
print(destinations)

# Use reverse() to change the order of your list.
destinations.reverse()
# Print the list to show that its order has changed.
print(destinations)

# Use reverse() to change the order of your list again.
destinations.reverse()
#Print the list to show it’s back to its original order.
print(destinations)


# Use sort() to change your list so its stored in
# alphabetical order.
destinations.sort()


# Print the list to show that its order has been changed.
print(destinations)

# Use sort() to change your list so it’s stored in reverse
# alphabetical order.
destinations.sort(reverse = True)

# Print the list to show that its order has changed.
print(destinations)


