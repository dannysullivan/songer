import random
import re
from pydub import AudioSegment
from note import Note
import os
from hyphen import Hyphenator

class Phrase():
    scale_degrees = [0, 2, 4, 7, 9, 12]
    chord_bass_map = {
        "I": 0,
        "ii": 2,
        "iii": 4,
        "IV": 5,
        "V": 7,
        "vi": 9
    }
    degrees_to_notes_map = {
        0: 'C',
        2: 'D',
        4: 'E',
        5: 'F',
        7: 'G',
        9: 'A',
        11: 'B',
        12: 'c',
        'rest': 'x'
    }

    def __init__(self, lyric, number_of_measures, beats_per_measure):
        self.words = re.split("\s|\-", lyric.lower())
        self.number_of_measures = number_of_measures

        chords = Phrase.chord_bass_map.keys()
        self.chord_progression = [random.choice(chords) for i in range(self.number_of_measures/2)]
        self.beats_per_measure = beats_per_measure

        self.create_melody()

    @property
    def bass_notes(self):
        return [Phrase.chord_bass_map[chord] for chord in self.chord_progression]

    def total_beats(self):
        return self.number_of_measures * self.beats_per_measure

    def create_melody(self):
        # hyphenator = Hyphenator('en_US')
        self.melody = []
        for word in self.words:
            syllables = [word]
            # syllables = hyphenator.syllables(unicode(word))
            if len(syllables) > 1:
                for syllable in syllables:
                    self.melody.append(self._note_for_syllable(syllable, True))
            else:
                self.melody.append(self._note_for_syllable(word, False))
        self._add_rests()

    def to_abc_notation(self):
        notation = ""
        for note in self.melody:
            notation += Phrase.degrees_to_notes_map[note.pitch]
            notation += str(note.rhythm)
        return notation

    def _note_for_syllable(self, syllable, part_of_word):
        """
        Go for stepwise motion or no motion most of the time
        """
        rhythm = random.choice([2])

        if len(self.melody) > 0:
            previous_note = self.melody[-1]
            # motion = random.choice(["stepwise", "none", "random"])
            motion = random.choice(["stepwise", "none"])
            if motion == "stepwise":
                note_position = Phrase.scale_degrees.index(previous_note.pitch)
                neighbors = []
                if note_position != 0:
                    neighbors.append(Phrase.scale_degrees[note_position - 1])
                if note_position != (len(Phrase.scale_degrees)-1):
                    neighbors.append(Phrase.scale_degrees[note_position + 1])
                pitch = random.choice(neighbors)
            elif motion == "none":
                pitch = previous_note.pitch
            else:
                pitch = random.choice(Phrase.scale_degrees)
        else:
            pitch = random.choice(Phrase.scale_degrees)

        return Note(pitch, rhythm, syllable, part_of_word)

    def _add_rests(self):
        """
        If the melody doesn't fill the phrase, add rests randomly
        """
        beats_in_melody = sum([note.rhythm for note in self.melody])
        while beats_in_melody < self.total_beats():
            indices_between_words = [index for (index, note) in enumerate(self.melody) if not note.part_of_word]
            random_note_position = random.choice(indices_between_words)
            self.melody.insert(random_note_position, Note('rest', 1, ''))
            beats_in_melody += 1
