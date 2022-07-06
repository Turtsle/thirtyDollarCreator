from mido import MidiFile

SET_THIS = 'midi file goes here'

mid = MidiFile(SET_THIS)
songtext = '🚫@'
for msg in mid.tracks[1]:
  if not msg.is_meta:
    if msg.type == 'note_on':
      #print(msg.note)
      songtext = songtext + str(int(msg.note)-72) + '|🚫@'
print(songtext)
with open('thirydollar.txt', 'w') as f:
  f.write(songtext)
