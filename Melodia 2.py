#Alexa Bravo
#Andres Coutiño 
#Daniela Villamar 
#Noviembre 21, 2023

from music import *

#Le asignamos un tempo a la melodia
Melodia2 = Score("Melodia Prueba 2", 108.0)  

#Definimos los instrumentos 
flutePart    = Part(FLUTE, 0)        
trumpetPart  = Part(TRUMPET, 1)      
clarinetPart = Part(CLARINET, 2)     
 
#Creamos una "frase" 
themePhrase = Phrase(0.0)            
 
#Definimos las notas musicales
pitches1   = [C4, D4, E4, G4, A4]
#Definimos la duración
durations1 = [QN, EN, SN, EN, SN]

#Definimos las notas musicales
pitches2 = [G5, G5, G5, D5, D5, D5, B4, B4, B4, G4, G4, G4]
#Definimos la duración
durations2 = [ENT, DSN, SN, DEN, DEN, DEN, SN, DSN, SN, DEN, DEN, SN]
 
#Definimos las notas musicales
pitches3 = [D5, F4, E4, D4, C4]
#Definimos la duración
durations3 = [DEN, QN, SN, DEN, HN]
 
#Vamos agregando las listas a la frase, cada una con las notras y la duración) 
themePhrase.addNoteList(pitches1, durations1)
themePhrase.addNoteList(pitches2, durations2)
themePhrase.addNoteList(pitches3, durations3)
 
#Hacemos dos frases nuevas
response1Phrase = themePhrase.copy()
response2Phrase = themePhrase.copy()
 
response1Phrase.setStartTime(4.0)     
response2Phrase.setStartTime(8.0)    
 
#Le damos play en orden aleatoreo
Mod.transpose(themePhrase, 12)         
Mod.transpose(response2Phrase, -12)    
 
#Repetimos la frase dos veces
Mod.repeat(themePhrase, 2)
Mod.repeat(response1Phrase, 2)
Mod.repeat(response2Phrase, 2)
 
#Agregamos las "frases"
flutePart.addPhrase(themePhrase)
trumpetPart.addPhrase(response1Phrase)
clarinetPart.addPhrase(response2Phrase)

Melodia2.addPart(flutePart)
Melodia2.addPart(trumpetPart)
Melodia2.addPart(clarinetPart)
 
#Play a la musica y creamos un archivo midi
Play.midi(Melodia2)
Write.midi(Melodia2, "Melodia2.mid")