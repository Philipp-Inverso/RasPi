import LEDMatrix
import RPi.GPIO as GPIO, time
import random

LSBFIRST = 1
MSBFIRST = 2
#define the pins connect to 74HC595
dataPin   = 11      #DS Pin of 74HC595(Pin14)
latchPin  = 13      #ST_CP Pin of 74HC595(Pin12)
clockPin = 15       #SH_CP Pin of 74HC595(Pin11)

def Dot():
    for c in range(0,100):
        z = random.randint(0,7)
        s = random.randint(0,7)
        if z == 0:
            pos = 128
        elif z == 1:
            pos = 64
        elif z == 2:
            pos = 32
        elif z == 3:
            pos = 16
        elif z == 4:
            pos = 8
        elif z == 5:
            pos = 4
        elif z == 6:
            pos = 2
        elif z == 7:
            pos = 1
        data = [0, 0, 0, 0, 0, 0, 0, 0]
        data[s] = pos
        data[not s] = 0
        for j in range(0,15):
            x = 0x80
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,data[i]) #first shift data of line information to first stage 74HC959   
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1