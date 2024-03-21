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

追記(2024/3/21):
MIDIキーボードの機種によって、動作が異なるようです。具体的には、MIDIイベントの入力形式が異なっていたりします。
よって、押された時・離された時の判定が一部機種で正常に機能しません。
こちらで全てに対応できるコードを書くのは難しいので、その判定を上書きできるようにしました。

`main.py`で方法を示していますが、判定メソッドをお手元の環境に合わせて書き換えてください。<br>
（手元のMIDIキーボードでは、押されたらstatusが144、離されたらstatusが128になっていました。したがってそう実装しています）
```python
# キーボードに合わせて押した判定の方法をオーバーライドする
def is_keydown(event: MIDIEvent):
    return event.status == 144

def is_keyup(event: MIDIEvent):
    return event.status == 128

listener.is_keydown = is_keydown
listener.is_keyup = is_keyup
```

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
設定するためのノートナンバーの確認用に`print_key.py`をご利用ください。<br>
実行してキーボードを押すと、MIDIのノートナンバーと音階を出力します。
