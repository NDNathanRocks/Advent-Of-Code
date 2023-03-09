

f = open("input.txt", 'r')
sum = 0

for line in f:
    line = line.strip()

    line = line.split(',')
    line[0] = line[0].split('-')
    line[1] = line[1].split('-')

    a = int(line[0][0])
    b = int(line[0][1])
    c = int(line[1][0])
    d = int(line[1][1])

# check inside
    if (a >= c and a <= d and b >= c and b <= d):
        sum += 1
    elif (c >= a and c <= b and d >= a and d <= b):
        sum += 1
# check if seperate on num scale
    elif ( b >= c ):
        if( not(d < a)  ):
            sum += 1

print("sum =", sum)

