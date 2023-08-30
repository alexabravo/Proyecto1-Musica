#Alexa Bravo 18831
#Andres Coutiño 
#Daniela Villamar 
#Agosto 30, 2023
#Transcripción de "Super Mario Bros: Theme Song" de Kōji Kondō.

#Importamos la libreria para musica.
from music import *

pianoPart = Part(PIANO, 0) # create piano part

#Transcripción de las notas (Do, Re, Mi, Fa, Sol, La, Si) y la duración de cada una de ellas.
pitches1   = [E5, E5, REST, E5, REST, C5, E5, G5, REST, G4, REST, C5, G4, REST, E4, E4, A4, B4, AS4, A4, G4, E5, G5, B5, F5, G5]
durations1 = [EN, EN, EN, EN, EN, EN, QN, QN, QN, QN, QN, DQN, EN, QN, QN, EN, QN, QN, EN, QN, QN, EN, EN, QN, EN, EN]

pitches2   = [REST, E5, C5, D5, B4, C5, G4, REST, E4, E4, A4, B4, AS4, A4, G4, E5, G5, B5, F5, G5, REST, E5, C5, D5, B4]
durations2 = [EN, QN, EN, EN, DQN, DQN, EN, QN, QN, EN, QN, QN, EN, QN, QN, EN, EN, QN, EN, EN, EN, QN, EN, EN, DQN]

pitches3   = [REST, G5, FS5, FS5, DS5, E5, REST, G4, A4, C5, REST, A4, C5, D5, REST, G5, FS5, FS5, DS5, E5, REST, C6, C6, C6]
durations3 = [QN, EN, EN, EN, QN, EN, EN, EN, EN, EN, EN, EN, EN, EN, QN, EN, EN, EN, QN, EN, EN, QN, EN, HN]

pitches4   = [REST, G5, FS5, FS5, DS5, E5, REST, G4, A4, C5, REST, A4, C5, D5, REST, DS5, REST, D5, C5, REST, C5, C5, C5, REST, C5, D5]
durations4 = [QN, EN, EN, EN, QN, EN, EN, EN, EN, EN, EN, EN, EN, EN, QN, QN, EN, DQN, HN, HN, EN, QN, EN, EN, EN, QN]

pitches5   = [E5, C5, A4, G4, C5, C5, C5, REST, C5, D5, E5, D5, C5, C5, C5, REST, C5, D5, E5, C5, A4, G4]
durations5 = [EN, QN, EN, HN, EN, QN, EN, EN, EN, EN, EN, WN, EN, QN, EN, EN, EN, QN, EN, QN, EN, HN]

pitches6   = [E5, C5, G4, REST, GS4, A4, F5, F5, A4, G4, A5, A5, A5, G5, F5, E5, C5, A4, G4, E5, C5, G4, REST, GS4]
durations6 = [EN, QN, EN, QN, QN, EN, QN, EN, HN, QN, EN, EN, EN, EN, QN, EN, QN, EN, HN, EN, QN, EN, QN, QN]

pitches7   = [A4, F5, F5, A4, B4, F5, F5, F5, E5, D5, C5, REST, C5, C5, C5, REST, C5, D5, E5, C5, A4, G4]
durations7 = [EN, QN, EN, HN, EN, QN, EN, QN, EN, EN, HN, HN, EN, QN, EN, EN, EN, QN, EN, QN, EN, HN]

pitches8   = [C5, C5, C5, REST, C5, D5, E5, REST, C5, C5, C5, REST, C5, D5, E5, C5, A4, G4, E5, E5, REST, E5, REST, C5, E5]
durations8 = [EN, QN, EN, EN, EN, EN, EN, WN, EN, QN, EN, EN, EN, QN, EN, QN, EN, HN, EN, EN, EN, EN, EN, EN, QN]
#Creamos una "frase" vacia, para ir guardando.
theme = Phrase() 

#Vamos agregando las listas a la frase, cada una con las notras y la duración) 
theme.addNoteList(pitches1, durations1)
theme.addNoteList(pitches2, durations2)
theme.addNoteList(pitches3, durations3)
theme.addNoteList(pitches4, durations4)
theme.addNoteList(pitches5, durations5)
theme.addNoteList(pitches1, durations1)
theme.addNoteList(pitches2, durations2)
theme.addNoteList(pitches2, durations2)
theme.addNoteList(pitches7, durations7)
theme.addNoteList(pitches8, durations8)

theme.setTempo(200.0)   # set tempo to 100 beats-per-minute

pianoPart.addPhrase(theme) 
#Lo escuchamos todo junto!
Play.midi(pianoPart)