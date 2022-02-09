from extract.extract_songs import extract_songs
from parse.parse import parse_songs


def main():
    songs = extract_songs("C:\\Users\\orian\\Desktop\\songs\\*")
    new_songs = parse_songs(songs)
    for song in new_songs:
        print(str(song))


if __name__ == '__main__':
    main()
