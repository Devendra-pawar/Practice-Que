# Getting Started-----------------------------------------------------------

#Question no. 1 

# num = int(input("Enter any no.:"))
# if num >0 :
#     print("it is a positive no.")
# elif num == 0:
#     print("It is neither positive nor negative")
# else :
#     print( "It is a negative no.")


#Question no. 2

# num = int(input("Enter any no.:"))

# if num%2==0:
#     print("It is even no.")
# else :
#     print("It is a odd no.")


#Question no. 3

# num = int(input("Enter any number:"))
# sum = 0
# for i in range(1,num+1):
#     sum = sum + i
# print(sum)


#Question no. 4
#same


#Question no. 5

# low = int(input("Enter the low of the number:"))
# high= int(input("Enter the high of the number:"))
# sum = 0 
# for i in range(low,high+1):
#     sum += i
# print(sum)


#Question no. 6

# num1 = int(input("Enter any number:"))
# num2 = int(input("Enter any number:"))

# if num1 > num2:
#     print("Greatest number is :", num1 )
# elif num1 == num2 :
#     print("Both are equal")
# else:
#     print("Greatest number is:",num2)


#Question no. 7

# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter second number:"))
# num3 = int(input("Enter third number:"))

# if num1 >num2 :
#     if num1 >num3 :
#         print("Greatest number is:",num1)
#     else:
#         print("Greatest number is:",num3)
# else:
#     if num2 >num3 :
#         print("Greatest number is:",num2)
#     else :
#         print("Greatest number is:",num3)
        

#Question no. 8
# print("Checking a year is a leap year or not-")
# year = int(input("Enter any year:"))

# if (year%4 == 0 and year%100 !=0 ) or year %400== 0 :
#     print("It's a leap Year")
# else:
#     print("Not a leap year")


#Question no. 9

# num = int(input("Enter any number:"))

# if num > 1 :
#     count = 0
#     for i in range(2,num):
#         if num%i ==0:
#            count += 1
#     if count ==0 :
#         print("It is a prime number")
#     else:
#         print("It is not a prime number")
# else :
#     print("Not prime")


#Question no. 10

# low = int(input("Enter the low of the number:"))
# high= int(input("Enter the high of the number:"))

# for i in range(low, high+1):

#     count = 0
#     for j in range(2,i):       
#         if i % j == 0:
#             count+=1
#     if count == 0:
#         print(i,end=" ")


#Question no. 11

# num = int(input("Enter any number :"))
# sum = 0 
# while num > 0 :
#     single = num% 10
#     num = num//10
#     sum += single
# print(sum)


#Question no. 12
# num = int(input("Enter any number :"))
# rev = 0 
# while num > 0 :
#     single = num% 10
#     num = num//10
#     rev = rev*10 + single
# print(rev)


#Question no. 13

# num = int(input("Enter a no.:"))
# temp = num
# check = 0
# while temp >0:
#     last = temp%10 
#     temp = temp//10
#     check = check * 10 + last
# if num == check:
#     print(num," is a palindrome")
# else:
#     print("Not a palindrome")

#Question no. 14

# num = int(input("Enter any no.:"))
# temp = num
# l = len(str(num))
# sum = 0

# while temp>0:
#     ldigit = temp %10
#     temp = temp//10
#     sum = sum + (ldigit**l)
# if sum == num :
#     print(num,"is a armstrong number")
# else:
#     print(num," is not a armstrong number")

#Question no. 15


















#Working with Numbers--------------------------------------

#Question no . 1 

# num1 = 36
# num2 = 60
# hcf = 1

# for i in range(1,min(num1,num2)):
#     if num1%i==0 and num2%i==0:
#         hcf = i
# print("Highest common factor is ",hcf)


#Question no. 2 

# num1 = 12
# num2 = 14

# for i in range(max(num1,num2),(num1*num2)+1):
#     if i % num1 ==0 and i % num2 ==0:
#         lcm = i
#         break
# print("Least common multiplier is ",lcm)


# Question no. 3
#same as 1

#Question no. 4

# bn = int(input("Enter any binary no.:"))
# ans = 0
# base = 1
# while bn>0:
#     rem = bn%10
#     rem *= base
#     ans += rem
    
#     bn= bn//10
#     base *= 2
# print("Decimal no is ",ans)















#Codes for Recursion---------------------------------------

#Question no. 1

# def fun(a,b):
#     if b ==0:
#         return 1 
#     else:
#         return a*fun(a,b-1)
# base = 2
# power= 3
# print("answer is",fun(base,power))


#Question no. 2

# def prime(n,i):
#     if n==i :
#         return True
#     elif n %i ==0:
#         return False
    
#     else:
#         return prime(n,i+1) 

# n = 971
# i = 2
# if prime(n,i):
#     print("It is a prime no.")
# else :
#     print("It is not a prime no.")


#Question no. 3

# def fun(A,n):
#     if n ==0:
#         return A[0]
#     return max(A[n-1], fun(A,n-1))

# A = [1, 4, 3, -5, -4, 8, 6]
# n = len(A)
# print(fun(A,n))


#Question no. 4

# def fun(A,n):
#     if n ==0:
#         return A[0]
#     return min(A[n-1], fun(A,n-1))

# A = [1, 4, 3, -5, -4, 8, 6]
# n = len(A)
# print(fun(A,n))











#Important Codes related to Arrays-------------------------

# QUESTION NO. 1

# a = [10, 89, 9, 56, 4, 80, 8]
# print(max(a))

#or

# a = [10, 89, 9, 56, 4, 80, 8]
# a.sort()
# print(a[-1])

#or 

# a = [10, 89, 9, 56, 4, 80, 8]
# max = a[0]
# for i in range(len(a)):
#     if a[i]>max:
#         max = a[i]
# print(max)

#Question 2 

# a = [10, 89, 9, 56, 4, 80, 8]
# min = a[0]
# for i in range(len(a)):
#     if a[i]< min:
#         min = a[i]
# print(min)

#Question 3

# arr = [10, 89, 9, 56, 4, 80, 8]
# min = arr[0]
# max = arr[0]
# for i in arr:
#     if i < min : min = i
#     if i > max : max = i
# print(min,max)

#Question no. 4

# arr = [10, 13, 17, 11, 34, 21]
# first = arr[0]
# second = arr[1]

# for i in arr:
#     if i <first: first = i
# for i in arr:
#     if i < second and i != first: second = i
# print(second)









#Operations on Strings-------------------------------------

# Question no. 1

# c = input("Enter a character:")

# if c == "a" or c == "e" or c == "i" or c == "o" or c == "u" or c == "A" or c == "E" or c == "I" or c == "O" or c == "U":
#     print("It is a vowel")
# else:
#     print("It is a consonant")

# Question no. 2

# ch = input("Enter any character:")

# if "a"<= ch <= "z" or "A"<= ch <= "Z":
#     print("It is a alphabet ")
# else:
#     print("It is not a alphabet")


#Question no. 3

# ch = input("Enter any character:")
# print("the ascii value is",ord(ch))

#Question no. 4

# string = input("Enter :")
# count=0
# for i in string:
#     count +=1
# print(count)


















