import unittest
from song import Song

class TestSongMethods(unittest.TestCase):
    def test_tune_notation(self):
        song = Song(8)
        lyric = "hi"

        verse = song.create_phrase(lyric, 4)
        song.append_phrase(verse)

        notation = song.tune_notation()

        self.assertRegexpMatches(notation, "[[inpt TUNE]]")
        self.assertRegexpMatches(notation, "1AY {D 435; P 370:0}")
        self.assertRegexpMatches(notation, "hh {D 65; P 370:0}")
        self.assertRegexpMatches(notation, "[[inpt TEXT]]")

if __name__ == "__main__":
    unittest.main()
