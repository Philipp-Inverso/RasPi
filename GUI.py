from tkinter import *
import LEDMatrix
import RPi.GPIO as GPIO
import time
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

root = Tk()
root.configure(bg = 'lightgreen')
LSBFIRST = 1
MSBFIRST = 2
#define the pins connect to 74HC595
dataPin   = 11      #DS Pin of 74HC595(Pin14)
latchPin  = 13      #ST_CP Pin of 74HC595(Pin12)
clockPin = 15
msg_text = "Ansteuerung einzelner LEDs durch Auswahl der Kaestchen.\n\nBewegung des Musters duch Schieberegler.\n\nkleine Programme enthalten (Knoepfe)"

class Checkbar(Frame):
    
    def __init__(self, parent = None, picks = [], side = LEFT, anchor = W):
        Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text=pick, variable=var)
            chk.configure(bg = 'lightgreen', bd = 1)
            chk.pack(side = side, anchor = anchor, expand = YES)
            self.vars.append(var)
            
    def state(self):
        return map((lambda var: var.get()), self.vars)
    
def setup():
    global ver, hor, z1, z2, z3, z4, z5, z6, z7, z8
    GPIO.setmode(GPIO.BOARD)    # Number GPIOs by its physical location
    GPIO.setup(dataPin, GPIO.OUT)
    GPIO.setup(latchPin, GPIO.OUT)
    GPIO.setup(clockPin, GPIO.OUT)
    z1 = Checkbar(root, ['', '', '', '', '', '', '', ''])
    z2 = Checkbar(root, ['', '', '', '', '', '', '', ''])
    z3 = Checkbar(root, ['', '', '', '', '', '', '', ''])
    z4 = Checkbar(root, ['', '', '', '', '', '', '', ''])
    z5 = Checkbar(root, ['', '', '', '', '', '', '', ''])
    z6 = Checkbar(root, ['', '', '', '', '', '', '', ''])
    z7 = Checkbar(root, ['', '', '', '', '', '', '', ''])
    z8 = Checkbar(root, ['', '', '', '', '', '', '', ''])
    z1.grid(row = 0, column = 0, padx = 2, pady = 5)
    z2.grid(row = 1, column = 0, padx = 2, pady = 5)
    z3.grid(row = 2, column = 0, padx = 2, pady = 5)
    z4.grid(row = 3, column = 0, padx = 2, pady = 5)
    z5.grid(row = 4, column = 0, padx = 2, pady = 5)
    z6.grid(row = 5, column = 0, padx = 2, pady = 5)
    z7.grid(row = 6, column = 0, padx = 2, pady = 5)
    z8.grid(row = 7, column = 0, padx = 2, pady = 5)
    ver = Scale(root, from_ = 1, to = -1)
    ver.set(0)
    ver.grid(row = 9, column = 1)
    hor = Scale(root, from_ = -1, to = 1, orient=HORIZONTAL)
    hor.set(0)
    hor.grid(row = 10, column = 2)
    tut = Message(root, text = msg_text, width = 220)
    tut.grid(row = 9, column = 0)
                
def getstates():
    global z1, z2, z3, z4, z5, z6, z7, z8, data
    data = [0, 0, 0, 0, 0, 0, 0, 0]
    for c in range(0,8):
        if list(z1.state())[c] == 1:
            data[c] = data[c] + 128
        if list(z2.state())[c] == 1:
            data[c] = data[c] + 64
        if list(z3.state())[c] == 1:
            data[c] = data[c] + 32
        if list(z4.state())[c] == 1:
            data[c] = data[c] + 16
        if list(z5.state())[c] == 1:
            data[c] = data[c] + 8
        if list(z6.state())[c] == 1:
            data[c] = data[c] + 4
        if list(z7.state())[c] == 1:
            data[c] = data[c] + 2
        if list(z8.state())[c] == 1:
            data[c] = data[c] + 1
    
def printstates():
    global data
    msg = Message(root, text = data)
    msg.config(bg='lightblue', font=('times', 12, 'italic'), width = 225)
    msg.grid(row = 8, column = 0)
    print(data)
    
def down():
    global data, d_ver, d_hor
    if (d_hor == 1 and d_ver == 1) or (d_hor == 1 and d_ver == -1) or (d_hor == -1 and d_ver == -1) or (d_hor == -1 and d_ver == 1):
        for p in range(8,16):
            data[p] = data[p] / 2
    else:
        for p in range(0,8):
            data[p] = data[p] / 2
    
def up():
    global data, ver, hor
    if (d_hor == 1 and d_ver == 1) or (d_hor == 1 and d_ver == -1) or (d_hor == -1 and d_ver == -1) or (d_hor == -1 and d_ver == 1):
        for p in range(8,16):
            data[p] = data[p] * 2
    else:
        for p in range(0,8):
            data[p] = data[p] * 2

