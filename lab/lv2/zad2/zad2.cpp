#include "mbed.h"

BusOut leds(p5, p6, p7, p8, p9, p10, p11, p12);
DigitalIn btn(BUTTON1);
int main() {
    int counter = 0;
    bool increment = true;
    while (1) {
        leds = counter;
        if(btn == 1)
            increment = !increment;
        if(increment)
            counter++;
        else
            counter--;
        if(counter < 0) counter = 255;
        if(counter > 255) counter = 0;
        wait_us(1000000);
    }
}
