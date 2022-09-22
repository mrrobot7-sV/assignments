def list_operation(x, y, n):
    if (x >= y):
        raise ValueError('x parameter value cannot be greater than y parameter')
    result = []
    for v in range(x, y + 1):    
        if v % n == 0:
            result.append(v)
    return result

def main():
    try:
        print(list_operation(1, 10, 3)) 
        print(list_operation(7, 9, 2))
        print(list_operation(15, 20, 7))
        print(list_operation(15, 21, 7))
        print(list_operation(22, 21, 7))
    except ValueError as err:
        print(err)

if __name__ == "__main__":
    main()            