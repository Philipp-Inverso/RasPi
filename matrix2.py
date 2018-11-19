import LEDMatrix         #ca 1400 zeilen
import RPi.GPIO as GPIO
import time
import random

LSBFIRST = 1
MSBFIRST = 2
#define the pins connect to 74HC595
dataPin   = 11      #DS Pin of 74HC595(Pin14)
latchPin  = 13      #ST_CP Pin of 74HC595(Pin12)
clockPin = 15       #SH_CP Pin of 74HC595(Pin11)

def randomize():
    global pos1, pos2, pos3, pos4, l1, l2, l3, l4
    anz = random.randint(1,4)
    if anz == 1:
            pos1 = random.randint(0,7)
            pos2 = 0
            pos3 = 0
            pos4 = 0
            l2 = 0
            l3 = 0
            l4 = 0
            laenge = random.randint(1,6)
            if laenge == 1:
                l1 = 2 * 128
            elif laenge == 2:
                l1 = 24 * 128
            elif laenge == 3:
                l1 = 112 * 128
            elif laenge == 4:
                l1 = 140 * 128
            elif laenge == 5:
                l1 = 31 * 128
            elif laenge == 6:
                l1 = 126 * 128
    elif anz == 2:
            pos1 = random.randint(0,7)
            pos2 = random.randint(0,7)
            pos3 = 0
            pos4 = 0
            l3 = 0
            l4 = 0
            laenge = random.randint(1,6)
            if laenge == 1:
                l1 = 2 * 128
            elif laenge == 2:
                l1 = 24 * 128
            elif laenge == 3:
                l1 = 112 * 128
            elif laenge == 4:
                l1 = 140 * 128
            elif laenge == 5:
                l1 = 31 * 128
            elif laenge == 6:
                l1 = 126 * 128
            laenge = random.randint(1,6)
            if laenge == 1:
                l2 = 2 * 128
            elif laenge == 2:
                l2 = 24 * 128
            elif laenge == 3:
                l2 = 112 * 128
            elif laenge == 4:
                l2 = 140 * 128
            elif laenge == 5:
                l2 = 31 * 128
            elif laenge == 6:
                l2 = 126 * 128
    elif anz == 3:
            pos1 = random.randint(0,7)
            pos2 = random.randint(0,7)
            pos3 = random.randint(0,7)
            pos4 = 0
            l4 = 0
            laenge = random.randint(1,6)
            if laenge == 1:
                l1 = 2 * 128
            elif laenge == 2:
                l1 = 24 * 128
            elif laenge == 3:
                l1 = 112 * 128
            elif laenge == 4:
                l1 = 140 * 128
            elif laenge == 5:
                l1 = 31 * 128
            elif laenge == 6:
                l1 = 126 * 128
            laenge = random.randint(1,6)
            if laenge == 1:
                l2 = 2  * 128
            elif laenge == 2:
                l2 = 24  * 128
            elif laenge == 3:
                l2 = 112  * 128
            elif laenge == 4:
                l2 = 140  * 128
            elif laenge == 5:
                l2 = 31  * 128
            elif laenge == 6:
                l2 = 126  * 128
            laenge = random.randint(1,6)
            if laenge == 1:
                l3 = 2  * 128
            elif laenge == 2:
                l3 = 24  * 128
            elif laenge == 3:
                l3 = 112  * 128
            elif laenge == 4:
                l3 = 140  * 128
            elif laenge == 5:
                l3 = 31  * 128
            elif laenge == 6:
                l3 = 126  * 128
    elif anz == 4:
            pos1 = random.randint(0,7)
            pos2 = random.randint(0,7)
            pos3 = random.randint(0,7)
            pos4 = random.randint(0,7)
            laenge = random.randint(1,6)
            if laenge == 1:
                l1 = 2 * 128
            elif laenge == 2:
                l1 = 24 * 128
            elif laenge == 3:
                l1 = 112 * 128
            elif laenge == 4:
                l1 = 140 * 128
            elif laenge == 5:
                l1 = 31 * 128
            elif laenge == 6:
                l1 = 126 * 128
            laenge = random.randint(1,6)
            if laenge == 1:
                l2 = 2 * 128 
            elif laenge == 2:
                l2 = 24 * 128
            elif laenge == 3:
                l2 = 112 * 128
            elif laenge == 4:
                l2 = 140 * 128
            elif laenge == 5:
                l2 = 31 * 128
            elif laenge == 6:
                l2 = 126 * 128
            laenge = random.randint(1,6)
            if laenge == 1:
                l3 = 2 * 128
            elif laenge == 2:
                l3 = 24 * 128
            elif laenge == 3:
                l3 = 112 * 128
            elif laenge == 4:
                l3 = 140 * 128
            elif laenge == 5:
                l3 = 31 * 128
            elif laenge == 6:
                l3 = 126 * 128
            laenge = random.randint(1,6)
            if laenge == 1:
                l4 = 2 * 128
            elif laenge == 2:
                l4 = 24 * 128
            elif laenge == 3:
                l4 = 112 * 128
            elif laenge == 4:
                l4 = 140 * 128
            elif laenge == 5:
                l4 = 31 * 128
            elif laenge == 6:
                l4 = 126 * 128
    
def posi():
    global l1, l2, l3, l4
    l1 = l1/2
    l2 = l2/2
    l3 = l3/2
    l4 = l4/2
    
def matrixx():
    global pos1, pos2, pos3, pos4, l1, l2, l3, l4, data
    data = [0, 0, 0, 0, 0, 0, 0, 0]
    data.clear()
    for z in range(0,100):
        data = [0, 0, 0, 0, 0, 0, 0, 0]
        randomize()
        for l in range(0,15):
            data[pos1] = l1
            data[pos2] = l2
            data[pos3] = l3
            data[pos4] = l4
            #data[not pos] = 0
            for j in range(0,2):
                x = 0x01
                for i in range(0,8):
                    GPIO.output(latchPin,GPIO.LOW)
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,int(data[i])) #first shift data of line information to first stage 74HC959   
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                    GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                    time.sleep(0.001)# display the next column
                    x<<=1
            posi()