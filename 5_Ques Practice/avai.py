# arr = [1,2,3,4,5]
# d=4
# for i in range(d):
#     arr.append(arr[0])
#     arr.pop(0)
# print(arr)


# a = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# for i in a:
#     # j = i.split()
#     arr=[]
#     for j in i:
#         arr+=j
#     print(arr)
#     break


# str= "devendra"
# new=[]
# for i in str:
#     new += " "
# new.insert(5,"o")
# print(new)


# a = [" ", " ", " "]
# a[2]= 2
# print(a)


# arr =["iabd" ,"utxrfqdva", "ccgbugwg", 'lj']
# ans = 0
# out = ""
# for i in arr:
#     co = len(i)
#     vo = 0
#     for j in i:
#         if j == "a" or j == "e" or j == "i" or j == "o" or j == "u" or j == "A" or j == "E" or j == "I" or j == "O" or j == "U" :
#             vo +=1
#     dif = co-vo
#     if ans < dif:
#         ans = dif 
#         out = i
# print(out)


# print(ans)



# a = ""
# b = 9
# if a< 9:
#     print(b)

    

arr = "aabbcaaabbcccb"
# ans= 'abcabcb'
b = " "
c="0"
for i in arr:
    if c != i:
        b+=i
        c=i
print(b)
































