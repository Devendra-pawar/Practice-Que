# link- https://www.youtube.com/watch?v=RrrlAeGXARQ
l = [3,6,8,1,4]
n = 5
for i in range(n):
    for j in range(n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1] =l[j+1],l[j]
print("sorted list is ",l)