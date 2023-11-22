#Alexa Bravo
#Andres Coutiño 
#Daniela Villamar 
#Noviembre 21, 2023

from music import *

#Le asignamos un tempo a la melodia
musica2 = Score("musica2", 80.0)

#Definimos los instrumentos 
bassPart = Part(SYNTH_BASS_1, 1)

#Creamos una "frase Lead"
leadPhrase = Phrase(0.0)

#Definimos las notas musicales
leadPitches = [E4, G4, A4, B4, D5, E5, D5, B4]
#Definimos la duración
leadDurations = [QN, EN, SN, EN, SN, QN, EN, SN]

leadPhrase.addNoteList(leadPitches, leadDurations)
Mod.repeat(leadPhrase, 2) 

#Creamos una "frase Bass" 
bassPhrase = Phrase(0.0)

#Definimos las notas musicales
bassPitches = [E2, G2, A2, B2, D3, E3, D3, B2]
#Definimos la duración
bassDurations = [QN, EN, SN, EN, SN, QN, EN, SN]

bassPhrase.addNoteList(bassPitches, bassDurations)
Mod.repeat(bassPhrase, 2)

#Creamos una "frase" de percusión 
percussionPhrase = Phrase(0.0)

#Creamos un patrón de percusión 
percussionPattern = [ACOUSTIC_BASS_DRUM, CLOSED_HI_HAT, ACOUSTIC_SNARE, CLOSED_HI_HAT]
percussionDurations = [QN] * len(percussionPattern)

percussionPhrase.addNoteList(percussionPattern, percussionDurations)

#Repetimos la frase 
Mod.repeat(leadPhrase, 4) 
Mod.repeat(bassPhrase, 4)  
Mod.repeat(percussionPhrase, 4)  

bassPart.addPhrase(bassPhrase)
musica2.addPart(bassPart)


#Play a la musica y creamos un archivo midi
Play.midi(musica2)
Write.midi(musica2, "musica2.mid")
