
import json
import time
from online_protocol_process import create_frame
import common_link

def get_except_by_str(except_str):
    if except_str == "BaseException":
        return BaseException

    elif except_str == "SystemExit":
        return SystemExit

    elif except_str == "KeyboardInterrupt":
        return KeyboardInterrupt

    elif except_str == "Exception":
        return Exception

    elif except_str == "StopIteration":
        return StopIteration

    elif except_str == "GeneratorExit":
        return GeneratorExit

    elif except_str == "StandardError":
        return StandardError

    elif except_str == "ArithmeticError":
        return ArithmeticError

    elif except_str == "FloatingPointError":
        return FloatingPointError

    elif except_str == "OverflowError":
        return OverflowError

    elif except_str == "ZeroDivisionError":
        return ZeroDivisionError

    elif except_str == "AssertionError":
        return AssertionError

    elif except_str == "AttributeError":
        return AttributeError

    elif except_str == "EOFError":
        return EOFError

    elif except_str == "EnvironmentError":
        return EnvironmentError

    elif except_str == "IOError":
        return IOError

    elif except_str == "OSError":
        return OSError

    elif except_str == "WindowsError":
        return WindowsError

    elif except_str == "ImportError":
        return ImportError

    elif except_str == "LookupError":
        return LookupError

    elif except_str == "IndexError":
        return IndexError

    elif except_str == "KeyError":
        return KeyError

    elif except_str == "MemoryError":
        return MemoryError

    elif except_str == "NameError":
        return NameError

    elif except_str == "UnboundLocalError":
        return WindowsError

    elif except_str == "UnboundLocalError":
        return WindowsError

    elif except_str == "ReferenceError":
        return ReferenceError

    elif except_str == "RuntimeError":
        return RuntimeError

    elif except_str == "NotImplementedError":
        return NotImplementedError

    elif except_str == "SyntaxError":
        return SyntaxError

    elif except_str == "RuntimeError":
        return RuntimeError

    elif except_str == "IndentationError":
        return IndentationError

    elif except_str == "TabError":
        return TabError

    elif except_str == "TypeError":
        return TypeError

    elif except_str == "SystemError":
        return SystemError

    elif except_str == "ValueError":
        return ValueError

    elif except_str == "UnicodeError":
        return UnicodeError

    elif except_str == "UnicodeDecodeError":
        return UnicodeDecodeError

    elif except_str == "UnicodeEncodeError":
        return UnicodeEncodeError

    elif except_str == "UnicodeTranslateError":
        return UnicodeTranslateError

    elif except_str == "UnicodeDecodeError":
        return UnicodeDecodeError

    elif except_str == "Warning":
        return Warning

    elif except_str == "DeprecationWarning":
        return DeprecationWarning

    elif except_str == "FutureWarning":
        return FutureWarning

    elif except_str == "PendingDeprecationWarning":
        return PendingDeprecationWarning

    elif except_str == "RuntimeWarning":
        return RuntimeWarning

    elif except_str == "SyntaxWarning":
        return SyntaxWarning

    elif except_str == "UserWarning":
        return UserWarning



# define online apis, each name of the apis is the same with offline's
class api_format():
    def __init__(self):
        self.version = "v1.0"

# import firefly
def __import_firefly():
    frame = create_frame("from firefly import *")    
    common_link.communication.write(frame)

    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept

# button
def __button_is_pressed():
    frame = create_frame("button.is_pressed()")
    common_link.communication.write(frame)
    
    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept
#led
def __led_show_all(r, g, b):
    frame = create_frame(("led.show_all(%d, %d, %d)" %(r, g, b)))
    common_link.communication.write(frame)
    
    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept

def __led_show_single(index, r , g, b):
    frame = create_frame(("led.show_single(%d, %d, %d, %d)" %(index, r, g, b)))
    common_link.communication.write(frame)
    
    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept

def __led_off_all():
    frame = create_frame("led.off_all()" )
    common_link.communication.write(frame)
    
    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept
    
def __led_off_single(index):
    frame = create_frame(("led.off_single(%d)" %(index,)))
    common_link.communication.write(frame)
        
    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept

#vibration motor
def __vibration_motor_on(value):
    frame = create_frame(("vibration_motor.on(%d)" %(value,)))
    common_link.communication.write(frame)
        
    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept

def __vibration_motor_set_strength(value):
    frame = create_frame(("vibration_motor.set_strength(%d)" %(value,)))
    common_link.communication.write(frame)
        
    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept

# music
def __music_play_melody(name):
    frame = create_frame(("music.play_melody(\"%s\")" %(name,)))
    common_link.communication.write(frame)
        
    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept

def __music_play_melody_to_stop(name):
    frame = create_frame(("music.play_melody_to_stop(\"%s\")" %(name,)))
    common_link.communication.write(frame)
        
    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept

def __music_play_tone(frequency, beat):
    frame = create_frame(("music.play_tone(%d, %d)" %(frequency, beat)))
    common_link.communication.write(frame)
    
    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept

