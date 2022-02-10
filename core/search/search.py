from core.const import SearchResults, UserType
from core.extract.extract_songs import extract_songs
from core.modules.user import User
from core.parse.parse import parse_songs
from core.transform import *
from core.user_interface.show_results import *
from core.user_interface.user_input import *

songs = extract_songs("C:\\Users\\orian\\Desktop\\songs\\*")
new_songs = parse_songs(songs)
artists = get_artists(new_songs)
albums = get_albums(new_songs)


def search_artists():
    show_search_results(artists.keys())


def search_albums_by_artist():
    name = artist_name()
    show_search_results(artists.get(name))
    return


def search_artist_top_songs(user: User):
    name = artist_name()
    artist_songs = []
    for album in artists.get(name):
        for song in albums.get(album):
            artist_songs.append(song)
    sorted_songs = sorted(artist_songs, key=lambda song: song.popularity, reverse=True)
    artist_songs.clear()
    for song in sorted_songs:
        artist_songs.append(song.name)
    if user.type is UserType.REGULAR:
        show_search_results(artist_songs[0:SearchResults.REGULAR_RESULTS + 1])
    else:
        show_search_results(artist_songs[0:SearchResults.PREMIUM_RESULTS + 1])


def search_songs_by_album():
    name = album_name()
    album_songs = []
    album = albums.get(name)
    if album is None:
        return
    for song in album:
        album_songs.append(song.name)
    show_search_results(album_songs)
    return album_songs
