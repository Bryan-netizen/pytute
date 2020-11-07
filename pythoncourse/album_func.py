def make_album(name, title, track=''):
    """Describe a music album."""
    album = {'artist': name, 'album': title}
    if track:
        album[track] = 'track'

    return album


song = make_album('elvis prestley', 'satisfy me', track=7)
print(song)
song = make_album('jonte john', 'everything')
print(song)
song = make_album('bob marley', 'roots')
print(song)


def make_album(name, title):
    """Album dictionary."""
    album = {'artist': name, 'album': title}
    return album


while True:
    print("\nPlease enter artist name: ")
    print("enter 'q' at any time to quit.")
    art_name = input("name: ")
    if art_name == 'q':
        break
    alb_name = input("title: ")
    if alb_name == 'q':
        break

    artist_album = make_album(art_name, alb_name)

    print(artist_album)
