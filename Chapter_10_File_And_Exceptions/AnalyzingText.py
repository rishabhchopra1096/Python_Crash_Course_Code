title = "Alice in Wonderland"
# title.split()
# #>>>['Alice','in','Wonderland']

# print(title.find(" "))

'''Trying to replicate the split method'''

index1 = 0
index2 = 0
spilt_list = []

while index2 <= len(title):
    if index2 == -1:
        break
    else:
        index2 = title.find(" ", index2+1)
        print(index2)
        to_add = title[index1:index2]
        print(to_add)
        spilt_list.append(to_add)
        print(spilt_list)
        index = index2 - index1
        print(index)
        index1+=index
        print(index1)


# print(title.find(" ",6))
# print(title.find(" ",9))
# print(len(title))


# file_name = 'alice.txt'
# try:
#     with open(file_name) as f_obj:
#         contents = f_obj.read()
#         print(contents)
# except IOError:
#     msg = "Sorry, the file " + file_name + " does not exist."
#     print(msg)
# else:
#     #Count the approximate number of words in the file.
#     words = contents.split()
#     print(contents.split())
#     num_words = len(words)
#     print("The file "+ file_name + " has about " + str(num_words) + " words.")







