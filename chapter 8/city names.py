def make_album(artist, title, num_songs=None):
    """Build a dictionary describing a music album."""
    album = {'artist': artist, 'title': title}
    if num_songs:
        album['num_songs'] = num_songs
    return album

# Creating three dictionaries representing different albums
album1 = make_album('Taylor Swift', '1989')
album2 = make_album('Adele', '25')
album3 = make_album('Ed Sheeran', 'Divide', num_songs=16)

# Printing each return value to show the dictionaries are storing the album information correctly
print(album1)
print(album2)
print(album3)