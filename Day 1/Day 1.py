arr = []
count = 0


with open("input.txt","r") as f:
    for line in f:
        arr.append(int(line))

for i in range(1,len(arr)):
    if arr[i] > arr[i-1]:
        count += 1;

print("There are ", count, " measurments that are larger than the previous measurment")
