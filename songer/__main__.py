from song import Song

def main():
    song = Song()
    song.append_phrase("I", "this is a")
    song.append_phrase("vi", "ly-ri-cal test")
    song.append_phrase("IV", "lets see it go")
    song.append_phrase("V", "lets try it now")
    song.create_voice_mp3()
    song.write_to_midi()

if __name__ == "__main__":
    main()
