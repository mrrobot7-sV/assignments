def hamming_distance(str1, str2):

    dist = 0 
    rangeLength = len(str1)

    # -- if greater, then calc. difference and add to dist
    # -- calc. length of range to check every character 
    #    on difference in remaining string
    if (len(str1) > len(str2)): 
        dist += len(str1)-len(str2)        
        rangeLength = len(str2)
    elif (len(str2) > len(str1)):
        dist += len(str2)-len(str1)
        rangeLength = len(str1)

    # -- check every character on difference
    for i in range(0, rangeLength):
        if (str1[i] != str2[i]):
            dist += 1
    return dist

def main():
    print(hamming_distance("abcde", "bcdef")) # 5
    print(hamming_distance("abcde", "abcde")) # 0
    print(hamming_distance("strong", "strung")) # 1
    print(hamming_distance("strstrong", "strstrong1234567")) # 7
    print(hamming_distance("strstrong", "1234567strstrong")) # 16
    print(hamming_distance("strstrong", "str456789rstrong")) # 13

if __name__ == "__main__":
    main()
