favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

names = ['jen','rohan','rishabh','sarah','edward','nishi']

for name in names:
    if name in favorite_languages.keys():
        print(name.title() + " has already taken the poll.")
    else:
        print("Hey, " + name.title() + "! Would you like to take out 'favourite languages' poll ?")

