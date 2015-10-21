from random import randint

class RhythmGenerator():
    beats_per_rhythm = 4

    def create_rhythm(self):
        return [randint(1,4) for beat in range(RhythmGenerator.beats_per_rhythm)]
