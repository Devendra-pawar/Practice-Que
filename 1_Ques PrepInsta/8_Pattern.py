# Pattern Printing----------------------

#Que 1 - Square Star Pattern-

# l =4
# for i in range(l):
#     for i in range(l):
#         print("*",end="")
#     print("")


#Que 2 - Hollow Square Star Pattern-

# l = 4
# for i in range(l):
#     for j in range(l):
#         if i==0 or i ==l-1 or j==0 or j==l-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print("")


#Que 3 - Rhombus Star Pattern-
# n = 4
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for j in range(n):
#         print("*",end="")   
#     print(" ")

#Que 4- Hollow Rectangle Star Pattern-

# n = 4
# m =6
# for i in range(n):  
#     for j in range(m):
#         if i ==0 or i == n-1 or j==0 or j ==m-1:
#             print("*",end="")   
#         else:
#             print(" ",end="")
#     print(" ")

#Que 5- Inverted Pyramid Star Pattern

# n =4
# m =7
# n1 = n
# for i in range(n):
#     for j in range(i):
#         print(end=" ")         
#     for j in range(n1):
#         print("*",end="")   
#     for j in range(n1-1):
#         print("*",end="")
#     n1 -=1
#     print()


#Que 6- Inverted Hollow Pyramid Star Pattern

# n =4
# m =7

# a = 0
# b = m -1
# for i in range(n):   
#     for j in range(m):
#         if i ==0 or  j==a or j ==b:
#             print("*",end="")
#         else:
#             print(end=" ")
#     a+=1
#     b-= 1
#     print()

