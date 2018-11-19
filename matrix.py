import LEDMatrix
import RPi.GPIO as GPIO
import Data
import time
import random

LSBFIRST = 1
MSBFIRST = 2
#define the pins connect to 74HC595
dataPin   = 11      #DS Pin of 74HC595(Pin14)
latchPin  = 13      #ST_CP Pin of 74HC595(Pin12)
clockPin = 15       #SH_CP Pin of 74HC595(Pin11)
data = [Data.data0, Data.data1]

def matrix():
    for c in range(0,8):
        r=random.randint(0,1)
        for k in range(0,len(data[r])-8):
            for j in range(0,5):# Repeat enough times to display the smiling face a period of time
                x=0x80
                for i in range(k,k+8):
                    GPIO.output(latchPin,GPIO.LOW)
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,data[r][i]) #first shift data of line information to first stage 74HC959
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                    GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                    time.sleep(0.001)# display the next column
                    x>>=1