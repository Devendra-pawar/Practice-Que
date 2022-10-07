#PREPINSTA 100-codes solution in Python

#Que 1-Positive or Negative number:
# num = 20
# if num>0:
#     print("The number is positive")
# elif num==0:
#     print("The number is zero")
# else:
#     print("The number is negative")

#Que 2- Even or Odd number:
# num = 3
# if num%2==0:
#     print("the no.is even")
# else:
#     print("the no. is odd")

#Que 3- Sum of First N Natural numbers:
# num = 8
# sum = 0
# for i in range(1,num+1):
#         sum +=i
# print(sum)

#Que 4- Sum of N natural numbers:
# num = 15
# sum = 0
# for i in range(1,num+1):
#         sum +=i
# print(sum)

#Que 5- Sum of numbers in a given range:
# low= 2
# high= 5
# sum = 0
# for i in range(low,high+1):
#     sum +=i
# print(sum)

#Que 6- Greatest of two numbers:
# a = int(input("Enter a no."))
# b = int(input("Enter one more no."))
# if a>b:
#     print("first is greater no.")
# else:
#     print("second is greater no.")

#Que 7- Greatest of the Three numbers:

# a = int(input("Enter a no."))
# b = int(input("Enter one more no."))
# c = int(input("Enter one more no."))
# if a>b:
#     if a>c:
#        print(f"{a} is greater no.")
#     else:
#         print(f"{c} is greater no.")
# else:
#     if b>c:
#         print(f"{b} is greater no.")
#     else:
#         print(f"{c} is greater no.")

#Que 8- Leap year or not:

# year = int(input("Enter the year: "))
# if (year%4==0 and year%100!=0) or (year%400==0):
#     print("Leap year")
# else:
#     print("not a leap year")

#Que 9- Prime number:
# num = int(input("Enter the num: "))
# c = 0
# if num==0:
#     print("zero is not a prime")
# else:
#     for i in range(2,num):
#         if num%i==0:
#             c+=1
#             break
#     if c==0:
#         print("this is a prime no.")
#     else:
#         print("this is not a prime no.")

# Que 10- Prime number within a given range:----------------------------------------------------------


#Que 11- Sum of digits of a number:
# num = 1234
# sum = 0
# while num !=0:
#     a = int(num%10)
#     sum+=a
#     num= num/10
# print(sum)


#Que 12- Reverse of a number :
# num = 12345
# b=0
# while num>0:
#     a = int(num%10)
#     b = (b*10)+a
#     num=num//10
# print(b)


#Que 13- Palindrome number:
# num = 1234321
# temp = str(num)
# a = temp[::-1]
# if int(num)==int(a) :
#     print("this is a palindrome no. ")
# else:print("nhi h")


#Que 14- Armstrong number :
# n = 1634
# b=len(str(n))
# r = 0
# for i in str(n):
#     r += pow(int(i),b)
# if r==n:
#         print("it is a armstrong no.")
# else:print("not a arm strong no.")


#Que 15- Armstrong number in a given range :
# low,high= 1,10000
# for n in range(low,high+1):
#         order = len(str(n))
#         sum = 0
#         for i in str(n):
#             sum += int(i)**order
#         if sum == n : print(n,end=" ")


#Que 16- Fibonacci Series upto nth term : 
# n = 10
# n1,n2 = 0,1
# print(n1,n2,end=" ")
# for i in range(2,n):
#     n3 = n1+n2
#     n1 = n2
#     n2= n3
#     print(n3,end=" ")

#Que 17-Find the Nth Term of the Fibonacci Series :
#same

#Que 18- Factorial of a number :
# n =5
# a =1
# for i in range(1,n+1):
#     a*= i
# print(a)

#Que 19- Power of a number :
# a,b=2,3
# print(a**b)

#Que 20- Factor of a number : 
# n = 100
# for i in range(1,n+1):
#     if n%i==0: print(i,end=" ")

#Que 21- Finding Prime Factors of a number : --------------------------------------


#Que 22- Strong number :
# n = 145
# res= 0
# for i in str(n):
#     a = 1
#     for j in range(1,int(i)+1):
#         a *= j
#     res += a
# if n==res:print("strong no.")

#Que 23- Perfect number :

    