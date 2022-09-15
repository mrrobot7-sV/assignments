'''
Print met behulp van een For loop het volgende teken uit:
Probeer het met een for loop te maken en het dynamisch 
te houden (Dus makkelijk aan te passen)

@
@@
@@@
@@@@
@@@@@
@@@@@@
@@@@@
@@@@
@@@
@@
@
'''
def print_arrow(size, symbol = '@'):

    symbolNum = 1
    printBackwards = False
    while symbolNum > 0:

        arrowPart = ''

        for s in range(1, symbolNum+1):
            arrowPart += symbol

        print(arrowPart) # print part of arrow

        if symbolNum == size:
            printBackwards = True

        if printBackwards:
            symbolNum -= 1
        else:
            symbolNum += 1

print_arrow(7)
print_arrow(7, '#')
print_arrow(12, '-')