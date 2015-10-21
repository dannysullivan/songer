from section import Section
from rhythm_generator import RhythmGenerator

def main():
    section = Section(["IV", "I", "V", "V"])
    rhythm = RhythmGenerator().create_rhythm()
    section.create_melody_for_rhythm(rhythm)
    print sum([duration for (note, duration) in section.melody])
    section.duplicate_melody()
    section.write_to_midi()

if __name__ == "__main__":
    main()
