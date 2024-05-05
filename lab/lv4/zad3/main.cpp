#include "mbed.h"  
#include "lpc1114etf.h"

BusOut leds(LED0, LED1, LED2, LED3, LED4, LED5, LED6, LED7);  
AnalogIn adc (dp9);  
DigitalOut e(LED_ACT); 

int main() {
    e = 0;
    while (1) {
        if(adc < 1./9) leds = 255;
        else if (adc > 1./9 && adc < 2 * 1./9) leds = 127;
        else if (adc >= 2 * 1./9 && adc < 3 * 1./9) leds = 63;
        else if (adc >= 3 * 1./9 && adc < 4 * 1./9) leds = 31;
        else if (adc >= 4 * 1./9 && adc < 5 * 1./9) leds = 15;
        else if (adc >= 5 * 1./9 && adc < 6 * 1./9) leds = 7;
        else if (adc >= 6 * 1./9 && adc < 7 * 1./9) leds = 3;
        else if (adc >= 7 * 1./9 && adc < 8 * 1./9) leds = 1;
        else leds = 0;
        wait_us(10);
    }
}
