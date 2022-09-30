'''
midiキーボードの出力確認用
2022 / 9 / 30
'''
import pygame.midi as m

### midiキーボードを定義
m.init()
i = m.Input( m.get_default_input_id() )

flg  = True
while flg:
    if i.poll(): # MIDIが受信されるとTrue

        # MIDI入力を取得
        midi_events = i.read(4)

        for event in midi_events:
            if event[0][1] != 0:
                print(event[0][1])
                flg = False
