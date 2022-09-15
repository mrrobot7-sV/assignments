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
def print_arrow_part(at):
    arrow_part = ''
    for i in range(1, at):
        arrow_part += '@'
    print(arrow_part)

def print_arrow(x):
    for i in range(1, x):
        print_arrow_part(i)
    
    x -= 1
    while (x > 0):
        print_arrow_part(x)
        x -= 1

print_arrow(20)