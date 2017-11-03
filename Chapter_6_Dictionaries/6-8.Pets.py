Lexus = {
    'name':'lexus',
    'animal':'dog',
    'owner':'rishabh'
}

Mimi = {
    'name':'mimi',
    'animal':'dogiiii',
    'owner':'rohan'
}

Tyler = {
    'name':'tyler',
    'animal':'dog',
    'owner':'dhairya',

}

pets = [Lexus,Mimi,Tyler]

for pet in pets:
    print(pet['name'].title() + ":")
    for info_type , info in pet.items():
        if info_type == 'animal':
            print("is a " + info)
        elif info_type == 'owner':
            print("is owned by " + info.title())

