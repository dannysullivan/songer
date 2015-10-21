import unittest
from section import Section

class TestChordProgressionMethods(unittest.TestCase):
    def test_get_chords(self):
        section = Section(['IV', 'I', 'V', 'V'])
        self.assertEqual(section.get_chords(), ['IV', 'I', 'V', 'V'])

    def test_create_melody(self):
        section = Section(['IV', 'I', 'V', 'V'])
        section.create_melody()
        self.assertTrue(len(section.melody) > 0)

    def test_get_bass_notes(self):
        section = Section(['IV', 'I', 'V', 'V'])
        self.assertEqual(section.get_bass_notes(), [5, 0, 7, 7])

if __name__ == "__main__":
    unittest.main()
