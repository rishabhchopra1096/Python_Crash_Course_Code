rivers = {
    'nile':'egypt',
    'godavari':'india',
    'seine':'france',

}

for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")

print("Here are a list of keys:")
for river in rivers.keys():
    print(river.title())

print("\nHere are a list of all countries in the dictionary.")
for country in rivers.values():
    print(country.title())



