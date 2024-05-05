from machine import Pin, Timer
import time
time.sleep(0.1) # Wait for USB to become ready

leds = [Pin(i,Pin.OUT) for i in range(4, 12)]

clk = Pin(0,Pin.IN)
dt = Pin(1,Pin.IN)
sw = Pin(2,Pin.IN)

initState = clk.value()
counter = 0
debouncing = 1

def buttonPressed(pin):
    global counter
    counter = 0
    print("pritisnuto!")
    updateLeds('{0:08b}'.format(counter))

def updateLeds(x):
    for i in range(0,8):
        if x[i] == "1":
            leds[i].on()
        else:
            leds[i].off()

def encoderValue(pin):
    global initState,counter
    currentState = clk.value()
    if (currentState != initState and currentState == 1):
        if dt.value() != currentState:
            counter += 1
            if counter > 255:
                counter = 0
        else:
            counter -= 1
            if counter < 0:
                counter = 255
        print("Counter: ",counter)
    initState = currentState
    updateLeds('{0:08b}'.format(counter))

sw.irq(trigger=Pin.IRQ_RISING,handler=buttonPressed)
clk.irq(trigger=Pin.IRQ_RISING,handler=encoderValue)
dt.irq(trigger=Pin.IRQ_RISING,handler=encoderValue)

while True:
    time.sleep(0.02)