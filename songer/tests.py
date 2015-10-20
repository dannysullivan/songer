import unittest
from chord_progression import ChordProgression

class TestChordProgressionMethods(unittest.TestCase):
    def test_chords(self):
        chord_progression = ChordProgression(['IV', 'I', 'V', 'V'])
        self.assertEqual(chord_progression.get_chords(), ['IV', 'I', 'V', 'V'])

if __name__ == "__main__":
    unittest.main()
