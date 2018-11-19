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
data0 = [ 0x00, 0x00, 0x3E, 0x41, 0x41, 0x3E, 0x00, 0x00]
data1 = [	0x00, 0x00, 0x21, 0x7F, 0x01, 0x00, 0x00, 0x00]
data2 = [ 0x00, 0x00, 0x23, 0x45, 0x49, 0x31, 0x00, 0x00]
data3 = [ 0x00, 0x00, 0x22, 0x49, 0x49, 0x36, 0x00, 0x00]
data4 = [ 0x00, 0x00, 0x0E, 0x32, 0x7F, 0x02, 0x00, 0x00]
data5 = [ 0x00, 0x00, 0x79, 0x49, 0x49, 0x46, 0x00, 0x00]
data6 = [ 0x00, 0x00, 0x3E, 0x49, 0x49, 0x26, 0x00, 0x00]
data7 = [ 0x00, 0x00, 0x60, 0x47, 0x48, 0x70, 0x00, 0x00]
data8 = [ 0x00, 0x00, 0x36, 0x49, 0x49, 0x36, 0x00, 0x00]
data9 = [ 0x00, 0x00, 0x32, 0x49, 0x49, 0x3E, 0x00, 0x00]
dataA = [ 0x00, 0x00, 0x3F, 0x44, 0x44, 0x3F, 0x00, 0x00]
dataB = [ 0x00, 0x00, 0x7F, 0x49, 0x49, 0x36, 0x00, 0x00]
dataC = [ 0x00, 0x00, 0x3E, 0x41, 0x41, 0x22, 0x00, 0x00]
dataD = [ 0x00, 0x00, 0x7F, 0x41, 0x41, 0x3E, 0x00, 0x00]
dataE = [ 0x00, 0x00, 0x7F, 0x49, 0x49, 0x41, 0x00, 0x00]
dataF = [ 0x00, 0x00, 0x7F, 0x48, 0x48, 0x40, 0x00, 0x00]

def zufall():
    for k in range(0,len(Data.data)-8):#len(data) total number of "0-F" columns 
        for j in range(0,5):# times of repeated displaying LEDMatrix in every frame, the bigger the "j", the longer the display time.
            x=0x80      # Set the column information to start from the first column
            for i in range(k,k+8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,Data.data[i])
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x)
                GPIO.output(latchPin,GPIO.HIGH)
                time.sleep(0.001)
                x>>=1
    zahl=random.randint(0,15)
    if zahl == 0:
        for j in range(0,20):# Repeat enough times to display the smiling face a period of time
            x=0x80
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,data0[i]) #first shift data of line information to first stage 74HC959
                        
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif zahl == 1:
        for j in range(0,500):# Repeat enough times to display the smiling face a period of time
            x=0x80
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,data1[i]) #first shift data of line information to first stage 74HC959

                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif zahl == 2:
        for j in range(0,500):# Repeat enough times to display the smiling face a period of time
            x=0x80
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,data2[i]) #first shift data of line information to first stage 74HC959

                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif zahl == 3:
        for j in range(0,500):# Repeat enough times to display the smiling face a period of time
            x=0x80
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,data3[i]) #first shift data of line information to first stage 74HC959

                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif zahl == 4:
        for j in range(0,500):# Repeat enough times to display the smiling face a period of time
            x=0x80
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,data4[i]) #first shift data of line information to first stage 74HC959

                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif zahl == 5:
        for j in range(0,500):# Repeat enough times to display the smiling face a period of time
            x=0x80
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,data5[i]) #first shift data of line information to first stage 74HC959

                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif zahl == 6:
        for j in range(0,500):# Repeat enough times to display the smiling face a period of time
            x=0x80
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,data6[i]) #first shift data of line information to first stage 74HC959

                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif zahl == 7:
        for j in range(0,500):# Repeat enough times to display the smiling face a period of time
            x=0x80
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,data7[i]) #first shift data of line information to first stage 74HC959

                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif zahl == 8:
        for j in range(0,500):# Repeat enough times to display the smiling face a period of time
            x=0x80
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,data8[i]) #first shift data of line information to first stage 74HC959

                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif zahl == 9:
        for j in range(0,500):# Repeat enough times to display the smiling face a period of time
            x=0x80
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,data9[i]) #first shift data of line information to first stage 74HC959

                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif zahl == 10:
        for j in range(0,500):# Repeat enough times to display the smiling face a period of time
            x=0x80
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,dataA[i]) #first shift data of line information to first stage 74HC959

                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif zahl == 11:
        for j in range(0,500):# Repeat enough times to display the smiling face a period of time
            x=0x80
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,dataB[i]) #first shift data of line information to first stage 74HC959

                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif zahl == 12:
        for j in range(0,500):# Repeat enough times to display the smiling face a period of time
             x=0x80
             for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,dataC[i]) #first shift data of line information to first stage 74HC959

                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif zahl == 13:
        for j in range(0,500):# Repeat enough times to display the smiling face a period of time
            x=0x80
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,dataD[i]) #first shift data of line information to first stage 74HC959

                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif zahl == 14:
        for j in range(0,500):# Repeat enough times to display the smiling face a period of time
            x=0x80
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,dataE[i]) #first shift data of line information to first stage 74HC959

                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif zahl == 15:
        for j in range(0,500):# Repeat enough times to display the smiling face a period of time
            x=0x80
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,dataF[i]) #first shift data of line information to first stage 74HC959

                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1