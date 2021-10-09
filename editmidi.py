import mido
from mido import MidiFile, MidiTrack

def edit_midi (dkey=0, bpm=120, filename="", output=""):
    # Input MIDI File
    if filename == "":
        print("No such MIDI file (.mid)")
        return False
    mid = MidiFile(filename)

    # Create an output MIDI file.
    chmid = MidiFile()
    vocaltrack = MidiTrack()
    chmid.tracks.append(vocaltrack)

    # Edit the sequence of midi messages.
    for i, track in enumerate(mid.tracks):
        for msg in track:
            # Edit the tempo
            if msg.type == 'set_tempo':
                vocaltrack.append(msg.copy(tempo = mido.bpm2tempo(bpm)))
            # Edit the key
            elif not msg.is_meta:
                if msg.note + dkey < 0: 
                    vocaltrack.append(msg.copy(note=0))
                elif msg.note + dkey > 127:
                    vocaltrack.append(msg.copy(note=127))
                else:
                    vocaltrack.append(msg.copy(note=msg.note + dkey))
            # Copy the metadata
            else:
                vocaltrack.append(msg.copy())

    # Save the completed MIDI file

    chmid.save(output)
    return True

#edit_midi(dkey=5, bpm=320, filename="little_star.mid")