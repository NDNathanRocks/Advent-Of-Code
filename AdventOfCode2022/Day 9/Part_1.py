
def checkTail(x, y, xhead, yhead, lastHeadx, lastHeady):
    if (pow((pow((xhead - x), 2) + pow((yhead - y), 2)), 0.5) < 2):
        return x, y
    else:
        return lastHeadx, lastHeady

def move(line, dir):
    if line == "R":
        dir = 1
        return True, dir
    elif line == "L":
        dir = -1
        return True, dir
    elif line == "U":
        dir = 1
        return False, dir
    elif line == "D":
        dir = -1
        return False, dir

sample = 1
f = open("sample.txt" if sample else "input.txt", 'r')

x = 0
y = 0
xhead = 0
yhead = 0
visited = set()

for line in f:
    line = line.split(" ")
    for i in range(int(line[1])):

        lastHeadx = xhead
        lastHeady = yhead

        axisX, dir = move(line[0], dir)
        if axisX:
            xhead = xhead + dir
        else:
            yhead = yhead + dir
        
        x, y = checkTail(x, y, xhead, yhead, lastHeadx, lastHeady)
        visited.add((x, y))

print(len(visited))
