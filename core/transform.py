from typing import List
from core.modules.song import Song


def get_artists(songs: List[Song]):
    artists = {}
    for song in songs:
        current_artists = song.artists
        for artist in current_artists:
            if artist.name not in artists.keys():
                artists[artist.name] = set()
            artists[artist.name].add(song.album.name)
    return artists


def get_albums(songs: List[Song]):
    albums = {}
    for song in songs:
        if song.album.name not in albums.keys():
            albums[song.album.name] = set()
        albums[song.album.name].add(song)

    return albums
