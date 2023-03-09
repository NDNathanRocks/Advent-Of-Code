import math
sample = 0
f = open("sample.txt" if sample else "input.txt", 'r')

arr = []
sum = 1
line = f.readline().strip()

while(line):

    tempArr = [0, 0, 0, 0, 0]

    line = f.readline().strip()
    line = line.split(": ")
    line = line[1].split(", ")
    # Item list
    tempArr[0] = list(map(int, line))
    line = f.readline().strip()
    line = line.split(" = ")
    line = line[1].split(" ")
    # Operation
    tempArr[1] = line
    line = f.readline().strip()
    line = line.split(" ")
    # Test
    tempArr[2] = int(line[3])
    sum *= int(line[3])
    line = f.readline().strip()
    line = line.split("monkey ")
    # True case
    tempArr[3] = int(line[1])
    line = f.readline().strip()
    line = line.split("monkey ")
    # False case
    tempArr[4] = int(line[1])

    arr.append(tempArr)

    line = f.readline().strip()
    line = f.readline().strip()

activity = [0 for i in range(len(arr))]

for i in range(10000):
    for m in range(len(arr)):
        for item in arr[m][0]:
            activity[m] += 1

            if arr[m][1][0] == "old":temp1 = item
            else:temp1 = int(arr[m][1][0])
            if arr[m][1][2] == "old":temp2 = item
            else:temp2 = int(arr[m][1][2])

            if arr[m][1][1] == '*':
                worry = temp1 * temp2
            else:
                worry = temp1 + temp2
            
            if worry % arr[m][2] == 0:
                arr[arr[m][3]][0].append(worry%sum)
            else:
                arr[arr[m][4]][0].append(worry%sum)
            
        arr[m][0] = []


for a in range(len(activity)):
    print("monkey", a, "inspected: ", activity[a])

i1 = activity.index(max(activity))
t1 = activity[i1]
activity.pop(activity.index(max(activity)))
i2 = activity.index(max(activity))

print( t1 * activity[i2])