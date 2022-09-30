# midify
use your midi keyboard as pc keyboard.  
MIDIキーボードをPCのキーボードとして使用できるようになります。

## 動作環境
Python3

M1Macのみ動作確認済み。おそらく他OSでも動くはずです・・・

## 使い方
1. ターミナルで任意の場所で `git clone git@github.com:toripppppy/midify.git`
2. `cd midify`で移動
3. midifyで使用するモジュールをインストール `pip install keyboard pygame`
4. MIDIキーボードをPCに接続
5. `python3 main.py`でmidifyを実行。適当な鍵盤を押して、文字が打ち込まれたら成功です

### キー設定を変更
keyboard.json を書き換えます。
```json:keybind.json
[
    {
        "midi" : 60,
        "key" : "a"
    },
]
```
**midi** : MIDIキーボードのノートナンバー  
C3 = 60です。  

**key** : 制御するPCのキー  
keyboardモジュールに対応したキーが設定されていないと入力が無視されます。

## その他
設定用GUI製作中です  
今は代用として`printKey.py`を置いてます。  
実行すると、一番初めに押されたMIDIのノートナンバーを出力します。
