#Alexa Bravo
#Andres Coutiño 
#Daniela Villamar 
#Noviembre 21, 2023

from music import *

#Le asignamos un tempo a la melodia
musica3 = Score("musica3", 90)

#Definimos los instrumentos 
flutePart = Part(FLUTE, 0)
celloPart = Part(CELLO, 1)
bassPart = Part(ACOUSTIC_BASS, 2)

#Definimos una función para crear la melodía
def createMelody():
   #Creamos una "frase" 
    melodyPhrase = Phrase()
    #Definimos las notas musicales
    melodyPitches = [REST, D5, E5, D5, B4, D5, A4, REST, D4, E4, D4]
    #Definimos la duración
    melodyDurations = [QN, EN, EN, EN, QN, EN, EN, QN, EN, EN, WN]
    melodyPhrase.addNoteList(melodyPitches, melodyDurations)
    return melodyPhrase

#Creamos una función para los acordes
def createChords():
   #Creamos una "frase" 
    chordPhrase = Phrase()
    #Definimos las notas musicales
    chordPitches = [
        [D4, F4, A4],
        [E4, G4, B4],
        [D4, F4, A4],
        [B3, D4, G4],
    ]
    #Definimos la duración
    chordDurations = [HN, HN, HN, HN]
    chordPhrase.addNoteList(chordPitches, chordDurations)
    return chordPhrase

#Función para el bajo
def createBass():
   #Creamos una "frase" 
    bassPhrase = Phrase()
    #Definimos las notas musicales
    bassPitches = [D3, G2, A2, B2, D3, G2, A2, D3]
    #Definimos la duración
    bassDurations = [QN, QN, QN, QN, QN, QN, QN, WN]
    bassPhrase.addNoteList(bassPitches, bassDurations)
    return bassPhrase

#Combinamos los instrumentos
flutePart.addPhrase(createMelody())
celloPart.addPhrase(createChords())
bassPart.addPhrase(createBass())

#Creamos una función para repetir la melodia
for i in range(3):  
    flutePart.addPhrase(createMelody())
    celloPart.addPhrase(createChords())
    bassPart.addPhrase(createBass())
musica3.addPart(flutePart)
musica3.addPart(celloPart)
musica3.addPart(bassPart)

#Play a la musica y creamos un archivo midi
Play.midi(musica3)
Write.midi(musica3, "musica3.mid")
