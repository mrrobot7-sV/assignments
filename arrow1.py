'''
Print met behulp van een For loop het volgende teken uit:
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
x = 13 # size of arrow

# first part of arrow
for i in range(1, x):
    arrow_part = ''
    for j in range(1, i):
        arrow_part += '@'
    print(arrow_part)

# second part of arrow
x -= 1
while (x > 0):
    arrow_part = ''
    for j in range(1, x):
        arrow_part += '@'
    print(arrow_part)
    x -= 1