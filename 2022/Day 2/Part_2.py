
sum = 0

f = open("input.txt", 'r')
for line in f:
    line = line.strip()
    if line[2] == 'X':
        sum += 0
    elif line[2] == 'Y':
        sum += 3
    elif line[2] == 'Z':
        sum += 6

    if (line[0] == 'A' and line[2] == 'X') or (line[0] == 'B' and line[2] == 'Z') or (line[0] == 'C' and line[2] == 'Y'):
        sum += 3
    elif(line[0] == 'A' and line[2] == 'Y') or (line[0] == 'B' and line[2] == 'X') or (line[0] == 'C' and line[2] == 'Z'):
        sum += 1
    else:
        sum += 2

print(sum)

        