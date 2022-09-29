'''
The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case.

Examples
-- reverse("Hello World") ➞ "DLROw OLLEh"
-- reverse("ReVeRsE") ➞ "eSrEvEr"
-- reverse("Radar") ➞ "RADAr"

Notes

There will be no punctuation in any of the test cases.
'''

# def reverse(str):
#     result = ''
#     for i in range(len(str)-1, -1, -1):
#         if str[i].islower():
#             result += str[i].upper()
#         else:
#             result += str[i].lower()

#     return result

def reverse(str):
    return str[::-1].swapcase()

print(reverse("Hello World")) # "DLROw OLLEh"
print(reverse("ReVeRsE")) # "eSrEvEr"
print(reverse("Radar")) # "RADAr"