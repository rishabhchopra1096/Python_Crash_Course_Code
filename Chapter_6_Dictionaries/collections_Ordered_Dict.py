from collections import OrderedDict
favourite_languages = OrderedDict()

favourite_languages['jen'] = 'python'
favourite_languages['sarah'] = 'c'
favourite_languages['edward'] = 'ruby'
favourite_languages['phil'] = 'python'

# favourite_languages = {
#     'jen':'python',
#     'sarah':'c',
#     'edward':'ruby',
#     'phil':'python'
# }

for name, language in favourite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

