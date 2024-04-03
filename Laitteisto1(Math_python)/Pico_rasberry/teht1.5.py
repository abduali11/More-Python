from machine import Pin
import time

leds = [Pin(20, Pin.OUT), Pin(21, Pin.OUT), Pin(22, Pin.OUT)]
button = Pin(12, Pin.IN, Pin.PULL_UP)

variable = 0

while True:
    if button.value() == 0:
        variable = (variable + 1) % 8
        for i in range(3):
            leds[i].value((variable >> i) & 1)
        time.sleep(0.3)


