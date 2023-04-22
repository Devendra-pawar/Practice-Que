# Que 1

# n =3
# for i in range(n+1):
#     for j in range(n):
#         print("*", end=" ")
#     print('')

# Que 2

# n = 3
# for i in range(n):
#     a = 1
#     for j in range(n):
#         print(a,end=" ")
#         a +=1
#     print("")


# Que 3 

# n = 3
# for i in range(n):
#     b = 97    
#     for j in range(n):
#         print(chr(b),end=" ")
#         b +=1
#     print("")

#Que 4

# n = 3
# b = 65
# for i in range(n):       
#     for j in range(n):
#         print(chr(b),end=" ")
#     b +=1
#     print("")


#que 5 

# n = 3
# a= 1
# for i in range(n):    
#     for j in range(n):
#         print(a,end=" ")
#     a += 1
#     print(" ")


# Que 6

# n =3
# a = 1
# for i in range(n):
#     for j in range(n):
#         print(a,end=" ")
#         a+=1
#     print(" ")


#Que 7

# n =3
# a = 97
# for i in range(n):
#     for j in range(n):
#         print(chr(a),end=" ")
#         a+=1
#     print(" ")


# Que 8

# n = 5
# for i in range(n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print(" ")

# Que 9

# n = 5
# for i in range(n+1):
#     a =1
#     for j in range(i):
#         print(a,end=" ")
#         a +=1
#     print(" ")

# Que 10

# n = 5
# for i in range(n+1):
#     a = 97
#     for j in range(i):
#         print(chr(a),end=" ")
#         a +=1
#     print(" ")

# Que 11

# n = 5
# a = 65
# for i in range(n+1):     
#     for j in range(i):
#         print(chr(a-1),end=" ")
#     a+=1
#     print(" ")

# Que 12

# n = 5
# a = 0
# for i in range(n+1):
#     for j in range(i):
#         print(a,end=" ")
#     a+=1
#     print(" ")

# Que 13

# n = 4
# a =1
# for i in range(n+1):
#     for j in range(i):
#         print(a,end=" ")
#         a +=1
#     print(" ")


# Que 14

# n = 4
# a = 97
# for i in range(n+1):
#     for j in range(i):
#         print(chr(a),end=" ")
#         a += 1
#     print(" ")


# Que 15

# n =5
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end= " ")
#     print(" ")


# Que 16 - Que 21 ----> same hi h yaar 

# Que 22

# n = 5
# a=1
# for i in range(n,0,-1):
#     for j in range(i-1):
#         print(" ",end=" ")
#     for k in range(a):
#         print("*",end=" ")
#     a+=1
#     print(" ")    

# or

# n = 5
# a = 2*n - 2
# for i in range(1, n+1):
    
#     for j in range(1, a+1):
#         print(end=" ")
#     a=a - 2
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print(" ")

#Que 23

# n = 5
# k = n*2 -2
# for i in range(0,n):
#     a= 1
#     for j in range(0,k+1):
#         print(end=" ")
#     k = k-2
#     for j in range(0,i+1):
#         print(a,end=" ")
#         a+=1
#     print(" ")


# Que 29

# n = 5
# a = 5
# for i in range(n):
#     for j in range(0,i):
#         print(" ",end=" ")
#     for j in range(0,a):
#         print("*",end= " ")
#     a-=1
#     print(" ")


#Que 31

# n = 5
# a= n
# for i in range(n):
#     c = 97
#     for j in range(0,i):
#         print(" ",end=" ")
    
#     for j in range(0,a):
#         print(chr(c),end=" ")
#         c += 1
#     a -= 1
#     print(" ")


#Que 36

# n  = 4
# a = n-1
# b = 1
# for i in range(n):
#     for j in range(0,a):
#         print(" ",end=" ")
#     a -= 1
#     for j in range(0,i+1):
#         print("*",end=" ")
#     for j in range(b-1):
#         print("*",end=" ")
#     b +=1
#     print(" ")


# Que 43

# n =4
# a = 0
# b = n
# c=n-1
# for i in range(n):
#     for j in range(a):
#         print(" ",end=" ")
#     a +=1
#     for j in range(b):
#         print("*",end=" ")
#     b -=1
#     for j in range(c):
#         print("*",end=" ")
#     c-=1
#     print(" ")



# Que 53

# n = 4
# a = n-1
# b = 1
# for i in range(n-1):
#     for j in range(a):
#         print(" ",end=" ")
#     a-=1
#     for j in range(b):
#         print("*",end=" ") 
#     b += 1 
#     for j in range(b-2):
#         print("*",end=" ")
#     print(" ")

# c =0
# d = n
# for i in range(n):
#     for j in range(c):
#         print(" ",end=" ")
#     c+=1
#     for j in range(d):
#         print("*",end=" ")  
#     d -=1
#     for j in range(d):
#         print("*",end=" ")
#     print(" ")
    
    

#again

# n = 4
# a = n-1
# for i in range(n-1):
#     for j in range(a):
#         print(" ",end=" ")
#     a -= 1
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print(" ")
# b= 0
# c =n
# for i in range(n):
#     for j in range(b):
#         print(" ",end=" ")
#     b+=1
#     for j in range(c):
#         print("*",end=" ")
#     for j in range(c-1):
#         print("*",end=" ")
#     c-=1
#     print(" ")





