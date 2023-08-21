#Que 1- Check whether a character is a vowel or consonant :

# c = input("Enter a character :")
# if c== "A" or c== "a" or c =="E" or c =="e" or c =="I" or c =="i" or c =="O" or c =="o" or c=="U" or c == "u":
#     print("Its's a vowel")
# else:
#     print("consonant")


#Que 2 - Check whether a character is a alphabet or not :
# c = input("Enter a character :")
# # if (ord(c) >= 65 and ord(c)<= 90) or (ord(c) >= 97 and ord(c)<= 122):
# if "a"<= c <= "z" or "A"<= c <= "Z":

#     print("its a alphabet")
# else:
#     print("nhi h")

#Que 3 - Find the ASCII value of a character :

# c = input("Enter a character :")
# print(ord(c))

#Que 4 - Length of the string without using strlen() function :

# string= "Devendra pawar"
# length = 0
# for i in string :
#     length +=1 
# print(length)

#Que 5 - Toggle each character in a string :

# s = "DevENdrA"
# s1 =""
# for i in s :
#     if 65<= ord(i) <= 90:
#         a = ord(i) + 32
#         s1+= chr(a)
#     elif 97<= ord(i) <= 122:
#         b = ord(i) - 32
#         s1+=chr(b)
# print(s,"converted to: ",s1)

## lower() or upper() bhi use kr skte the

#Que 6 - Count the number of vowels :

# ch ="Devendra Pawar"
# count= 0
# for c in ch:
#     if c== "A" or c== "a" or c =="E" or c =="e" or c =="I" or c =="i" or c =="O" or c =="o" or c=="U" or c == "u":
#         count +=1
# print(count)


#Que 7 - Remove the vowels from a String :
# ch ="Devendra Pawar"
# ch1=""
# for i in ch:
#     if i== "A" or i== "a" or i =="E" or i =="e" or i =="I" or i =="i" or i =="O" or i =="o" or i=="U" or i == "u":
#         pass
#     else:
#         ch1+=i
# print(ch1)

#Que 8 - Check if the given string is Palindrome or not :

# s= "abcba"
# s1= ""
# for i in reversed(s):
#     s1+= i
# print(s, "is converted to ",s1)
    
## will also use string slicing 


##-------------------------------------------------- ---------------------- something important
# a = '12345'
# b =""
# for i in a :
#     b = i + b     # for reverse 54321
#     #b = b + i    # for simple 12345
# print(b)
##-------------------------------------------------------------------------

#Que 9 - Print the given string in reverse order :

# a = " Hello world"
# b = ""

# for i in a :
#     b = i+b
# print("reverse of :",a)
# print("reverse is :",b) 

#Que 10 - Remove all characters from string except alphabets

# a = "#Justice!For@Chutki123"
# b=""
# for i in a :
#     if "a"<=i<="z" or "A"<=i<="Z":
#         b += i 
# print(b)


#Que 11- Remove spaces from a string :

# a =  "PrepInsta is fabulous"
# b=""
# for i in a :
#     if "a"<=i<="z" or "A"<=i<="Z":
#         b += i 
# print(b)

## one more way

# a =  "PrepInsta is fabulous"
# b=""
# for i in a:
#     if i == " ":
#         continue
#         # pass
#     else:
#         b+=i
# print(b)


#Que 12 - Remove brackets from an algebraic expression :

# a = "(a-b)+[c*d]+{e/f}"
# b =""

# for i in a:
#     if i == "(" or i == ")" or i == "{" or i == "}" or i == "[" or i == "]":
#         continue
#     else:
#         b+= i
# print(b)


#Que 13- Count the sum of numbers in a string : 
# a ="Daya123Ben456"

# sum =0
# for i in a :
#     if 48<= ord(i) <= 57 :
#         sum += int(i)
# print(sum)


#Que 14 - Capitalize the first and last character of each word of a string :













##not done


#Que 15 - Calculate frequency of characters in a string :


# st = 'devendra pawar'

# dict =  {}
# for i in st:
    
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i] = 1
# print(dict)


## another way 










#Que 16- Find non-repeating characters in a string :


# def fun(s,n):
#     for i in s:
        
#         count = 0 
#         for j in s:
#             if i == j :
#                 count += 1
#         if count == 1 :
#             print(i,end=" ")

# s = "prepinsta"
# n = len(s)
# fun(s,n)




#Que 17 - Check if two strings are Anagram or not :

# s1 = "Listen"
# s2 = "Silent"
# s1 = sorted(s1.lower())
# s2 = sorted(s2.lower())

# if s1==s2 :
#     print("they are anagram")






















































