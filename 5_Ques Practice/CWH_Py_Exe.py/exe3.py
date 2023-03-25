# https://prepinsta.com/tcs-coding-questions/
#Que 1


v = int(input("Enter no. of vehicle:")) 
w = int(input("Enter no. of wheels:")) 

for i in range(1,v):
    a = i *2 
    for j in range(200,1,-1):
        b = j*4
        if a +b == w:
            print(b)
            print(f"TW = {i} FW= {j}")
        

