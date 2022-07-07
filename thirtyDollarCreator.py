from mido import MidiFile

SET_THIS = 'midi file goes here' #midi file path
TRANSPOSITION = '' #how many notes it should be transposed by
NOTES_ABOVE = '' #play only notes with pitch above certain amount
FILE_NAME = '' #what you want the name of the file made called

mid = MidiFile(SET_THIS)
songtext = '🚫@'
for msg in mid.tracks[1]:
  if not msg.is_meta:
    if msg.type == 'note_on':
      #print(msg.note)
      if int(msg.note)+(-72+int(TRANSPOSITION)) > int(NOTES_ABOVE):
        songtext = songtext + str(int(msg.note)-72) + '|🚫@'
print(songtext)
with open(FILE_NAME, 'w') as f:
  f.write(songtext)
