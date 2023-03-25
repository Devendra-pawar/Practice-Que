import time
timestamp =time.strftime('%H:%M:%S')
print(timestamp)

h = int(time.strftime('%H'))
m = int(time.strftime('%M'))
s = int(time.strftime('%S'))

if (h>=0 and h<12):
    print("Good Morning Sir!") 
elif (h>=12 and h<17):
    print("Good Afternoon Sir!") 
elif (h>=17 and h<21):
    print("Good Night Sir!") 
