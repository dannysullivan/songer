from song import Song
import datetime
import os
import shutil
import requests
from pymarkovchain import MarkovChain

def fetch_lyrics(artist, lines):
    uri = "http://api.lyricsnmusic.com/songs"
    params = {
        'api_key': API_KEY,
        'artist': artist,
    }
    response = requests.get(uri, params=params)
    lyric_list = response.json()

    lyrics = ''
    for lyric_dict in lyric_list:
        lyrics += lyric_dict['snippet'].replace('...', '') + ' '

    # Generate a Markov model
    mc = MarkovChain('./markov')
    mc.generateDatabase(lyrics)

    # Add lines of lyrics
    result = []
    for line in range(0, lines):
        line_string = mc.generateString()
        result.append(line_string)
    return result


def main():
    song = Song()
    lyric = fetch_lyrics('Coheed and Cambria', 1)[0]
    song.add_lyric(lyric, 4)
    song.write_to_midi(str(datetime.datetime.now())+".mid")
    # if not os.path.isdir('mp3s'):
        # os.mkdir('mp3s')
    # song.create_voice_mp3()
    # shutil.rmtree('mp3s')


if __name__ == "__main__":
    main()
