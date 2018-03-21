# main.py
# CircuitPython Blink with Switch

import time
from digitalio import DigitalInOut, Direction, Pull
import board

led = DigitalInOut(board.D6)
led.direction = Direction.OUTPUT

switch = DigitalInOut(board.D9). # use pin D9
switch.direction = Direction.INPUT
switch.pull = Pull.DOWN

while True:
    if switch.value:  # if switch.value = true
        led.value = False
    else:  # all other possibilities
        led.value = True
        
    time.sleep(0.01). # Debounce switch
