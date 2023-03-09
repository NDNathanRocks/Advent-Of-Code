
sample = 0
f = open("sample.txt" if sample else "input.txt", 'r')

arr = []

line1 = f.readline().strip()
while(line1):

    arr.append(eval(line1))
    line1 = f.readline().strip()
    arr.append(eval(line1))

    f.readline()
    line1 = f.readline().strip()

def recursion(a, b):
    
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return 1
        if a > b:
            return -1
        return 0

    elif isinstance(a, list) and isinstance(b, int):
        b = [b]
        return recursion(a, b)

    elif isinstance(a, int) and isinstance(b, list):
        a = [a]
        return recursion(a, b)

    elif isinstance(a, list) and isinstance(b, list):
        lenA = len(a)
        lenB = len(b)

        for i in range(lenA if lenA < lenB else lenB):
            flag = recursion(a[i], b[i])
            if flag == 1:
                return 1
            if flag == -1:
                return -1

        # If continue check sizes
        if lenA > lenB:
            return -1
        elif lenA == lenB:
            return 0
        return 1

def bubbleSort(array):
    n = len(array)
    swapped = False

    for i in range(n-1):
        for j in range(0, n-i-1):            
            flag = recursion(array[j], array[j + 1])
            if flag == -1:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
         
        if not swapped:
            return

arr.append([[2]])
arr.append([[6]])
    
bubbleSort(arr)

sum = 1
[ sum := (index+1)*sum for index,i in enumerate(arr) if i == [[2]] or i == [[6]]]

print(sum)
