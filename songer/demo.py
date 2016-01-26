from composer.song import Song
import datetime
from voice.voice import Voice
from lyrics_tools import fetch_lyrics

def main():
    lyric = "\n".join(fetch_lyrics('The Beatles', 4))

    song = Song(lyrics=lyric)

    song.write_to_midi("midi_output.mid")
    voice = Voice(song.tune_notation())
    voice.write_to_audio()

if __name__ == "__main__":
    main()
