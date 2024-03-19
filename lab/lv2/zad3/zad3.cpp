#include "mbed.h"

BusOut leds(p5, p6, p7, p8, p9, p10, p11, p12);
int main() {
    int counter = 1;
    bool increment = true;
    while (1) {
        leds = counter;
        if(increment && counter == 64){
            counter = 255;
            increment = false;
        }
        else if(!increment && counter == 1)
            increment = true;
        else if(increment)
            counter *= 2;
        else
            counter /= 2;
        if(counter < 0) counter = 255;
        if(counter > 255) counter = 0;
        wait_us(100000);
    }
}
