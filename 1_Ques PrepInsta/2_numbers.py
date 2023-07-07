#Que 1 - Highest Common Factor(HCF):

# num1 = 36
# num2 = 60
# hcf =1
# for i in range(2,max(num2,num1)):     # minimum tk chalao min(num1,num2)
#      if num2 % i == 0 and num1 % i == 0 :
#           hcf = i

# print(f"Hcf of {num1} and {num2} is", hcf)

#Que 2 -Lowest Common Multiple (LCM):

# num1 = 12
# num2 = 14
# lcm =  num1 * num2 

# for i in range(lcm, max(num1,num2),-1):  # ya fir shidha chalao or break laga do
#     if i % num1 ==0 and i % num2 ==0:
#         lcm = i
# print(f"lcm of {num1} and {num2} is",lcm )

#Que 3 - greatest common divisior == highest common factor


#Que 4- Binary to Decimal to conversion : 

# bin = 101011
# dec = 0
# n =0
# # for array
# k =str(bin)
# arr =[]
# for i in k:
#     arr.append(i)

# for j in reversed(arr):
#     a = int(j) * (2**n)
#     dec += a
#     n += 1
# print(dec)


     # one more way without functions :

# bin = 101011
# base = 0
# dec=0

# while bin > 0 :
#      rem = bin%10 
#      dec = dec + (rem*(2**base))    
#      base+=1
#      bin = bin//10
# print("decimal no. is ",dec)


#Que 5 - Octal to Decimal conversion :

# oct = 125
# base = 0
# dec = 0

# while oct>0:
#      rem = oct%10
#      dec = dec + (rem*(8**base))
#      base +=1
#      oct = oct//10
# print("decimal value is",dec)

#Que 6- Hexadecimal to Decimal conversion:
