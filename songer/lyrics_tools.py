import requests
import os
import nltk
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

def word_to_syllables(word):
    """
    Takes as input a word and returns an array where each array index 
    contains a syllable (represented as an array of phonemes in that syllable)
    """
    phonemes = nltk.corpus.cmudict.dict()[word][0]
    syllable_array = []
    current_non_vowels = []
    for phoneme in phonemes:
        phoneme = str(phoneme)
        if phoneme[-1].isdigit():
            syllable_array.append(current_non_vowels + [phoneme])
            current_non_vowels = []
        else:
            current_non_vowels.append(phoneme)
    syllable_array[-1] += current_non_vowels
    return syllable_array
