import unittest
from voice import Voice

class TestVoice(unittest.TestCase):
    def test_tune_notation(self):
        notation = "[[inpt TUNE]]\n[[input TEXT]]"
        voice = Voice(notation, "test_midi_file.mid")

        self.assertEquals(voice.tune_notation, "[[inpt TUNE]]\n[[input TEXT]]")

    def test_midi_filename(self):
        notation = "[[inpt TUNE]]\n[[input TEXT]]"
        voice = Voice(notation, "test_midi_file.mid")

        self.assertEquals(voice.midi_filename, "test_midi_file.mid")

if __name__ == "__main__":
    unittest.main()
