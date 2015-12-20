from song import Song
import datetime
from phrase import Phrase
from pydub import AudioSegment
from lyric_translator import LyricTranslator

def main():
    song = Song(8)
    # lyric = " ".join(["oh"] * 8)
    lyric = "is this real or am I real at all"

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

    song.write_to_audio()

if __name__ == "__main__":
    main()
