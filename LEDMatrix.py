import RPi.GPIO as GPIO
#from tkinter import *
import Keypad
import wurf
import time_pr
import snake
import matrix
import temp
import matrix2
import random_dot
import snake_game
import random_dot2
import TR
import bin_hex
import GUI
import Karte

LSBFIRST = 1
MSBFIRST = 2
#define the pins connect to 74HC595
dataPin   = 11      #DS Pin of 74HC595(Pin14)
latchPin  = 13      #ST_CP Pin of 74HC595(Pin12)
clockPin = 15       #SH_CP Pin of 74HC595(Pin11)

ROWS = 4
COLS = 4
keys = 	['1','2','3','A',
	 '4','5','6','B',
	 '7','8','9','C',
	 '*','0','#','D']
rowsPins = [7,32,22,36]
colsPins = [19,18,16,12]	
Num = bool

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
        
def Numpad(jn):
    if jn == 'j':
        return True
    elif jn == 'n':
        return False

def loop():
    global inCmd
    print()
    inCmd = input('Numpad j/n : ')
    if Numpad(inCmd) == True:
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
        while True:
            keypad = Keypad.Keypad(keys,rowsPins,colsPins,ROWS,COLS)
            keypad.setDebounceTime(50)
            key = keypad.getKey()
            try:
                if (key == '1'):
                    wurf.zufall()
                elif (key == '2'):
                    print(time_pr.time_wert())
                    time_pr.Time()
                elif (key == '3'):
                    temp.cpu_temp()
                elif (key == '4'):
                    snake.snakeL()
                elif key == '5':
                    try:
                        snake_game.main()
                    except:
                        print('Spiel beendet.')
                        pass
                elif (key == '6'):
                    matrix.matrix()
                elif key == '7':
                    matrix2.matrixx()
                elif key == '8':
                    random_dot.Dot()
                elif key == '9':
                    random_dot2.main()
                elif key == '0':
                    Karte.main()
                elif key == 'A':
                    TR.main()
                elif key == 'B':
                    bin_hex.main()
                elif key == 'C':
                    GUI.main()
                    break
                elif key == '*':
                    destroy()
                    break
                elif (key == '#'):
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
            except:
                print('Ein Fehler ist aufgetreten!')
                pass
    elif Numpad(inCmd) == False:
        print("'quit' = beenden")
        print("'wurf' = wuerfeln (16-seitig)")
        print("'time' = Zeit anzeigen")
        print("'temp' = Display CPU-Temp")
        print("'snake'")
        print("'snake-game' ---- WIP -----")
        print("'matrix'")
        print("'matrix2'")
        print("'random' = random Punkt")
        print("'random2' = 'Bilschrimschoner'")
        print("'TR' = Taschenrechner ----WIP----")
        print("'bin_hex' = Dez-Bin-Hex-Rechner ----WIP----")
        print("'karte' = Karte ziehen")
        try:
            inCmd=input()
            if inCmd == "wurf":
                wurf.zufall()
            elif (inCmd == "time"):
                print(time_pr.time_wert())
                time_pr.Time()
            elif (inCmd == "snake"):
                snake.snakeL()
            elif (inCmd == "matrix"):
                matrix.matrix()
            elif (inCmd == 'temp'):
                temp.cpu_temp
            elif (inCmd == 'matrix2'):
                matrix2.matrixx
    ##        elif inCmd == 'snake-game':
    ##            snake_game.main()
            elif inCmd == 'random':
                random_dot.Dot()
            elif inCmd == 'random2':
                random_dot2.main()
##            elif inCmd == 'TR':
##                TR.main()
            elif inCmd == 'gui':
                GUI.main()
            elif inCmd == 'karte':
                Karte.main
            elif inCmd == 'quit':
                destroy()
            else: print('Befehl nicht erkannt')
        except:
            print('Ein Fehler ist aufgetreten!')
            pass

def destroy():   # When 'Ctrl+C' is pressed, the function is executed. 
    GPIO.cleanup()
    
if __name__ == '__main__': # Program starting from here 
    print ('Program is starting...' )
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()