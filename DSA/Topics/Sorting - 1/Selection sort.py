#link - https://www.youtube.com/watch?v=xYb6cvCGM7U&list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&index=41

def selection_sort(l):
    n = len(l)
    for i in range(n):          ## range(n-1)
        min_index = i
        for j in range(i+1,n):
            if l[j]<l[min_index]:
                min_index = j
        l[i],l[min_index]= l[min_index],l[i]

l = [5, 50 ,70 ,10 ,90, 70 ,30 ,20 ,60]
selection_sort(l)
print(l)