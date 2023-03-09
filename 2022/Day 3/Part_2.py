
def check(letter):
    val = ord(letter)
    
    if (val >= 65 and val <= 90):
        val = val - 38
    else:
        val = val - 96

    return val

# f = open("tempIn.txt", 'r')
f = open("input.txt", 'r')
flag = False
sum = 0

line1 = f.readline().strip()
line2 = f.readline().strip()
line3 = f.readline().strip()

while(line1 and line2 and line3):
    flag = False
    for l1 in line1:
        if l1 in line2 and l1 in line3:
            sum += check(l1)
            flag = True
            break
    if not flag:
        for l2 in line2:
            if l2 in line1 and l2 in line3:
                sum += check(l2)
                flag = True
                break
    if not flag:
        for l3 in line3:
            if l3 in line1 and l3 in line2:
                sum += check(l3)
                flag = True
                break

    line1 = f.readline().strip()
    line2 = f.readline().strip()
    line3 = f.readline().strip()

print(sum)
