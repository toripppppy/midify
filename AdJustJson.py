'''
### adJustJson.py
keybind.json からキー設定を読み込み、整形して返す。

2022 / 9 / 29
'''
import json

### 音階整形用
NOTE_DICT = {
    0 : 'C',
    1 : 'C#',
    2 : 'D',
    3 : 'D#',
    4 : 'E',
    5 : 'F',
    6 : 'F#',
    7 : 'G',
    8 : 'G#',
    9 : 'A',
    10 : 'A#',
    11 : 'B',
}


def getKeyBind(option = ''):
    '''
    keybind.json からキー設定を読み込み、整形して返す。

    Parameters
    ----------
    option : str
        変換オプション
        'rename': ノートナンバーを音名に修正

    Return
    ------
    { MIDI : KEY ... }
    
    '''
    ### keybind.json を読み込み
    json_open = open('keybind.json', 'r')
    json_load = json.load(json_open)

    ### 整形
    # json_adj = { MIDI : KEY ... }
    json_adj = { json_load[i]['midi'] : json_load[i]['key'] for i in range( len(json_load) ) }

    result = {}
    
    if option == 'rename': # 表示用に音名に修正

        json_adj = sorted(json_adj.items()) # 昇順にソート

        for j in json_adj:
            note = j[0] % 12 # 音階
            note_name = NOTE_DICT[note] # 辞書に沿って音名に修正
            octave = str( (j[0] // 12) - 2 ) # オクターブ

            result.update( {note_name + octave : j[1]} ) # C3, D#4 etc...

    else: # 修正せず返す
        result = json_adj

    return result

print(getKeyBind('rename'))