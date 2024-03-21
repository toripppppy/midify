# midify
Let's use your MIDI Keyboard as PC Keyboard!<br>
MIDIキーボードをPCのキーボードとして使用できるようになります。

## 動作環境
Python 3.11.2
pygame 2.5.2

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
設定するためのノートナンバーの確認用に`printKey.py`をご利用ください。<br>
実行してキーボードを押すと、MIDIのノートナンバーと音階を出力します。