def show():
    global d_ver, d_hor, ver, hor, data
    d_ver = ver.get()
    d_hor = hor.get()
    
    if d_hor == 1 and d_ver == 1:
        
        getstates()
        for l in range(0,8):
            data[l] = data[l] / 128
        for i in range(0,8):
            data.insert(0,0)
            data.append(0)        
        for k in range(0,len(data)-8):
            for j in range(0,20):
                x = 0x01
                for i in range(k,k+8):
                    GPIO.output(latchPin,GPIO.LOW)
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,int(data[i])) #first shift data of line information to first stage 74HC959
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                    GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                    time.sleep(0.001)# display the next column
                    x<<=1
            up()
            
    elif d_hor == 1 and d_ver == -1:
        
        getstates()
        for l in range(0,8):
            data[l] = data[l] * 128
        for i in range(0,8):
            data.insert(0,0)
            data.append(0)
        for k in range(0,len(data)-8):
            for j in range(0,10):
                x = 0x01
                for i in range(k,k+8):
                    GPIO.output(latchPin,GPIO.LOW)
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,int(data[i])) #first shift data of line information to first stage 74HC959
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                    GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                    time.sleep(0.001)# display the next column
                    x<<=1
            down()
                
    elif d_hor == -1 and d_ver == 1:
        
        getstates()
        for l in range(0,8):
            data[l] = data[l] / 128
        for i in range(0,8):
            data.insert(0,0)
            data.append(0)
        for k in range(0,len(data)-8):
            for j in range(0,10):
                x = 0x80
                for i in range(k,k+8):
                    GPIO.output(latchPin,GPIO.LOW)
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,int(data[i])) #first shift data of line information to first stage 74HC959
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                    GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                    time.sleep(0.001)# display the next column
                    x>>=1
            up()
                
    elif d_hor == -1 and d_ver == -1:
        
        getstates()
        for l in range(0,8):
            data[l] = data[l] * 128
        for i in range(0,8):
            data.insert(0,0)
            data.append(0)
        for k in range(0,len(data)-8):
            for j in range(0,10):
                x = 0x80
                for i in range(k,k+8):
                    GPIO.output(latchPin,GPIO.LOW)
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,int(data[i])) #first shift data of line information to first stage 74HC959
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                    GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                    time.sleep(0.001)# display the next column
                    x>>=1
            down()
                
    elif d_hor == 1 and d_ver == 0:
        
        getstates()
        for i in range(0,8):
            data.insert(0,0)
            data.append(0)
        for k in range(0,len(data)-8):
            for j in range(0,10):
                x = 0x01
                for i in range(k,k+8):
                    GPIO.output(latchPin,GPIO.LOW)
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,data[i]) #first shift data of line information to first stage 74HC959
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                    GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                    time.sleep(0.001)# display the next column
                    x<<=1
                    
    elif d_hor == -1 and d_ver == 0:
        
        getstates()
        for i in range(0,8):
            data.insert(0,0)
            data.append(0)
        for k in range(0,len(data)-8):
            for j in range(0,10):
                x = 0x80
                for i in range(k,k+8):
                    GPIO.output(latchPin,GPIO.LOW)
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,data[i]) #first shift data of line information to first stage 74HC959
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                    GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                    time.sleep(0.001)# display the next column
                    x>>=1
                    
    elif d_hor == 0 and d_ver == 1:
        
        getstates()
        for l in range(0,8):
            data[l] = data[l] / 128
        for c in range(0,16):
            for j in range(0,10):
                x = 0x80
                for i in range(0,8):
                    GPIO.output(latchPin,GPIO.LOW)
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,int(data[i])) #first shift data of line information to first stage 74HC959
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                    GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                    time.sleep(0.001)# display the next column
                    x>>=1
            up()
            
    elif d_hor == 0 and d_ver == -1:
        
        getstates()
        for l in range(0,8):
            data[l] = data[l] * 128
        while max(data) >= 1:
            for j in range(0,10):
                x = 0x80
                for i in range(0,8):
                    GPIO.output(latchPin,GPIO.LOW)
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,int(data[i])) #first shift data of line information to first stage 74HC959
                    LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                    GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                    time.sleep(0.001)# display the next column
                    x>>=1
            down()
            
    elif d_hor == 0 and d_ver == 0:
        
        for j in range(0,500):
            x = 0x80
            for i in range(0,8):
                GPIO.output(latchPin,GPIO.LOW)
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,data[i]) #first shift data of line information to first stage 74HC959
                LEDMatrix.shiftOut(dataPin,clockPin,MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                GPIO.output(latchPin,GPIO.HIGH)# Output data of two stage 74HC595 at the same time
                time.sleep(0.001)# display the next column
                x>>=1
                
def destroy():
    root.destroy()
    LEDMatrix.destroy()
            
def main():
    setup()
    try:
        Button(root, text='Quit', fg = 'red', command=destroy).grid(row = 5, column = 2, ipadx = 46)
        
        Button(root, text='Wurf', command=wurf.zufall).grid(row = 0, column = 1, ipadx = 15, padx = 2)
        Button(root, text='Time', command=time_pr.Time).grid(row = 1, column = 1, ipadx = 13, padx = 2)
        Button(root, text='Temp', command=temp.cpu_temp).grid(row = 2, column = 1, ipadx = 11, padx = 2)
        Button(root, text='snake', command=snake.snakeL).grid(row = 3, column = 1, ipadx = 9, padx = 2)
        Button(root, text='snake_g', command=snake_game.main).grid(row = 4, column = 1, ipadx = 2, padx = 2)
        Button(root, text='matrix', command=matrix.matrix).grid(row = 5, column = 1, ipadx = 8, padx = 2)
        
        Button(root, text='matrix2', command=matrix2.matrixx).grid(row = 0, column = 2, ipadx = 36, padx = 2)
        Button(root, text='randomDot', command=random_dot.Dot).grid(row = 1, column = 2, ipadx = 24, padx = 2)
        Button(root, text='Bildschirmschoner', command=random_dot2.main).grid(row = 2, column = 2, ipadx = 2, padx = 2)
        
        Button(root, text='Get Data', bg = 'lightblue', fg = 'blue', command=getstates).grid(row = 3, column = 2, ipadx = 31, padx = 2)
        Button(root, text='Print Data', bg = 'lightblue', fg = 'blue', command=printstates).grid(row = 4, column = 2, ipadx = 27, padx = 2)
        
        Button(root, text='Display', bg = 'lightgreen', fg = 'green', command=show, font = ('times', 16)).grid(row = 9, column = 2, ipadx = 8, ipady = 10)
        root.mainloop()
    except:
        print("Ein Fehler ist aufgetreten: GUI")