with open('AliceInWonderLand.txt') as file_object:
    contents = file_object.read()
    print(contents.lower().count("is"))

