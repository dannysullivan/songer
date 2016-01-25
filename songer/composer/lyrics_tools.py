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

def pitch_to_frequency(pitch):
    """
    Takes a midi note pitch and converts it to a frequency in hz
    """
    return (2 ** ((pitch-69)/12.0)) * 440.0

def syllable_to_tune_notation(syllable, pitch, total_duration):
    """
    Takes a syllable (i.e., an array of phonemes) and returns the TUNE notation for that
    syllable at the given pitch
    """
    number_of_consonants = len(syllable) - 1
    length_of_vowel = total_duration - (number_of_consonants*65)
    tune_notation = []
    frequency = pitch_to_frequency(pitch)
    for phoneme in syllable:
        if phoneme[-1].isdigit():
            tune_notation.append(str(phoneme[-1])+phoneme[:-1] + " {D "+str(length_of_vowel)+"; P "+str(frequency)+":0}")
        else:
            tune_notation.append(phoneme.lower() + " {D 65; P "+str(frequency)+":0}")
    return tune_notation
