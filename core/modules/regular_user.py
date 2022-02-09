from typing import List
from core.const import RegularUserLimit, UserType
from core.modules.user import User


class RegularUser(User):

    def __init__(self, name, password):
        super().__init__(name, password, typy=UserType.REGULAR)

    @staticmethod
    def create_playlist(self, playlist_name, songs=None):
        if RegularUser.check_playlists_limit(self):
            super().create_playlist(self, playlist_name, songs)

    @staticmethod
    def add_song(self, playlist_name, songs: List):
        for song in songs:
            if RegularUser.check_songs_limit(self, playlist_name):
                super().add_song(self, playlist_name, [song])

    def check_playlists_limit(self):
        return False if len(self.playlists.keys()) == RegularUserLimit.PLAYLIST_LIMIT else True

    def check_songs_limit(self, playlist_name):
        return False if len(self.playlists.get(playlist_name)) == RegularUserLimit.SONG_LIMIT else True
