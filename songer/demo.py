from composer.song import Song
import datetime
from voice.voice import Voice
from lyrics_tools import fetch_lyrics

def main():
    lyric = "\n".join(fetch_lyrics('The Beatles', 6))
    lyric = lyric.replace(",", "")

    song = Song(lyrics=lyric)

    song.write_to_midi("midi_output.mid")
    voice = Voice(song.tune_notation(), "midi_output.mid")
    voice.write_to_audio(True)

if __name__ == "__main__":
    main()
