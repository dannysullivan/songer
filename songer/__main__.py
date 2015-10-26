from song import Song

def main():
    song = Song()
    song.add_lyric("take me out to the cliffs Im not red-dee for all this")
    song.create_voice_mp3()
    song.write_to_midi()

if __name__ == "__main__":
    main()
