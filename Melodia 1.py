#Alexa Bravo
#Andres Coutiño 
#Daniela Villamar 
#Noviembre 21, 2023

from music import *
 
#Le asignamos un tempo a la melodia
PruebaMelodia = Score("Melodia de Prueba", 140) 

#Definimos los instrumentos  
trumpetPart = Part(TRUMPET, 3)       
vibesPart  = Part(VIBES, 5)          
bassPart    = Part(ACOUSTIC_BASS, 2) 

#Creamos una "frase" para cada instrumento
melodyPhrase = Phrase()   
chordPhrase  = Phrase()   
bassPhrase   = Phrase()    

#Definimos las notas musicales
melodyPitch2 = [REST, F4, G4, A4, C5, REST, D4, C5, B4, A4]
#Definimos la duración
melodyDur2   = [QN,   QN, QN, QN, WN, EN,   DQN,QN, QN, WN+HN]

#Definimos las notas musicales
thirdMelodyPitches = [REST, C5, D5, E5, G5, REST, F5, G5, A5, C6, D6]
#Definimos la duración
thirdMelodyDurations = [QN,   QN, QN, QN, WN, EN,   DQN,QN, QN,  DQN, HN+EN]

#Combinamos las melodias
combinedMelodyPitches = melodyPitch2 + thirdMelodyPitches
combinedMelodyDurations =  melodyDur2 + thirdMelodyDurations

melodyPhrase.addNoteList(melodyPitch2, melodyDur2)
melodyPhrase.addNoteList(thirdMelodyPitches, thirdMelodyDurations)
melodyPhrase.addNoteList(combinedMelodyPitches, combinedMelodyDurations)
 
#Creamos el coro
chordPitches1   = [REST, [E3, G3, A3, C4], [E3, G3, A3, C4], REST, 
                    [FS3, A3, C4, D4]]
chordDurations1 = [WN,    HN,               QN,              QN,    
                    QN]           
chordPitches2   = [REST, [D3, FS3, G3, B3], [D3, FS3, G3, B3, D4]]
chordDurations2 = [DHN,  HN,                QN]               
chordPitches3   = [REST, [C3, E3, G3, B3], REST, [E3, FS3, A3, C4, D4], 
                    [E3, FS3, A3, C4, D4]]
chordDurations3 = [QN,   QN,               DHN,  HN,                
                    QN]
chordPitches4   = [REST, [DS3, FS3, A3, B3], REST, [E3, G3, B3, D4], 
                   [DS3, FS3, A3, B3, D4]]
chordDurations4 = [QN,   QN,                DHN,  HN,           
                   QN]
chordPitches5   = [REST, [E3, G3, B3, D4], REST]
chordDurations5 = [QN,   HN,           HN]

#Juntamos el coro
chordPhrase.addNoteList(chordPitches1, chordDurations1) 
chordPhrase.addNoteList(chordPitches2, chordDurations2)
chordPhrase.addNoteList(chordPitches3, chordDurations3)
chordPhrase.addNoteList(chordPitches4, chordDurations4)
chordPhrase.addNoteList(chordPitches5, chordDurations5)
 
#Creamos el bass
bassPitches1   = [REST, A2, REST, A2, E2, D2, REST, D2, A2, G2, REST, 
                   G2, D2, C2] 
bassDurations1 = [WN,   QN, EN,   EN, HN, QN, EN,   EN, HN, QN, EN,   
                   EN, HN, QN] 
bassDurations2 = [EN,   EN, HN, QN,  EN,   EN,  HN, QN, EN,   EN, HN,  
                   QN]
bassPitches2   = [REST, C2, G2, FS2, REST, FS2, C2, B1, REST, B1, FS2, 
                   E2] 
bassPitches3   = [REST, E2, E2, B1, E2, REST]
bassDurations3 = [EN,   EN, QN, QN, HN, HN]

#Juntamos el bass
bassPhrase.addNoteList(bassPitches1, bassDurations1)  
bassPhrase.addNoteList(bassPitches2, bassDurations2)
bassPhrase.addNoteList(bassPitches3, bassDurations3)

#Combinamos todo
trumpetPart.addPhrase(melodyPhrase)
vibesPart.addPhrase(chordPhrase)
bassPart.addPhrase(bassPhrase)
 
PruebaMelodia.addPart(trumpetPart) 
PruebaMelodia.addPart(vibesPart)
PruebaMelodia.addPart(bassPart)
 
#Play a la musica y creamos un archivo midi
Play.midi(PruebaMelodia) 
Write.midi(PruebaMelodia, "Melodia1.mid")