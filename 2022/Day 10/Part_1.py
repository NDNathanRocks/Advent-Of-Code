
sample = 0
f = open("sample.txt" if sample else "input.txt", 'r')

x = 1
cycle = 1
sum = 0

for line in f:

    line = line.split(" ")
    added = False
    flag = False

    while (not added):

        if cycle in [20, 60, 100, 140, 180, 220]:
            sum = sum + (cycle * x)
        
        if(len(line) > 1):
            if (flag):
                x += int(line[1])
                added = True
            if (not flag):
                flag = True
            cycle += 1
        else:
            cycle += 1
            added = True
    
print(sum)
