#Question 1
#Given an array Arr[ ] of N integers and a positive integer K. 
# The task is to cyclically rotate the array clockwise by K.


# def rotate(n,arr,k):
#     f = arr[:n-k]
#     s = arr[n-k:]

#     return s+f

# n = 5
# arr= [10,20,30,40,50]
# k= 2
# print(rotate(n,arr,k))

#------------------------------------------------------------------------------
#Que - 2

#Given two non-negative integers n1 and n2, where n1<n2. 
#The task is to find the total number of integers in the
#range [n1, n2](both inclusive) which have no repeated digits.


# def fun(n1,n2):
#     s=[]
#     for i in range(n1,n2+1):
#         c=[]
#         for j in str(i):   
#             if j not in c :
#                 c.append(j)  
#         if len(c)==len(str(i)):
#             s.append(i)
#     return len(s)
# # n1 = 11
# # n2 = 15
# n1 = 101 
# n2 = 200
# print(fun(n1,n2))



#------------------------------------------------------------------------------
#Que 3 
#Given an array Arr[ ] of N integer numbers. 
# The task is to rewrite the array by putting all multipliers at the end of the given array


# def fun(n,arr):
#     s1 = []
#     s2 = []
#     for i in arr:
#         if i %10 == 0:
#             s2.append(i)
#         else:
#             s1.append(i)
#     return s1+s2

# n =9
# arr= [10, 12, 5, 40, 30, 7, 5, 9, 10]
# print(fun(n,arr))


#------------------------------------------------------------------------------
#Que 4 - 
#Given an array Arr[ ] of N integers and a positive integer K.
# The task is to Divide the array into two sub array
# from right after the Kth position and 
# slide the left sub array of K elements to the end.


# def fun(n,arr,k):
#     s1 = arr[:k]
#     s2 = arr[k:]
#     return s2+s1

# n = 4
# arr =[10,20,30,40]
# k = 1
# print(fun(n,arr,k))


#----------------------------------------------------------------------------------------------
#Que 5 - 
'''For hiring a car, a travel agency charges R1 rupees per hour for the first N hours and then R2 rupees per hour.
Given the total time of travel in minutes in X.
The task is to find the total travelling cost in rupees.'''

# def fun(r1,r2,n,x):
#     hour = x//60
#     if x/60 > x//60:
#         hour +=1

#     a = n*r1

#     y = hour-n
#     if y >0:
#         b = y*r2
#     else:
#         b = 0
#     return a+b

# r1 = 20
# r2= 40
# n = 4
# x = 300
# print(fun(r1,r2,n,x))



#---------------------------------------------------------------------------------
#Que 6 - 
'''There is a bag with three types of gemstones: Ruby of type R, Garnet of G, and Topaz of type T.
Write a program to find the total number of possible arrangements to make a series of gemstones where no two
gemstones of the same type are adjacent to each other.'''





#not done 












#---------------------------------------------------------------------
#Que 7 - 
''' Question1 :
Given a sentence cstr, written in a camel case (i.e. every word starts with an uppercase letter and there is no
space or punctuation between two consecutive words). The task is to put one space after every word and
convert every uppercase letter to lowercase.'''

# def fun(cstr):
#     st = ""
#     for i in cstr:
#         if i >= "a" and i <= "z":
#             st += i 
#         else:
#             a = ord(i)+ 32
#             i = ord(a)
#             st = st+ " " + i
#     return st
            

# cstr = "ThisIsAnAutomationEra"
# print(fun(cstr))


a = ord('a') 
print(ord('a'))


