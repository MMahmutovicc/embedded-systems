#include "mbed.h"
DigitalOut led1(LED1);
int main() {
    double t = 1;
    double t1 = t, t2 = t,kt = 1.9 * t, step = (kt - t)/15;
    int counter = 0, limit = 32;
    bool increment = true;
    while (1) {
        if(counter == 0 && increment == false) increment = true;
        else if(counter == limit && increment == true) {
            increment = false;
            limit = 62;
            counter = limit;
        }
        else if(counter % 2 == 0 && counter != 0) {
            if(increment) {
                t1 += step;
                t2 -= step;
            }
            else {
                t1 -=step;
                t2 +=step;
            }
        }
        led1 = !led1;
        if(increment) counter++;
        else counter--;
        if(counter % 2 != 0) wait(t1);
        else wait(t2);
        printf("Brojac = %d, t1 = %f, t2 = %f\n",counter,t1,t2);
    }
}
