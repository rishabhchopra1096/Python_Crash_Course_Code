import json

file_name = 'username.json'

with open(file_name) as file_object:
    username = json.load(file_object) # read the information stored in username.json
    print("Welcome back, " + username + "!")
