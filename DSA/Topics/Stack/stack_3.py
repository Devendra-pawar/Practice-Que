# link - https://www.youtube.com/watch?v=6M50z-X1dSc&list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&index=15

# Implementation of Stack using linked list concept 

class Node():
    def __init__(self,item=None , next= None):
        self.item = item
        self.next = next
        
class Stack():
    def __init__(self) :
        self.top =None             # start == Top
        self.item_count = 0
    def is_empty(self):
        return self.top == None
    
    def push(self,data):
        n = Node(data,self.top)
        self.top = n
        self.item_count += 1
    
    def pop(self):
        if not self.is_empty():
            data = self.top.item 
            self.top = self.top.next
            self.item_count -= 1
            return data
        else:
            raise IndexError("under flow")

    def peek(self):
        if not self.is_empty():
            return self.top.item           
        else:
            raise IndexError("under flow")

    def size(self):
        return self.item_count


s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)

print("total elements in stack", s1.size())
print("top element ",s1.peek())
print("poped element is ",s1.pop())
print()
print("total elements in stack", s1.size())
print("top element ",s1.peek())

print("stack is empty ",s1.is_empty())
































