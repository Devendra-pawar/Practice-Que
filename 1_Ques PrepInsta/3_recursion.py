#Que 1 - Power  of  a  Number

# def power(base,pow):
#     if pow == 0:
#         return 1
#     else:
#         return base * power(base ,pow-1)
# base = 2
# pow = 5
# print("power of the no. is :",power(base,pow))


#Que 2 - Prime Number using Recursion

# def prime(n,i):   
#     if n ==0:
#         return True
#     if n == 1:
#         return True 
#     #base 
#     if n ==i:
#         return True
#     if n%i == 0:
#         return False
    
#     return prime(n,i+1)

# n = 96
# i = 2
# if prime(n,i):
#     print("Yes, it is a prime no.")
# else :
#     print("No, it is not a prime no.")



#Que 3 - Largest element in an array –

# def lar(a,n):
#     if (n == 1):
#         return a[0]
#     return max(a[n-1], lar(a,n-1))
        
# A = [1, 4, 3, -5, -4, 8, 6]
# n = len(A)
# print("largest element is",lar(A,n))



#Que 4 - smallest element in an array –

# def sma(a,n):
#     if (n == 1):
#         return a[0]
#     return min(a[n-1], sma(a,n-1))
        
# A = [1, 4, 3, -5, -4, 8, 6]
# n = len(A)
# print("smallest element is",sma(A,n))


#Que 5 - Reversing a Number –

# s = 0
# def rev(a):
#     global s
#     if a>0 :
#         r = a%10
#         s = s*10 +r
#         a = a//10
#         rev(a)
#     return s

# a = 12345
# print("reverse of no. is ", rev(a))



#Que 6 - HCF of two numbers –



































































