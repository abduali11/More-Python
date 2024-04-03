from machine import Pin, ADC

import time
pot = ADC(26)
led = Pin("LED", Pin.OUT)

while True:
    adcVal = pot.read_u16()
    print("ADC VAL: ()".format(adcVal))
    print("Voltage: ()".format((adcVal/65535)))
    led.toggle()
    timer = adcVal/65535/2
    print(timer)
    time.sleep(timer)
    #led.on()
    #time.sleep(0.25)
    #led.off()
    #time.sleep(0.5)

# koodi mahdollistaa laitteen vilkkumista, kun säädetään nappia