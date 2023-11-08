# def binary_search_iterative(data,target):
#     low = 0
#     high = len(data)-1
#     while low <= high:
#         mid = (low + high) //2

#         if target == data[mid] :
#             return mid       #if u want the targets position
#         elif target < data[mid]:
#             high = mid-1
#         else:
#             low = mid+1

# data = [1,3,5,7,9,12,14]
# target = 5
# print(binary_search_iterative(data,target))

# ---------------------------------------------------

# def binary_search_recursive(data, target,low,high):
#     if low > high:
#         return False
#     else :
#         mid = (low +high)//2
#         if target == data[mid]:
#             return mid
#         elif target < data[mid]:
#             return binary_search_recursive(data,target,low,mid-1)
#         else :
#             return binary_search_recursive(data,target,mid+1,high)

# data = [1,3,5,7,9,10,12,14]
# target= 12
# print(binary_search_recursive(data,target,0,len(data)-1))





#--------------------------------------------------------
##itrative again 

# def BS(arr,K):
#     low = 0 
#     high = len(arr)-1

#     while low <= high:
#         mid = (low + high) // 2

#         if K == arr[mid] :
#             return mid 
#         else:
#             if K > arr[mid]:
#                 low = mid + 1
#             else:
#                 high = mid-1


# arr = [ 2, 3, 4, 10, 40 ]
# K = 10
# print("found at ",BS(arr,K),"th position")



## Recursive again 


# def BS(arr,target,low,high):

#     if low > high:
#         return "Not found"

#     else:
#         mid = (low+high)//2

#         if target == arr[mid]:
#             return mid 
#         else:
#             if target > arr[mid]:
#                 return BS(arr,target,mid+1,high)
#             else:
#                 return BS(arr,target,low,mid-1)

# arr = [2, 3, 5, 9,10, 40]
# target = 10
# low = 0
# high = len(arr)-1
# print(BS(arr,target,low,high))








