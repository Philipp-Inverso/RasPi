import LEDMatrix
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
##    print(LEDMatrix.Numpad(LEDMatrix.inCmd))
##    if LEDMatrix.Numpad(LEDMatrix.inCmd) == True:
        input = str()
        input2 = str()
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
                    print(str(input) + ' + ' + str(input2) +' = '+ str(int(input) + int(input2)))
                    input = ''
                    input2 = ''
                    merke = ''
                if merke == 'B':
                    print(str(input) + ' - ' + str(input2) +' = '+ str(int(input) - int(input2)))
                    input = ''
                    input2 = ''
                    merke = ''
                if merke == 'C':
                    print(str(input) + ' * ' + str(input2) +' = '+ str(int(input) * int(input2)))
                    input = ''
                    input2 = ''
                    merke = ''
                if merke == 'D':
                    print(str(input) + ' / ' + str(input2) +' = '+ str(int(input) / int(input2)))
                    input = ''
                    input2 = ''
                    merke = ''
            elif key != keypad.NULL:
                if not merke:
                    input = input + key
                    print(input)
                else:
                    input2 = input2 + key
                    print(input2)
##    elif LEDMatrix.Numpad(LEDMatrix.inCmd) == False: