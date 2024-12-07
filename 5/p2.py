f = open("5/input.txt", "r")
rules = []
updates = []
total = 0
while (line:= f.readline()) != "\n":
    rules.append(line.strip().split("|"))

while (line:= f.readline()):
    updates.append(line.strip().split(","))
"""
print(rules[-1])
print(updates[0])
print(updates[-1])
"""
l = []
print(len(rules))
for rule in rules:
    if rule[1] not in l:
        if rule[0] not in l:
            l.append(rule[0])
            l.append(rule[1])
        else:
            l.append(rule[1])
    else:
        if rule[0] not in l:
            l.insert(0, rule[0])
        if l.index(rule[0]) < l.index(rule[1]):
            pass#good
        else: #badf
            total +=1
            

# i have no fucking clue how to do this



print(total)                              