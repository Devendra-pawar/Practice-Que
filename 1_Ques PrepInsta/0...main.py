#########################################################
                        #Again#

#Que 1 - Prime Number Program in Python
# num = int(input("enter the no. :"))
# count = 0 
# for i in range(2,num):
#     if num%i == 0 :
#          count += 1
# if count == 0 :
#      print("prime no.")
# else:
#      print("not a prime no.")



#Que 2 - Prime number within a given range:

# a = 2
# b = 10 

# for i in range(a,b+1):
#     count = 0 
#     for j in range(2,i):
#         if i%j == 0 :
#             count += 1
#     if count ==0 :
#         print(i,end=" ")
        


#Que 3 - Armstrong number : 

# num = 1634
# n = len(str(num))
# sum = 0
# for i in str(num):
#     sum += int(i)**n
# if sum == num :
#     print("its an armstrong no.")
# else:
#     print("ni hai")



#Que 4 - Armstrong number in a given range : 


# num1 = 150 
# num2 = 160 

# for i in range(num1,num2+1):
#     n = len(str(i))
#     count = 0 
#     for j in str(i):
#         count += int(j)**n
#     if count == i :
#         print(i)



#Que 5 - Fibonacci Series upto nth term :

# n = 10
# lb = 0
# mb = 1
# ub = 0 
# for i in range(n):
#     print(lb,end=" ")
#     ub = lb + mb 
#     lb = mb
#     mb = ub


#Que 6 - Factor of a number :

# n = 10 
# for i in range(2, n):
#     if n %i == 0 :
#         print(i,end=" ")

#Que 7 - Finding Prime Factors of a number :

# n = 10
# for i in range(2, n):
#     if n %i == 0 :
#         count = 0 
#         for j in range(2,i):
#             if i % j == 0 :
#                 count +=1
#         if count == 0 :
#             print(i,end=" ")


#Que 8 - Strong number :

# num = 145
# sum = 0
# for i in str(num):
#     mul = 1
#     for j in range(1,int(i)+1):
#         mul *= j
#     sum+= mul
# if sum == num :
#     print("it's a strong no.")
# else:
#     print("weak hai ")



#Que 9 - Perfect number : 

# num = 28 
# sum = 0 
# for i in range(1,num):
#     if num % i == 0:
#         sum += i 

# if sum == num :
#     print("perfect no.")
# else:
#     print("nhi hai")



#Que 10 - Perfect Square :

# n = 64
# for i in range(1,n):
#     if i*i == n:
#         print(True)



#Que 11 - Automorphic number :

# n = 76
# sq = n*n
# end = str(sq)[len(str(n)):]
# if n == end:   
#     print(end)

#shi hai pr chal nhi rha


#Que 12 - Harshad number : 

# n = 21
# sum =0 
# for i in str(n):
#     sum += int(i)
# if n%sum == 0 :
#     print("harshad no.")

#Que 13 - Abundant number : 

# n = 12
# sum = 0
# for i in range(1,n):
#     if n %i == 0 :
#         sum += i
# if n < sum :
#     print("anundant no.")



#Que 14 - Friendly pair : 

# def fun(n):
#     sum = 0 
#     for i in range(1,n):
#         if n%i == 0 :
#             sum += i
#     a = n//sum
#     return a 

# num1 = 6
# num2 = 28 

# m = fun(num1)
# n = fun(num2)
# if m == n :
#     print("they are friendly pair")



#Que 15 - Highest Common Factor(HCF):

# num1 = 36 
# num2 = 60 
# hcf = 1

# for i in range(1,min(num1,num2)):
#     if num1 % i == 0 and num2 % i == 0 :
#         hcf = i
# print("hcf = ", hcf)


#Que 16 - 

# num1 = 12 
# num2 = 14
# num3 = num1 * num2 

# for i in range(max(num1,num2),num3):
#     if i % num1 == 0 and i % num2 == 0 :
#         print("lcm = ",i)
#         break


#Que 17 - Binary to Decimal to conversion : 


# b = 111
# res = 0
# a = 1
# while b > 0 :
#     r = b%10 
#     res = res + r*a
#     b = b//10
#     a *=  2

# print(res)


#Que 18 - Decimal to Binary conversion: :











#Que 19 - Find Second Smallest Element in an Array :

# ar = [10, 13, 17, 11, 34, 21]
# a = min(ar)
# min  = max(ar)
# for i in ar:
#     if i < min and i != a :
#         min = i
# print(min )


#Que 20 - Sort the elements of an array :

# a = [5,4,6,8,2,40,0]
# a.sort()
# print(a)


#Que 21 - Finding the frequency of elements in an array :

# a =[10, 30, 10, 20, 10, 20, 30, 10]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
#         count =0 
#         for j in a :
#             if j == i:
#                 count += 1
#         print(i,count)


#Que 22 - Sorting elements of an array by frequency : 

# a= [10, 20, 30, 30,30, 30, 40, 40, 50, 50, 50]

# b =[]
# c =[]
# for i in a:
#     if i not in b:
#         b.append(i)
#         count = 0 
#         for j in a:
#             if j == i :
#                 count += 1
#         c.append(count)
# for i in range(len(c)):
#     for j in range(c[i])


# not completed 







#Que 23- Finding the Longest Palindrome in an Array : 

# arr = [1, 232, 5545455, 909090, 161]
# a = arr[0]
# for i in arr:
#     if str(i) == str(i)[::-1]:
#         if len(str(i)) > len(str(a)):
#             a  = i
# print(a)



#Que 24 - Counting Distinct Elements in an Array :

# a =  [10, 20, 40, 30, 50, 20, 10, 20]

# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(len(b))


#Que 25 - Finding  Repeating elements in an Array :

# a = [10, 20, 40, 30, 50, 20, 10, 20]
# c=[]
# for i in range(len(a)):  
#     for j in range(i+1,len(a)):
#         if a[i] == a[j]:
#             if a[i] not in c:
#                 c.append(a[i])
#                 print(a[i], end=" ")



#Que 26 - Finding Non Repeating elements in an Array : 

# a = [10, 20, 70, 90, 80, 20, 10, 20]
# b =[]

# for i in range(len(a)):
#     count = 0
#     for j in range(i+1,len(a)):
#         if a[i] ==a[j]:
#             b.append(a[i])
#             count += 1
#     if count == 0:
#         if a[i] not in b:
#             print(a[i],end=" ")


#Que 27 - Removing Duplicate elements from an array :

# a= [10, 20, 20, 30, 40, 40, 40, 50, 50]
# b= []
# for i in a:
#     if i not in b:
#         b.append(i)
#         print(i,end=" ")



#Que 28 - Finding Minimum scalar product of two vectors : 


# arr1 = [1, 2, 6, 3, 7]
# arr2 = [10, 7, 45, 3, 7]

# arr1.sort()
# arr2.sort(reverse=True)

# res = 0
# for i in range(len(arr1)):
#     res += (arr1[i]*arr2[i])

# print(res)


#Que 29 - Finding Maximum scalar product of two vectors in an array:

# arr1 = [10, 30, 40, 20]
# arr2 = [2, 4, 5, 1]

# arr1.sort()
# arr2.sort()
# res = 0
# for i in range(len(arr1)):
#     res+=  (arr1[i]*arr2[i])
# print(res)

#Que 30 - Counting the number of even and odd elements in an array
 
# a = [1, 7, 8, 4, 5, 16, 8]
# even = 0
# odd = 0

# for i in a:
#     if i%2 ==0:
#         even+=1
#     else:
#         odd+=1
# print(f"even: {even} and odd: {odd}")


#Que 31- Find all Symmetric pairs in an array : 











































