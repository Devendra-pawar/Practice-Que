

# Deque Data Structure 


# class Deque():
#     def __init__(self):
#         self.items = []
    
#     def is_empty(self):
#         return len(self.items)== 0

#     def insert_front(self,data):
#         self.items.insert(0,data)
    
#     def insert_rear(self,data):
#         self.items.append(data)
    
#     def delete_front(self):
#         if not self.is_empty():
#             self.items.pop(0)
#         else:
#             raise IndexError("underflow!")

#     def delete_rear(self):
#         if not self.is_empty():
#             self.items.pop(-1)  
#         else:
#             raise IndexError("underflow!")

#     def get_front(self):
#         if not self.is_empty():
#             return self.items[0]
#         else:
#             raise IndexError("underflow!")
    
#     def get_rear(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             raise IndexError("underflow!")

#     def size(self):
#         return len(self.items)


# q1 = Deque()
# q1.insert_front(10)
# q1.insert_rear(20)
# q1.insert_front(30)
# q1.insert_rear(40)
# print("front=",q1.get_front(),"| Rear=",q1.get_rear())
# q1.delete_front()
# q1.delete_rear()
# print("front=",q1.get_front(),"| Rear=",q1.get_rear())







## Again 


class Deque():
    def __init__(self):
        self.items= []

    def is_empty(self):
        if len(self.items)==0:
            return True 
        else:
            return False 
        
    def insert_front(self,data):
        self.items.insert(0,data)
    
    def insert_rear(self,data):
        self.items.append(data)
    
    def delete_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "stack underflow"

    def delete_rear(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "stack underflow!"

    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "stack underflow!"

    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "stack underflow!"


obj = Deque()














