arr = []
state = False
foldArr = []

with open("input.txt", "r") as f:
    for line in f:
        if state:
            line = line.replace("fold along ",'')
            line = line.split('=')
            foldArr.append(line)
        else:
            if line == '\n':
                state = True;
                continue
            line = line.split(',')
            line[0] = int(line[0])
            line[1] = int(line[1])
            arr.append(line)

for fold in foldArr:
    i = ord(fold[0]) - 120
    foldValue = int(fold[1])
    for cord in arr:
        if cord[i] == foldValue:
                arr.remove(cord)
                continue
        if cord[i] > foldValue:
            cord[i] = cord[i] - 2*(cord[i] - foldValue)

nums2 = [] 
[nums2.append(val) for val in arr if val not in nums2]

print(len(nums2))

maxX,maxY = 0,0
for cord in nums2:
    if cord[0] > maxX:
        maxX = cord[0]
    if cord[1] > maxY:
        maxY = cord[1]
        
hashArr = []
for y in range(0, maxY + 1):
    temp = []
    for x in range(0, maxX + 1):
        temp.append('.')
    hashArr.append(temp)


for cord in nums2:
    hashArr[cord[1]][cord[0]] = '#'

for cord in hashArr:
    print(cord, '\n')
    



