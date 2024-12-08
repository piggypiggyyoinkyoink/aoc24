from copy import deepcopy as Dupinator5000
f = open("8/input.txt", "r")
map1 = list(f.read().splitlines())
chars = set()
for line in map1:
    for char in line:
        chars.add(char)
chars.remove(".")
print(chars)
locations = set()


for char in chars:
    map2 = Dupinator5000(map1)
    tmp = []
    for i in range(rows:=len(map2)):
        for j in range(cols:=len(map2[i])):
            if map2[i][j] == char:
                tmp.append((i,j))
    
    for loc in tmp:
        tmp2 = Dupinator5000(tmp)
        tmp2.remove(loc)
        for loc2 in tmp2:
            dif_y = loc2[0]-loc[0]
            dif_x = loc2[1]-loc[1]
            if dif_x == 0:
                dif_y = 1
            elif dif_y == 0:
                dif_x = 1
            else:
                for num in range(max(dif_y, dif_x),1, -1):
                    if dif_y % num == dif_x % num == 0:
                        dif_y = dif_y // num; dif_x = dif_x // num
                        break


            for mult in range(-rows, rows):
                if mult != 0:
                    newloc1 = (loc2[0] + mult * dif_y, loc2[1] + mult*dif_x)
                    if newloc1[0] < 0 or newloc1[1] < 0 or newloc1[0] >= rows or newloc1[1] >= cols:
                        pass
                    else:
                        locations.add(newloc1)
                    newloc2 = (loc[0] - (mult * dif_y), loc[1] - (mult* dif_x))
                    if newloc2[0] < 0 or newloc2[1] < 0 or newloc2[0] >= rows or newloc2[1] >= cols:
                        pass
                    else:
                        locations.add(newloc2)

print(locations)
print(len(locations))