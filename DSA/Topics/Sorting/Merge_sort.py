#link - https://www.youtube.com/watch?v=jlHkDBEumP0



def merge(a,lb,mid,ub):
    i = lb
    j = mid+1
    k = lb

    while i <=mid and j<=ub:
        if a[i] <= a[j]:
            b[k]= a[i]
            i+=1
            k+=1
        else:
            b[k]= a[j]
            j+=1
            k+=1
    if i>mid:
        while j <= ub:
            b[k]=a[j]
            j+=1
            k+=1
    else:
        while i<= mid :
            b[k]=a[i]
            i+=1
            k+=1


def merge_sort(a, lb, ub):
    if lb>=ub:
        return
    
    mid = (lb+ub)/2
    merge_sort(a, lb, mid)
    merge_sort(a,mid+1,ub)
    merge(a, lb, mid, ub)



a =[7,1,8,3,6,5,4,2]
merge_sort(a,0,len(a)-1)
print(a)


## not completed
