
sample = 0
f = open("sample.txt" if sample else "input.txt", 'r')

arr = []

line1 = f.readline().strip()
line2 = f.readline().strip()
while(line1 and line2):

    tempArr = []
    tempArr.append(eval(line1))
    tempArr.append(eval(line2))

    arr.append(tempArr)

    f.readline()
    line1 = f.readline().strip()
    line2 = f.readline().strip()


def recursion(a, b):
    
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return 1
        if a > b:
            return -1
        return 0

    elif isinstance(a, list) and isinstance(b, int):
        b = [b]
        return recursion(a, b)

    elif isinstance(a, int) and isinstance(b, list):
        a = [a]
        return recursion(a, b)

    elif isinstance(a, list) and isinstance(b, list):
        lenA = len(a)
        lenB = len(b)

        for i in range(lenA if lenA < lenB else lenB):
            flag = recursion(a[i], b[i])
            if flag == 1:
                return 1
            if flag == -1:
                return -1

        # If continue check sizes
        if lenA > lenB:
            return -1
        elif lenA == lenB:
            return 0
        return 1
        
indices = []
i = 0
for a in arr:
    i += 1
    flag = recursion(a[0], a[1])
    if flag == 1:
        indices.append(i)

print(indices)
print(sum(indices))