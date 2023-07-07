#Implementation of selection sort 
#link-https://www.youtube.com/watch?v=hhkLdjIimlw

def Selection_sort(arr):
        for i in range(len(arr)):
            min_index = i
            for j in range(i+1,len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i],arr[min_index]=arr[min_index],arr[i]

arr = [12,45,78,22,9,2,467,87,32,41,1]
Selection_sort(arr)
print(arr)

