from core.modules.user import User
from core.search.search import *
from core.modules.regular_user import RegularUser


def main():
    user1 = User("1", "1")
    user2 = RegularUser("a", "a")
    user2.create_playlist(user2, "a")
    user2.add_song(user2, "a", ["sa", "ds", "afaf", "dsfsg"])
    print(user1.type)
    print(user2.type)

    print(search_songs_by_album("AM"))



if __name__ == '__main__':
    main()
