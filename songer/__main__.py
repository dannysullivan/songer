from song import Song

def main():
    song = Song()
    song.append_phrase("I", "take me out")
    song.append_phrase("vi", "to the cliffs")
    song.append_phrase("IV", "Im not red-dee")
    song.append_phrase("ii", "for this")
    song.append_phrase("I", "look me straight", song.phrases[0].melody)
    song.append_phrase("vi", "in the eye", song.phrases[1].melody)
    song.append_phrase("IV", "let me teach you", song.phrases[2].melody)
    song.append_phrase("V", "to fly", song.phrases[3].melody)
    song.create_voice_mp3()
    song.write_to_midi()

if __name__ == "__main__":
    main()
