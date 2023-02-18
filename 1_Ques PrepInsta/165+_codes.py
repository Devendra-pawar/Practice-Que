# Getting Started-----------------------------------------------------------

#Que 1  Positive or Negative number:

# num = int(input("Enter any no.:"))
# if num >0 :
#     print("it is a positive no.")
# elif num == 0:
#     print("It is neither positive nor negative")
# else :
#     print( "It is a negative no.")


#Que 2 Even or Odd number:

# num = int(input("Enter any no.:"))

# if num%2==0:
#     print("It is even no.")
# else :
#     print("It is a odd no.")


#Que 3 Sum of First N Natural numbers:

# num = int(input("Enter any number:"))
# sum = 0
# for i in range(1,num+1):
#     sum = sum + i
# print(sum)


#Que 4-Sum of First N Natural numbers:
#same


#Que 5-Sum of numbers in a given range: 

# low = int(input("Enter the low of the number:"))
# high= int(input("Enter the high of the number:"))
# sum = 0 
# for i in range(low,high+1):
#     sum += i
# print(sum)


#Que 6 Greatest of two numbers: 

# num1 = int(input("Enter any number:"))
# num2 = int(input("Enter any number:"))

# if num1 > num2:
#     print("Greatest number is :", num1 )
# elif num1 == num2 :
#     print("Both are equal")
# else:
#     print("Greatest number is:",num2)


#Que 7 Greatest of the Three numbers:

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
        

#Que 8 Leap year or not: 
# print("Checking a year is a leap year or not-")
# year = int(input("Enter any year:"))

# if (year%4 == 0 and year%100 !=0 ) or year %400== 0 :
#     print("It's a leap Year")
# else:
#     print("Not a leap year")


#Que 9 Prime number:

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


#Que 10 Prime number within a given range:

# low = int(input("Enter the low of the number:"))
# high= int(input("Enter the high of the number:"))

# for i in range(low, high+1):

#     count = 0
#     for j in range(2,i):       
#         if i % j == 0:
#             count+=1
#     if count == 0:
#         print(i,end=" ")


#Que 11 Sum of digits of a number: 

# num = int(input("Enter any number :"))
# sum = 0 
# while num > 0 :
#     single = num% 10
#     num = num//10
#     sum += single
# print(sum)


#Que 12 Reverse of a number :
# num = int(input("Enter any number :"))
# rev = 0 
# while num > 0 :
#     single = num% 10
#     num = num//10
#     rev = rev*10 + single
# print(rev)


#Que 13 Palindrome number: 

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


#Que 14 Armstrong number : 

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


#Que 15 Armstrong number in a given range :

#low,high = int(input("Enter low no.")),int(input("Enter high no."))
# low,high = 150,160
# for i in range(low,high+1):
#     j = i
#     sum = 0
#     while i > 0:
#         last = i %10
#         sum = sum + pow(last,len(str(j)))
#         i = i//10
#     if j == sum :print(j)

#Que 16 Fibonacci Series upto nth term : 

# len = 10
# first = 0
# sec= 1
# print("Fibonacci series is ",first ,sec,end=" ")
# for i in range(2,len):
#     third = first + sec
#     first = sec
#     sec = third 
#     print(third,end=" ")

#Que 17 Find the Nth Term of the Fibonacci Series : 
# num = 10

# old = 0
# new = 1
# for i in range(num):
#     print(old,end=" ")
#     next = old + new 
#     old = new 
#     new = next 
    
#Que 18 Factorial of a number :

# n = 5
# fac= 1
# for i in range(1,n+1):
#     fac = fac*i
# print(fac)

#Que 19- Power of a number :

# num =int(input("Enter any no."))
# power = int(input("Emter power of the no."))
# print("the power of th no. is:",pow(num,power))


#Que 20- Factor of a number :

# num =100
# for i in range(1,num+1):
#     if num % i ==0:
#         print(i,end =" ")


#Que 21 -Finding Prime Factors of a number :











#Working with Numbers--------------------------------------

#Question no . 1 Highest Common Factor(HCF):

# num1 = 36
# num2 = 60
# hcf = 1

# for i in range(1,min(num1,num2)):
#     if num1%i==0 and num2%i==0:
#         hcf = i
# print("Highest common factor is ",hcf)


#Question no. 2 Lowest Common Multiple (LCM) : 

# num1 = 12
# num2 = 14

# for i in range(max(num1,num2),(num1*num2)+1):
#     if i % num1 ==0 and i % num2 ==0:
#         lcm = i
#         break
# print("Least common multiplier is ",lcm)


# Question no. 3 Greatest Common Divisor :
#same as 1

#Question no. 4 Binary to Decimal to conversion : 

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

#Question no. 5 Octal to Decimal conversion :

# num = 512
# dec = 0
# base = 1

# while num >0:
#     digit = num % 10
#     dec = dec + digit *base 
#     base *= 8
#     num = num//10
# print("Decimal no. is ",dec)


#Question no. 6 Hexadecimal to Decimal conversion:














#Codes for Recursion---------------------------------------

#Question no. 1 Power of a Number –

# def fun(a,b):
#     if b ==0:
#         return 1 
#     else:
#         return a*fun(a,b-1)
# base = 2
# power= 3
# print("answer is",fun(base,power))


