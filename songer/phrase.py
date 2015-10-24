import random
import re

class Phrase():
    beats_per_phrase = 8
    scale_degrees = [0, 2, 4, 7, 9, 12] # 4 bars of eighth notes
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
            self.melody.append(self._note_for_syllable(syllable))
        self._add_rests()

    def _note_for_syllable(self, syllable):
        """
        Go for stepwise motion or no motion most of the time
        """
        rhythm = random.choice([1,2])

        if len(self.melody) > 0:
            previous_note = self.melody[-1]
            motion = random.choice(["stepwise", "none", "random"])
            if motion == "stepwise":
                note_position = Phrase.scale_degrees.index(previous_note[0])
                neighbors = []
                if note_position != 0:
                    neighbors.append(Phrase.scale_degrees[note_position - 1])
                if note_position != (len(Phrase.scale_degrees)-1):
                    neighbors.append(Phrase.scale_degrees[note_position + 1])
                note = random.choice(neighbors)
            elif motion == "none":
                note = previous_note[0]
            else:
                note = random.choice(Phrase.scale_degrees)
        else:
            note = random.choice(Phrase.scale_degrees)

        return (note, rhythm)

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
