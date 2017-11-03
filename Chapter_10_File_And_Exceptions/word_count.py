file_name = 'alice.txt'
def count_words(file_name):
    '''Counts the approximate number of words in a file'''
    try:
        with open(file_name) as f_obj:
            contents = f_obj.read()
    except IOError:
        msg = "Sorry, the file " + file_name + " does not exist."
        print(msg)
    else:
        #Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file "+ file_name + " has about " + str(num_words) + " words.")


count_words('alice.txt')

books = ['AliceInWonderland.txt' , 'Siddhartha.txt' , 'MobyDick.txt', 'LittleWomen.txt']

for book in books:
    count_words(book)

'''If i did not have an except block in count_words'''

# def count_words(file_name):
#     with open(file_name) as f_obj:
#         contents = f_obj.read()
#         words = contents.split()
#         num_words = len(words)
#         print("The file "+ file_name + " has about " + str(num_words) + " words.")

# books = ['AliceInWonderland.txt' , 'Siddhartha.txt' , 'MobyDick.txt', 'LittleWomen.txt']

# for book in books:
#     count_words(book)

