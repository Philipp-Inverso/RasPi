import LEDMatrix
import RPi.GPIO as GPIO
import time
import random

LSBFIRST = 1
MSBFIRST = 2
#define the pins connect to 74HC595
dataPin   = 11      #DS Pin of 74HC595(Pin14)
latchPin  = 13      #ST_CP Pin of 74HC595(Pin12)
clockPin = 15       #SH_CP Pin of 74HC595(Pin11)

data0 = [0x00, 0x00, 0x3E, 0x41, 0x41, 0x3E, 0x00, 0x00] # "0"
data1 = [0x00, 0x00, 0x21, 0x7F, 0x01, 0x00, 0x00, 0x00] # "1"
data2 = [0x00, 0x00, 0x23, 0x45, 0x49, 0x31, 0x00, 0x00] # "2"
data3 = [0x00, 0x00, 0x22, 0x49, 0x49, 0x36, 0x00, 0x00] # "3"
data4 = [0x00, 0x00, 0x0E, 0x32, 0x7F, 0x02, 0x00, 0x00] # "4"
data5 = [0x00, 0x00, 0x79, 0x49, 0x49, 0x46, 0x00, 0x00] # "5"
data6 = [0x00, 0x00, 0x3E, 0x49, 0x49, 0x26, 0x00, 0x00] # "6"
data7 = [0x00, 0x00, 0x60, 0x47, 0x48, 0x70, 0x00, 0x00] # "7"
data8 = [0x00, 0x00, 0x36, 0x49, 0x49, 0x36, 0x00, 0x00] # "8"
data9 = [0x00, 0x00, 0x32, 0x49, 0x49, 0x3E, 0x00, 0x00] # "9"   
dataA = [0x00, 0x00, 0x3F, 0x44, 0x44, 0x3F, 0x00, 0x00] # "A"
dataB = [0x00, 0x00, 0x7F, 0x49, 0x49, 0x36, 0x00, 0x00] # "B"
dataD = [0x00, 0x00, 0x7F, 0x41, 0x41, 0x3E, 0x00, 0x00] # "D"
dataK = [0x00, 0, 0x7f, 0x08, 20, 34, 65, 0]
    
dataKreuz = [0, 28, 8, 73, 127, 73, 8, 28]
dataKaro  = [0, 8, 28, 62, 127, 62, 28, 8]
dataHerz  = [0, 24, 60, 62, 31, 62, 60, 24]
dataPik   = [0, 24, 60, 125, 255, 125, 60, 24]

    
def main():
    f = random.randint(0,3)
    if f == 0:
        Farbe = 'Kreuz'
    elif f == 1:
        Farbe = 'Karo'
    elif f == 2:
        Farbe = 'Pik'
    elif f == 3:
        Farbe = 'Herz'
    print(Farbe)
    Z = random.randint(2,14)
    if Z == 14:
        Zahl = 'ASS'
    elif Z == 13:
        Zahl = 'Koenig'
    elif Z == 12:
        Zahl = 'Dame'
    elif Z == 11:
        Zahl = 'Bube'
    else:
        Zahl = str(Z)
    print(Zahl)
    if Farbe == 'Kreuz':
        for j in range(0,100):
            x = 128
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,dataKreuz[i]) #first shift data of line information to first stage 74HC959
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif Farbe == 'Karo':
        for j in range(0,100):
            x = 128
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,dataKaro[i]) #first shift data of line information to first stage 74HC959
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif Farbe == 'Herz':
        for j in range(0,100):
            x = 128
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,dataHerz[i]) #first shift data of line information to first stage 74HC959
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif Farbe == 'Pik':
        for j in range(0,100):
            x = 128
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,dataPik[i]) #first shift data of line information to first stage 74HC959
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    
    if Zahl == '2':
        for j in range(0,100):
            x = 128
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,data2[i]) #first shift data of line information to first stage 74HC959
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif Zahl == '3':
        for j in range(0,100):
            x = 128
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,data3[i]) #first shift data of line information to first stage 74HC959
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif Zahl == '4':
        for j in range(0,100):
            x = 128
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,data4[i]) #first shift data of line information to first stage 74HC959
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif Zahl == '5':
        for j in range(0,100):
            x = 128
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,data5[i]) #first shift data of line information to first stage 74HC959
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif Zahl == '6':
        for j in range(0,100):
            x = 128
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,data6[i]) #first shift data of line information to first stage 74HC959
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif Zahl == '7':
        for j in range(0,100):
            x = 128
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,data7[i]) #first shift data of line information to first stage 74HC959
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif Zahl == '8':
        for j in range(0,100):
            x = 128
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,data8[i]) #first shift data of line information to first stage 74HC959
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif Zahl == '9':
        for j in range(0,100):
            x = 128
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,data9[i]) #first shift data of line information to first stage 74HC959
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif Zahl == '10':
        for j in range(0,100):
            x = 128
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,data1[i]) #first shift data of line information to first stage 74HC959
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
        for j in range(0,100):
            x = 128
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,data0[i]) #first shift data of line information to first stage 74HC959
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif Zahl == 'Bube':
        for j in range(0,100):
            x = 128
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,dataB[i]) #first shift data of line information to first stage 74HC959
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif Zahl == 'Dame':
        for j in range(0,100):
            x = 128
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,dataD[i]) #first shift data of line information to first stage 74HC959
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif Zahl == 'Koenig':
        for j in range(0,100):
            x = 128
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,dataK[i]) #first shift data of line information to first stage 74HC959
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
    elif Zahl == 'ASS':
        for j in range(0,100):
            x = 128
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,dataA[i]) #first shift data of line information to first stage 74HC959
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1