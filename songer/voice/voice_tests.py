import unittest
from voice import Voice

class TestVoiceMethods(unittest.TestCase):
    def test_tune_notation(self):
        notation = "[[inpt TUNE]]\n[[input TEXT]]"
        voice = Voice(notation)

        self.assertEquals(voice.tune_notation, "[[inpt TUNE]]\n[[input TEXT]]")

if __name__ == "__main__":
    unittest.main()
