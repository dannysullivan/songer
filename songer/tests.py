import unittest
import lyrics_tools

class TestLyricsMethods(unittest.TestCase):
    def test_word_to_syllables(self):
        self.assertEqual(lyrics_tools.word_to_syllables("hi"), [['HH', 'AY1']])
        self.assertEqual(lyrics_tools.word_to_syllables("strength"), [['S', 'T', 'R', 'EH1', 'NG', 'K', 'TH']])
        self.assertEqual(lyrics_tools.word_to_syllables("syllable"), [['S', 'IH1'], ['L', 'AH0'], ['B', 'AH0', 'L']])

    def test_syllable_to_tune_notation(self):
        self.assertEqual(lyrics_tools.syllable_to_tune_notation(['HH', 'AY1'], 370),
                ["hh {D 65; P 370:0}", "1AY {D 415; P 370:0}"]
        )
        self.assertEqual(lyrics_tools.syllable_to_tune_notation(['S', 'T', 'R', 'EH1', 'NG', 'K', 'TH'], 370),
                [
                    "s {D 65; P 370:0}",
                    "t {D 65; P 370:0}",
                    "r {D 65; P 370:0}",
                    "1EH {D 90; P 370:0}",
                    "ng {D 65; P 370:0}",
                    "k {D 65; P 370:0}",
                    "th {D 65; P 370:0}"
                ]
        )

if __name__ == "__main__":
    unittest.main()
