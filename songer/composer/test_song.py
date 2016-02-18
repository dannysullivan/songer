import unittest
from song import Song

class TestSong(unittest.TestCase):
    def test_phrase_setup(self):
        """
        A new song takes as input a series of lyrics split up onto
        multiple lines and constructs a phrase for each unique line
        """
        three_line_song = Song(lyrics="hello\nit is me\nI was wondering")
        self.assertEqual(len(three_line_song.phrases), 3)
        hello_phrase = three_line_song.phrases[0]
        it_is_me_phrase = three_line_song.phrases[1]
        self.assertEqual(len(hello_phrase.words), 1)
        self.assertEqual(len(it_is_me_phrase.words), 3)

        two_line_song = Song(lyrics="where\nare we")
        self.assertEqual(len(two_line_song.phrases), 2)

    def test_phrase_setup_repetition(self):
        """
        Multiple copies of the same line are given the same
        melodic treatment
        """
        song = Song(lyrics="first line\nsecond line\nfirst line")
        self.assertEqual(song.phrases[0], song.phrases[2])

    def test_tune_notation(self):
        song = Song(lyrics="hi")

        notation = song.tune_notation()

        self.assertRegexpMatches(notation, "[[inpt TUNE]]")
        self.assertRegexpMatches(notation, "1AY {D 435; P")
        self.assertRegexpMatches(notation, "hh {D 65; P")
        self.assertRegexpMatches(notation, "[[inpt TEXT]]")

if __name__ == "__main__":
    unittest.main()
