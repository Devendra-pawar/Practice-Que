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












##not done









#Que 11- Finding the Longest Palindrome in an Array :

# arr = [1, 232, 5545455, 9090909, 12321,161]

# a = 0
# for i in arr:
#     i = str(i)
#     rev = i[::-1]

#     if i == rev :
#         i  = int(i)
#         if a < i:
#             a = i

# print("longest palindrome is" , a)



#Que 12 - Counting Distinct Elements in an Array :


# arr = [10, 20, 40, 30, 50, 20, 10, 20]
# brr=[]

# for i in arr:
#     if i not in brr:
#         brr.append(i)
# print(len(brr))



#Que 13 - Finding  Repeating elements in an Array :

# arr = [10, 20, 40, 30, 50, 20, 10, 20]
# brr = []
# crr = []
# for i in arr:
#     if i not in brr:
#         brr.append(i)
#     else:
#         if i not in crr:
#             crr.append(i)
#             print(i,end=" ")



#Que 14 - Finding Non Repeating elements in an Array : 

# arr = [10, 20, 70, 90, 80, 20, 10, 20]
# brr=[]
# for i in range(len(arr)):
#     count = 0 
#     for j in range(i+1,len(arr)):
#         if arr[i] == arr[j] :
#             brr.append(arr[i])
#             count +=1
#     if count == 0 :
#         if arr[i] not in brr:
#             print(arr[i],end=" ")




#Que 15 - Removing Duplicate elements from an array :


# arr = [10, 20, 20, 30, 40, 40, 40, 50, 50]
# brr = []

# for i in arr:
#     if i not in brr:
#         brr.append(i)
#         print(i,end=" ")




#Que 16 - Finding Minimum scalar product of two vectors : 


# arr1 = [10, 30, 40, 20]
# arr2 = [2, 4, 5, 1]


# for i in arr1 :
#     if i 







## not completed 



#Que 17 - Finding Maximum scalar product of two vectors 














## not completed



#Que 18 - Counting the number of even and odd elements in an array

# a = [11, 20, 35, 40, 53]
# ev = []
# od = []
# for i in a :
#     if i %2 == 0 :
#         ev.append(i)
#     else:
#         od.append(i)

# print("even: ",len(ev),ev)
# print("odd: ",len(od),od)



#Que 19 - Find all Symmetric pairs in an array :

# def findPairs(pairs):

#     s = set()

#     for (x, y) in pairs:
#         s.add((x, y))
#         if (y, x) in s:
#             print((x, y))
 
# pairs = [(3, 4), (1, 2), (5, 2), (7, 10), (4, 3), (2, 5)]
# findPairs(pairs)



#Que 20 - Find maximum product sub-array in a given array :














## not done 
  


#Que 21 - Finding Arrays are disjoint or not :

# arr1 = [1,2,3,4,5,6]
# arr2 = [7,8,9,10,11]

# count = 0
# for i in arr1:
#     if i in arr2:
#         count +=1

# if count >0 :
#     print("not a disjoint")
# else:
#     print("disjoint ")


#Que 22 - Determine Array is a subset of another array or not : 

# arr1 = [1,3,4,5,6,7]
# arr2 = [3,5,7,8]
# count = 0 

# for i in arr2:
#     if i not in arr1:
#         count +=1 

# if count >0 :
#     print(" it is not a subset")
# else:
#     print(" it is a subset ")



#Que 23 - Determine can all numbers of an array be made equal :








## not done 


#Que 24 - Finding Minimum sum of absolute difference of given array : 









## not done 



#Que 25 - Sort an array according to the order defined by another array : 






##not done 


















#Que 26 - Replace each element of the array by its rank in the array :












































































