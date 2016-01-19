from phrase import Phrase
import midi
import re
import random
import os
import lyrics_tools

class Song():
    def __init__(self, beats_per_measure=8, tonic_pitch=40):
        self.phrases = []
        self.tonic_pitch = tonic_pitch
        self.beats_per_measure = beats_per_measure

    def create_phrase(self, lyric, number_of_measures):
        phrase = Phrase(lyric, number_of_measures, self.beats_per_measure)
        return phrase

    def append_phrase(self, phrase):
        self.phrases.append(phrase)

    def to_abc_notation(self):
        return "".join([phrase.to_abc_notation() for phrase in self.phrases])

    def lyrics(self):
        lyrics_array = [" ".join(phrase.words) for phrase in self.phrases]
        return " ".join(lyrics_array)

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
                if note.pitch == "rest":
                    offset += 110*note.rhythm
                else:
                    track.append(midi.NoteOnEvent(tick=offset, velocity=120, pitch=self.tonic_pitch+24+note.pitch))
                    track.append(midi.NoteOffEvent(tick=(110*note.rhythm), pitch=self.tonic_pitch+24+note.pitch))
                    offset = 0

            for bass_note in phrase.bass_notes:
                bass_track.append(midi.NoteOnEvent(tick=0, velocity=120, pitch=self.tonic_pitch+bass_note))
                bass_track.append(midi.NoteOffEvent(tick=220 * self.beats_per_measure, pitch=self.tonic_pitch+bass_note))

        track.append(midi.EndOfTrackEvent(tick=1))
        bass_track.append(midi.EndOfTrackEvent(tick=1))

        pattern.append(track)
        pattern.append(bass_track)

        midi.write_midifile(filename, pattern)

    def tune_notation(self):
        output = "[[inpt TUNE]]\n"
        for phrase in self.phrases:
            for note in phrase.melody:
                output += "~\n"
                if note.pitch == "rest":
                    output += "% {D 250}\n"
                else:
                    output += "\n".join(
                        lyrics_tools.syllable_to_tune_notation(note.syllable, 370, 450)
                    ) + "\n"
        output += "[[inpt TEXT]]"
        return output
