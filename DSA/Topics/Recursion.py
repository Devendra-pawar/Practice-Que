# link  -  https://www.youtube.com/watch?v=D00dMdaEU0U&list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&index=28





#Que 1 - print N natural no.


# def fun(n):

#     if n <= 0:
#         return 1
#     fun(n-1)
#     print(n,end=" ")

# N = 6
# fun(N)

#Que 2 - natural no. in reverse order 

# def fun(n):

#     if n <= 0:
#         return 1
#     print(n,end=" ")
#     fun(n-1)
# N = 6
# fun(N)


#Que 3 print odd no. and even number

# def odd(n):

#     if n >0:
#         odd(n-1)
#         print(2*n-1,end=" ")

# def even(n):
#     if n>0:
#         even(n-1)
#         print(2*n,end=" ")

# even(10)
# print()
# odd(10)

#Que 4- print reverse odd no. and even number

# def odd(n):

#     if n >0:
#         print(2*n-1,end=" ")
#         odd(n-1)


# def even(n):
#     if n>0:
        
#         print(2*n,end=" ")
#         even(n-1)

# even(10)
# print()
# odd(10)


#Que 5- sum of first n natural no.,odd,even

# def sumN(n):
#     if n==1:
#         return 1
#     return n + sumN(n-1)
# def sumodd(n):
#     if n==1:
#         return 1
#     return 2*n-1 + sumodd(n-1)
# def sumeven(n):
#     if n==1 :
#         return 2
#     return 2*n + sumeven(n-1)

# n = 10
# print(f"sum of first {n} no. is", sumN(n))
# print(f"sum of first {n} odd no. is", sumodd(n))
# print(f"sum of first {n} even no. is", sumeven(n))



#Que 6 - Factorial of a number

# def fact(n):
#     if n == 0:
#         return 1
#     return n* fact(n-1)
# n = 5
# print(f"factorial of {n} N no. is ",fact(n))

#Que 7 - sum of square of N natural no.

# def sqsumN(n):
#     if n==1:
#         return 1
#     return n**2 + sqsumN(n-1)
# n = 5
# print(f"sum of square of {n} N natural no. is ",sqsumN(n))




























