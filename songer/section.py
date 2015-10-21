import random
import midi

class Section():

    beats = 32 # 4 bars of eighth notes
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

    def get_chords(self):
        return self.chords

    def get_bass_notes(self):
        bass_notes = []
        for chord in self.get_chords():
            bass_notes.append(Section.chord_bass_map.get(chord))
        return bass_notes

    def create_melody(self):
        self.melody = []
        for beat in range(Section.beats):
            random_note = random.choice(Section.scale_degrees)
            self.melody.append(random.choice([random_note, 'rest']))

    def write_to_midi(self):
        pattern = midi.Pattern()
        track = midi.Track()
        pattern.append(track)
        offset = 0
        for scale_degree in self.melody:
            if scale_degree == "rest":
                offset += 240
            else:
                track.append(midi.NoteOnEvent(tick=offset, velocity=120, pitch=60+scale_degree))
                track.append(midi.NoteOffEvent(tick=240, pitch=60+scale_degree))
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
