f = open("5/input.txt", "r")
rules = []
updates = []
total = 0
while (line:= f.readline()) != "\n":
    rules.append(line.strip().split("|"))

while (line:= f.readline()):
    updates.append(line.strip().split(","))

print(rules[-1])
print(updates[0])
print(updates[-1])

for update in updates:
    valid = True
    for rule in rules:
        try:
            if (a:= update.index(rule[0])) > (b:= update.index(rule[1])):
                valid = False
                break
        except:pass
    if valid:
        total += int(update[((len(update)+1)//2)-1])

print(total)                                   