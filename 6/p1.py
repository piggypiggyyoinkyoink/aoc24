f = open("6/input.txt", "r")
#map1=[list(f.readline().strip()) for line in  f]
map1=[]
map2 = list(f.read().splitlines())
for line in map2:
    map1.append(list(line))
f7 = open("6/bizwas2.txt", "w")

f7.writelines([("".join(map(str, map1[i])) + "\n") for i in range(len(map1))])
print([("".join(map(str, map1[i])) + "\n") for i in range(len(map1))])
f7.close()
print(map1)
off = False
dir = 1
for i in range(len(map1)):
    try:
        loc = (i,map1[i].index("^"))
        break
    except:pass
print(loc)
print(len(map1))

total = 0
iters = 0
while not off:
    iters += 1
    if dir == 1:
        if loc[0] == 0:
            off = True

        else:
            try:
                if (map1[loc[0]-1][loc[1]]) == "#":
                    dir = 2
                else:
                    if map1[loc[0]-1][loc[1]] != "X":
                        total +=1
                    map1[loc[0]-1][loc[1]] = "X"
                    loc = (loc[0]-1,loc[1])
            except:
                off = True
    elif dir ==2:
        try:
            if (map1[loc[0]][loc[1]+1]) == "#":
                dir = 3
            else:
                if map1[loc[0]][loc[1]+1] != "X":
                        total +=1
                map1[loc[0]][loc[1]+1] = "X"
                loc = (loc[0],loc[1]+1)
        except:
            off = True
    elif dir == 3:
        try:
            if (map1[loc[0]+1][loc[1]]) == "#":
                dir = 4
            else:
                if map1[loc[0]+1][loc[1]] != "X":
                        total +=1
                map1[loc[0]+1][loc[1]] = "X"
                loc = (loc[0]+1,loc[1])
        except:
            off = True
    elif dir == 4:
        if loc[1] == 0:
            off = True
        else:
            try:
                if (map1[loc[0]][loc[1]-1]) == "#":
                    dir = 1
                else:
                    if map1[loc[0]][loc[1]-1]!= "X":
                        total +=1
                    map1[loc[0]][loc[1]-1] = "X"
                    loc = (loc[0],loc[1]-1)
            except:
                off = True
print(total)
print(iters)
f7 = open("6/bizwas.txt", "w")
f7.writelines([("".join(map(str, map1[i])) + "\n") for i in range(len(map1))])
f7.close()