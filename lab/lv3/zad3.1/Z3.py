import time
from machine import Pin
time.sleep(0.1) # Wait for USB to become ready

R1=Pin(21,Pin.OUT)
R2=Pin(22,Pin.OUT)
R3=Pin(26,Pin.OUT)
R4=Pin(27,Pin.OUT)
rows = [R1,R2,R3,R4]
C1=Pin(0,Pin.IN, Pin.PULL_DOWN)
C2=Pin(1,Pin.IN, Pin.PULL_DOWN)
C3=Pin(2,Pin.IN, Pin.PULL_DOWN)
C4=Pin(3,Pin.IN, Pin.PULL_DOWN)
cols = [C1,C2,C3,C4]

D1=Pin(4, Pin.OUT)
D2=Pin(5, Pin.OUT)
D3=Pin(6, Pin.OUT)
D4=Pin(7, Pin.OUT)
A=Pin(8, Pin.OUT)
B=Pin(9, Pin.OUT)
C=Pin(10, Pin.OUT)
D=Pin(11, Pin.OUT)
E=Pin(12, Pin.OUT)
F=Pin(13, Pin.OUT)
G=Pin(14, Pin.OUT)
DP=Pin(15, Pin.OUT)

digits = [D1, D2, D3, D4]
segments = [A,B,C,D,E,F,G]

keys = ['1','2','3','A',
        '4','5','6','B',
        '7','8','9','C',
        '*','0','#','D']

digit = [[0,0,0,0,0,0,1],[1,0,0,1,1,1,1],
          [0,0,1,0,0,1,0],[0,0,0,0,1,1,0],
          [1,0,0,1,1,0,0],[0,1,0,0,1,0,0],
          [0,1,0,0,0,0,0],[0,0,0,1,1,1,1],
          [0,0,0,0,0,0,0],[0,0,0,0,1,0,0]]

period = [0.001,.002,.003,.004,0.005,.006,.007,.008,.009,.01]
t=.01

def keyInput():
    for i in range(0,4):
        rows[i].on()
        for j in range(0,4):
            if cols[j].value():
                rows[i].off()
                return keys[i*4+j]
        rows[i].off() 
    return ''

def display(x):
    for i in range(0,4):
        for seg in segments:
            seg.on() 
        digits[i].off()
        for j in range(0,7):
                if digit[int(x[i])][j]:
                    segments[j].on()
                else:
                    segments[j].off()
        digits[i].on()
    time.sleep(t*0.3)


out=Pin(28,Pin.OUT)
out.off()
DP.on()
curr=9

while True:
    c=keyInput()
    while keyInput()!='':
        display('{0:04d}'.format(int(curr+1)))
        time.sleep(t/2) 
    if c>'0' and c<='9':
        curr=int(c)
        curr-=1
        t=period[curr]
    elif c=='0':
        curr=9
        t=period[curr]
    elif c=='C':
        if curr<9:
            curr+=1
            t=period[curr]
    elif c=='D':
        if curr>0:
            curr-=1
            t=period[curr]
    if out.value() == 1:
        out.off()
        display('{0:04d}'.format(int(curr+1)))  
    else:
        out.on()
        #time.sleep(t/2)
        display('{0:04d}'.format(int(curr+1)))
    