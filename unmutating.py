def change(x, times):
    y = x.copy()
    for i in range(len(x)):
        j = 1
        while j <= times:
            if i >= j and i < len(x)-j:
                y[i] -= 1
            j += 1
    return y

x = [3, 3, 3, 3, 3, 3, 3]
print(change(x, 2))  
print(change(x, 2))  

