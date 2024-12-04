import re
f = open("4/input.txt", "r")
total = 0
full = f.readlines()
#horizontal
for i in range(len(full)):
    total += len(re.findall(r"XMAS", full[i]))
    total += len(re.findall(r"SAMX", full[i]))

    #vertical
    for j in range(len(full[i])):
        try:
            if (x:= full[i][j] + full[i+1][j] + full[i+2][j] + full[i+3][j]) == "XMAS" or x == "SAMX":
                total += 1
        except:pass

    for k in range(len(full[i])):
        try:
            if (y:= full[i][k] + full[i+1][k+1] + full[i+2][k+2] + full[i+3][k+3]) == "XMAS" or y == "SAMX":
                total += 1
        except:pass
        try:
            if (z:= full[i][k] + full[i+1][k-1] + full[i+2][k-2] + full[i+3][k-3]) == "XMAS" or z == "SAMX":
                total += 1
        except:pass
print(total)
