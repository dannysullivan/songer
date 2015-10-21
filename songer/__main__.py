from section import Section

def main():
    section = Section(["IV", "I", "V", "V"])
    section.create_melody()
    section.write_to_midi()

if __name__ == "__main__":
    main()
