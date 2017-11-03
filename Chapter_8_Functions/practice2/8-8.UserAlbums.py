albums = {}
def make_album(artist_name,album_title,number_of_tracks = ""):
    dic = {}
    dic["Artist's Name: "] = artist_name.title()
    dic["Album's Name: "] = album_title.title()
    if number_of_tracks:
        dic["Number of tracks: "] = number_of_tracks
    albums[artist_name.title()] = dic
    return(albums)

print(make_album('arijit singh','ashiqui2'))
