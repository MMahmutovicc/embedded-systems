from ili934xnew import ILI9341, color565
from machine import Pin, SPI
from micropython import const
import os
import glcdfont
import tt14
import tt24
import tt32
import time
import gfx
    
from machine import ADC
adc = ADC(Pin(28))

# Dimenzije displeja
SCR_WIDTH = const(320)
SCR_HEIGHT = const(240)
SCR_ROT = const(2)
CENTER_Y = int(SCR_WIDTH/2)
CENTER_X = int(SCR_HEIGHT/2)

print(os.uname())

# Podešenja SPI komunikacije sa displejem
TFT_CLK_PIN = const(18)
TFT_MOSI_PIN = const(19)
TFT_MISO_PIN = const(16)
TFT_CS_PIN = const(17)
TFT_RST_PIN = const(20)
TFT_DC_PIN = const(15)

# Fontovi na raspolaganju
fonts = [glcdfont, tt14, tt24, tt32]
text = 'RPi Pico/ILI9341'
print(text)

print("Fontovi:")
for f in fonts:
    print(f.__name__)

spi = SPI(0,
          baudrate=62500000,
          miso=Pin(TFT_MISO_PIN),
          mosi=Pin(TFT_MOSI_PIN),
          sck=Pin(TFT_CLK_PIN))
print(spi)

display = ILI9341(spi,
                  cs=Pin(TFT_CS_PIN),
                  dc=Pin(TFT_DC_PIN),
                  rst=Pin(TFT_RST_PIN),
                  w=SCR_WIDTH,
                  h=SCR_HEIGHT,
                  r=SCR_ROT)

# Brisanje displeja i odabir pozicije (0,0)
display.erase()
display.set_pos(0,0)

# Ispis teksta različitim fontovima, počevši od odabrane pozicije
for ff in fonts:
    display.set_font(ff)
    display.print(text)

# Ispis teksta u drugoj boji
display.set_font(tt14)
display.set_color(color565(150, 200, 0), color565(0, 0, 0))
time.sleep(1)

#Brisanje displeja
display.erase()

# Dodatna funkcija za crtanje kružnice ispisom pojedinačnih piksela
display.set_font(tt14)
display.erase()

# Različita orijentacija teksta na displeju
display.set_pos(10,100)
display.rotation=0
display.erase()
display.set_pos(10,100)
display.rotation=1
display.init()
display.erase()
display.set_pos(10,100)
display.rotation=2
display.init()
display.erase()
display.set_pos(10,100)
display.rotation=3
display.init()
display.erase()

display.set_pos(10,100)
display.rotation=4
display.init()
display.erase()
display.set_pos(10,100)
display.rotation=5
display.init()
display.erase()
display.set_pos(10,100)
display.rotation=6
display.init()
display.erase()
display.set_pos(10,100)
display.rotation=7
display.init()
display.erase()

def linija(x0, y0, x1, y1, color):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1
    err = dx - dy
    
    while True:
        display.pixel(x0, y0, color)
        display.pixel(x0, y0+1, color)
        
        if x0 == x1 and y0 == y1:
            break
        
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

def fast_hline(x, y, width, color):
    display.fill_rectangle(x, y, width, 1, color)

def fast_vline(x, y, height, color):
    display.fill_rectangle(x, y, 1, height, color)
    
def draw_circle(xpos0, ypos0, rad, col=color565(255, 255, 255)):
    x = rad - 1
    y = 0
    dx = 1
    dy = 1
    err = dx - (rad << 1)
    while x >= y:
        # Prikaz pojedinačnih piksela
        display.pixel(xpos0 + x, ypos0 + y, col)
        display.pixel(xpos0 + y, ypos0 + x, col)
        display.pixel(xpos0 - y, ypos0 + x, col)
        display.pixel(xpos0 - x, ypos0 + y, col)
        display.pixel(xpos0 - x, ypos0 - y, col)
        display.pixel(xpos0 - y, ypos0 - x, col)
        display.pixel(xpos0 + y, ypos0 - x, col)
        display.pixel(xpos0 + x, ypos0 - y, col)
        if err <= 0:
            y += 1
            err += dy
            dy += 2
        if err > 0:
            x -= 1
            dx += 2
            err += dx - (rad << 1)

def line(self, x0, y0, x1, y1, *args, **kwargs):
# Line drawing function. Will draw a single pixel wide line starting at
# x0, y0 and ending at x1, y1.
    steep = abs(y1 - y0) > abs(x1 - x0)
    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    dx = x1 - x0
    dy = abs(y1 - y0)
    err = dx // 2
    ystep = 0
    if y0 < y1:
        ystep = 1
    else:
        ystep = -1
    while x0 <= x1:
        if steep:
            self._pixel(y0, x0, *args, **kwargs)
        else:
            self._pixel(x0, y0, *args, **kwargs)
        err -= dy
        if err < 0:
            y0 += ystep
            err += dx
        x0 += 1
        
def lines():
    display.fill_rectangle(0,0,SCR_WIDTH,SCR_HEIGHT, color565(0,0,0))
    display.set_font(tt24)
    display.set_color(color565(255,255,255), color565(0,0,0))
    display.set_pos(14, 180)
    display.print("20")
    display.set_pos(14, 100)
    display.print("30")
    display.set_pos(14, 20)
    display.print("40")
    display.set_color(color565(255,255,255), color565(255,255,255))
    display.fill_rectangle(10,10,2,220, color565(255,255,255))
    display.fill_rectangle(5,200,285,2, color565(255,255,255))
        

graphics = gfx.GFX(240, 320, display.pixel, hline=fast_hline, vline=fast_vline)

#graphics.line(0, 0, 239, 319, color565(255, 0, 0))
t = 0
t_act = 0
vrijeme = 5
t=0
temp_tac = (12,200)
while True :
    t += 1
    t_act += 1
    volt = round(adc.read_u16()*3300/65535,2)
    tmp = round(volt/10,1)
    display.set_pos(180,10)
    display.rotation=1
    display.init()
    display.print('Temp: '+ str(tmp) + " C")
    display.print('Napon: ' + str(volt) + 'mV')
    display.print('Vrijeme: ' + str(t) + 's')
    x = 12 + t * 12
    y = 199 + (20 - int(tmp)) * 8

    #graphics.line(20,20,20,100)

    linija(temp_tac[0],temp_tac[1],x,y,color565(255,0,0))
    for i in range(5):
        draw_circle(temp_tac[0], temp_tac[1],i,color565(255,255,255))
    for i in range(5):
        draw_circle(x, y,i,color565(255,0,0))
    temp_tac=(x,y)
    #if t%23 == 0:
    #    t=0
    #    lines()
    #    temp_tac=(x-23*12,y)
    time.sleep(1)