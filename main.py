'''
main.py
midi入力を取得し、keybind.json に対応してPCのキーボードを制御。

2022 / 9 / 30
'''
import pygame.midi as m
import pyautogui

### Midify
import AdJustJson

### 危険! ###
# pyautoguiのリミッター解除（入力の高速化）
pyautogui.PAUSE = 0

### midiキーボード
m.init()
i = m.Input( m.get_default_input_id() )

# keybind.json を読み込み
keybind_dict = AdJustJson.getKeyBind()

while True:
    if i.poll(): # MIDIが受信されるとTrue

        # MIDI入力を取得
        midi_events = i.read(4)

        for event in midi_events:
            '''
            keybind.json に対応したキーを制御

            memo
            ---------
            event[0][0]: ステータス
                ON | OFF の情報

            event[0][1]: ノートナンバー
                押した時・離した時にそれぞれ一回出現
            '''

            status = event[0][0]
            note = event[0][1]

            # ON
            if status == 144:
                # 対応するキーを取得して押す
                key = keybind_dict.get(note)
                if key:
                    pyautogui.keyDown(key)

            # OFF
            elif status == 128:
                # 対応するキーを取得して離す
                key = keybind_dict.get(note)
                if key:
                    pyautogui.keyUp(key)
                