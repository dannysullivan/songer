import unittest
from section import Section
from phrase import Phrase

class TestPhraseMethods(unittest.TestCase):
    def test_constructor(self):
        phrase = Phrase("this is a ly-ric")
        self.assertEqual(phrase.syllables, ["this", "is", "a", "ly", "ric"])

    def test_create_melody(self):
        phrase = Phrase("this is a ly-ric")
        phrase.create_melody()
        melody_beats = [rhythm for (note, rhythm) in phrase.melody]
        self.assertEqual(sum(melody_beats), Phrase.beats_per_phrase)

if __name__ == "__main__":
    unittest.main()
