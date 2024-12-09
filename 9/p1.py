f = open("9/input.txt", "r")
li = list(f.readline().strip())
driveMap = []
idnum = 0
for i in range(len(li)):
    if i % 2 == 0:
        for j in range(int(li[i])):
            driveMap.append(idnum)
        idnum += 1
    else:
        for j in range(int(li[i])):
            driveMap.append(".")

import re
print(len(driveMap))
j = 0
while re.fullmatch(r"[0-9]*\.*", "".join(str(x) for x in driveMap)) == None:
        while j < len(driveMap) and driveMap[j]!= ".":
            j+=1
        if j == len(driveMap):
            break
        if driveMap[j] == ".":
            for i in range(len(driveMap)-1, -1, -1):
                if driveMap[i] != ".":
                    break
            driveMap[j] = driveMap[i]
            driveMap[i] = "."
        


print("hello")
print(driveMap)
checksum = 0
for i in range(len(driveMap)):
    if driveMap[i] == ".":
        break
    else:
        checksum += driveMap[i] * i

print(checksum)