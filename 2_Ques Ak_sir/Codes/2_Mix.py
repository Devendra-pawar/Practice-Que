#----------------------------------------   star pattern 
#Que 60 

# num =4
# for i in range(1, num+1):
#     for j in range(1, num):
#         print("*",end=" ")
#     print(" ")

#Que 61

# num = 3
# for i in range(1,num+1):
#     for  j in range(1, num+1):
#         print(j , end= "")
#     print(" ")

#Que 62 -Que 66 -- easy h

#Que 67

# num = 5
# for i in range(1,num+1):
#     for j in range(i):
#         print("*",end=" ")
#     print(" ")

#Que 69

# num = 5
# for i in range(1,num+1):
#     a = 97
#     for j in range(i):       
#         print( chr(a),end=" ")
#         a+=1
#     print(" ")

#Que 74 

# num =5
# for i in range(num,0,-1):
#     for j in range(i):
#         print("*",end= " ")
#     print("")

#Que 77

# num =5
# a = 65
# for i in range(num,0,-1):
#     for j in range(i):
#         print(chr(a),end= " ")
#     a +=1
#     print("")

#Que 81

# num = 5
# b = num-1
# for i in range(1,num+1):
#     for j in range(b):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     b-=1
#     print(" ")
        
#Que 85

# num = 5
# a = 1
# b = num-1
# for i in range(1,num+1):
#     for j in range(b):
#         print(" ",end=" ")
#     for j in range(i):
#         print(a,end=" ")
#     b -= 1
#     a += 1
#     print(" ")
        

#Que 88

# num = 5
# b = 0
# for i in range(num,0 , -1):
#     for j in range(b):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     b += 1
#     print(" ")

#Que 93

# num = 4
# a =1
# b = 0
# for i in range(num,0 , -1):
#     for j in range(b):
#         print(" ",end=" ")
#     for j in range(i):
#         print(a,end=" ")
#         a += 1
#     b += 1    
#     print(" ")


#Que 95

# num = 4 

# b = num-1
# for i in range(1,num+1):
#     for j in range(b):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end= " ")
#     b -= 1
#     for j in range(i-1):
#         print("*",end=" ")
#     print(" ")

#### sayad 95 nhi hua h ####



#---------------------------------------------    One Dimensional Array
#Que 112 - 

# n = int(input("Enter no. of elements :"))
# arr=[]
# for i in range(n):
#     a= int(input("Enter here:"))
#     arr.append(a)
# sum = 0
# for i in arr:
#     sum += i 
# avg = sum/n

# print(f"sum of {arr} is {sum} and average is {avg}.")


#Que 113- 

# n = int(input("Enter no. of elements :"))
# arr=[]
# for i in range(n):
#     a= int(input("Enter here:"))
#     arr.append(a)
# evensum = 0
# oddsum = 0
# for i in arr:
#     if i%2 ==0:
#         evensum += i 
#     else:
#         oddsum+= i

# print("Even sum is ",evensum)
# print("Odd sum is ",oddsum)


#Que 114 --- 








# dont know how to do 


#Que 115

# arr =[]
# n = int(input("entern the no. of elements :"))
# for i in range(n):
#     a = int(input("enter unique no."))
#     arr.append(a)

# num = int(input("Enter the no. to find out the position :"))
# pos = -1
# for i in range(n):
#     if arr[i] == num:
#         pos= i

# if pos >= 0:
#     print(f"position of {num} in {arr} is {pos}.")
# else:
#     print("number not found")



#Que 116-

# arr =[]
# n = int(input("enter the no. of elements :"))
# for i in range(n):
#     a = int(input("enter unique no."))
#     arr.append(a)

# for i in range(len(arr)):
#     for j in range(len(arr)-1-i):
#         if arr[j]> arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
# print(arr)
        


#----------------------------------------------  Strings


#Que 117

# string = input("enter any string: ")
# print("string is ",string)
# print("string type is ",type(string))

#Que 118

# st= input("Enter any string : ")
# for i in range(len(st)):
#     print(f"The character at {i} index position = {st[i]}")


#Que 119

# st= input("Enter any string : ")
# count= 0 
# for i in st:
#     count+=1
# print(f"length of {st} is {count}")


#Que 120

# st= input("Enter any string : ")
# count = 0 
# ch = input("enter the character :")
# for i in st:
#     if i == ch :
#         count+=1
# print(f"the character '{ch}' comes {count} times in {st}")


#Que 121

# st= input("Enter any string : ")
# count = 0 
# for i in st:
#     if i == "A" or i == "E" or i == "I" or i == "O" or i == "U" or i == "a" or i == "e" or i == "i" or i == "o" or i == "u" :
#         count+=1
# print(f"In {st} vowels came {count} times")


#Que 122

# st= input("Enter any string : ")
# temp = list(st)
# for i in range(len(temp)):
#     for i in range(len(temp)-1-i):
#         if temp[i] > temp[i+1]:
#             temp[i],temp[i+1] = temp[i+1],temp[i]
# st = "".join(temp)
# print(st)

# one more way

# st= input("Enter any string : ")
# temp = list(st)
# temp.sort()
# st= "".join(temp)
# print(st)


#####################################
# st = "devendra"
# temp = list(st)  # too list

# temp[0]= "D"      # change
# st = "".join(temp)  # to string 
# print(st)
#####################################

#Que 123

# a = "Devendra pawar"
# b=""
# for i in a:
#     b +=i
# print(b)


#Que 124

# s = "Devendra pawar"
# b = s[::-1]
# print(b)


##OR##

# s ="Devendra pawar"
# b=""
# for i in s:
#     b = i+b
# print(b)


#Que 125

# s = "Beauty is in the eye of the beholder"
# a =list(s.split(" "))
# st = "the"
# count = 0

# for i in a:
#     if i == st:
#         count +=1
# print(count)


#Que 126

# a = "Devendra"
# b = "pawar"
# a,b = b,a
# print(a,b)


#Que 127
# a = "devendra"
# b ="devendra"
# if a==b :
#     print("Both are same")


#Que 128

# a = "devendra"
# b ="pawar"
# print(a+" "+ b)


#Que 129

a = "pine"
b = "nipe"

for i in a:
    count2 = 0
    for j in b:
        if i == j:
            count2+=1
    count1+=1


















































