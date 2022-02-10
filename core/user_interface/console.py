from consolemenu import *
from consolemenu.items import *
from core.search.search import *


def run_menu(user):
    main_menu = ConsoleMenu(title="spotipy")

    search_menu = ConsoleMenu(title="search")

    search_menu_item = SubmenuItem("Search options", search_menu, menu=main_menu)
    add_playlist_item = FunctionItem("Add playlist", user.create_playlist)

    main_menu.append_item(search_menu_item)
    main_menu.append_item(add_playlist_item)

    search_artists_item = FunctionItem("Search artists", search_artists)
    search_artist_top_songs_item = FunctionItem("search_artist_top_songs", search_artist_top_songs, [user])
    search_songs_by_album_item = FunctionItem("search_songs_by_album", search_songs_by_album)
    search_albums_by_artist_item = FunctionItem("search_albums_by_artist", search_albums_by_artist)

    search_menu.append_item(search_artists_item)
    search_menu.append_item(search_albums_by_artist_item)
    search_menu.append_item(search_songs_by_album_item)
    search_menu.append_item(search_artist_top_songs_item)

    main_menu.show()
