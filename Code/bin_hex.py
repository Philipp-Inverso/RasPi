import RPi.GPIO as GPIO
import Keypad
import os

ROWS = 4
COLS = 4
keys = 	['1','2','3','A',
	 '4','5','6','B',
	 '7','8','9','C',
	 '*','0','#','D']
rowsPins = [7,32,22,36]
colsPins = [19,18,16,12]	      

def main():
    if os.path.isfile("/home/pi/Code/Git/RasPi/Code/Numpad"):
        type = str()
        eink = str()
        eink2 = str()
        eink16 = str()
        print('eink:')
        print("'A' = Dez")
        print("'B' = Bin")
        print("'C' = Hex")
        while True:
            keypad = Keypad.Keypad(keys,rowsPins,colsPins,ROWS,COLS)
            keypad.setDebounceTime(50)
            key = keypad.getKey()
            if key == '*':
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
            elif key == '#':
                type = ''
                eink = ''
                eink2 = ''
                eink16 = ''
            elif key == 'A':
                type = 'Dez'
            elif key == 'B':
                type = 'Bin'
            elif key == 'C':
                type = 'Hex'
                print('Bitte Dez angeben (z.B.: 01 = 1; F = 15)')
            elif key != keypad.NULL:
                if type == 'Dez':
                    eink = eink + key
                    print()
                    print(eink)
                    print(bin(int(eink)))
                    print(hex(int(eink)))
                elif type == 'Bin':
                    if key == '0' or key == '1':
                        eink2 = eink2 + key
                        eink = eink + bin(int(eink2)).split('0b')[1]
                        eink2 = ''
                        try:
                            eink = '0b' + eink.split('0b')[1]
                        except:
                            eink = '0b' + eink
                        print()
                        print(eink)
                        print(eval(eink))
                        print(hex(eval(eink)))
                    else:
                        print('no binary number')
                elif type == 'Hex':
                    eink16 = eink16 + key
                    if len(eink16) == 2:
                        eink = eink + hex(int(eink16)).split('0x')[1]
                        eink16 = ''
                        try:
                            eink = '0x' + eink.split('0x')[1]
                        except:
                            eink = '0x' + eink
                        print()
                        print(eink)
                        print(eval(eink))
                        print(bin(eval(eink)))
    else:
        while True:
            modus = input('Welcher Eingabetyp? (dez, bin, hex) ')
            eingabe = input('Zahl: ')
            if modus == 'dez':
                print(bin(int(eingabe)))
                print(hex(int(eingabe)))
            elif modus == 'bin':
                try:
                    eingabe = '0b' + eingabe.split('0b')[1]
                except:
                    eingabe = '0b' + eingabe
                print(eval(eingabe))
                print(hex(eval(eingabe)))
            elif modus == 'hex':
                try:
                    eingabe = '0x' + eingabe.split('0x')[1]
                except:
                    eingabe = '0x' + eingabe
                print(eval(eingabe))
                print(bin(eval(eingabe)))
            else: print('unzulaeassige Eingabe')
            if input('Ende? ') == 'ja':
                break
            else:
                pass