#Question no. 2 Prime Number –

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


#Question no. 3 Largest element in an array –

# def fun(A,n):
#     if n ==0:
#         return A[0]
#     return max(A[n-1], fun(A,n-1))

# A = [1, 4, 3, -5, -4, 8, 6]
# n = len(A)
# print(fun(A,n))


#Question no. 4 Smallest element in an array –

# def fun(A,n):
#     if n ==0:
#         return A[0]
#     return min(A[n-1], fun(A,n-1))

# A = [1, 4, 3, -5, -4, 8, 6]
# n = len(A)
# print(fun(A,n))


#Question no. 5 Reversing a Number –

#...............


#Question no. 6 HCF of two numbers –













#Important Codes related to Arrays-------------------------

# QUESTION NO. 1 Find Largest element in an array : 

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

#Question 2  Find Smallest Element in an Array : 

# a = [10, 89, 9, 56, 4, 80, 8]
# min = a[0]
# for i in range(len(a)):
#     if a[i]< min:
#         min = a[i]
# print(min)

#Question 3 Find the Smallest and largest element in an array : 

# arr = [10, 89, 9, 56, 4, 80, 8]
# min = arr[0]
# max = arr[0]
# for i in arr:
#     if i < min : min = i
#     if i > max : max = i
# print(min,max)

#Question no. 4 Find Second Smallest Element in an Array : 

# arr = [10, 13, 17, 11, 34, 21]
# first = arr[0]
# second = arr[1]

# for i in arr:
#     if i <first: first = i
# for i in arr:
#     if i < second and i != first: second = i
# print(second)

#Question no. 5 Calculate the sum of elements in an array : 

# arr = [10, 89, 9, 56, 4, 80, 8]
# sum = 0
# for i in arr:
#     sum+= i
# print(sum)


#Question no. 6 Reverse an Array :

# A = [10, 20, 30, 40, 50]
# a = A[::-1]
# print(a)

#Question no. 7  Sort first half in ascending order and second half in descending : 

# arr = [1, 90, 34, 89, 7, 9]
# half = len(arr)//2
# arr.sort()

# a1 = arr[:half]
# a2 = arr[half:]
# a2.sort(reverse= True)
# print(a1+a2)


#Question no. 8 Sort the elements of an array : 
# arr = [10, 40, 20, 30]
# arr.sort()
# print("in ascending:",arr)
# arr.sort(reverse=True)
# print("in decending:",arr)

#Que 9-Finding the frequency of elements in an array :

# arr = [10, 30, 10, 20, 10, 20, 30, 10]

# for i in arr:








#Operations on Strings-------------------------------------

# Question no. 1 Check whether a character is a vowel or consonant : 

# c = input("Enter a character:")

# if c == "a" or c == "e" or c == "i" or c == "o" or c == "u" or c == "A" or c == "E" or c == "I" or c == "O" or c == "U":
#     print("It is a vowel")
# else:
#     print("It is a consonant")

# Question no. 2 Check whether a character is a alphabet or not :

# ch = input("Enter any character:")

# if "a"<= ch <= "z" or "A"<= ch <= "Z":
#     print("It is a alphabet ")
# else:
#     print("It is not a alphabet")


#Question no. 3 Find the ASCII value of a character :

# ch = input("Enter any character:")
# print("the ascii value is",ord(ch))

#Question no. 4 Length of the string without using strlen() function :

# string = input("Enter :")
# count=0
# for i in string:
#     count +=1
# print(count)


#Question no. 5 Toggle each character in a string :

# String = 'GuDDuBHaiyA'
# new = str()

# for i in String:
#     if i.isupper():
#         i = i.lower()
#         new +=i
#     else:
#         i = i.upper()
#         new+=i
# print(new)


#Question no. 6 Count the number of vowels : 

# string = "prepinsta"
# count = 0
# for i in string:
#     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#         count+=1
# print(count)


#Question no. 7 Remove the vowels from a String :

# string = "PrepInsta"
# new =""
# for i in string:
#     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
#         pass
#     else :
#         new +=i
# print(new)

#Que 8 Check if the given string is Palindrome or not : 
# num = '12321'
# pal = num[::-1]
# if pal == num:print("Palidrome no.")
# else:print("not a palidrome")

#Que 9- Print the given string in reverse order :

# a = "Hello world"
# for i in reversed(a) : 
#     print(i,end="")

#Que 10- Remove all characters from string except alphabets : 

# a = "Justice!For@Chutki123"
# b = ""
# for i in a:
#     if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
#         b+= i
# print(b)


#Que 11-Remove spaces from a string : 

# s = "PrepInsta is fabulous"
# a =""
# for i in s:
#     if i != " ":
#         a+= i
# print(a)
#or
# s = "".join(s.split())
# print(s)


#Que 12-Remove brackets from an algebraic expression : 
######################

#Que 13-Count the sum of numbers in a string : 

# s ="Daya123Ben456"
# sum = 0
# for i in s:
#     if i >= "1" and  i<= "9":
#         sum += int(i)
# print(sum)


#Que 14- Capitalize the first and last character of each word of a string :





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


for i in range(1,1):
    print("8")
