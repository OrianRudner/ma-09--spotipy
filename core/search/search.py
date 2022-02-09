from core.transform import *
from core.extract.extract_songs import extract_songs
from core.parse.parse import parse_songs
from core.modules.song import Song

songs = extract_songs("C:\\Users\\orian\\Desktop\\songs\\*")
new_songs = parse_songs(songs)
artists = get_artists(new_songs)
albums = get_albums(new_songs)


def search_artists():
    return artists.keys()


def search_albums_by_artist(artist_name):
    return artists.get(artist_name)


def search_artist_top_songs(artist_name):
    artist_songs = []
    for album in artists.get(artist_name):
        for song in albums.get(album):
            artist_songs.append(song)

    return sorted(artist_songs, key=lambda song: song.popularity, reverse=True)


def search_songs_by_album(album_name):
    album_songs = []
    for song in albums.get(album_name):
        album_songs.append(song.name)
    return album_songs