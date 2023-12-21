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
        self.head = n

    def insert_end(self,data):
        n = Node(data,None)
        if not self.is_empty():
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = n
        else:
            self.head = n                          

    def search(self,data):
        temp = self.head
        while temp != None:
            if temp.data == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self,after,data):
        temp = self.search(after)
        if temp is not None:
            n = Node(data,temp.next)
            temp.next = n
    
    def display(self):
        temp =self.head
        while temp != None:
            print(temp.data,end=" ")
            temp= temp.next

    def delete_first(self):
        if self.head is not None:
            self.head = self.head.next

    def delete_end(self):  
        if self.head is None:
            pass
        elif self.head.next == None:
            self.head = None
        else:
            temp = self.head 
            while temp.next.next != None:
                temp = temp.next
            temp.next = None


    def delete_item(self,data):
        if self.head == None:
            pass
        elif self.head.next == None :
            if self.head.item == data:
                self.head = None
        else:
            temp = self.head 
            while temp.next







sl = Linked_list()

sl.insert_start(10)
sl.insert_end(20)     
sl.insert_start(30)
sl.insert_end(40) 
sl.insert_after(10,50)
sl.display()
print()
sl.delete_end()
sl.display()
sl.insert_end(60) 
print()
sl.display()





































