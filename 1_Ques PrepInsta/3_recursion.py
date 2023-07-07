#Que 1 - Power  of  a  Number

# def power(base,pow):
#     if pow == 0:
#         return 1
#     else:
#         return base * power(base ,pow-1)
# base = 2
# pow = 5
# print("Answer is :",power(base,pow))


#Que 2 - Prime Number using Recursion

def prime(n,i):   
    if n ==0:
        return True
    if n == 1:
        return True 
    #base 
    if n ==i:
        return True
    if n%i == 0:
        return False
    
    return prime(n,i+1)

n = 96
i = 2
if prime(n,i):
    print("Yes, it is a prime no.")
else :
    print("No, it is not a prime no.")