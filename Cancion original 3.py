from music import *


 
Jupyter = Score("Jupyter", 100.0)  # tempo is 108 bpm


themePart = Part(70,0)
MelodyPart    = Part(10, 0)        # 93 , 10 , 48 ,70 on channel 0
MelodyPart2 = Part(10,0)

themePhrase= Phrase(0.0)
chords1 = Phrase(0.0)            # theme starts at the beginning
chords2 = Phrase(0.0)


cord1= [a2,d3,fs3]
cord2= [g2,c3,e3]
cord3= [f2,a2,c3]
cord4 = [g2,b2,d3]



chord5=[d3,f3]
chord6=[c3,e3]
chord7=[c3,a2]
chord8=[a2,f2]

chords1.addChord(cord1,HN)
chords1.addChord(cord2,HN)
chords1.addChord(cord3,HN)
chords1.addChord(cord4,HN)
chords1.addChord(cord1,HN)


chords2.addChord(chord5,HN)
chords2.addChord(chord5,HN)
chords2.addChord(chord6,HN)
chords2.addChord(chord7,HN)
chords2.addChord(chord5,HN)
chords2.addChord(chord5,HN)
chords2.addChord(chord7,HN)
chords2.addChord(chord8,HN)



pitches1 = [d3,d3,d3,d3,d3,d3,d3,d3,c3,c3]
durations1= [QN,QN,QN,QN,QN,QN,QN,QN,QN,QN]



themePhrase.addNoteList(pitches1, durations1)
#set delays
chords2.setStartTime(chords1.getEndTime()*2)
themePhrase.setStartTime(chords1.getEndTime()*2 + chords2.getEndTime() )



# play different parts in different registers
Mod.transpose(chords1, 13)         # one octave higher
Mod.transpose (chords2,13)
Mod.transpose (themePhrase,13)
# play each phrase twice
Mod.repeat(chords1, 2)
Mod.repeat(chords2, 6)
Mod.repeat(themePhrase, 4)

# add phrases to corresponding parts
MelodyPart.addPhrase(chords1)
MelodyPart2.addPhrase(chords2)
themePart.addPhrase(themePhrase)


# add parts to score
Jupyter.addPart(MelodyPart)
Jupyter.addPart(MelodyPart2)
Jupyter.addPart(themePart)


# play score
Play.midi(Jupyter)
Write.midi(Jupyter, "song.mid")