from music import *

# Define the data structure
musica1 = Score("Musica1", 140)


trumpetPart = Part(ELECTRIC_GRAND, 0)
vibesPart = Part(SYNTH_VOICE, 1)
bassPart = Part(ACOUSTIC_BASS, 2)

# Define una función para crear la melodía
def createMelody():
    melodyPhrase = Phrase()
    melodyPitches = [REST, E4, G4, A4, B4, D5, REST, C4, D4, E4, G4, A4,
                     A4, G4, E4, D4, E4, REST, G4, A4, B4, D5, REST, C4,
                     D4, E4, G4, A4]
    melodyDurations = [QN, QN, QN, QN, WN, EN, DQN, QN, QN, DQN, HN + EN,
                       QN, EN, DQN, QN, QN, EN, EN, DQN, QN, QN, WN, EN,
                       DQN, QN, QN, DQN, HN + EN]
    melodyPhrase.addNoteList(melodyPitches, melodyDurations)
    return melodyPhrase

# Crea las secciones de la melodía, acordes y bajo
melody1 = createMelody()

# Repite las secciones en un bucle
for i in range(4):  # Puedes ajustar el número de repeticiones según sea necesario
    trumpetPart.addPhrase(melody1)


# Combine musical material
musica1.addPart(trumpetPart)
musica1.addPart(vibesPart)
musica1.addPart(bassPart)

# Play the music
Play.midi(musica1)
Write.midi(musica1, "musica1.mid")
