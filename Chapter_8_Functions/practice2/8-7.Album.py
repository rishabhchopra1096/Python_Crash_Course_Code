def make_album(artist_name,album_title,number_of_tracks = ""):
    album = {}
    album[artist_name.title()] = album_title.title()
    if number_of_tracks:
        album['Number of tracks '] = number_of_tracks
    return album

print(make_album('arijit singh','ashiqui2',9))
print(make_album('enrique','why not me'))
print(make_album('david guetta','dangerous',10))

