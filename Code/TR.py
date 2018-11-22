import LEDMatrix
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
        eingabe = str()
        eingabe2 = str()
        merke = str()
        print("'A' = '+'")
        print("'B' = '-'")
        print("'C' = '*'")
        print("'D' = '/'")
        print("'#' = '='")
        print("'*' = beenden")
        while True:
            keypad = Keypad.Keypad(keys,rowsPins,colsPins,ROWS,COLS)
            keypad.setDebounceTime(0.1)
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
            elif key == 'A':
                merke = 'A'
            elif key == 'B':
                merke = 'B'
            elif key == 'C':
                merke = 'C'
            elif key == 'D':
                merke = 'D'
            elif key == '#':
                if merke == 'A':
                    print(str(eingabe) + ' + ' + str(eingabe2) +' = '+ str(int(eingabe) + int(eingabe2)))
                    eingabe = ''
                    eingabe2 = ''
                    merke = ''
                if merke == 'B':
                    print(str(eingabe) + ' - ' + str(eingabe2) +' = '+ str(int(eingabe) - int(eingabe2)))
                    eingabe = ''
                    eingabe2 = ''
                    merke = ''
                if merke == 'C':
                    print(str(eingabe) + ' * ' + str(eingabe2) +' = '+ str(int(eingabe) * int(eingabe2)))
                    eingabe = ''
                    eingabe2 = ''
                    merke = ''
                if merke == 'D':
                    print(str(eingabe) + ' / ' + str(eingabe2) +' = '+ str(int(eingabe) / int(eingabe2)))
                    eingabe = ''
                    eingabe2 = ''
                    merke = ''
            elif key != keypad.NULL:
                if not merke:
                    eingabe = eingabe + key
                    print(eingabe)
                else:
                    eingabe2 = eingabe2 + key
                    print(eingabe2)
    else:
        while True:
            print()
            zahl1 = int(input('1.Zahl: '))
            operator = input('Operation: ')
            zahl2 = int(input('2.Zahl: '))
            if operator == '+':
                print(zahl1 + zahl2)
            elif operator == '-':
                print(zahl1 - zahl2)
            elif operator == '*':
                print(zahl1 * zahl2)
            elif operator == '/':
                print(zahl1 / zahl2)
            stop = input('Weiter? ')
            if stop == 'nein'or'Nein'or'n':
                break
            elif stop == 'ja'or'Ja'or'j':
                pass
