'''
### adJustJson.py
keybind.json からキー設定を読み込み、整形して返す。

2022 / 9 / 29
'''
import json


def get_keybind_dict():
    '''
    keybind.json からキー設定を読み込み、整形して返す。

    Return
    ------
    { MIDI : KEY ... }
    
    '''
    ### keybind.json を読み込み
    json_open = open('keybind.json', 'r')
    json_load = json.load(json_open)

    ### 整形
    keybind_dict = { json_load[i]['midi'] : json_load[i]['key'] for i in range( len(json_load) ) }

    return keybind_dict
