from phrase import Phrase
import midi

class Song():
    def __init__(self):
        self.phrases = []

    def append_phrase(self, chord, lyric):
        phrase = Phrase(chord, lyric)
        phrase.create_melody()
        self.phrases.append(phrase)

    def write_to_midi(self):
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

            bass_track.append(midi.NoteOnEvent(tick=0, velocity=120, pitch=48+phrase.bass_note))
            bass_track.append(midi.NoteOffEvent(tick=880, pitch=48+phrase.bass_note))

        track.append(midi.EndOfTrackEvent(tick=1))
        bass_track.append(midi.EndOfTrackEvent(tick=1))

        pattern.append(track)
        pattern.append(bass_track)

        midi.write_midifile("example.mid", pattern)
