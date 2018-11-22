import RPi.GPIO as GPIO
import time
import random

LSBFIRST = 1
MSBFIRST = 2
#define the pins connect to 74HC595
dataPin   = 11      #DS Pin of 74HC595(Pin14)
latchPin  = 13      #ST_CP Pin of 74HC595(Pin12)
clockPin = 15       #SH_CP Pin of 74HC595(Pin11)

def setup():
    GPIO.setmode(GPIO.BOARD)    # Number GPIOs by its physical location
    GPIO.setup(dataPin, GPIO.OUT)
    GPIO.setup(latchPin, GPIO.OUT)
    GPIO.setup(clockPin, GPIO.OUT)
    
def shiftOut(dPin,cPin,order,val):
    for i in range(0,8):
        GPIO.output(cPin,GPIO.LOW);
        if(order == LSBFIRST):
           GPIO.output(dPin,(0x01&(val>>i)==0x01) and GPIO.HIGH or GPIO.LOW)
        elif(order == MSBFIRST):
            GPIO.output(dPin,(0x80&(val<<i)==0x80) and GPIO.HIGH or GPIO.LOW)
        GPIO.output(cPin,GPIO.HIGH);        

def main():
    for c in range(0,25):
        data = [0, 0, 0, 0, 0, 0, 0, 0]
        mode = random.randint(0,2)
        if mode == 0:
            zeile = random.randint(0,7)
            if zeile == 0:
                z1 = 1
            elif zeile == 1:
                z1 = 2
            elif zeile == 2:
                z1 = 4
            elif zeile == 3:
                z1 = 8
            elif zeile == 4:
                z1 = 16
            elif zeile == 5:
                z1 = 32
            elif zeile == 6:
                z1 = 64
            elif zeile == 7:
                z1 = 128
            data1 = [0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, z1, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0]
            for k in range(0,len(data1)-8):
                for j in range(0,5):# Repeat enough times to display the smiling face a period of time
                    x=0x01
                    for i in range(k,k+8):
                        GPIO.output(latchPin,GPIO.LOW)
                        shiftOut(dataPin,clockPin,MSBFIRST,data1[i]) #first shift data of line information to first stage 74HC959
                        shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                        GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                        time.sleep(0.001)# display the next column
                        x<<=1
        elif mode == 1:
            spalte = random.randint(0,7)
            p = 256
            data[spalte] = p
            while p >= 1:
                for j in range(0,5):# Repeat enough times to display the smiling face a period of time
                    x=0x80
                    for i in range(0,8):
                        GPIO.output(latchPin,GPIO.LOW)
                        shiftOut(dataPin,clockPin,MSBFIRST,data[i]) #first shift data of line information to first stage 74HC959
                        shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                        GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                        time.sleep(0.001)# display the next column
                        x>>=1
                p = p//2
                data[spalte] = p
        if mode == 2:
            dataD = [0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0]
            dir = random.randint(0,3)
            if dir == 0:
                a1 = random.randint(0,3)
                if a1 == 0:
                    z1d = 1
                elif a1 == 1:
                    z1d = 2
                elif a1 == 2:
                    z1d = 4
                elif a1 == 3:
                    z1d = 8
                a2 = random.randint(4,7)
                dataD[a2] = z1d
                while z1d < 128:
                    for k  in range(0,len(dataD)-8):
                        for j in range(0,5):# Repeat enough times to display the smiling face a period of time
                            x=0x01
                            for i in range(k,k+8):
                                GPIO.output(latchPin,GPIO.LOW)
                                shiftOut(dataPin,clockPin,MSBFIRST,dataD[i]) #first shift data of line information to first stage 74HC959
                                shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                                time.sleep(0.001)# display the next column
                                x<<=1
                        z1d = z1d * 2
                        dataD[a2] = z1d
            elif dir == 1:
                b1 = random.randint(0,3)
                if b1 == 0:
                    z2d = 1
                elif b1 == 1:
                    z2d = 2
                elif b1 == 2:
                    z2d = 4
                elif b1 == 3:
                    z2d = 8
                b2 = random.randint(4,7)
                dataD[b2] = z2d
                while z2d < 128:
                    for k  in range(0,len(dataD)-8):
                        for j in range(0,5):# Repeat enough times to display the smiling face a period of time
                            x=0x80
                            for i in range(k,k+8):
                                GPIO.output(latchPin,GPIO.LOW)
                                shiftOut(dataPin,clockPin,MSBFIRST,dataD[i]) #first shift data of line information to first stage 74HC959
                                shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                                time.sleep(0.001)# display the next column
                                x>>=1
                        z2d = z2d * 2
                        dataD[b2] = z2d
            elif dir == 2:
                c1 = random.randint(0,3)
                if c1 == 0:
                    z3d = 16
                elif c1 == 1:
                    z3d = 32
                elif c1 == 2:
                    z3d = 64
                elif c1 == 3:
                    z3d = 128
                c2 = random.randint(4,7)
                dataD[c2] = z3d
                while z3d >= 1:
                    for k  in range(0,len(dataD)-8):
                        for j in range(0,5):# Repeat enough times to display the smiling face a period of time
                            x=0x01
                            for i in range(k,k+8):
                                GPIO.output(latchPin,GPIO.LOW)
                                shiftOut(dataPin,clockPin,MSBFIRST,dataD[i]) #first shift data of line information to first stage 74HC959
                                shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                                time.sleep(0.001)# display the next column
                                x<<=1
                        z3d = z3d // 2
                        dataD[c2] = z3d
            elif dir == 3:
                d1 = random.randint(0,3)
                if d1 == 0:
                    z4d = 16
                elif d1 == 1:
                    z4d = 32
                elif d1 == 2:
                    z4d = 64
                elif d1 == 3:
                    z4d = 128
                d2 = random.randint(4,7)
                dataD[d2] = z4d
                while z4d >= 1:
                    for k  in range(0,len(dataD)-8):
                        for j in range(0,5):# Repeat enough times to display the smiling face a period of time
                            x=0x80
                            for i in range(k,k+8):
                                GPIO.output(latchPin,GPIO.LOW)
                                shiftOut(dataPin,clockPin,MSBFIRST,dataD[i]) #first shift data of line information to first stage 74HC959
                                shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                                time.sleep(0.001)# display the next column
                                x>>=1
                        z4d = z4d//2
                        dataD[d2] = z4d           

def destroy():   # When 'Ctrl+C' is pressed, the function is executed. 
    GPIO.cleanup()
    
if __name__ == '__main__': # Program starting from here 
    print ('Program is starting...' )
    setup() 
    try:
        main()
    except KeyboardInterrupt:
        destroy()