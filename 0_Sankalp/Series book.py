# CAMPUS MONK
 #by akshat sir
 # link - https://web.classplusapp.com/viewPdf


#Que 1 - 

# a = [-1,2,-1,3,2]

# k =[]
# for i in range(len(a)):
#     count = 0
#     for j in range(i+1,len(a)):
#         if a[i]== a[j]:
#                 k.append(a[j])
#                 count+=1 
#     if count == 0:
#         if a[i] not in k:
#             print(a[i],end=" ") 
        

#Que 2 - 

# a = [1,0,2,0,1,0,2]
# a.sort()
# print(a)


#Que 3 - array subset of another array 


# a = [11,1,13,21,7,3]
# b = [11,3,7,1]
# count= 0
# for i in b:
#     if i not in a:
#         print("no")
#         count = 1
#         break 
# if count == 0 : print("yes")
    

#Que 5 - Frequencies of limited range array elements 

# n = 5
# arr = [2,3,2,3,5]

# for i in range(1,n+1):
#     count = 0 
#     for j in arr:
#         if i == j :
#             count +=1
#     print(count,end=" ")


#que 6- Remove duplicates

# arr = [2,2,2,2,2,1]
# j =[]
# for i in arr:
#     if i not in j :
#         j.append(i)

# print(j)


############## TAKING INPUT IN FOR LOOP
# a = []
# b= 1
# for i in range(5):
    
#     c = int(input(f"enter the {b} no. :"))
#     b +=1
#     a.append(c)

# print("the final list is" ,a)

#####################################


#Que 7 - smallest and second smallest element

# a= [2,10,8,9,5,7]
# smallest = a[0]
# for i in range(len(a)):
#     if smallest > a[i]:
#         smallest = a[i]
# ss = a[-1] 
# for i in range(len(a)):
#     if a[i] < ss and a[i]!= smallest:
#         ss= a[i]
# print("smallest is :" , smallest)
# print("second smallest is :",ss)


#Que 8 - Binary no. to decimal number 

# b = 10001000    # 136
## b = 101100   #44
# d = 0
# a= 1
# while b :
#     last = b%10
#     d = d+(a * last)

#     a *= 2
#     b = b//10
# print(d)



#Que 9 - decimal to binary




a = 1//2
b = 1%2
print(a)
print(b)





 

#Que 10 - searching a number

# k = 16 
# a= [9,7,2,16,4]

# for i in range(len(a)):
#     if k == a[i] :
#         print(i+1)
#         break
# else:
#     print(-1)



#Que 11 - binary search 


# def fun(a,k):

#     low = 0 
#     high = len(a)

#     while low<= high:
#         mid = (low+high)//2
        
#         if a[mid]< k :
#             low  = mid+1
#         elif a[mid]>k:
#             high = mid-1
#         else:
#             return mid
#     return -1

# k =  40
# a = [5,8,2,9,6,7,3,4,1]
# a.sort()

# mid = len(a)//2
# print("present at index: ",fun(a,k))











































