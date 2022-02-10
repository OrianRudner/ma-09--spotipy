from typing import List, Dict
from core.modules.album import Album
from core.modules.artist import Artist
from core.modules.song import Song


def parse_songs(tracks: List[Dict]):
    songs = []
    for track in tracks:
        album = parse_album(track["track"]["album"])
        current_artists = parse_artists(track["track"]["artists"])
        songs.append(
            Song(track["track"]["id"], track["track"]["name"], track["track"]["popularity"], album, current_artists))
    return songs


def parse_album(unparsed_album: Dict):
    return Album(unparsed_album["id"], unparsed_album["name"])


def parse_artists(unparsed_artists: List[Dict]):
    artists = []
    for artist in unparsed_artists:
        artists.append(Artist(artist["id"], artist["name"]))
    return artists
