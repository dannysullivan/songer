from phrase import Phrase
import midi
import re
import random
import os

from pydub import AudioSegment

class Song():
    def __init__(self, beats_per_measure=8):
        self.phrases = []
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
                    track.append(midi.NoteOnEvent(tick=offset, velocity=120, pitch=64+note.pitch))
                    track.append(midi.NoteOffEvent(tick=(110*note.rhythm), pitch=64+note.pitch))
                    offset = 0

            for bass_note in phrase.bass_notes:
                bass_track.append(midi.NoteOnEvent(tick=0, velocity=120, pitch=40+bass_note))
                bass_track.append(midi.NoteOffEvent(tick=220 * self.beats_per_measure, pitch=40+bass_note))

        track.append(midi.EndOfTrackEvent(tick=1))
        bass_track.append(midi.EndOfTrackEvent(tick=1))

        pattern.append(track)
        pattern.append(bass_track)

        midi.write_midifile(filename, pattern)

    def write_to_audio(self):
        self.write_to_midi("midi_output.mid")
        abc_notation = self.to_abc_notation()
        os.system("perl external/sing/sing.pl -n 0 -t 1.2 -p "+abc_notation+" "+self.lyrics()+" &>voice_notation.txt")
        os.system("say -o vocal_track.aiff -v Victoria -f voice_notation.txt")
        os.system("fluidsynth -g 0.8 -F accompaniment.aiff external/soundfont.SF2 midi_output.mid")

        vocal_track = AudioSegment.from_file('vocal_track.aiff', 'aiff')
        accompaniment = AudioSegment.from_file('accompaniment.aiff', 'aiff')
        full_mix = vocal_track.overlay(accompaniment)
        full_mix.export("full_mix.aiff", format="aiff")

        os.remove('vocal_track.aiff')
        os.remove('accompaniment.aiff')
        os.remove('voice_notation.txt')
        os.remove('midi_output.mid')
