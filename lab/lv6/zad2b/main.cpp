#include "mbed.h"

DigitalOut signal(p5);
Ticker t;
InterruptIn input(p6);
BusOut d1(LED1,LED2,LED3,LED4);
BusOut d2(p7,p8,p9,p10);
int digit1 = 0, digit2 = 0;
void increment() {
    digit1++;
    if(digit1 == 10) {
        digit2++;
        digit1 = 0;
        if(digit2 == 10)
            digit2 = 0;
    }
    d1 = digit1;
    d2 = digit2;
}
void toggle() {
    signal = !signal;
}
int main() {
    input.rise(&increment);
    t.attach(&toggle,0.01);
    while (1) {
        wait_ms(20);
    }
}
