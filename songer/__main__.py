from song import Song
import datetime
import os
import shutil

def main():
    song = Song()
    song.add_lyric("take me out to the cliffs Im not red-dee for all this")
    song.write_to_midi(str(datetime.datetime.now())+".mid")
    # if not os.path.isdir('mp3s'):
        # os.mkdir('mp3s')
    # song.create_voice_mp3()
    # shutil.rmtree('mp3s')


if __name__ == "__main__":
    main()
