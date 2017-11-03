def count_words(file_name):
    '''Counts the approximate number of words in a file'''
    try:
        with open(file_name) as f_obj:
            contents = f_obj.read()
    except IOError:
        pass
        # with open('missing_text.txt' , 'a') as file_object:
        #     file_object.write(file_name)
    else:
        #Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file "+ file_name + " has about " + str(num_words) + " words.")


count_words('alice.txt')

books = ['AliceInWonderland.txt' , 'Siddhartha.txt' , 'MobyDick.txt', 'LittleWomen.txt']

for book in books:
    count_words(book)
