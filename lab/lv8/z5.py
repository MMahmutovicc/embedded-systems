import RPi.GPIO  as GPIO
import time

GPIO.setmode(GPIO.BCM) # 2 i 17

GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.output(3, True)
GPIO.output(4, True)
GPIO.setup(17, GPIO.IN)
duty = 100

p = GPIO.PWM(2, 100)
p.start(100)

while True:
    if GPIO.input(17) == 0:
        print("pritisnut taster")
        duty -= 10
        if duty < 0:
            duty = 100
        p.ChangeDutyCycle(duty)
        while GPIO.input(17) == 0:
            time.sleep(0.001)
    time.sleep(0.001)
