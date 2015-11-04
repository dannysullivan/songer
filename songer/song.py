from phrase import Phrase
import midi
import re
import random

class Song():
    def __init__(self):
        self.phrases = []

    def add_lyric(self, lyric, number_of_measures):
        syllables = re.split("\s|\-", lyric)

        phrase = Phrase(syllables, number_of_measures)
        phrase.create_melody()
        self.phrases.append(phrase)

    def to_abc_notation(self):
        return "".join([phrase.to_abc_notation() for phrase in self.phrases])

    def write_to_midi(self, filename):
        """
        Resolution is 220 ticks per quarter note
        """
        pattern = midi.Pattern()
        track = midi.Track([], False)
        bass_track = midi.Track([], False)

        offset = 0
        for phrase in self.phrases:
            for note in phrase.melody:
                print note
                if note.pitch == "rest":
                    offset += 110*note.rhythm
                else:
                    track.append(midi.NoteOnEvent(tick=offset, velocity=120, pitch=60+note.pitch))
                    track.append(midi.NoteOffEvent(tick=(110*note.rhythm), pitch=60+note.pitch))
                    offset = 0

            for bass_note in phrase.bass_notes:
                bass_track.append(midi.NoteOnEvent(tick=0, velocity=120, pitch=36+bass_note))
                bass_track.append(midi.NoteOffEvent(tick=1760, pitch=36+bass_note))

        track.append(midi.EndOfTrackEvent(tick=1))
        bass_track.append(midi.EndOfTrackEvent(tick=1))

        pattern.append(track)
        pattern.append(bass_track)

        midi.write_midifile(filename, pattern)
