from typing import List, Dict
from modules.song import Song
from modules.album import Album
from modules.artist import Artist


def parse_songs(unparsed_songs: List[Dict]):
    songs = []
    for song in unparsed_songs:
        album = parse_album(song["track"]["album"])
        artists = parse_artists(song["track"]["artists"])
        songs.append(Song(song["track"]["id"], song["track"]["name"], song["track"]["popularity"], album, artists))
    return songs


def parse_album(unparsed_album: Dict):
    return Album(unparsed_album["id"], unparsed_album["name"])


def parse_artists(unparsed_artists: List[Dict]):
    artists = []
    for artist in unparsed_artists:
        artists.append(Artist(artist["id"], artist["name"]))
    return artists
