f = open("1/input.txt", "r")
l1, l2 = [], []
for line in f:
    a = line.split(" ")
    l1.append(a[0])
    l2.append(a[-1][:-1])

#print(l1,l2)
sim = []
f.close()
for i in range(len(l1)):
    sm1 = l1.pop(l1.index(min(l1)))
    count = 0
    true = True
    while true:
        try:
            l2.pop(l2.index(sm1))
            count += 1
        except:true = False
    #print(count)
    sim.append(int(sm1)*count)
    
    
print(sum(sim))