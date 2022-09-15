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
# -- no string slice
# -- no function
# -- inside 1 loop

ARROW_SIZE = 12 # size of arrow

symbolNum = 1
printBackwards = False
while symbolNum > 0:

    arrowPart = ''

    for s in range(1, symbolNum+1):
        arrowPart += '@'    

    print(arrowPart) # print part of arrow

    if symbolNum == ARROW_SIZE:
        printBackwards = True

    if printBackwards:
        symbolNum -= 1
    else:
        symbolNum += 1