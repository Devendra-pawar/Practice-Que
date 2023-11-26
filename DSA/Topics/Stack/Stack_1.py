# link - https://www.youtube.com/watch?v=2H8QmXhVvoY&list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&index=13

# Implementation of Stack using list 

class Stack :
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        if len(self.items)==0:
            return True
        else:
            return False

    def push(self,data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)
    

dev = Stack()
dev.push(10)
dev.push(20)
dev.push(30)
print(dev.peek())
print(dev.pop())
print(dev.peek())









#Again 

# class Stack :
#     def __init__(self):
#         self.item = []

#     def is_empty(self):
#         if len(self.item) ==0:
#             return True
#         else:
#             False

#     def push(self,data):
#         self.item.append(data)
    
#     def pop(self):
#         if not self.is_empty():
#             return self.item.pop()
#         else:
#             raise IndexError("stack is empty")

#     def peek(self):
#         if not self.is_empty():
#             return self.item[-1]
#         else:
#             raise IndexError("stack is empty")

#     def size(self):
#         return len(self.item)



























































