# Task - 
#Q1 Stack using array
#Q2 Queue using array
#Q3 Linked list using array
#Q4 Deque using array
#Q5 stack using linked list
#Q6 Queue using linked list



#Que 1 - Stack using array 


# class Stack:
#     def __init__(self):
#         self.items = []

    
#     def is_empty(self):
#         return len(self.items)==0
    
#     def push(self,data):
#         self.items.append(data)

#     def pop(self):
#         if self.is_empty():
#             return "underflow!"
#         else:
#             return self.items.pop()

#     def top(self):
#         if self.is_empty():
#             return "underflow!"
#         else:
#             return self.items[-1]

#     def size(self):
#         return len(self.items)
    

# s1 = Stack()
# s1.push(10)
# s1.push(20)
# s1.push(30)
# s1.push(40)
# print("size=",s1.size(), "top = ",s1.top())
# s1.pop()
# s1.pop()
# print("size=",s1.size(), "top = ",s1.top())



#---------------------------------------------------------------------------------------
#Q2 Queue using array

# class Queue():
#     def __init__(self):
#         self.items = []
    
#     def is_empty(self):
#         return len(self.items)==0

#     def enqueue(self,data):
#         self.items.append(data)

#     def dequeue(self):
#         if self.is_empty():
#             return "Underflow!"
#         else:
#             return self.items.pop(0)

#     def get_front(self):
#         if self.is_empty():
#             return "Underflow!"
#         else:
#             return self.items[0]

#     def get_rear(self):
#         if self.is_empty():
#             return "Underflow!"
#         else:
#             return self.items[-1]

#     def size(self):
#         if self.is_empty():
#             return "Underflow!"
#         else:
#             return len(self.items)


# q1 = Queue()
# q1.enqueue(10)
# q1.enqueue(20)
# q1.enqueue(30)
# q1.enqueue(40)
# print("size=",q1.size(), "front = ",q1.get_front()," rear=",q1.get_rear())
# q1.dequeue()
# print("size=",q1.size(), "front = ",q1.get_front()," rear=",q1.get_rear())
# q1.dequeue()
# print("size=",q1.size(), "front = ",q1.get_front()," rear=",q1.get_rear())



#Q3 Linked list using array

class Node():
    def __init__(self,data = None,next = None ):
        self.data = data
        self.next = next

class Linked_list():
    def __init__(self,head=None):
        self.head = head

    def is_empty(self):
        return self.head == None
    
    def insert_start(self,data):
        n = Node(data,self.head)





    def insert_end(self,data):




    def insert_anywhere(self,):












































