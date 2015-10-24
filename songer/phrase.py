import random
import re

class Phrase():
    beats_per_phrase = 8
    scale_degrees = [0, 2, 4, 7, 9] # 4 bars of eighth notes
    chord_bass_map = {
        "I": 0,
        "ii": 2,
        "iii": 4,
        "IV": 5,
        "V": 7,
        "vi": 9
    }

    def __init__(self, chord, lyric):
        self.chord = chord
        self.syllables = re.split("\s|\-", lyric)

    @property
    def bass_note(self):
        return Phrase.chord_bass_map[self.chord]

    def create_melody(self):
        self.melody = []
        for syllable in self.syllables:
            rhythm = random.choice([1,2])
            note = random.choice(Phrase.scale_degrees)
            self.melody.append((note, rhythm))
        self._add_rests()

    def _add_rests(self):
        """
        If the melody doesn't fill the phrase, add a rest to its beginning or end
        """
        beats_in_melody = sum([rhythm for (note, rhythm) in self.melody]) 
        if beats_in_melody < Phrase.beats_per_phrase:
            if random.choice([True, False]):
                self.melody.append(('rest', Phrase.beats_per_phrase - beats_in_melody))
            else:
                self.melody.insert(0, ('rest', Phrase.beats_per_phrase - beats_in_melody))
