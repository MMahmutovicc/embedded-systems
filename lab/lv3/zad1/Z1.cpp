#include "mbed.h"
#include "lpc1114etf.h"

BusOut leds (LED0,LED1,LED2,LED3,LED4,LED5,LED6,LED7);
DigitalOut E(LED_ACT);
BusOut rows(dp18,dp17,dp15,dp16);
BusIn cols(dp9,dp10,dp11,dp13);

char keys[16] = {'1','2','3','A',
                '4','5','6','B',
                '7','8','9','C',
                '*','0','#','D'};

char keyInput(){
    for(int i=0;i<4;i++){
        rows=pow(2,i);
        int col=cols;
        if(col==1) return keys[i*4 + 0];
        else if(col==2) return keys[i*4 + 1];
        else if(col==4) return keys[i*4 + 2];
        else if(col==8) return keys[i*4 + 3];
    }
    return 0;
}

int main(){
    E=0;
    leds=0;
    while (true){
        char n=keyInput();
        if(n>'0' && n<'9'){
            leds[n-49]=1;
            while(cols>0){
                thread_sleep_for(100);
            }
        }
        else if(n=='C'){
            leds=0;
            while(cols>0){
                thread_sleep_for(100);
            }
        }
        thread_sleep_for(100);
    }
}
