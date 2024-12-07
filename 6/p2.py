import copy
f = open("6/input.txt", "r")
#map1=[list(f.readline().strip()) for line in  f]
map3=[]
map2 = list(f.read().splitlines())
for line in map2:
    map3.append(list(line))

total = 0

for row in range(len(map2)):
    for col in range(len(map2[row])):
        map1 = copy.deepcopy(map3)
        map1[row][col] = "#"



        off = False
        dir = 1
        for i in range(len(map1)):
            try:
                loc = (i,map1[i].index("^"))
                break
            except:pass
        print(loc)
        iters = 0
        while not off and iters < 25000:
            iters += 1
            if dir == 1:
                if loc[0] == 0:
                    off = True

                else:
                    try:
                        if (map1[loc[0]-1][loc[1]]) == "#":
                            dir = 2
                        else:
                            
                            map1[loc[0]-1][loc[1]] = "X"
                            loc = (loc[0]-1,loc[1])
                    except:
                        off = True
            elif dir ==2:
                try:
                    if (map1[loc[0]][loc[1]+1]) == "#":
                        dir = 3
                    else:
                        
                        map1[loc[0]][loc[1]+1] = "X"
                        loc = (loc[0],loc[1]+1)
                except:
                    off = True
            elif dir == 3:
                try:
                    if (map1[loc[0]+1][loc[1]]) == "#":
                        dir = 4
                    else:
                        
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
                            
                            map1[loc[0]][loc[1]-1] = "X"
                            loc = (loc[0],loc[1]-1)
                    except:
                        off = True
        if iters > 24999:
            total +=1
        print(iters)
print(total)
