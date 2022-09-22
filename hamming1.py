
from math import dist


def hamming_distance(str1, str2):
    dist = 0
    if (len(str1) != len(str2)):
        raise IndexError("Strings don't have the same length")
    else:    
        for i in range(0, len(str1)):
            if (str1[i] != str2[i]):
                dist += 1
    return dist


print(hamming_distance("abcde", "bcdef"))
print(hamming_distance("abcde", "abcde"))
print(hamming_distance("strong", "strung"))

try:
    print(hamming_distance("strdsfdfs", "strsdfsdfdfdsfsfd"))
except IndexError as e:
    print(e)