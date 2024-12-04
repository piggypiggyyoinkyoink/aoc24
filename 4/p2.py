import re
f = open("4/input.txt", "r")
total = 0
full = f.readlines()
#horizontal
for i in range(len(full)):
    
    for j in range(len(full[i])):
        try:

            if full[i+1][j+1] == "A" and set([full[i][j], full[i+2][j+2]]) == {"M","S"} and set([full[i+2][j], full[i][j+2]]) == {"M","S"}:
                total += 1
        except:pass
print(total)
