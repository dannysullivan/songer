from song import Song
import datetime
import os
from phrase import Phrase
from pydub import AudioSegment
from lyric_translator import LyricTranslator

def main():
    song = Song(8)
    lyric = " ".join(["oh"] * 8)
    # lyric = "is this real or am I real at all"

    verse = song.create_phrase(lyric, 4)
    song.append_phrase(verse)
    song.append_phrase(verse)

    chorus = song.create_phrase(lyric, 4)
    song.append_phrase(chorus)
    song.append_phrase(chorus)

    song.append_phrase(verse)
    song.append_phrase(verse)

    song.append_phrase(chorus)
    song.append_phrase(chorus)

    bridge = song.create_phrase(lyric, 4)
    song.append_phrase(bridge)
    song.append_phrase(bridge)

    song.append_phrase(verse)
    song.append_phrase(verse)

    song.write_to_midi("midi_output.mid")
    abc_notation = song.to_abc_notation()
    os.system("perl external/sing/sing.pl -n 0 -t 1.2 -p "+abc_notation+" "+song.lyrics()+" &>voice_notation.txt")
    os.system("say -o vocal_track_"+str(index)+".aiff -v Victoria -f voice_notation.txt")
    os.system("fluidsynth -g 0.8 -F accompaniment.aiff external/soundfont.SF2 midi_output.mid")

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
