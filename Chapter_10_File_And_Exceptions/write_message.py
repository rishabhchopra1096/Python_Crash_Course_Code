file_name = 'programming.txt'
'''Writing Multiple Lines'''

with open(file_name , 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games")
#Now , if you open programming.txt: You will the above two lines squished together.
#Use \n and \t to create white spaces in your text file.

with open(file_name , 'w') as file_object:
    file_object.write("Using white spaces now: ")
    file_object.write("I love programming.")
    file_object.write("\nI love creating new games")

with open(file_name , 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in the browser.\n")
