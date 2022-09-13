# Print met de volgende lijst en indexering de zin "Hallo, ik ben [naam] en ik zit bij Hacklab"

'''
Print as follows:

letterList[0].upper()
letterList[6]
letterList[3]
...

Index per letter:
q:0, w:1, e:2, r:3, t:4, y:5, u:6, i:7, o:8, p:9, l:10, k:11, j:12, h:13, g:14, f:15, d:16, s:17, a:18, z:19, x:20, c:21, v:22, b:23, n:24, m:25

'''
letterList = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i' , 'o', 'p', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's', 'a', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
str1 = letterList[13].upper() + letterList[18] + letterList[10] + letterList[10] + letterList[8] + ', '
str2 = letterList[7] + letterList[11] + ' '
str3 = letterList[23] + letterList[2] + letterList[24] + ' '
str4 = letterList[9].upper() + letterList[7] + letterList[2] + letterList[4] + letterList[2] + letterList[3] + ' '
str5 = letterList[2] + letterList[24] + ' '
str6 = letterList[7] + letterList[11] + ' '
str7 = letterList[19] + letterList[7] + letterList[4] + ' '
str8 = letterList[23] + letterList[7] + letterList[12] + ' '
str9 = letterList[13].upper() + letterList[18] + letterList[21] + letterList[11] + letterList[10] + letterList[18] + letterList[23] + ' '
sentence = str1 + str2 + str3 + str4 + str5 + str6 + str7 + str8 + str9
print(sentence)