from music import *


 
Jupyter = Score("Jupyter", 108.0)  # tempo is 108 bpm

#Candidatos: 97 ; 83 
MelodyPart    = Part(83, 0)        # Melody  part on channel 0

themePhrase = Phrase(0.0)            # theme starts at the beginning
 


#pitches1 = [G2,G2,G2,B2,B2,G2,G2,D2]
#pitches1 = [G3,G3,G3,B3,B3,G3,G3,D3]
pitches1 = [G5,G5,G5,B5,B5,G5,G5,D5]
durations1= [DEN, DEN,DEN, QN,QN, DEN,DEN, HN]

pitches2 = [G2,G2,G2,C2,D2,G2,G2,D2]
durations2= [DEN, DEN,DEN, QN,QN, DEN,DEN, HN]


# add the notes to the theme
themePhrase.addNoteList(pitches1, durations1)
themePhrase.addNoteList(pitches2, durations2)

# make two new phrases and change start times to make a round
response1Phrase = themePhrase.copy()

response1Phrase.setStartTime(8.0)     # start after 4 quarter notes

# play different parts in different registers
Mod.transpose(themePhrase, 12)         # one octave higher

# play each phrase twice
Mod.repeat(themePhrase, 5)
Mod.repeat(response1Phrase, 5)

# add phrases to corresponding parts
MelodyPart.addPhrase(themePhrase)

# add parts to score
Jupyter.addPart(MelodyPart)

# play score
Play.midi(Jupyter)