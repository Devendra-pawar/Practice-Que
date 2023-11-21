## link - https://www.youtube.com/watch?v=R3KyH6OyxHo


# Enqueue() , dequeue() , peek()


# Implentation 

Q = []
f = None
r = None

def isEmpty(Que):
    if Que==[]:
        return True 
    else:
        return False
 
def enqueue(Que, item):
    Q.append(item)
    if len(Q) == 1:
        f=r=0
    else:
        r = len(Q)-1

def dequeue(Que):
    if (isEmpty(Que)) :
        return("UnderFlow")
    else:
        i = Que.pop(0)
    
    if (len(Que)==0):
        f=r=None
    return i


def peek(Que):
    if (isEmpty(Que)):
        return("UnderFlow")
    else:
        f=0
    return Que[f]

def display(Que):
    if len(Que)==0:
        print("Queue is empty")
    elif len(Que)==1:
        print(Que[0],"<--- Front <--- Rear")
    else:
        f = 0
        r = len(Que)-1  
        print(Que[f], "<--- Front")

        for x in range(1,r):
            print(Que[x])

        print(Que[r],"<--- Rear")


while True :
    print("\n \n")
    print("This is queue implementation!")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    ch = int(input("Enter the choice(1-5) : "))
    
    if ch ==1:
        item = int(input("Enter the element you want to insert : "))
        enqueue(Q,item)
        input("press and key to continue..")
    
    if ch==2:
        item= dequeue(Q)
        if(item=="UnderFlow"):
            print("Queue is empty!, Underflow!")
        else:
            print(f"{item} is dequeued!")
        input("press any key to continue")
    
    if ch==3:
        item = peek(Q)
        if item=="UnderFlow":
            print("Queue is empty!, Underflow!")
        else:
            print(f"Front is {item}")
        input("press any key to continue")
        
    if ch==4:
        display(Q)
        input("press any key to continue")
    
    if ch==5:
        break


    else: print("choose from 1-5")