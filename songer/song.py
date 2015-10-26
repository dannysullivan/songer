from phrase import Phrase
import midi
import re
import random
from gtts import gTTS

class Song():
    def __init__(self):
        self.phrases = []
        chords = Phrase.chord_bass_map.keys()
        self.chord_progression = [random.choice(chords) for i in range(4)]

    def add_lyric(self, lyric):
        syllables = re.split("\s|\-", lyric)
        print syllables
        parts_of_lyric = []
        previous_split_index = 0
        # for now, split lyric into roughly equal quarters
        for index in range(1,5):
            split_index = index * (len(syllables)/4) + 1
            parts_of_lyric.append(syllables[previous_split_index:split_index])
            previous_split_index = split_index

        [self._append_phrase(part_of_lyric) for part_of_lyric in parts_of_lyric]

    def _append_phrase(self, lyric, melody_to_copy=None):
        chords_so_far = len(self.phrases)
        next_chord = self.chord_progression[chords_so_far % len(self.chord_progression)]

        phrase = Phrase(lyric, next_chord)
        if melody_to_copy:
            phrase.melody = melody_to_copy
        else:
            phrase.create_melody()
        self.phrases.append(phrase)

    def create_voice_mp3(self):
        phrase_mp3s = [phrase.create_mp3() for phrase in self.phrases]

        joined_mp3 = phrase_mp3s[0] + phrase_mp3s[1]
        for phrase_mp3 in phrase_mp3s[2:]:
            joined_mp3 += phrase_mp3
        joined_mp3.export('full.mp3', format='mp3')

    def write_to_midi(self, filename):
        """
        Resolution is 220 ticks per quarter note
        """
        pattern = midi.Pattern()
        track = midi.Track([], False)
        bass_track = midi.Track([], False)

        offset = 0
        for phrase in self.phrases:
            print phrase.melody
            for (scale_degree, duration) in phrase.melody:
                if scale_degree == "rest":
                    offset += 110*duration
                else:
                    track.append(midi.NoteOnEvent(tick=offset, velocity=120, pitch=60+scale_degree))
                    track.append(midi.NoteOffEvent(tick=(110*duration), pitch=60+scale_degree))
                    offset = 0

            bass_track.append(midi.NoteOnEvent(tick=0, velocity=120, pitch=36+phrase.bass_note))
            bass_track.append(midi.NoteOffEvent(tick=1760, pitch=36+phrase.bass_note))

        track.append(midi.EndOfTrackEvent(tick=1))
        bass_track.append(midi.EndOfTrackEvent(tick=1))

        pattern.append(track)
        pattern.append(bass_track)

        midi.write_midifile(filename, pattern)
