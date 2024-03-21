import pygame.midi as pmidi


class MIDIEvent:
    """
    単体のMIDI入力イベントを整理するクラス
    
    note: ノートナンバー
    velocity: 音量
    channel: 入力チャンネル
    timestamp: 経過時間
    """
    def __init__(self, event) -> None:
        self.status = event[0][0]
        self.note = event[0][1]
        self.velocity = event[0][2]
        self.channel = event[0][3]
        self.timestamp = event[1]


class MIDIListener:
    """
    MIDIイベントをリッスンして都度イベントを発生させる
    
    on_keydown: キーが押された時
    on_keyup  : キーが離された時
    """
    def __init__(self):
        # MIDI
        pmidi.init()
        self.input = pmidi.Input(pmidi.get_default_input_id())

        # Initialise a list of listeners
        self.__keydown_listeners = []
        self.__keyup_listeners = []
        
    @property
    def on_keydown(self):
        # キーが押された時に呼ばれるイベント
        def wrapper(func):
            self.add_keydown_listener(func)
            return func
        return wrapper
    
    @property
    def on_keyup(self):
        # キーが離された時に呼ばれるイベント
        def wrapper(func):
            self.add_keyup_listener(func)
            return func
        return wrapper
    
    def add_keydown_listener(self,func):
        if func in self.__keydown_listeners: return
        self.__keydown_listeners.append(func)

    def add_keyup_listener(self,func):
        if func in self.__keyup_listeners: return
        self.__keyup_listeners.append(func)
    
    # イベントトリガー
    def on_keydown_trigger(self, event: MIDIEvent):
        # キーが押された時にイベントを呼び出す
        for func in self.__keydown_listeners:
            func(event)

    def on_keyup_trigger(self, event: MIDIEvent):
        # キーが離された時にイベントを呼び出す
        for func in self.__keyup_listeners:
            func(event)

    """
    キーが押された・離されたの判定
    オーバーライドして個人の環境に合わせて使ってもらう
    """
    def is_keydown(self, event: MIDIEvent) -> bool:
        return event.status == 144
    
    def is_keyup(self, event: MIDIEvent) -> bool:
        return event.status == 128

    def run(self):
        """
        リスナーの開始
        """
        while True:
            if self.input.poll():
                # MIDI入力を取得
                midi_events = self.input.read(4)

                for midi_event in midi_events:
                    event = MIDIEvent(midi_event)

                    if self.is_keydown(event):
                        self.on_keydown_trigger(event)

                    elif self.is_keyup(event):
                        self.on_keyup_trigger(event)