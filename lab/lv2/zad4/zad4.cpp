#include "mbed.h"
DigitalOut led1(LED1);
DigitalIn taster_1(BUTTON1);
DigitalIn taster_2(p5);
BusOut leds(p6, p7, p8, p9, p10, p11, p12, p13);
int vrijeme = 500000;
int main() {
    int counter = 1;
    bool loop = false, increment = true;
    while (1) {
        led1 = !led1;
        if(taster_1) {
            loop = true;
            vrijeme = 100000;
        }
        else if(taster_2) {
            loop = true;
            vrijeme = 500000;
        }
        while(loop) {
            leds = counter;
            if(increment && counter == 64){
                counter = 255;
                increment = false;
            }
            else if(!increment && counter == 1) {
                increment = true;
                loop = false;
                vrijeme = 500000;
                leds = 0;
            }
            else if(increment)
                counter *= 2;
            else
                counter /= 2;
            if(counter < 0) counter = 255;
            if(counter > 255) counter = 0;
            wait_us(vrijeme);
        }
        wait_us(vrijeme);
    }
}
