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