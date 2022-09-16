'''
Print met behulp van een For loop het volgende teken uit:
Probeer het met een for loop te maken en het dynamisch 
te houden (Dus makkelijk aan te passen)

@
@@
@@@
@@@@
@@@@@
<<<<<<< HEAD
@@@@@@  # ARROW_SIZE = 6
=======
@@@@@@  #ARROW_SIZE = 6
>>>>>>> 5f8491086df368bfa792085a519e11ef52b2879d
@@@@@
@@@@
@@@
@@
@

NOTE: The arrow size in my implementation is the size of the 
<<<<<<< HEAD
middle part of the arrow; in the implementation of ..., 
=======
middle part of the arrow; in the implementation of Martin, 
>>>>>>> 5f8491086df368bfa792085a519e11ef52b2879d
the 'arrow length' is divided in 2 and so making the result
half of what I expected.
'''
# -- no string slice
# -- no function
# -- inside 1 loop

ARROW_SIZE = 6 # size of arrow

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