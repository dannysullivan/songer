import random
import midi

class Section():

    melody_beats = 16 # 2 bars of eighth notes
    scale_degrees = [0, 2, 4, 7, 9] # 4 bars of eighth notes
    chord_bass_map = {
        "I": 0,
        "ii": 2,
        "iii": 4,
        "IV": 5,
        "V": 7,
        "vi": 9
    }

    def __init__(self, chords):
        self.chords = chords
        self.melody = []

    def get_chords(self):
        return self.chords

    def get_bass_notes(self):
        bass_notes = []
        for chord in self.get_chords():
            bass_notes.append(Section.chord_bass_map.get(chord))
        return bass_notes

    def create_melody_for_rhythm(self, rhythm):
        rhythm_beats = sum(rhythm)
        repetitions = Section.melody_beats / rhythm_beats
        leftover_beats = Section.melody_beats % rhythm_beats
        for repetition in range(repetitions):
            self.create_snippet_for_rhythm(rhythm)
        self.melody.append(('rest', leftover_beats))

    def duplicate_melody(self):
        melody = self.melody
        self.melody += melody

    def create_snippet_for_rhythm(self, rhythm):
        """
        Melodies are lists of tuples (note, duration)
        """
        for beat in rhythm:
            if random.choice([True, True, True, False]):
                random_note = random.choice(Section.scale_degrees)
                self.melody.append((random_note, beat))
            else:
                self.melody.append(('rest', beat))

    def write_to_midi(self):
        pattern = midi.Pattern()
        track = midi.Track()
        pattern.append(track)
        offset = 0
        for (scale_degree, duration) in self.melody:
            if scale_degree == "rest":
                offset += 240*duration
            else:
                track.append(midi.NoteOnEvent(tick=offset, velocity=120, pitch=60+scale_degree))
                track.append(midi.NoteOffEvent(tick=(240*duration), pitch=60+scale_degree))
                offset = 0

        track.append(midi.EndOfTrackEvent(tick=1))

        bass_track = midi.Track()
        pattern.append(bass_track)
        for scale_degree in self.get_bass_notes():
            bass_track.append(midi.NoteOnEvent(tick=0, velocity=120, pitch=48+scale_degree))
            bass_track.append(midi.NoteOffEvent(tick=1920, pitch=48+scale_degree))
        bass_track.append(midi.EndOfTrackEvent(tick=1))
        print(pattern)

        midi.write_midifile("example.mid", pattern)

    def __str__(self):
        output = ""
        for scale_degree in self.melody:
            output += str(scale_degree) + " "
        output += "\n"
        for chord in self.get_chords():
            output += chord + " - - - - - - - "
        return output
