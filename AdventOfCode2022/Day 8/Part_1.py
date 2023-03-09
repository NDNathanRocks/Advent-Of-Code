
def rowCheck(line, index, dir):
    compIndex = index
    while compIndex > 0 and compIndex < len(line) - 1:
        if int(line[index]) > int(line[compIndex+dir]):
            compIndex += dir
        else:
            return False
    return True

def colCheck(lines, col, row, dir):
    compIndex = row
    while compIndex > 0 and compIndex < len(lines) - 1:
        if int(lines[row][col]) > int(lines[compIndex+dir][col]):
            compIndex += dir
        else:
            return False
    return True

sample = 0
f = open("sample.txt" if sample else "input.txt", 'r')

lines = f.read().splitlines() 

inside = 0

for i in range(1, len(lines) - 1):
    line = lines[i]
    for s in range(1, len(lines[i]) - 1):
        #left
        if(rowCheck(line, s, -1)):
            inside += 1
            print(s, i, "left")
        #right
        elif(rowCheck(line, s, 1)):
            inside += 1
            print(s, i, "right")
        #top
        elif(colCheck(lines, s, i, -1)):
            inside += 1
            print(s, i, "top")
        #bot
        elif(colCheck(lines, s, i, 1)):
            inside += 1
            print(s, i,"bot")
        
perimeter = len(lines)
width = len(lines[0])

perimeter = 2*perimeter + 2*width - 4

print("border =", perimeter)
print("inside =", inside)
print("total =", inside + perimeter)


