arr = [1,2,3,4,5]
d=4
for i in range(d):
    arr.append(arr[0])
    arr.pop(0)
print(arr)


