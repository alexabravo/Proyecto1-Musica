from music import *
 
# Create the necessary musical data
Melodia2 = Score("Melodia Prueba 2", 108.0)  # tempo is 108 bpm
 
flutePart    = Part(12, 0)        # flute part on channel 0
trumpetPart  = Part(10, 1)      # trumpet part on channel 1
clarinetPart = Part(CLARINET, 2)     # clarinet part on channel 2
 
themePhrase = Phrase(0.0)            # theme starts at the beginning
 

pitches1   = [C4, D4, E4, G4, A4]
durations1 = [QN, EN, SN, EN, SN]

pitches2 = [G5, G5, G5, D5, D5, D5, B4, B4, B4, G4, G4, G4]
durations2 = [ENT, DSN, SN, DEN, DEN, DEN, SN, DSN, SN, DEN, DEN, SN]
 

pitches3 = [D5, F4, E4, D4, C4]
durations3 = [DEN, QN, SN, DEN, HN]
 
# add the notes to the theme
themePhrase.addNoteList(pitches1, durations1)
themePhrase.addNoteList(pitches2, durations2)
themePhrase.addNoteList(pitches3, durations3)
 
# make two new phrases and change start times to make a round
response1Phrase = themePhrase.copy()
response2Phrase = themePhrase.copy()
 
response1Phrase.setStartTime(4.0)     # start after 4 quarter notes
response2Phrase.setStartTime(8.0)     # start after 8 quarter notes
 
# play different parts in different registers
Mod.transpose(themePhrase, 13)         # one octave higher
Mod.transpose(response2Phrase, 13)    # one octave lower
 
# play each phrase twice
Mod.repeat(themePhrase, 2)
Mod.repeat(response1Phrase, 2)
Mod.repeat(response2Phrase, 2)
 
# add phrases to corresponding parts
flutePart.addPhrase(themePhrase)
trumpetPart.addPhrase(response1Phrase)
clarinetPart.addPhrase(response2Phrase)
 
# add parts to score
Melodia2.addPart(flutePart)
Melodia2.addPart(trumpetPart)
#Melodia2.addPart(clarinetPart)
 
# play score
Play.midi(Melodia2)