import RPi.GPIO as GPIO
import Keypad

ROWS = 4
COLS = 4
keys = 	['1','2','3','A',
	 '4','5','6','B',
	 '7','8','9','C',
	 '*','0','#','D']
rowsPins = [7,32,22,36]
colsPins = [19,18,16,12]	      

def main():
    type = str()
    input = str()
    input2 = str()
    input16 = str()
    print('Input:')
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
            input = ''
            input2 = ''
            input16 = ''
        elif key == 'A':
            type = 'Dez'
        elif key == 'B':
            type = 'Bin'
        elif key == 'C':
            type = 'Hex'
            print('Bitte Dez angeben (z.B.: 01 = 1; F = 15)')
        elif key != keypad.NULL:
            if type == 'Dez':
                input = input + key
                print()
                print(input)
                print(bin(int(input)))
                print(hex(int(input)))
            elif type == 'Bin':
                if key == '0' or key == '1':
                    input2 = input2 + key
                    input = input + bin(int(input2)).split('0b')[1]
                    input2 = ''
                    try:
                        input = '0b' + input.split('0b')[1]
                    except:
                        input = '0b' + input
                    print()
                    print(input)
                    print(eval(input))
                    print(hex(eval(input)))
                else:
                    print('no binary number')
            elif type == 'Hex':
                input16 = input16 + key
                if len(input16) == 2:
                    input = input + hex(int(input16)).split('0x')[1]
                    input16 = ''
                    try:
                        input = '0x' + input.split('0x')[1]
                    except:
                        input = '0x' + input
                    print()
                    print(input)
                    print(eval(input))
                    print(bin(eval(input)))