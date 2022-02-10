import glob
import json


def extract_songs(directory_path):
    files = glob.glob(directory_path)
    songs = []
    for file in files:
        with open(file, 'r') as current_file:
            temp_song = json.loads(current_file.read())
            songs.append(temp_song)
    return songs
