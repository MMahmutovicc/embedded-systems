import time
time.sleep(0.1) # Wait for USB to become ready
from machine import ADC, Pin

leds = [Pin(4,Pin.OUT),Pin(5,Pin.OUT),Pin(6,Pin.OUT),Pin(7,Pin.OUT),
        Pin(8,Pin.OUT),Pin(9,Pin.OUT),Pin(10,Pin.OUT),Pin(11,Pin.OUT)]

adc = ADC(Pin(28))

counter = 0
increment = 1

while True:
    val = adc.read_u16()
    t = 0.1 + (val / 34492.1) 
    print(t)
    if counter == 0:
        if increment == -1:
            leds[counter].off()
            increment = 1
            counter -= 1
        else:
            leds[counter].value(1)
    elif (counter == 7 and increment == 1):
        for i in range(8):
            leds[i].on()
        increment = -1
        counter += 1
    elif (counter == 7 and increment == -1):
        leds[counter].off()
    else:
        if increment == 1:
            leds[counter - 1].off()
            leds[counter].on()
        else:
            leds[counter].off()
    counter += increment
    time.sleep(t)
    
