import re
f = open("3/input.txt", "r")
x = f.read()
#print(x)
#x = str("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
#print(x)
#print("init lenx",len(x))
"""
m1 = re.search(r"don\'t\(\)", x).start()
m2 = re.search(r"do\(\)", x).end()
while m1 or m2:
    if m1 and m2:
        x = x[:m1] + x[m2:]
        print(len(x))
        try:
            m1 = re.search(r"don\'t\(\)", x).start()
            v = False
            while not v:
                try:
                    m3 = re.search(r"do\(\)", x).start()
                    m4 = re.search(r"do\(\)", x).end()
                    if m3 < m1:
                        x = x[:m3] + x[m4:]
                    else:
                        v = True
                   
                except:v=True
        except:m1 = False
        try:
            m2 = re.search(r"do\(\)", x).end()
        except:m2=False

    elif m1:
        x = x[:m1]
        
    elif m2:
        break

    print(m1,m2)
print(x)
"""
inits=[]
fins = []
flag = False
for i in range(len(x)-6):
    if not flag:
        if x[i] + x[i+1] + x[i+2] + x[i+3] + x[i+4] + x[i+5] + x[i+6] == "don't()":
            init = i
            inits.append(i)
            flag = True
    if flag:
        if x[i] + x[i+1] + x[i+2] + x[i+3] == "do()":
            #x = x[:init] + x[i+4:]
            flag = False
            fins.append(i+4)
#print(inits,"\n", fins)
y = ""
y+= x[:inits[0]]
for i in range(1,len(inits)):
    y += x[fins[i-1]:inits[i]] #+ x[fins[i]:inits[i+1]]
y+= x[fins[len(inits)-1]:]
#print(len(y))
li = re.findall(r'mul\([0-9]+,[0-9]+\)', y)
#print(li)
sum = 0
for dingus in li:
    num = dingus.strip("mul()").split(",")
    sum += (prod:= int(num[0]) * int(num[1]))
print(sum)