def recursion(t:int, ans, li):
    if len(li) == 1:
        if int(t) + int(li[0]) == int(ans) or int(t) * int(li[0]) == int(ans):
            return True
        else:return False
    elif t == 0:
        if recursion(li[0], ans, li[1:]):
            return True
        else:return False
    else:
        if recursion(int(t)+int(li[0]), ans, li[1:]) or recursion(int(t)*int(li[0]), ans, li[1:]):
            return True
        else:return False

f = open("7/input.txt", "r")
total = 0
for line in f:
    l = line.split(":")
    l[1] = l[1].strip().split(" ")
    if recursion(0,l[0], l[1]):
        total += int(l[0])

print(total)
