import LEDMatrix
import RPi.GPIO as GPIO
import Data
import time
import random
from datetime import datetime

LSBFIRST = 1
MSBFIRST = 2
#define the pins connect to 74HC595
dataPin   = 11      #DS Pin of 74HC595(Pin14)
latchPin  = 13      #ST_CP Pin of 74HC595(Pin12)
clockPin = 15       #SH_CP Pin of 74HC595(Pin11)
dataDay = []
dataDate = []
dataTime = []

def time_wert():
    return datetime.now().strftime('%a:%d.%m.%y %H:%M:%S ')

def Time():
    dataDay.clear()
    if time_wert()[0:3] == 'Mon':
        dataDay.append(Data.dataM)
        dataDay.append(Data.dataO)
        dataDay.append(Data.dataN)
        dataDay.append(Data.dataColon)
    elif time_wert()[0:3] == 'Tue':
        dataDay.append(Data.dataT)
        dataDay.append(Data.dataU)
        dataDay.append(Data.dataE)
        dataDay.append(Data.dataColon)
    elif time_wert()[0:3] == 'Wed':
        dataDay.append(Data.dataW)
        dataDay.append(Data.dataE)
        dataDay.append(Data.dataD)
        dataDay.append(Data.dataColon)
    elif time_wert()[0:3] == 'Thu':
        dataDay.append(Data.dataT)
        dataDay.append(Data.dataH)
        dataDay.append(Data.dataU)
        dataDay.append(Data.dataColon)
    elif time_wert()[0:3] == 'Fri':
        dataDay.append(Data.dataF)
        dataDay.append(Data.dataR)
        dataDay.append(Data.dataI)
        dataDay.append(Data.dataColon)
    elif time_wert()[0:3] == 'Sat':
        dataDay.append(Data.dataS)
        dataDay.append(Data.dataA)
        dataDay.append(Data.dataT)
        dataDay.append(Data.dataColon)
    elif time_wert()[0:3] != 'Sun':
        dataDay.append(Data.dataS)
        dataDay.append(Data.dataU)
        dataDay.append(Data.dataN) 
        dataDay.append(Data.dataColon)
    dataDate.clear()   
    if time_wert()[4] == '1':   #Tag
        dataDate.append(Data.data1)
    elif time_wert()[4] == '2':
        dataDate.append(Data.data2)
    elif time_wert()[4] == '3':
        dataDate.append(Data.data3)
    elif time_wert()[4] == '4':
        dataDate.append(Data.data4)
    elif time_wert()[4] == '5':
        dataDate.append(Data.data5)
    elif time_wert()[4] == '6':
        dataDate.append(Data.data6)
    elif time_wert()[4] == '7':
        dataDate.append(Data.data7)
    elif time_wert()[4] == '8':
        dataDate.append(Data.data8)
    elif time_wert()[4] == '9':
        dataDate.append(Data.data9)
    elif time_wert()[4] == '0':
        dataDate.append(Data.data0)
    if time_wert()[5] == '1':
        dataDate.append(Data.data1)
    elif time_wert()[5] == '2':
        dataDate.append(Data.data2)
    elif time_wert()[5] == '3':
        dataDate.append(Data.data3)
    elif time_wert()[5] == '4':
        dataDate.append(Data.data4)
    elif time_wert()[5] == '5':
        dataDate.append(Data.data5)
    elif time_wert()[5] == '6':
        dataDate.append(Data.data6)
    elif time_wert()[5] == '7':
        dataDate.append(Data.data7)
    elif time_wert()[5] == '8':
        dataDate.append(Data.data8)
    elif time_wert()[5] == '9':
        dataDate.append(Data.data9)
    elif time_wert()[5] == '0':
        dataDate.append(Data.data0)
    dataDate.append(Data.dataDot)
    if time_wert()[7] == '1':    #Monat
        dataDate.append(Data.data1)
    elif time_wert()[7] == '2':
        dataDate.append(Data.data2)
    elif time_wert()[7] == '3':
        dataDate.append(Data.data3)
    elif time_wert()[7] == '4':
        dataDate.append(Data.data4)
    elif time_wert()[7] == '5':
        dataDate.append(Data.data5)
    elif time_wert()[7] == '6':
        dataDate.append(Data.data6)
    elif time_wert()[7] == '7':
        dataDate.append(Data.data7)
    elif time_wert()[7] == '8':
        dataDate.append(Data.data8)
    elif time_wert()[7] == '9':
        dataDate.append(Data.data9)
    elif time_wert()[7] == '0':
        dataDate.append(Data.data0)
    if time_wert()[8] == '1':
        dataDate.append(Data.data1)
    elif time_wert()[8] == '2':
        dataDate.append(Data.data2)
    elif time_wert()[8] == '3':
        dataDate.append(Data.data3)
    elif time_wert()[8] == '4':
        dataDate.append(Data.data4)
    elif time_wert()[8] == '5':
        dataDate.append(Data.data5)
    elif time_wert()[8] == '6':
        dataDate.append(Data.data6)
    elif time_wert()[8] == '7':
        dataDate.append(Data.data7)
    elif time_wert()[8] == '8':
        dataDate.append(Data.data8)
    elif time_wert()[8] == '9':
        dataDate.append(Data.data9)
    elif time_wert()[8] == '0':
        dataDate.append(Data.data0)
    dataDate.append(Data.dataDot)
    dataDate.append(Data.data1)
    dataDate.append(Data.data8)
    dataTime.clear()   
    if time_wert()[13] == '1':    #Stunde
        dataTime.append(Data.data1)
    elif time_wert()[13] == '2':
        dataTime.append(Data.data2)
    elif time_wert()[13] == '3':
        dataTime.append(Data.data3)
    elif time_wert()[13] == '4':
        dataTime.append(Data.data4)
    elif time_wert()[13] == '5':
        dataTime.append(Data.data5)
    elif time_wert()[13] == '6':
        dataTime.append(Data.data6)
    elif time_wert()[13] == '7':
        dataTime.append(Data.data7)
    elif time_wert()[13] == '8':
        dataTime.append(Data.data8)
    elif time_wert()[13] == '9':
        dataTime.append(Data.data9)
    elif time_wert()[13] == '0':
        dataTime.append(Data.data0)
    if time_wert()[14] == '1':
        dataTime.append(Data.data1)
    elif time_wert()[14] == '2':
        dataTime.append(Data.data2)
    elif time_wert()[14] == '3':
        dataTime.append(Data.data3)
    elif time_wert()[14] == '4':
        dataTime.append(Data.data4)
    elif time_wert()[14] == '5':
        dataTime.append(Data.data5)
    elif time_wert()[14] == '6':
        dataTime.append(Data.data6)
    elif time_wert()[14] == '7':
        dataTime.append(Data.data7)
    elif time_wert()[14] == '8':
        dataTime.append(Data.data8)
    elif time_wert()[14] == '9':
        dataTime.append(Data.data9)
    elif time_wert()[14] == '0':
        dataTime.append(Data.data0)
    dataTime.append(Data.dataColon)
    if time_wert()[16] == '1':     #Minute
        dataTime.append(Data.data1)
    elif time_wert()[16] == '2':
        dataTime.append(Data.data2)
    elif time_wert()[16] == '3':
        dataTime.append(Data.data3)
    elif time_wert()[16] == '4':
        dataTime.append(Data.data4)
    elif time_wert()[16] == '5':
        dataTime.append(Data.data5)
    elif time_wert()[16] == '6':
        dataTime.append(Data.data6)
    elif time_wert()[16] == '7':
        dataTime.append(Data.data7)
    elif time_wert()[16] == '8':
        dataTime.append(Data.data8)
    elif time_wert()[16] == '9':
        dataTime.append(Data.data9)
    elif time_wert()[16] == '0':
        dataTime.append(Data.data0)
    if time_wert()[17] == '1':
        dataTime.append(Data.data1)
    elif time_wert()[17] == '2':
        dataTime.append(Data.data2)
    elif time_wert()[17] == '3':
        dataTime.append(Data.data3)
    elif time_wert()[17] == '4':
        dataTime.append(Data.data4)
    elif time_wert()[17] == '5':
        dataTime.append(Data.data5)
    elif time_wert()[17] == '6':
        dataTime.append(Data.data6)
    elif time_wert()[17] == '7':
        dataTime.append(Data.data7)
    elif time_wert()[17] == '8':
        dataTime.append(Data.data8)
    elif time_wert()[17] == '9':
        dataTime.append(Data.data9)
    elif time_wert()[17] == '0':
        dataTime.append(Data.data0)
    dataTime.append(Data.dataColon)
    if time_wert()[19] == '1':    #Sekunde
        dataTime.append(Data.data1)
    elif time_wert()[19] == '2':
        dataTime.append(Data.data2)
    elif time_wert()[19] == '3':
        dataTime.append(Data.data3)
    elif time_wert()[19] == '4':
        dataTime.append(Data.data4)
    elif time_wert()[19] == '5':
        dataTime.append(Data.data5)
    elif time_wert()[19] == '6':
        dataTime.append(Data.data6)
    elif time_wert()[19] == '7':
        dataTime.append(Data.data7)
    elif time_wert()[19] == '8':
        dataTime.append(Data.data8)
    elif time_wert()[19] == '9':
        dataTime.append(Data.data9)
    elif time_wert()[19] == '0':
        dataTime.append(Data.data0)
    if time_wert()[20] == '1':
        dataTime.append(Data.data1)
    elif time_wert()[20] == '2':
        dataTime.append(Data.data2)
    elif time_wert()[20] == '3':
        dataTime.append(Data.data3)
    elif time_wert()[20] == '4':
        dataTime.append(Data.data4)
    elif time_wert()[20] == '5':
        dataTime.append(Data.data5)
    elif time_wert()[20] == '6':
        dataTime.append(Data.data6)
    elif time_wert()[20] == '7':
        dataTime.append(Data.data7)
    elif time_wert()[20] == '8':
        dataTime.append(Data.data8)
    elif time_wert()[20] == '9':
        dataTime.append(Data.data9)
    elif time_wert()[20] == '0':
        dataTime.append(Data.data0) 
    
    time.sleep(1)
    for m in range(0,4):
        for k in range(0,len(dataDay[m])-8):
            for j in range(0,5):
                x=0x80
                for i in range(k,k+8):
                    GPIO.output(latchPin,GPIO.LOW)
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,dataDay[m][i]) #first shift data of line information to first stage 74HC959   
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                    GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                    time.sleep(0.001)# display the next column
                    x>>=1
    for m in range(0,8):
        for k in range(0,len(dataDate[m])-8):
            for j in range(0,5):
                x=0x80
                for i in range(k,k+8):
                    GPIO.output(latchPin,GPIO.LOW)
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,dataDate[m][i]) #first shift data of line information to first stage 74HC959   
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                    GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                    time.sleep(0.001)# display the next column
                    x>>=1
    time.sleep(0.5)
    for m in range(0,8):
        for k in range(0,len(dataTime[m])-8):
            for j in range(0,5):
                x=0x80
                for i in range(k,k+8):
                    GPIO.output(latchPin,GPIO.LOW)
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,dataTime[m][i]) #first shift data of line information to first stage 74HC959   
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                    GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                    time.sleep(0.001)# display the next column
                    x>>=1