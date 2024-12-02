f = open("2/input.txt", "r")
b = []
for line in f:
    a = line.split(" ")
    a[-1] = a[-1][:-1]
    b.append(a)

count = 0
for l in b:
    dec = True
    inc = True
    for i in range(len(l)-1):
        if int(l[i+1]) <= int(l[i]):
            inc = False
        if int(l[i+1]) >= int(l[i]):
            dec = False
        if abs(int(l[i+1]) - int(l[i])) > 3:
            inc, dec = False, False
    if inc or dec:
        count += 1
print(count)