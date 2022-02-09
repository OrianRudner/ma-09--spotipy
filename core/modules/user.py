from typing import List
from abc import ABC
from core.const import UserType


class User(ABC):
    def __init__(self, name, password, typy=UserType.PREMIUM):
        self.name = name
        self.password = password
        self.type = typy
        self.playlists = {}

    @staticmethod
    def create_playlist(self, playlist_name, songs=None):
        if playlist_name not in self.playlists.keys():
            self.playlists[playlist_name] = []
        if songs is not None:
            self.add_song(playlist_name, songs)

    @staticmethod
    def add_song(self, playlist_name, songs: List):
        for song in songs:
            if song not in self.playlists.get(playlist_name):
                self.playlists[playlist_name].append(song)

