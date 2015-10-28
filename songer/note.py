class Note():
    def __init__(self, pitch, rhythm, syllable):
        self.pitch = pitch
        self.rhythm = rhythm
        self.syllable = syllable

    def __str__(self):
        return str(self.pitch) + ", " + str(self.rhythm) + ", " + str(self.syllable)
