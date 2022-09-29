# def find_even_nums(num):
#     result = []
#     for n in range(1, num+1):
#         if n % 2 == 0:
#             result.append(n)
#     return result
#     # return [n for n in range(1, num) if n % 2 == 0 in n]

def find_even_nums(num):
    return [n for n in range(1, num+1) if n % 2 == 0]

print(find_even_nums(8)) # [2, 4, 6, 8]
print(find_even_nums(4)) # [2, 4]
print(find_even_nums(2)) # [2]
print(find_even_nums(1)) # []