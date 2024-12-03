import re
f = open("3/input.txt", "r")
x = f.read()
print(x)
li = re.findall(r'mul\([0-9]+,[0-9]+\)', x)
print(li)
sum = 0
for dingus in li:
    num = dingus.strip("mul()").split(",")
    sum += (prod:= int(num[0]) * int(num[1]))
print(sum)