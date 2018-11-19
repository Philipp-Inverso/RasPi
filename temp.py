import LEDMatrix
import RPi.GPIO as GPIO
import Data
import Keypad
import time

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
dataT = []

def get_cpu_temp():     # get CPU temperature and store it into file "/sys/class/thermal/thermal_zone0/temp"
    tmp = open('/sys/class/thermal/thermal_zone0/temp')
    cpu = tmp.read()
    tmp.close()
    return '{:.2f}'.format( float(cpu)/1000 )

def cpu_temp():
    t = float(get_cpu_temp())
    time.sleep(0.01)
    tempC = str(t) + ' C'
    time.sleep(0.01)
    tempF = str(t * 9/5 + 32) + ' F'
    time.sleep(0.01)
    tempK = str('{:.2f}'.format(t + 273.15)) + ' K'
    time.sleep(0.01)
    print('1 = Grad Celsius')
    print('2 = Grad Fahrenheit')
    print('3 = Kelvin')
    if LEDMatrix.Num:
        while True:
            keypad = Keypad.Keypad(keys,rowsPins,colsPins,ROWS,COLS)
            keypad.setDebounceTime(50)
            key = keypad.getKey()
            if key == '1':
                dataT.clear()
                if tempC[0] == '1':
                    dataT.append(Data.data1)
                elif tempC[0] == '2':
                    dataT.append(Data.data2)
                elif tempC[0] == '3':
                    dataT.append(Data.data3)
                elif tempC[0] == '4':
                    dataT.append(Data.data4)
                elif tempC[0] == '5':
                    dataT.append(Data.data5)
                elif tempC[0] == '6':
                    dataT.append(Data.data6)
                elif tempC[0] == '7':
                    dataT.append(Data.data7)
                elif tempC[0] == '8':
                    dataT.append(Data.data8)
                elif tempC[0] == '9':
                    dataT.append(Data.data9)
                elif tempC[0] == '0':
                    dataT.append(Data.data0)
                time.sleep(0.1)
                if tempC[1] == '1':
                    dataT.append(Data.data1)
                elif tempC[1] == '2':
                    dataT.append(Data.data2)
                elif tempC[1] == '3':
                    dataT.append(Data.data3)
                elif tempC[1] == '4':
                    dataT.append(Data.data4)
                elif tempC[1] == '5':
                    dataT.append(Data.data5)
                elif tempC[1] == '6':
                    dataT.append(Data.data6)
                elif tempC[1] == '7':
                    dataT.append(Data.data7)
                elif tempC[1] == '8':
                    dataT.append(Data.data8)
                elif tempC[1] == '9':
                    dataT.append(Data.data9)
                elif tempC[1] == '0':
                    dataT.append(Data.data0)
                dataT.append(Data.dataDot)
                time.sleep(0.1)
                if tempC[3] == '1':
                    dataT.append(Data.data1)
                elif tempC[3] == '2':
                    dataT.append(Data.data2)
                elif tempC[3] == '3':
                    dataT.append(Data.data3)
                elif tempC[3] == '4':
                    dataT.append(Data.data4)
                elif tempC[3] == '5':
                    dataT.append(Data.data5)
                elif tempC[3] == '6':
                    dataT.append(Data.data6)
                elif tempC[3] == '7':
                    dataT.append(Data.data7)
                elif tempC[3] == '8':
                    dataT.append(Data.data8)
                elif tempC[3] == '9':
                    dataT.append(Data.data9)
                elif tempC[3] == '0':
                    dataT.append(Data.data0)
                time.sleep(0.1)
                if tempC[4] == '1':
                    dataT.append(Data.data1)
                elif tempC[4] == '2':
                    dataT.append(Data.data2)
                elif tempC[4] == '3':
                    dataT.append(Data.data3)
                elif tempC[4] == '4':
                    dataT.append(Data.data4)
                elif tempC[4] == '5':
                    dataT.append(Data.data5)
                elif tempC[4] == '6':
                    dataT.append(Data.data6)
                elif tempC[4] == '7':
                    dataT.append(Data.data7)
                elif tempC[4] == '8':
                    dataT.append(Data.data8)
                elif tempC[4] == '9':
                    dataT.append(Data.data9)
                elif tempC[4] == '0':
                    dataT.append(Data.data0)
                dataT.append(Data.dataDeg)
                dataT.append(Data.dataC) 
                time.sleep(1)
                for m in range(0,7):
                    for k in range(0,len(dataT[m])-8):
                        for j in range(0,5):
                            x = 0x80
                            for i in range(k,k+8):
                                GPIO.output(latchPin,GPIO.LOW)
                                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,dataT[m][i]) #first shift data of line information to first stage 74HC959   
                                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                                time.sleep(0.001)# display the next column
                                x>>=1
                break
            elif key == '2':
                dataT.clear()
                if tempF[0] == '1':
                    dataT.append(Data.data1)
                elif tempF[0] == '2':
                    dataT.append(Data.data2)
                elif tempF[0] == '3':
                    dataT.append(Data.data3)
                elif tempF[0] == '4':
                    dataT.append(Data.data4)
                elif tempF[0] == '5':
                    dataT.append(Data.data5)
                elif tempF[0] == '6':
                    dataT.append(Data.data6)
                elif tempF[0] == '7':
                    dataT.append(Data.data7)
                elif tempF[0] == '8':
                    dataT.append(Data.data8)
                elif tempF[0] == '9':
                    dataT.append(Data.data9)
                elif tempF[0] == '0':
                    dataT.append(Data.data0)
                time.sleep(0.1)
                if tempF[1] == '1':
                    dataT.append(Data.data1)
                elif tempF[1] == '2':
                    dataT.append(Data.data2)
                elif tempF[1] == '3':
                    dataT.append(Data.data3)
                elif tempF[1] == '4':
                    dataT.append(Data.data4)
                elif tempF[1] == '5':
                    dataT.append(Data.data5)
                elif tempF[1] == '6':
                    dataT.append(Data.data6)
                elif tempF[1] == '7':
                    dataT.append(Data.data7)
                elif tempF[1] == '8':
                    dataT.append(Data.data8)
                elif tempF[1] == '9':
                    dataT.append(Data.data9)
                elif tempF[1] == '0':
                    dataT.append(Data.data0)
                time.sleep(0.1)
                if tempF[2] == '1':
                    dataT.append(Data.data1)
                elif tempF[2] == '2':
                    dataT.append(Data.data2)
                elif tempF[2] == '3':
                    dataT.append(Data.data3)
                elif tempF[2] == '4':
                    dataT.append(Data.data4)
                elif tempF[2] == '5':
                    dataT.append(Data.data5)
                elif tempF[2] == '6':
                    dataT.append(Data.data6)
                elif tempF[2] == '7':
                    dataT.append(Data.data7)
                elif tempF[2] == '8':
                    dataT.append(Data.data8)
                elif tempF[2] == '9':
                    dataT.append(Data.data9)
                elif tempF[2] == '0':
                    dataT.append(Data.data0)
                dataT.append(Data.dataDot)
                time.sleep(0.1)
                if tempF[4] == '1':
                    dataT.append(Data.data1)
                elif tempF[4] == '2':
                    dataT.append(Data.data2)
                elif tempF[4] == '3':
                    dataT.append(Data.data3)
                elif tempF[4] == '4':
                    dataT.append(Data.data4)
                elif tempF[4] == '5':
                    dataT.append(Data.data5)
                elif tempF[4] == '6':
                    dataT.append(Data.data6)
                elif tempF[4] == '7':
                    dataT.append(Data.data7)
                elif tempF[4] == '8':
                    dataT.append(Data.data8)
                elif tempF[4] == '9':
                    dataT.append(Data.data9)
                elif tempF[4] == '0':
                    dataT.append(Data.data0)
                time.sleep(0.1)
                if tempF[5] == '1':
                    dataT.append(Data.data1)
                elif tempF[5] == '2':
                    dataT.append(Data.data2)
                elif tempF[5] == '3':
                    dataT.append(Data.data3)
                elif tempF[5] == '4':
                    dataT.append(Data.data4)
                elif tempF[5] == '5':
                    dataT.append(Data.data5)
                elif tempF[5] == '6':
                    dataT.append(Data.data6)
                elif tempF[5] == '7':
                    dataT.append(Data.data7)
                elif tempF[5] == '8':
                    dataT.append(Data.data8)
                elif tempF[5] == '9':
                    dataT.append(Data.data9)
                elif tempF[5] == '0':
                    dataT.append(Data.data0)
                dataT.append(Data.dataDeg)
                dataT.append(Data.dataF) 
                time.sleep(1)
                for m in range(0,8):
                    for k in range(0,len(dataT[m])-8):
                        for j in range(0,5):
                            x = 0x80
                            for i in range(k,k+8):
                                GPIO.output(latchPin,GPIO.LOW)
                                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,dataT[m][i]) #first shift data of line information to first stage 74HC959   
                                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                                time.sleep(0.001)# display the next column
                                x>>=1
                break
            elif key == '3':
                dataT.clear()
                if tempK[0] == '1':
                    dataT.append(Data.data1)
                elif tempK[0] == '2':
                    dataT.append(Data.data2)
                elif tempK[0] == '3':
                    dataT.append(Data.data3)
                elif tempK[0] == '4':
                    dataT.append(Data.data4)
                elif tempK[0] == '5':
                    dataT.append(Data.data5)
                elif tempK[0] == '6':
                    dataT.append(Data.data6)
                elif tempK[0] == '7':
                    dataT.append(Data.data7)
                elif tempK[0] == '8':
                    dataT.append(Data.data8)
                elif tempK[0] == '9':
                    dataT.append(Data.data9)
                elif tempK[0] == '0':
                    dataT.append(Data.data0)
                time.sleep(0.1)
                if tempK[1] == '1':
                    dataT.append(Data.data1)
                elif tempK[1] == '2':
                    dataT.append(Data.data2)
                elif tempK[1] == '3':
                    dataT.append(Data.data3)
                elif tempK[1] == '4':
                    dataT.append(Data.data4)
                elif tempK[1] == '5':
                    dataT.append(Data.data5)
                elif tempK[1] == '6':
                    dataT.append(Data.data6)
                elif tempK[1] == '7':
                    dataT.append(Data.data7)
                elif tempK[1] == '8':
                    dataT.append(Data.data8)
                elif tempK[1] == '9':
                    dataT.append(Data.data9)
                elif tempK[1] == '0':
                    dataT.append(Data.data0)
                time.sleep(0.1)
                if tempF[2] == '1':
                    dataT.append(Data.data1)
                elif tempF[2] == '2':
                    dataT.append(Data.data2)
                elif tempF[2] == '3':
                    dataT.append(Data.data3)
                elif tempF[2] == '4':
                    dataT.append(Data.data4)
                elif tempF[2] == '5':
                    dataT.append(Data.data5)
                elif tempF[2] == '6':
                    dataT.append(Data.data6)
                elif tempF[2] == '7':
                    dataT.append(Data.data7)
                elif tempF[2] == '8':
                    dataT.append(Data.data8)
                elif tempF[2] == '9':
                    dataT.append(Data.data9)
                elif tempF[2] == '0':
                    dataT.append(Data.data0)
                dataT.append(Data.dataDot)
                time.sleep(0.1)
                if tempK[4] == '1':
                    dataT.append(Data.data1)
                elif tempK[4] == '2':
                    dataT.append(Data.data2)
                elif tempK[4] == '3':
                    dataT.append(Data.data3)
                elif tempK[4] == '4':
                    dataT.append(Data.data4)
                elif tempK[4] == '5':
                    dataT.append(Data.data5)
                elif tempK[4] == '6':
                    dataT.append(Data.data6)
                elif tempK[4] == '7':
                    dataT.append(Data.data7)
                elif tempK[4] == '8':
                    dataT.append(Data.data8)
                elif tempK[4] == '9':
                    dataT.append(Data.data9)
                elif tempK[4] == '0':
                    dataT.append(Data.data0)
                time.sleep(0.1)
                if tempK[5] == '1':
                    dataT.append(Data.data1)
                elif tempK[5] == '2':
                    dataT.append(Data.data2)
                elif tempK[5] == '3':
                    dataT.append(Data.data3)
                elif tempK[5] == '4':
                    dataT.append(Data.data4)
                elif tempK[5] == '5':
                    dataT.append(Data.data5)
                elif tempK[5] == '6':
                    dataT.append(Data.data6)
                elif tempK[5] == '7':
                    dataT.append(Data.data7)
                elif tempK[5] == '8':
                    dataT.append(Data.data8)
                elif tempK[5] == '9':
                    dataT.append(Data.data9)
                elif tempK[5] == '0':
                    dataT.append(Data.data0)
                dataT.append(Data.dataDeg)
                dataT.append(Data.dataK)
                time.sleep(1)
                for m in range(0,8):
                    for k in range(0,len(dataT[m])-8):
                        for j in range(0,5):
                            x = 0x80
                            for i in range(k,k+8):
                                GPIO.output(latchPin,GPIO.LOW)
                                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,dataT[m][i]) #first shift data of line information to first stage 74HC959   
                                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                                time.sleep(0.001)# display the next column
                                x>>=1
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
                break
