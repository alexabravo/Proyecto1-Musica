from music import *


 
Jupyter = Score("Jupyter", 140.0)  # tempo is 108 bpm

#Candidatos: 97 ; 83 
#MelodyPart    = Part(83, 0)        # Melody  part on channel 0
#BackgroundPart = Part(62,1)

MelodyPart    = Part(10, 0)        # Melody  part on channel 0
BackgroundPart = Part(14,1)

themePhrase = Phrase(0.0)            # theme starts at the beginning
backgroundPhrase= Phrase(0.0)


#pitches1 = [G2,G2,G2,B2,B2,G2,G2,D2]
#pitches1 = [G3,G3,G3,B3,B3,G3,G3,D3]
pitches1 = [G4,G4,G4,B4,B4,G4,G4,D4]
durations1= [DEN, DEN,DEN, QN,QN, DEN,DEN, HN]

pitches2 = [G2,G2,G2,C2,D2,G2,G2,D2]
durations2= [DEN, DEN,DEN, QN,QN, DEN,DEN, HN]


pitches3 = [G2,G2,G2,C2,D2,G2,G2,D2]
durations3= [DEN, DEN,QN, DEN,QN, DEN,HN, DEN]
# add the notes to the theme
themePhrase.addNoteList(pitches1, durations1)
themePhrase.addNoteList(pitches2, durations2)

backgroundPhrase.addNoteList(pitches3, durations2)

# make two new phrases and change start times to make a round
response1Phrase = themePhrase.copy()
# cada set dura 13/8 QN 
backgroundPhrase.setStartTime(23.0)     # start after 4 quarter notes

# play different parts in different registers
Mod.transpose(themePhrase, 18)         # one octave higher

# play each phrase twice
Mod.repeat(themePhrase, 5)
Mod.repeat(backgroundPhrase, 3)

# add phrases to corresponding parts
MelodyPart.addPhrase(themePhrase)
BackgroundPart.addPhrase(backgroundPhrase)


# add parts to score
Jupyter.addPart(MelodyPart)
Jupyter.addPart(BackgroundPart)


# play score
Play.midi(Jupyter)
Write.midi(Jupyter, "cou2.mid")
