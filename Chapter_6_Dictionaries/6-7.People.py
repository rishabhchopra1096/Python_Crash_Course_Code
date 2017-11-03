person1_info = {
    'name':'rishabh',
    'age':'20',
    'city':'new delhi',
    'last name':'chopra'
}

person2_info = {
    'name':'rohan',
    'last name':'chopra',
    'age':'20',
    'city':'pune'
}

person3_info = {
    'name':'rhea',
    'last name':'lungani',
    'age':'20',
    'city':'bombay',
}

people = [person3_info,person2_info,person1_info]

for person_info in people:
    for info_type , info in person_info.items():
        print(info_type.title() + ":" + info.title())


