# songer

A Python tool for generating songs.

Work in progress, will eventually involve three components:

* A lyrics generator that uses machine learning to produce fully structured pop song lyrics

* A melody/chord progression generator that will take a set of lyrics and compose a song

* A text-to-singing converter that will take lyrics and a set of notes and synthesize singing 


Right now, this code is a working prototype of the melody generator and an almost-working prototype of the text-to-singing converter.  I'm currently working on rewriting and testing this prototype code while simultaneously starting on the lyrics generator as a separate project with a collaborator.

## TODO

- [ ] Write a `__str__` method for Song that represents the whole song's lyrics and melody.

- [ ] Split the "singing" logic (that takes notes and words and outputs an audio file of a singing robot) from the song-generating logic

- [ ] Debug occasionally out-of-sync singing (potentially caused by too many consonant sounds in a row).
