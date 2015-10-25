from song import Song

def main():
    song = Song()
    song.append_phrase("I", "this is just")
    song.append_phrase("vi", "a test")
    song.append_phrase("IV", "I want to know")
    song.append_phrase("ii", "how it sounds")
    song.append_phrase("I", "we are just")
    song.append_phrase("vi", "the best")
    song.append_phrase("IV", "I want to go")
    song.append_phrase("V", "all a-round")
    song.create_voice_mp3()
    song.write_to_midi()

if __name__ == "__main__":
    main()
