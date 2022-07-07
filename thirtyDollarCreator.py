from mido import MidiFile

SET_THIS = 'enter midi file path here' #midi file path
TRANSPOSITION = '' #how many notes it should be transposed by - MUST HAVE AN INPUT, type 0 for no restrictions
NOTES_ABOVE = '' #play only notes with pitch above certain amount - MUST HAVE AN INPUT, type -1000 for no restrictions
HANDS = '' #ONLY 'yes' or 'no' - determines whether the next 2 settings apply - MUST HAVE AN INPUT
#Take note of transposition if you have any
LEFT_HAND = '' #whatever number you put here anything below that will be considred the left hand - MUST HAVE AN INPUT, if HANDS = yes
RIGHT_HAND = '' #whatever number you put here anything above that will be considred the right hand - MUST HAVE AN INPUT, if HANDS = yes
FILE_NAME = 'thirtyDollarCreator' #what you want the name of the file made called - MUST HAVE AN INPUT, could even just be "a" just something

mid = MidiFile(SET_THIS)
songtext = '🚫@'
for msg in mid.tracks[1]:
  if not msg.is_meta:
    if msg.type == 'note_on':
      #print(msg.note)
      if int(msg.note)+(-72+int(TRANSPOSITION)) > int(NOTES_ABOVE):
        if HANDS == "yes":
          if int(msg.note)-72 > int(RIGHT_HAND):
            songtext = songtext + "🚫@" + str(int(msg.note)-72) + '|!combine|'
          if int(msg.note)-72 < int(LEFT_HAND):
            songtext = songtext + '🚫@' + str(int(msg.note)-72) + "|"
        else:
          songtext = songtext + str(int(msg.note)-72) + '|🚫@'
print(songtext)
with open(FILE_NAME, 'w') as f:
  f.write(songtext)
