f = open("1/input.txt", "r")
l1, l2 = [], []
for line in f:
    a = line.split(" ")
    l1.append(a[0])
    l2.append(a[-1][:-1])

#print(l1,l2)
dif = []
f.close()
for i in range(len(l1)):
    sm1 = l1.pop(l1.index(min(l1)))
    sm2 = l2.pop(l2.index(min(l2)))
    #print(sm1, sm2)
    dif.append(abs(int(sm1)-int(sm2)))
print(sum(dif))