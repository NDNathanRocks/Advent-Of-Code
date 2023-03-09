
sample = 0
f = open("sample.txt" if sample else "input.txt", 'r')

x = 1
cycle = 1
sum = 0

crt = ['.' for i in range(240)]

for line in f:

    line = line.split(" ")
    added = False
    flag = False
    
    while (not added):

        if (cycle%40) == x or (cycle%40) == x + 1  or (cycle%40) == x + 2:
            crt[cycle-1] = '#'

        if(len(line) > 1):
            if (flag):
                x  = x + int(line[1])
                added = True
            if (not flag):
                flag = True
            cycle += 1
        else:
            cycle += 1
            added = True
        
for i in range(6):
    for j in range((i*40), (i*40)+40):
        print(crt[j], end='')
    print()
