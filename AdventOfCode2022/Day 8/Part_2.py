
def rowCheck(line, index, dir):
    sum = 0
    compIndex = index
    while compIndex > 0 and compIndex < len(line) - 1:
        if int(line[index]) > int(line[compIndex+dir]):
            compIndex += dir
            sum += 1
        else:
            sum += 1
            return sum
    return sum

def colCheck(lines, col, row, dir):
    sum = 0
    compIndex = row
    while compIndex > 0 and compIndex < len(lines) - 1:
        if int(lines[row][col]) > int(lines[compIndex+dir][col]):
            compIndex += dir
            sum += 1
        else:
            sum += 1
            return sum
    return sum

sample = 0
f = open("sample.txt" if sample else "input.txt", 'r')

lines = f.read().splitlines()

viewPoints = [[0 for j in range(len(lines[i]))] for i in range(len(lines))]

for i in range(1, len(lines) - 1):
    line = lines[i]
    for s in range(1, len(lines[i]) - 1):
        #left
        viewPoints[i][s] += rowCheck(line, s, -1)
        #right
        viewPoints[i][s] *= rowCheck(line, s, 1)
        #top
        viewPoints[i][s] *= colCheck(lines, s, i, -1)
        #bot
        viewPoints[i][s] *= colCheck(lines, s, i, 1)

print(max([max(p) for p in viewPoints]))
    
