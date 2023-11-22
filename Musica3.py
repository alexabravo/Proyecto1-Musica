from music import *

# Define the data structure
musica3 = Score("musica3", 90)

flutePart = Part(FLUTE, 0)
celloPart = Part(CELLO, 1)
bassPart = Part(ACOUSTIC_BASS, 2)

def createMelody():
    melodyPhrase = Phrase()
    melodyPitches = [REST, D5, E5, D5, B4, D5, A4, REST, D4, E4, D4]
    melodyDurations = [QN, EN, EN, EN, QN, EN, EN, QN, EN, EN, WN]
    melodyPhrase.addNoteList(melodyPitches, melodyDurations)
    return melodyPhrase

def createChords():
    chordPhrase = Phrase()
    chordPitches = [
        [D4, F4, A4],
        [E4, G4, B4],
        [D4, F4, A4],
        [B3, D4, G4],
    ]
    chordDurations = [HN, HN, HN, HN]
    chordPhrase.addNoteList(chordPitches, chordDurations)
    return chordPhrase

def createBass():
    bassPhrase = Phrase()
    bassPitches = [D3, G2, A2, B2, D3, G2, A2, D3]
    bassDurations = [QN, QN, QN, QN, QN, QN, QN, WN]
    bassPhrase.addNoteList(bassPitches, bassDurations)
    return bassPhrase

# Combine musical material
flutePart.addPhrase(createMelody())
celloPart.addPhrase(createChords())
bassPart.addPhrase(createBass())

# Repite las secciones manualmente para hacerlo más largo
for i in range(3):  # Repetir el bucle 7 veces (ajusta según sea necesario)
    flutePart.addPhrase(createMelody())
    celloPart.addPhrase(createChords())
    bassPart.addPhrase(createBass())
musica3.addPart(flutePart)
musica3.addPart(celloPart)
musica3.addPart(bassPart)

# Play the music
Play.midi(musica3)
Write.midi(musica3, "musica3.mid")
