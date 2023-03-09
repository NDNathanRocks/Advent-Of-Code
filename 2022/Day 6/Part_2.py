sample = 0
f = open("sample.txt" if sample else "input.txt", 'r')

arr = []

for line in f:
    line = line.strip()
    i = 0
    for l in line:
        i += 1
        arr.append(l)
        if len(arr) == 14:
            flag = True
            for elem in arr:
                if arr.count(elem) > 1:
                    flag = False
            if flag:
                print(i)
            else:
                arr.pop(0)
