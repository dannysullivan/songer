from song import Song

def main():
    song = Song()
    song.append_phrase("I", "This is a")
    song.append_phrase("vi", "ly-ri-cal test")
    song.append_phrase("IV", "lets see how it goes")
    song.append_phrase("V", "lets see how it goes")
    song.write_to_midi()

if __name__ == "__main__":
    main()
