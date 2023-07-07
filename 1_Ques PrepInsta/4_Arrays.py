#Que 1 - Find Largest element in an array :
# a = [10, 89, 9, 56, 4, 80, 8]
#                         # by function  ->   # print(max(a))
# c = a[0]
# for i in a:
#     if c < i :
#         c = i
# print(c)

#Que 2 -Find Smallest Element in an Array :
# a = [10, 89, 9, 56, 4, 80, 8]
# c = a[0]
# for i in a:
#     if c > i :
#         c = i
# print(c)

#Que 3 - Find the Smallest and largest element in an array :

# a = [10, 89, 9, 56, 4, 80, 8]
# # for largest element
# l = a[0]
# for i in a:
#     if l < i :
#         l = i
# #for smallest element
# s = a[0]
# for i in a:
#     if s > i :
#         s = i
# print(f"smallest elemnts is {s} and largest element is {l}")

#Que 4 - Find Second Smallest Element in an Array : 

# a = [10, 89, 9, 56, 4, 80, 8]

# ss = a[0]
# s  = a[0]
# for i in a:
#     if i < s :
#         s = i
# for i in a :
#     if i <ss and i>s:
#         ss= i
# print(ss)


#Que 5 - Calculate the sum of elements in an array :

# a = [10, 89, 9, 56, 4, 80, 8]
# sum = 0 
# for i in a:
#     sum += i 
# print(sum)


#Que 6 - Reverse an Array :

# a = [10, 89, 9, 56, 4, 80, 8]

## by reverse slicing
# b = a[::-1] 
# print(b)

## by swaping
# start = 0
# end= len(a)-1

# while start< end:
#     a[start],a[end]= a[end],a[start]

#     start+=1
#     end-=1
# print(a)


#Que 7- Sort first half in ascending order and second half in descending :
# a = [10, 89, 9, 56, 4, 80, 8]
# fh = a[:len(a)//2]
# sh = a[len(a)//2:]


# a = fh[0]
# for i in fh :
#     if i>

# res = fh+ sh
# print(res)

## not completed

#Que 8 - Sort the elements of an array :

# c = [10, 40, 20, 30]
# # ascending order 
# a = c
# for i in range(len(a)) :
#     for j in range(len(a)-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)
# # decending order 
# b = a[::-1]
# print(b)

#Que 9 - Finding the frequency of elements in an array :

# arr = [10, 30, 10, 20, 10, 20, 30, 10]
# a =[]
# for i in arr:
#     if i not in a:
#         a.append(i)
# for i in a :
#     count= 0
#     for j in arr:
        
#         if i == j:
#             count +=1
#     print(i , count)


#Que 10 - Sorting elements of an array by frequency : 






































































