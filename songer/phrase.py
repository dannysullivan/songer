import random
import re
from gtts import gTTS
from pydub import AudioSegment
import os

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

    def create_mp3(self):
        syllable_mp3s = []
        for syllable in self.syllables:
            # syllable_mp3 = gTTS(text=syllable, lang='en')
            # syllable_mp3.save('mp3s/' + syllable + '.mp3')
            os.system("say -o mp3s/"+syllable+".aiff -v Victoria "+syllable)
            syllable_mp3s.append(AudioSegment.from_file('mp3s/' + syllable + '.aiff', 'aiff'))

        mp3s_to_join = []
        index = 0
        for (note, rhythm) in self.melody:
            milliseconds = 250 * rhythm
            if note == "rest":
                mp3s_to_join.append(AudioSegment.from_mp3('empty.mp3')[:milliseconds])
            else:
                syllable_mp3 = syllable_mp3s[index]
                syllable_length = syllable_mp3.duration_seconds * 1000 # we want milliseconds
                if syllable_length < milliseconds:
                    mp3s_to_join.append(syllable_mp3)
                    mp3s_to_join.append(AudioSegment.from_mp3('empty.mp3')[:(milliseconds - syllable_length)])
                else:
                    mp3s_to_join.append(syllable_mp3[:milliseconds])
                index += 1

        print [mp3.duration_seconds for mp3 in mp3s_to_join]
        joined_mp3 = mp3s_to_join[0] + mp3s_to_join[1]
        for mp3 in mp3s_to_join[2:]:
            joined_mp3 += mp3
        return joined_mp3

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
