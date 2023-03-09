sum = 0
arr = []

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if (line != ''):
            sum += int(line)
        else:
            arr.append(sum)
            sum = 0

sum = 0
sum += max(arr)
arr.pop(arr.index(max(arr)))
sum += max(arr)
arr.pop(arr.index(max(arr)))
sum += max(arr)
arr.pop(arr.index(max(arr)))

print(sum)