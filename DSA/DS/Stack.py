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

def pop(stk):
    if (isEmpty(stk)):
        return("UnderFlow!!")
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
    if(isEmpty(stk)):
        return("stack is empty!")
    else:
         top = len(stk)-1    
         print(stk[top],"<----top")
         for i in range(top-1,-1,-1):
            print(stk(i))


