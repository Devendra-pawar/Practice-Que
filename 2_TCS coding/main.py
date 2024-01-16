
##            Numbers ----------------------------------------------

#Que 1 - Climbing stairs 


# def fun(n):
#     if n == 0 :
#         return 0 
#     elif n ==1 :
#         return 1 
#     else:
#         d = [0,1,2]
#         for i in range(2,n):
#             d.append(d[i]+ d[i-1])
#         return d[n]

# n = 6
# print(fun(n))



# Que 2 - Leap year 

# year = 1000

# if (year % 4 == 0 and year%100 != 0) or year%400 == 0:
#     print("leap year")
# else:
#     print("not a leap year")


# Que 5 - divisior of natural number

# n = 100
# for i in range(1,n+1):
#     if n % i == 0 :
#         print(i , end=" ")


# Que 6 - Convert a number to hexadecimal 











# Que 7 - perfect square
# n = 25
# c=0
# for i in range(1,n):
#     if i*i == n:
#         c= 1
#         print("perfect square")
#         break
# if c == 0:
#     print("Not a perfect square")

#//optimal answer

# n = 16
# if int(n**0.5)== n**0.5:
#     print("perfect square")
# else:
#     print("not a perfect square") 


# Que 8 - program to add two pointers



# Que 9 - Fibonnachi number 












## Array -----------------------------------------------------------

#Que 2 - Program to check if an array is sorted or not 

# arr = [2,5,7,9,11,12,15]
# count = 0 

# for i in range(1,len(arr)):
#     if arr[i-1] <= arr[i]:
#         pass
#     else:
#         count += 1

# if count ==0:
#     print("Yes")
# else:
#     print('no')



#Que 3 - Program to find sum of elements in a given array

# arr = [2,5,7,9,11,12,15]

# count = 0 
# for i in arr:
#     count+=i
# print(f"sum is {count}")



#Que 5 - Counting frequencies of array elements

# arr = [10, 20, 20, 10, 10, 20, 5, 20]

# d = {}
# for i in arr:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d) 



#Que  - 











## String -- ------------------------------------------

#Que 1  - Palindrome String
# s = "abbba"
# if s == s[::-1]:
#     print("it is")
# else:
#     print("not a palindrome")



#Que 3 - remove character 

s1 = "computer"
s2 = "cat"
ans = " "
for i in s1:
    if i not in s2 :
        ans+= i
print(ans)

















