class Note():
    def __init__(self, pitch, rhythm, syllable, part_of_word=False):
        self.pitch = pitch
        self.rhythm = rhythm
        self.syllable = syllable
        self.part_of_word = part_of_word

    def __str__(self):
        return str(self.pitch) + ", " + str(self.rhythm) + ", " + str(self.syllable) + ", " + str(self.part_of_word)

    def __eq__(self, other):
        return self.__dict__
