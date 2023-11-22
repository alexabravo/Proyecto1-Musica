from music import *

# Create the necessary musical data
musica2 = Score("musica2", 80.0)  # tempo is 80 bpm

bassPart = Part(SYNTH_BASS_1, 1)  # synth bass part on channel 1

# Synth Lead Phrase
leadPhrase = Phrase(0.0)

leadPitches = [E4, G4, A4, B4, D5, E5, D5, B4]
leadDurations = [QN, EN, SN, EN, SN, QN, EN, SN]

leadPhrase.addNoteList(leadPitches, leadDurations)
Mod.repeat(leadPhrase, 2)  # Repeat the lead phrase

# Synth Bass Phrase
bassPhrase = Phrase(0.0)

bassPitches = [E2, G2, A2, B2, D3, E3, D3, B2]
bassDurations = [QN, EN, SN, EN, SN, QN, EN, SN]

bassPhrase.addNoteList(bassPitches, bassDurations)
Mod.repeat(bassPhrase, 2)  # Repeat the bass phrase

# Percussion Phrase
percussionPhrase = Phrase(0.0)

# A simple percussion pattern
percussionPattern = [ACOUSTIC_BASS_DRUM, CLOSED_HI_HAT, ACOUSTIC_SNARE, CLOSED_HI_HAT]
percussionDurations = [QN] * len(percussionPattern)

percussionPhrase.addNoteList(percussionPattern, percussionDurations)

# Repeat the phrases to create a loop
Mod.repeat(leadPhrase, 4)  # Repeat the lead phrase 4 times
Mod.repeat(bassPhrase, 4)  # Repeat the bass phrase 4 times
Mod.repeat(percussionPhrase, 4)  # Repeat the percussion phrase 4 times

# Add phrases to corresponding parts
bassPart.addPhrase(bassPhrase)

# Add parts to score
musica2.addPart(bassPart)


# Play score
Play.midi(musica2)
Write.midi(musica2, "musica2.mid")
