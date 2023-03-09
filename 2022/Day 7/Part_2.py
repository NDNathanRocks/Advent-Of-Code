sample = 0
f = open("sample.txt" if sample else "input.txt", 'r')

path = []
dir = []

def doCDCommand(path, line):
    if line[2] == "/":
        path = []
    elif line[2] == "..":
        path.pop()
    else:
        path.append(line[2])

def getPathStr(path):
    string = '/'
    for p in path:
        string += p
        string += '/'
    return string


line = f.readline()
line = line.strip()
while(line):
    if (line[0:4] == "$ cd"):
        line = line.split(' ')
        doCDCommand(path, line)
    elif (line[0:4] == "$ ls"):
        dirSize = 0
        line = f.readline()
        line = line.strip()
        while (line and line[0] != '$'):
            line = line.split(' ')
            if (line[0] != "dir"):
                dirSize += int(line[0])
            line = f.readline()
            line = line.strip()
        dir.append([getPathStr(path), dirSize])
        continue
    line = f.readline()
    line = line.strip()

for dir1 in dir:
    for dir2 in dir:
        index = dir1[0].find(dir2[0])
        if (index == 0 and dir1 != dir2):
            dir2[1] += dir1[1]

weNeed = 30000000 - (70000000 - dir[0][1])
sum = 9999999999999999999

for d in dir:
    if (d[1] > weNeed and d[1] < sum):
        sum = int(d[1])

print(sum)

