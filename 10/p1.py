f = open("10/input.txt", "r")
map1 = list(f.read().splitlines())
#print(map1)
#map1 = list("""..90..9,...1.98,...2..7,6543456,765.987,876....,987....""".split(","))
for i in range(len(map1)):
    map1[i]= list(str(map1[i]))
#print(map1)
scores = 0


def recursion(row, column, headr, headc, visited):
    global scores
    if column >= 0:
        if (current:=str(map1[row][column])) == "9":
            if (row, column) not in visited:
                #print("hello")
                visited.append((row, column))
                print(row, column, map1[row][column])

                scores +=1
                #print(scores)
        else:
            
            #print(int(current)+1, map1[row+1][column])
            #print(map1[row+1][column] == str(int(current)+1))
            try:
                if map1[row+1][column] == str(int(current)+1):
                    visited = recursion(row+1, column, headr, headc, visited)
            except:pass
            try:
                if map1[row][column+1] == str(int(current)+1):
                    visited = recursion(row, column+1, headr, headc, visited)
            except:pass
            try:
                if map1[row-1][column] == str(int(current)+1) and row >0:
                    visited = recursion(row-1, column, headr, headc, visited)
            except:pass
            try:
                if map1[row][column-1] == str(int(current)+1) and column > 0:
                    visited = recursion(row, column-1, headr, headc, visited)
            except:pass
    #print(current)
    #print(visited)
    return visited

total = 0
for row in range(len(map1)):
    for column in range(len(map1[row])):
        if map1[row][column] == "0":
            print()
            visited = set(recursion(row, column, headr=row, headc=column, visited=[]))
            total += len(visited)

print(scores)

"""
for row in scores:
    for score in row:
        total += score"""
print(scores)
print(total)