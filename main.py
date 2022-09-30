import pygame.midi as m
import keyboard

### Midify
import AdJustJson

### midiキーボード
m.init()
i = m.Input( m.get_default_input_id() )

while True:
    if i.poll(): # MIDIが受信されるとTrue

        # MIDI入力を取得
        midi_events = i.read(4)

        for event in midi_events:
            '''
            keybind.json に対応したキーを制御

            memo
            ---------
            event[0][1]: ノートナンバー
                押した時・離した時にそれぞれ一回出現

            event[0][2]: ベロシティ
                押した時だけ出現

            '''
            # keybind.json を読み込み
            j = AdJustJson.getKeyBind()

            # ノートナンバーを取得
            if event[0][1] in j.keys():
                k = j[ event[0][1] ]
            else:
                k = -1

            # 長押し判定
            try:
                if event[0][2] != 0:
                    keyboard.press(k)
                else:
                    keyboard.release(k)

            except ValueError: # 何も押してない時
                pass