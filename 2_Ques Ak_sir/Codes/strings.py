##Programs on Strings

# st = "Devendra pawar"
# dk = st.split() 
# print(dk)            # for converting into array
# dp = " ".join(dk)
# print(dp)            # for converting into string



#Que 1. Write a program to find length of a string.

# string1 = "Devendra pawar"
# count = 0
# for i in string1:
#     count += 1
# print(count)

#or 
# s = "Devendra pawar"
# print(len(s))


#Que 2. Write a program to copy one string to another string.

# s = "Devendra pawar"
# d=""
# for i in s:
#     d += i
# print(d)

# \\or\\

# s = "Devendra pawar"
# d = ""
# d = s
# print(d)


#Que 3.  Write a program to concatenate two strings

# first = "Devendra"
# last = "Pawar"
# full = first + " " + last
# print(str(full))


#Que 4. Write a program to compare two strings.
# a = "hello"
# b = "hello"
# if a==b:
#     print("both are same")
# else :
#     print("they are different")


#Que 5. Write a program to convert lowercase string to uppercase.

# first = "Devendra"
# first = first.upper()
# print(first)

# \\or\\

# string = "DeVenDrA"
# string2 = ""
# for i in string:   
#     if ord(i) >= 65 and ord(i) <= 90:       
#         string2 += i        
#     elif ord(i) >=97 and ord(i) <= 122:        
#         j = ord(i) - 32       
#         string2 += chr(j)
# print(string2)



#Que 6. Write a program to convert uppercase string to lowercase.
# last = "PaWAR"
# last = last.lower()
# print(last)

# \\or\\

# string1 = "DevENdRa"
# string2 = ""

# for i in string1:
#     if ord(i)>= 65 and ord(i)<= 90:
#         j = ord(i)+32
#         string2 += chr(j)
#     else:
#         string2 += i
# print(string2)


#Que 7. Write a program to toggle case of each character of a string.
# s= "FIRST aid"
# final = ""
# for i in s :
#     if i.isupper():
#         i = i.lower()
#         final += i
#     else :
#         i = i.upper()
#         final+= i        
# print(final)

# \\or\\

# s = "FIRST aid"
# s2 =""
# for i in s :
#     if ord(i)>= 65 and ord(i)<= 90:
#         j = ord(i) + 32
#         s2 += chr(j)
#     elif ord(i) >=97 and ord(i) <= 122:        
#         j = ord(i) - 32       
#         s2 += chr(j)
#     else :
#         s2 += i
# print(s2)
    


#Que 8. Write a program to find total number of alphabets, digits or special character in a string.

# string1 = "My id is devendra_06/01/2003_pawar"
# alpha = 0
# digits = 0
# spec= 0

# for i in string1:
#     if (i >="A" and i<="Z") or (i >="a" and i<="z"):
#         alpha+=1
#     elif (i >="0" and i<="9"):
#         digits+=1
#     else:
#         spec+=1
# print(alpha , digits, spec)



#Que 9. Write a program to count total number of vowels and consonants in a string.
# string1 = "Devendra Pawar"
# vowel = 0
# consonant = 0
# extra = 0
# for i in string1:
#     if i == "A" or i =="E" or i =="I" or i =="O" or i =="U" or i =="a" or i =="e" or i =="i" or i =="o" or i =="u":
#         vowel +=1
#     elif (ord(i)>= 65 and ord(i)<= 90)  or (ord(i)>= 97 and ord(i)<= 122) :
#         consonant +=1
#     else :
#         extra +=1
# print(vowel,consonant,extra)
 

#Que. 10 Write a program to count total number of words in a string.

# st = "my name is devendra pawar"
# count = 1
# for i in st :
#     if i ==" ":
#         count += 1
# print(count)


# Que 11. Write a  program to find reverse of a string.

# st = "devendra"
# a = st[::-1]
# print(a)


# # //or//

# st1 = "devendra pawar"
# print("Before reversing : ",st1)

# arr= []           #converting string into array
# for i in st1:
#     arr += i

# length= 0         # finding length of a string/array
# for i in arr:
#     length += 1

# for i in range(length//2):       # reversing the array
#     temp = arr[i]
#     arr[i]= arr[length-i-1]
#     arr[length-i-1]= temp

# st2 =""           # converting array into string
# for i in arr:
#     st2 += i

# print("After reversing : ",st2)


#Que 12.Wr program to check whether a string is palindrome or not.
# st= "1232321"

# n= 0
# for i in st:
#     n+=1

# arr = []
# for i in st:
#     arr += i

# for i in range(n//2):
#     temp = arr[i]
#     arr[i]= arr[(n-1)-i]
#     arr[(n-1)-i] = temp

# copy =""
# for i in arr:
#     copy += i

# if copy == st:
#     print("its a palindrome")
# else :
#     print("not a palindrome")

#Que 13. Write a program to reverse order of words in a given string.


st = " my name is devendra"

st = list(st)
print(st)


















































































