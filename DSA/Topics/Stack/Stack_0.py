#Implementation
S = []
top = None
def isEmpty(stk):
    if (stk==[]): 
        return True
    else:
        return False

def push(stk,item):
    stk.append(item)
    top = len(stk)-1

def s_pop(stk):
    if (isEmpty(stk)):
        return("UnderFlow")
    else :
        i = stk.pop()
        if(len(stk)==0):
            top= None
        else :
          top = top-1
    return i 

def peek(stk):
    if(isEmpty(stk)):
        return("UnderFlow")
    else:
        top = len(stk)-1
        return stk[top]

def display(stk):
    if (isEmpty(stk)):
        print("stack is empty!")
    else:
        top = len(stk)-1    
        print(stk[top],"<----top")
        for i in range(top-1,-1,-1):
           print(stk[i])
        

while True :
    print("\n \n")
    print("Stack implementation")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter the choice(1-5) : "))

    if ch==1:
        item = int(input("Enter the item you want to push : "))
        push(S,item)
        print(f"{item} added successfully")
        input("press enter to continue...")

    elif ch== 2:
        item = s_pop(S)
        if item == "UnderFlow":
            print("Stack is empty!, underflow")
        else:
            print(f"{item} is popped")
        input("press enter to continue...")

    elif ch==3:
        item = peek(S)
        if item == "UnderFlow":
            print("Stack is empty!, underflow")
        else:
            print(f"{item} is at the top")
        input("press enter to continue...")

    elif ch==4:
        display(S)
        input("press enter to continue...")

    elif ch==5: break

    else:print("choose from 1-5")