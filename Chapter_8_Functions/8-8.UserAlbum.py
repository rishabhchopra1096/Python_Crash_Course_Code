def make_album(artist_name,album_title,number_of_tracks=''):
    if number_of_tracks:
        return {'artist':artist_name.title(),'album':album_title.title(),'number of tracks':number_of_tracks}
    return {'artist':artist_name.title(),'album':album_title.title()}
while True:
    intro=input("Enter anything in quotes to answer some questions about your taste in music OR\nEnter 'quit' at any moment to end the program.")
    if intro=='quit':
        break

    a_name=input("Who is your favourite singer?")
    if a_name=='quit':
        break
    a_title=input("Ohkay, so tell me the name of an album of this singer?")
    if a_title=='quit':
        break
    n_o_t=input("Good! How many songs are in this album?\nJust press enter '' if you don't know the answer.")
    if n_o_t=='quit':
        break
    else:
        user_album=make_album(a_name,a_title,n_o_t)
        print (user_album)

# Enter anything in quotes to answer some questions about your taste in music OR
# Enter 'quit' at any moment to end the program.'ok'
# Who is your favourite singer?'arijit singh'
# Ohkay, so tell me the name of an album of this singer?'tum hi ho'
# Good! How many songs are in this album?
# Just press enter '' if you don't know the answer.''#'
# {'album': 'Tum Hi Ho', 'artist': 'Arijit Singh'}
# Enter anything in quotes to answer some questions about your taste in music OR
# Enter 'quit' at any moment to end the program.


