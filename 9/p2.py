f = open("9/input.txt", "r")
li = list(f.readline().strip())
li = list("2333133121414131402")
print(len(li))
movements = []
for i in range(len(li)-1, 0, -2):
    num = int(li[i])
    for j in range(1, i, 2):
        if int(li[j]) >= num:
            print(i//2, j)
            movements.append(y:=[(i-2*len(list(filter(None,[m[1] <= (i+1)//2 for m in movements]))))//2, (j+1)//2,i-len(list(filter(None,[m[1] <= (i+1)//2 for m in movements])))])
            print(movements)
            for mov in movements:
                if  mov[1] >= (j+1)//2 and mov[1] < (i+1)//2 and mov != y:
                    mov[1] += 1
            print(li)
            x=int(li.pop(j))
            li.insert(j, "0")
            li.insert(j+1, str(x-num))
            li.insert(j+1, str(num))
            print("i=",i)
            print(li)
            if i == len(li):
                try:
                    a = int(li.pop(i+2))
                except:
                    a = 0
                li.insert(i+1, str(a+int(li.pop(i+1))))
                try:
                    li.pop(i+3)
                except:pass
            else:
                print(li)
                try:
                    d = li.pop(i+1)
                    e = li.pop(i+1)
                    f = li.pop(i+1)
                    li.insert(i+1, str(int(d)+int(e)+int(f)))
                except:
                    pass
            break
print(len(li))          

driveMap = []
idnum = 0
for i in range(len(li)):
    if (i % 2) == 0:
        v = False
        for mov in movements:
            if mov[1] == (i//2):
                for j in range(int(li[i])):
                    driveMap.append(mov[0])
                v = True
                break
        if not v:
            for j in range(int(li[i])):
                #print([m[1] <= (i+1)//2 for m in movements])
                #print(len(list(filter(None,[(m[0]*2) <= (i+1)//2 for m in movements]))))
                driveMap.append((i-2*len(list(filter(None,[m[1] <= (i+1)//2 for m in movements]))))//2+len(list(filter(None,[(m[0]*2) <= (i+1)//2 for m in movements]))))
                #print(driveMap)
            idnum += 1
    else:
        for j in range(int(li[i])):
            driveMap.append(".")
            #print(driveMap)

#print(movements)
print(driveMap)
checksum = 0
for i in range(len(driveMap)):
    if driveMap[i] == ".":
        break
    else:
        checksum += driveMap[i] * i
print(checksum)
