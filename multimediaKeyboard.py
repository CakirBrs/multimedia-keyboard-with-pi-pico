import digitalio
import analogio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import time
keyboard = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

value =0

a0=analogio.AnalogIn(board.GP27)

btn_pin = board.GP15
btn=digitalio.DigitalInOut(btn_pin)
btn.direction= digitalio.Direction.INPUT
btn.pull = digitalio.Pull.DOWN

btn2_pin = board.GP14
btn2=digitalio.DigitalInOut(btn2_pin)
btn2.direction= digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

value =int(a0.value/650)
perc=0
isMuted=False
for i in range(100):
    cc.send(ConsumerControlCode.VOLUME_DECREMENT)
for y in range(value):
    cc.send(ConsumerControlCode.VOLUME_INCREMENT)
    perc=perc+1





while True:
    value =int((a0.value/65000)*50)
    print((a0.value/65000)*50)
    
    if btn.value:
        cc.send(ConsumerControlCode.MUTE)
        isMuted = not isMuted
        time.sleep(0.1)
        
    if btn2.value:
        cc.send(ConsumerControlCode.PLAY_PAUSE)
        time.sleep(0.1)
        
    if not isMuted:
        if(perc < value):
            for c in range(value-perc):
                cc.send(ConsumerControlCode.VOLUME_INCREMENT)
                perc=perc+1
        if(perc > value):
            for c in range(perc-value):
                cc.send(ConsumerControlCode.VOLUME_DECREMENT)
                perc=perc-1
    time.sleep(0.1)
