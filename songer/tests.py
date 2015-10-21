import unittest
from section import Section
from rhythm_generator import RhythmGenerator

class TestChordProgressionMethods(unittest.TestCase):
    def test_get_chords(self):
        section = Section(['IV', 'I', 'V', 'V'])
        self.assertEqual(section.get_chords(), ['IV', 'I', 'V', 'V'])

    def test_create_melody_for_rhythm(self):
        section = Section(['IV', 'I', 'V', 'V'])
        rhythm = RhythmGenerator().create_rhythm()
        section.create_melody_for_rhythm(rhythm)
        melody_durations = [duration for (note, duration) in section.melody]
        self.assertEqual(sum(melody_durations), Section.melody_beats)

    def test_create_snippet_for_rhythm(self):
        section = Section(['IV', 'I', 'V', 'V'])
        rhythm = RhythmGenerator().create_rhythm()
        section.create_snippet_for_rhythm(rhythm)
        self.assertTrue(len(section.melody) > 0)

        melody_durations = [duration for (note, duration) in section.melody]
        self.assertEqual(melody_durations, rhythm)

    def test_get_bass_notes(self):
        section = Section(['IV', 'I', 'V', 'V'])
        self.assertEqual(section.get_bass_notes(), [5, 0, 7, 7])

class TestRhythmGeneratorMethods(unittest.TestCase):
    def test_create_rhythm(self):
        generator = RhythmGenerator()
        self.assertEqual(len(generator.create_rhythm()), RhythmGenerator.beats_per_rhythm)

if __name__ == "__main__":
    unittest.main()
