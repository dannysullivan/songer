import unittest
import lyrics_tools

class TestLyricsMethods(unittest.TestCase):
    def test_word_to_syllables(self):
        self.assertEqual(lyrics_tools.word_to_syllables("syllable"), [['S', 'IH1'], ['L', 'AH0'], ['B', 'AH0', 'L']])

if __name__ == "__main__":
    unittest.main()
