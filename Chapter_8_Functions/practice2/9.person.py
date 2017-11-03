def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first':first_name,'last':last_name}
    return person

musician = build_person('Jimmy','Hendrix')
print(musician)

def build_person(first_name, last_name, age =""):
    """Return a dictionary of information about a person."""
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person

print(build_person('rishabh','chopra',20))

