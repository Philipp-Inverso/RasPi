import LEDMatrix
import RPi.GPIO as GPIO
import time

LSBFIRST = 1
MSBFIRST = 2
#define the pins connect to 74HC595
dataPin   = 11      #DS Pin of 74HC595(Pin14)
latchPin  = 13      #ST_CP Pin of 74HC595(Pin12)
clockPin = 15       #SH_CP Pin of 74HC595(Pin11)
datal = [ 0x00 ,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
zeile1 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
zeile2 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
zeile3 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x20, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
zeile4 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x10,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
zeile5 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
zeile6 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
zeile7 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
zeile8 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
snake = [zeile1,zeile2,zeile3,zeile4,zeile5,zeile6,zeile7,zeile8]

def snakeL():
    for c in range (0,5):
        print(5-c)
        for h in range(0,7,2):
            for k in range(0,len(snake[h])-8):
                for j in range(0,5):# Repeat enough times to display the smiling face a period of time
                    x=0x01
                    for i in range(k,k+8):
                        GPIO.output(latchPin,GPIO.LOW)
                        LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,snake[h][i]) #first shift data of line information to first stage 74HC959
                    
                        LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                        GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                        time.sleep(0.001)# display the next column
                        x<<=1
            for k in range(0,len(snake[h+1])-8):
                for j in range(0,5):# Repeat enough times to display the smiling face a period of time
                    x=0x80 #x=0x80
                    for i in range(k,k+8):
                            GPIO.output(latchPin,GPIO.LOW)
                            LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,snake[h+1][i]) #first shift data of line information to first stage 74HC959
                   
                            LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                            GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                            time.sleep(0.001)# display the next column
                            x>>=1
    print(0)
    print()
    print()
    if LEDMatrix.Num:
        print("# = Diese Liste")
        print("* = beenden")
        print("A = Taschenrechner")
        print("B = Dez-Bin-Hex-Rechner")
        print("C = GUI")
        print("1 = wuerfeln (16-seitig)")
        print("2 = Zeit anzeigen")
        print("3 = Display CPU-Temp")
        print("4 = 'snake'")
        print("5 = 'snake-game'")
        print("6 = 'matrix'")
        print("7 = matrix2'")
        print("8 = random Punkt")
        print("9 = 'Bislschirmschoner'")
        print("0 = Karte ziehen")
