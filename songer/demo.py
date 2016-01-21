from song import Song
import datetime
from phrase import Phrase
from pydub import AudioSegment
from voice.voice import Voice

def main():
    lyric = ("is this real or am I real at all\n"
            "is this real or am I real at all\n"
            "la la la la la la la\n"
            "la la la la la la la la")
    song = Song(lyrics=lyric)

    song.write_to_midi("midi_output123.mid")
    voice = Voice(song.tune_notation())
    voice.write_to_audio()

if __name__ == "__main__":
    main()
