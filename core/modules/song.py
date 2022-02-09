class Song:
    def __init__(self, id, name, popularity, album, artists):
        self.id = id
        self.name = name
        self.popularity = popularity
        self.album = album
        self.artists = artists

    def get_popularity(self):
        return self.popularity
