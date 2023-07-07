#Que 1 - Positive or Negative number: 

# num = int(input("Enter any no. :"))
# if num > 0 :
#     print("The number is positive.")
# else:
#     print("The number is negative.")


#Que 2 - Even or Odd number:

# num = int(input("Enter any no. :"))
# print("even" if num%2==0 else "odd")


#Que 3 - Sum of First N Natural numbers: 

# num = int(input("Enter any no. :"))
# res = 0 
# for i in range(num+1):
#     res = res + i
# print(res)


#Que 4 - Sum of N natural numbers:
#same


#Que 5 - Sum of numbers in a given range: 
# num1 = int(input("Enter any no. :"))
# num2 = int(input("Enter any no. :"))
# sum =0 
# for i in range(num1,num2+1):
#     sum  =sum +i 
# print(sum)


#Que 6 - Greatest of two numbers:
# num1 = int(input("Enter any no. :"))
# num2 = int(input("Enter any no. :"))
# if num1 > num2 :
#     print("Greatest no. is ",num1 )
# else:
#     print("Greatest no. is ",num2 )


#Que 7 - Greatest of the Three numbers:
# num1 = int(input("Enter any no. : "))
# num2 = int(input("Enter any no. : "))
# num3 = int(input("Enter any no. : "))

# if num1 > num2 :
#     if num1 > num3 :
#         print("Greatest no. is ",num1 )
#     else: 
#         print("Greatest no. is ",num3 )
# else:
#     if num2 > num3 :
#         print("Greatest no. is ",num2 )
#     else: 
#         print("Greatest no. is ",num3 )


#Que 8 - Leap year or not:

# year = int(input("Enter any year: "))

# if (year%4 == 0 and year%100!=0 ) or year%400==0:
#     print("It's a leap year.")
# else:
#     print("Not a leap year")


#Que 9 - Prime number:

# num =13
# count= 0 
# for i in range(2,num):
#     if num % i == 0:
#         count+= 1
# if count == 0 :
#     print("it's a prime no.")
# else:
#     print("not a prime no.")

#Que 10 - Prime number within a given range:

#######################################################





#Que 11 - Sum of digits of a number:

# n = 123
# sum = 0
# while n>0:

#     rem = n%10
#     sum += rem
#     n = n//10
# print(sum)

#Que 12- Reverse of a number :

# n = 123456
# res = 0
# while n>0:
#     rem = n%10
#     res = (res*10) + rem
#     n = n//10
# print(res)


            ## slicing
# print(str(num)[::-1])



#Que 13- Palindrome number:

# n = 12321 
# a = n
# rev = 0

# while a>0:
#     rem = a%10
#     rev = rev*10 + rem
#     a = a//10

# if n == rev:
#     print("It's a palindrome")
# else:
#     print("It's not a palindrome")


#Que 14 - Armstrong number :

# n = 371
# temp = n
# sum= 0

# while temp>0:
#     rem = temp%10
#     sum = sum + (rem**len(str(n)))
#     temp = temp//10
# if n == sum :
#     print("It's an Armstrong number")
# else:
#     print("It's not an Armstrong number")


#Que 15 - Armstrong number in a given range : 

# num1 = 150
# num2 = 155

# for i in range(num1,num2+1):
#     print(i)
#     a = str(i)
#     b = len(a)
#     sum = 0
#     for i in a:
#         sum += (int(i)**b)
#     print(sum)
    
#     if sum == i : print("ok")

###################################################### not done 


#Que 16 - Fibonacci Series upto nth term :

# num = 10
# n1 = 0
# n2 = 1
# print(n1,n2, end=" ")
# for i in range(2,num):
#     n3 = n1+n2
#     n1 = n2
#     n2 = n3
#     print(n3,end=" ")


#Que 17 - Factorial of a number :

# num = 7
# fac=1
# for i in range(num,0,-1):        # bina reverse k bhi kr skte hai
#     fac*= i
# print(fac)


#Que 18 - Power of a number : 

# num = int(input("enter the no. : "))
# p = int(input("enter the power :"))
# pow = 0
# power = num**p
# print(power)


#Que 19 - Factor of a number : 

# num = 10
# for i in range(1,num+1):
#     if num%i ==0:
#         print(i,end=" ")


#Que 20 - Finding Prime Factors of a number : 

num = 50
for i in range(1,num):
    if num%i ==0:
        count = 0
        # print(i)
        for j in range(2,i):            
            if i %j!=0:
                count +=1      
        if i == 1 or i ==2:
            print(i,end=" ")          
        if count != 0 :
            print(i,end= " "  )


























































































































































