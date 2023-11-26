## link - https://www.youtube.com/watch?v=vvYBXD_IXuE&list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&index=14

# implementation of stack by inheriting list class




class Stack(list):
    def is_empty(self):
        return len(self)==0

    def push(self,data):
        self.append(data)
    
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("stack is empty")
        
    
    def peek(self):
        if not self.is_empty():
            return self[-1]
            
        else:
            raise IndexError("stack is empty")

    def size(self):
        return len(self)    

    def insert(self,index,data):
        raise AttributeError("No attribute insert in stack")


s1 = Stack()
s1.push(40)
s1.push(20)
s1.push(10)
print("top value ",s1.peek())
print(s1.pop())
print("top value ",s1.peek())
print("size ",s1.size())





















