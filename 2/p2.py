import copy
f = open("2/input.txt", "r")
b = []
for line in f:
    a = line.split(" ")
    a[-1] = a[-1][:-1]
    b.append(a)

count = 0
for l in b:
    
    for j in range(len(l)):
        l2 = copy.copy(l)
        del l2[j]
        dec = True
        inc = True
        for i in range(len(l2)-1):
            if int(l2[i+1]) <= int(l2[i]):
                inc = False
            if int(l2[i+1]) >= int(l2[i]):
                dec = False
            if abs(int(l2[i+1]) - int(l2[i])) > 3:
                inc, dec = False, False
        if inc or dec:
            count += 1
            break
        
print(count)