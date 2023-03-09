
def check(letter):
    val = ord(letter)
    
    if (val >= 65 and val <= 90):
        val = val - 38
    else:
        val = val - 96

    return val

f = open("input.txt", 'r')
flag = False
sum = 0

for line in f:
    line = line.strip()
    lineLen = int(len(line)/2)
    flag = False
    for i in range(0, lineLen):
        for j in range(lineLen, len(line)):
            if line[i] == line[j]:
                letter = line[i]
                sum += check(letter)
                flag = True
                break
        if(flag):
            break
print(sum)

