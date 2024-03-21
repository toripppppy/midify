'''
main.py
midi入力を取得し、keybind.json に対応してPCのキーボードを制御。

2022 / 9 / 30
'''
import pyautogui

### Midify
import adjust_json

from midify import MIDIEvent, MIDIListener

### 危険! ###
# pyautoguiのリミッター解除（入力の高速化）
pyautogui.PAUSE = 0


# keybind.json を読み込み
keybind_dict = adjust_json.get_keybind_dict()

listener = MIDIListener()

@listener.on_keydown
def keydown(event: MIDIEvent):
    key = keybind_dict.get(event.note)
    if key:
        pyautogui.keyDown(key)

@listener.on_keyup
def keydown(event: MIDIEvent):
    key = keybind_dict.get(event.note)
    if key:
        pyautogui.keyUp(key)

listener.run()