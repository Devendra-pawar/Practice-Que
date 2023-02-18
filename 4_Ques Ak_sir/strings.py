##Programs on Strings

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

#or

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


#Que 5. Write a program to convert lowercase string to uppercase.
# first = "Devendra"
# first = first.upper()
# print(first)

#Que 6. Write a program to convert uppercase string to lowercase.
# last = "PaWAR"
# last = last.lower()
# print(last)


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


#Que 8.Write a program to find total number of alphabets, digits or special character in a string.

# string1 = "kjf9wuet84ytufgjnjf9428f2498hns"
# alpha = 0
# digits = 0
# spec= 0

# for i in string1:
#     if (i >="A" and i<="Z") or (i >="a" and i<="z"):
#         alpha+=1
#     elif (int(i) >=0 and int(i)<=9):
#         digits+=1
#     else:
#         spec+=1
# print(alpha , digits, spec)

#not completed


#Que 9. Write a C program to count total number of vowels and consonants in a string.
