'''
midiキーボードの出力確認用
2022 / 9 / 30
'''
from midify import MIDIEvent, MIDIListener

listener = MIDIListener()

@listener.on_keydown
def keydown(event: MIDIEvent):
    print(event.note, "C|C#|D|D#|E|F|F#|G|G#|A|A#|B".split("|")[event.note % 12] + str((event.note // 12) - 2))

listener.run()