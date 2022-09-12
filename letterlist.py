# Print met de volgende lijst en indexering de zin "Hallo, ik ben [naam] en ik zit bij Hacklab"

letterList = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i' , 'o', 'p', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's', 'a', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

'''
    Usage: 

        1)  print_sentence() 
            prints the sentence according to the indexes that are found in 'letterList'.
        2)  print_sentence(False)
            prints the characters from the sentence when found in the 'letterList', otherwise continues to print the character 
            even if not found in 'letterList'.    
'''

name = "Pieter"
sentence = "Hallo, ik ben {fname} en ik zit bij Hacklab".format(fname =name)

def print_sentence(equalToIndex = True):
    result = ''
    for c in sentence:    
        if (equalToIndex):
            try:
                index = letterList.index(c)
            except ValueError as e:
                print(e)
                continue                
            result += letterList[index]
        else:
            if c.isupper() or c == ' ' or c == ',':
                result += c
            else:
                index = letterList.index(c)
                result += letterList[index]        
    return result

print(print_sentence()) # this means that you can't fully print the sentence as letterList doesn't include: ' ', ',', 'H', and 'P'
print(print_sentence(False))