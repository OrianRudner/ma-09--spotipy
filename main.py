from core.modules.user import User
from core.search.search import *
from core.modules.regular_user import RegularUser
from core.authentication import *


def main():
    x = sigh_up("user4", "pass4", "C:\\Users\\orian\\Desktop\\curseProject\\spotipy\\ma-09--spotipy\\core\\user.json")
    #print(x.name + " " + x.password)


if __name__ == '__main__':
    main()
