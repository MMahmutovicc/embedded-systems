#include "mbed.h"

PwmOut signal(p5);
DigitalIn input(p6);
BusOut d1(LED1,LED2,LED3,LED4);
BusOut d2(p7,p8,p9,p10);

int main() {
    int digit1 = 0, digit2 = 0, oldInput = input;
    signal.period_ms(2);
    while (1) {
        signal = 1;
        wait_ms(1);
        signal = 0;
        wait_ms(1);
        if(input == 1 && oldInput == 0) {
            digit1++;
            if(digit1 == 10) {
                digit2++;
                digit1 = 0;
                if(digit2 == 10)
                    digit2 = 0;
            }
            oldInput = 1;
        }
        if(input == 0 && oldInput == 1)
            oldInput = 0;
        d1 = digit1;
        d2 = digit2;
    }
}
