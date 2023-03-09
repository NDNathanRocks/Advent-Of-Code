f = open("input.txt", 'r')

#     [M]             [Z]     [V]    
#     [Z]     [P]     [L]     [Z] [J]
# [S] [D]     [W]     [W]     [H] [Q]
# [P] [V] [N] [D]     [P]     [C] [V]
# [H] [B] [J] [V] [B] [M]     [N] [P]
# [V] [F] [L] [Z] [C] [S] [P] [S] [G]
# [F] [J] [M] [G] [R] [R] [H] [R] [L]
# [G] [G] [G] [N] [V] [V] [T] [Q] [F]
#  1   2   3   4   5   6   7   8   9 

myList = [
    ['S','P','H','V','F','G'],
    ['M','Z','D','V','B','F','J','G'],
    ['N','J','L','M','G'],
    ['P','W','D','V','Z','G','N'],
    ['B', 'C', 'R', 'V'],
    ['Z','L','W','P','M','S','R','V'],
    ['P', 'H', 'T'],
    ['V','Z','H','C','N','S','R','Q'],
    ['J','Q','V','P','G','L','F']
]

for l in myList:
    l = l.reverse()

for line in f:
    line = line.strip()
    line = line.split(' ')
    
    loop = int(line[1]) - 1

    fromIndex = int(line[3]) - 1
    toIndex = int(line[5]) - 1
    listLen = len(myList[fromIndex]) - 1

    myList[toIndex] +=  myList[fromIndex][listLen-loop:] 
    myList[fromIndex] = myList[fromIndex][:listLen-loop]

for val in myList:
    print(val[len(val) - 1], end = '')
