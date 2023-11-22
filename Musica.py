#Alexa Bravo
#Andres Coutiño 
#Daniela Villamar 
#Noviembre 22, 2023

from music import *

#Le asignamos un tempo a la melodia
musica1 = Score("Musica1", 140)

#Definimos los instrumentos 
trumpetPart = Part(ELECTRIC_GRAND, 0)
vibesPart = Part(SYNTH_VOICE, 1)
bassPart = Part(ACOUSTIC_BASS, 2)

#Definimos una función para crear la melodía
def createMelody():
   #Creamos una "frase" 
    melodyPhrase = Phrase()
    #Definimos las notas musicales
    melodyPitches = [REST, E4, G4, A4, B4, D5, REST, C4, D4, E4, G4, A4, A4, G4, E4, D4, E4, REST, G4, A4, B4, D5, REST, C4, D4, E4, G4, A4]
    #Definimos la duración
    melodyDurations = [QN, QN, QN, QN, WN, EN, DQN, QN, QN, DQN, HN + EN, QN, EN, DQN, QN, QN, EN, EN, DQN, QN, QN, WN, EN, DQN, QN, QN, DQN, HN + EN]
    melodyPhrase.addNoteList(melodyPitches, melodyDurations)
    return melodyPhrase

#Creamos las secciones de la melodía, acordes y bajo
melody1 = createMelody()

#Repetimos las secciones en un bucle
for i in range(4): 
    trumpetPart.addPhrase(melody1)


#Combinamos el material musical
musica1.addPart(trumpetPart)
musica1.addPart(vibesPart)
musica1.addPart(bassPart)

#Play a la musica y creamos un archivo midi
Play.midi(musica1)
Write.midi(musica1, "musica1.mid")
