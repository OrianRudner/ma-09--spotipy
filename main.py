from core.modules.user import User
from core.search.search import *


def main():
    user1 = User("1", "1")
    user1.create_playlist("11")
    # print(user1.playlists)
    #print(search_artists())
    songsss = search_artist_top_songs("Arctic Monkeys")
    for song in songsss:
        print(str(song))

    print(search_songs_by_album("AM"))

   

if __name__ == '__main__':
    main()
