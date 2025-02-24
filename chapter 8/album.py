def make_album(artist, title, num_songs=None):
    """Build a dictionary describing a music album."""
    album = {'artist': artist, 'title': title}
    if num_songs:
        album['num_songs'] = num_songs
    return album

while True:
    print("\nPlease enter the album details:")
    print("(enter 'quit' at any time to stop)")
    
    artist = input("Artist name: ")
    if artist.lower() == 'quit':
        break
    
    title = input("Album title: ")
    if title.lower() == 'quit':
        break
    
    num_songs = input("Number of songs (optional): ")
    if num_songs.lower() == 'quit':
        break
    
    if num_songs:
        album = make_album(artist, title, num_songs=int(num_songs))
    else:
        album = make_album(artist, title)
    
    print("\nAlbum created:")
    print(album)