
dirDict = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

def checkTail(x, y, xhead, yhead):
    dx = xhead - x
    dy = yhead - y

    # x +- 2
    if(abs(dx) == 2 and yhead == y):
        if (xhead > x):
            x += 1
        else:
            x -= 1

    # y +- 2
    elif(abs(dy) == 2 and xhead == x):
        if (yhead > y):
            y += 1
        else:
            y -= 1

    # diagonal cases
    elif((abs(dx) >= 2) or (abs(dy) >= 2)):
        if (xhead > x and yhead > y):
            x += 1
            y += 1 
        elif(xhead < x and yhead > y):
            x -= 1
            y += 1
        elif(xhead < x and yhead < y):
            x -= 1
            y -= 1
        elif(xhead > x and yhead < y):
            x += 1
            y -= 1
    
    return (x, y)

sample = 0
f = open("sample.txt" if sample else "input.txt", 'r')

tail = [(0, 0) for i in range(9)]
head = (0, 0)
visited = set()

for line in f:
    dir, amt = line.split(" ")
    amt = int(amt)
    for i in range(amt):
        # head coordinates
        head = (head[0] + dirDict[dir][0], head[1] + dirDict[dir][1])
        # tail move
        tail[0] = checkTail(*tail[0], *head)
        for t in range(1, len(tail)):
            tail[t] = checkTail(*tail[t], *tail[t-1])
            if(t == 8):
                visited.add(tail[t])

print(len(visited))
