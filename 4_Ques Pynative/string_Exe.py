# Exercise 1A: Create a string made of the first, middle and last character

# str1 = "James"
# a = len(str1)
# print(str1[0]+str1[a//2]+str1[-1])


# Exercise 1B: Create a string made of the middle three characters

# str1 = "JhonDipPeta"
# l = len(str1)//2
# m1 = str1[l-1]
# m2 = str1[l]
# m3 = str1[l+1]
# res =m1+m2+m3
# print(res)


#Exercise 2: Append new string in the middle of a given string

# s1 = "Ault"
# s2 = "Kelly"
# a = len(s1)//2
# s3 = s1[:a] + s2 + s1[a:]
# print(s3)

#Exercise 3: Create a new string made of the first, middle, and last characters of each input string

# s1 = "America"
# s2 = "Japan"
# m1 = len(s1)//2
# m2 = len(s2)//2
# s3 = s1[0]+s2[0]+s1[m1]+s2[m2]+s1[-1]+s2[-1]
# print(s3)

#Exercise 4: Arrange string characters such that lowercase letters should come first

# str1 = "PyNaTive"

# s =""
# b =""
# for i in str1:
#     if i >= "a" and i<= "z":
#         s += i
#     else:
#         b+=i
# res =s+b
# print(res)


#Exercise 18: Replace each special symbol with # in the following string

# str1 = '/*Jon is @developer & musician!!'
# res =""
# for i in str1:
#     if i ==" ":
#         res += " "
#     elif (i >= "a" and i<= "z") or (i >= "A" and i<= "Z"):
#         res+= i
#     else:
#         res+= "#"
# print(res)


#Exercise 17: Find words with both alphabets and numbers

# str1 = "Emma25 is Data scientist50 and AI Expert"
# res=[]
# ar= str1.split()
 
# for i in ar:
#     if any(char.isalpha() for char in i) and any(char.isdigit() for char in i):
#         res.append(i)
# for i in res:
#     print(i)


#Exercise 14: Remove empty strings from a list of strings

str_list = ["Emma", "Jon", "", "Kelly",None, "Eric", ""]
res =[]
for i in str_list:
    if i:
        res.append(i) 
       
print(res)