def __music_stop_sounds():
    frame = create_frame("music.stop_sounds()")
    common_link.communication.write(frame)
        
    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept

def __music_set_volume(volume):
    frame = create_frame(("music.set_volume(%d)" %(volume, )))
    common_link.communication.write(frame)
        
    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept

def __music_get_volume():
    frame = create_frame("music.get_volume()")
    common_link.communication.write(frame)
        
    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept

def __music_change_volume(change_value):
    frame = create_frame(("music.change_volume(%d)" %(change_value, )))
    common_link.communication.write(frame)
    
    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept

# touchpad
def __tp0_is_touched():
    frame = create_frame("touchpad0.is_touched()")
    common_link.communication.write(frame)
    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept

def __tp0_set_touch_threshold(value):
    frame = create_frame(("touchpad0.set_touch_threshold(%d)" %(value, )))
    common_link.communication.write(frame)

    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept

def __tp0_get_value():
    frame = create_frame("touchpad0.get_value()")
    common_link.communication.write(frame)

    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept

def __tp1_is_touched():
    frame = create_frame("touchpad1.is_touched()")
    common_link.communication.write(frame)

    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept

def __tp1_set_touch_threshold(value):
    frame = create_frame(("touchpad1.set_touch_threshold(%d)" %(value, )))
    common_link.communication.write(frame)

    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept

def __tp1_get_value():
    frame = create_frame("touchpad1.get_value()")
    common_link.communication.write(frame)

    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept

def __tp2_is_touched():
    frame = create_frame("touchpad2.is_touched()")
    common_link.communication.write(frame)

    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept

def __tp2_set_touch_threshold(value):
    frame = create_frame(("touchpad2.set_touch_threshold(%d)" %(value, )))
    common_link.communication.write(frame)

    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept

def __tp2_get_value():
    frame = create_frame("touchpad2.get_value()")
    common_link.communication.write(frame)

    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept

def __tp3_is_touched():
    frame = create_frame("touchpad3.is_touched()")
    common_link.communication.write(frame)

    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept

def __tp3_set_touch_threshold(value):
    frame = create_frame(("touchpad3.set_touch_threshold(%d)" %(value, )))
    common_link.communication.write(frame)

    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept

def __tp3_get_value():
    frame = create_frame("touchpad3.get_value()")
    common_link.communication.write(frame)

    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept

# microphone
def __mic_get_loudness():
    frame = create_frame("microphone.get_loudness()")
    common_link.communication.write(frame)

    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept 

# wifi
def __wifi_start(ssid = "Maker-guest", password = "makeblock", mode = 1):
    frame = create_frame(("wifi.start(%s, %s, %d)" %(ssid, password, mode)))
    common_link.communication.write(frame)

    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept 

def __wifi_is_connected():
    frame = create_frame("wifi.is_connected()")
    common_link.communication.write(frame)

    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept 

# speech recognition    
def __speech_recognition_start(server = 0, language = 0, time = 5):
    frame = create_frame("speech_recognition.start(%d, %d, %d)" %(server, language, time))
    common_link.communication.write(frame)

    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept 

def __speech_recognition_get_result_code():
    frame = create_frame("speech_recognition.get_result_code()")
    common_link.communication.write(frame)
    json_ret = common_link.communication.read()
    if not json_ret:
        return None

    if "ret" in json_ret:
        return json_ret['ret']
    else:
        if "err" in json_ret:
            ept = get_except_by_str(str(json_ret['err']))
            raise ept 

button = api_format()
button.is_pressed = __button_is_pressed

led = api_format()
led.show_all = __led_show_all
led.show_single = __led_show_single
led.off_single = __led_off_single
led.off_all = __led_off_all

vibration_motor = api_format()
vibration_motor.set_strength = __vibration_motor_set_strength
vibration_motor.on = __vibration_motor_on

music = api_format()
music.play_melody = __music_play_melody
music.play_melody_to_stop = __music_play_melody_to_stop
music.play_tone = __music_play_tone
music.stop_sounds = __music_stop_sounds
music.set_volume = __music_set_volume
music.change_volume = __music_change_volume
music.get_volume = __music_get_volume

touchpad0 = api_format()
touchpad1 = api_format()
touchpad2 = api_format()
touchpad3 = api_format()

touchpad0.is_touched = __tp0_is_touched
touchpad0.set_touch_threshold = __tp0_set_touch_threshold
touchpad0.get_value = __tp0_get_value
touchpad1.is_touched = __tp1_is_touched
touchpad1.set_touch_threshold = __tp1_set_touch_threshold
touchpad1.get_value = __tp1_get_value
touchpad2.is_touched = __tp2_is_touched
touchpad2.set_touch_threshold = __tp2_set_touch_threshold
touchpad2.get_value = __tp2_get_value
touchpad3.is_touched = __tp3_is_touched
touchpad3.set_touch_threshold = __tp3_set_touch_threshold
touchpad3.get_value = __tp3_get_value

microphone = api_format()
microphone.get_loudness = __mic_get_loudness


# do initialize
__import_firefly()

