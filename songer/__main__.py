from song import Song
import datetime
import os
from pydub import AudioSegment
import requests
from pymarkovchain import MarkovChain

def fetch_lyrics(artist, lines):
    API_KEY = os.environ.get('API_KEY')

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
    lyric = " ".join(fetch_lyrics('System of a Down', 3))
    # lyric = " ".join(["one"] * 20)
    song.add_lyric(lyric, 8)
    song.write_to_midi("midi_output.mid")
    abc_notation = song.to_abc_notation()
    os.system("perl external/sing/sing.pl -n-4 -t 1.25 -p "+abc_notation+" "+lyric+" &>voice_notation.txt")
    os.system("say -o vocal_track.aiff -v Victoria -f voice_notation.txt")
    os.system("fluidsynth -g 0.7 -F accompaniment.aiff external/soundfont.SF2 midi_output.mid")

    vocal_track = AudioSegment.from_file('vocal_track.aiff', 'aiff')
    accompaniment = AudioSegment.from_file('accompaniment.aiff', 'aiff')
    full_mix = vocal_track.overlay(accompaniment)
    full_mix.export("full_mix.aiff", format="aiff")

    os.remove('vocal_track.aiff')
    os.remove('accompaniment.aiff')
    os.remove('voice_notation.txt')
    os.remove('midi_output.mid')

if __name__ == "__main__":
    main()
