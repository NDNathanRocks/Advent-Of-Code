
sum = 0

f = open("input.txt", 'r')
for line in f:
    line = line.strip()
    if line[2] == 'X':
        sum += 1
    elif line[2] == 'Y':
        sum += 2
    elif line[2] == 'Z':
        sum += 3

    if ((line[0] == 'A' and line[2] == 'X') or (line[0] == 'B' and line[2] == 'Y') or (line[0] == 'C' and line[2] == 'Z')):
        sum += 3
    elif ((line[0] == 'A' and line[2] == 'Z') or (line[0] == 'B' and line[2] == 'X') or (line[0] == 'C' and line[2] == 'Y')):
        sum += 0
    else:
        sum += 6

print(sum)

        