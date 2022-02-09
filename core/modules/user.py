from typing import List

class User:
    def __init__(self, name, password, typy="regular"):
        self.name = name
        self.password = password
        self.type = typy
        self.playlists = {}

    def create_playlist(self, playlist_name, songs=None):
        if playlist_name not in self.playlists.keys():
            self.playlists[playlist_name] = []
        if songs is not None:
            self.add_song(playlist_name, songs)

    def add_song(self, playlist_name, songs: List):
        for song in songs:
            if song not in self.playlists.get(playlist_name):
                self.playlists[playlist_name].append(song)

    def check_playlists_limit(self):
        return False if len(self.playlists.keys()) == 5 else True

    def check_songs_limit(self, playlist_name):
        return False if len(self.playlists.get(playlist_name)) == 20 else True
