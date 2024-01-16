## LINK -> https://www.youtube.com/watch?v=ZJW4eQcywYY


# operations -
# 1- Insert 
# 2- delete
# 3- traverse
# 4- search

# 5- sort
# 6- reverse





# class Node:
#     def __init__(self, item=None , next= None):
#         self.item = item
#         self.next = next 

# class SLL:
#     def __init__(self, start= None) :
#         self.start = start


#     def is_empty(self):
#         return self.start == None

#     def display(self):
#         temp = self.start
#         while temp != None:
#             print(temp.item, end=" ")
#             temp = temp.next

#     def search(self,data):
#         temp = self.start
#         while temp != None :
#             if temp.item == data :
#                 return temp
#             temp = temp.next
#         return None

#     def insert_at_start(self,data):
#         n = Node(data,self.start)
#         self.start = n

#     def insert_at_last(self,data):
#         n = Node(data,None)
#         if not self.is_empty():
#             temp = self.start
#             while temp.next != None:
#                 temp = temp.next
#             temp.next = n
#         else:
#             self.start = n

#     def insert_after(self,a,data):
#         temp = mylist.search(a)
#         if temp != None:
#             n = Node(data,temp.next)
#             temp.next = n
          


#     def delete_first(self):
#         if self.start != None:
#             self.start = self.start.next
         
#     def delete_last(self):
#         if self.start == None:
#             pass
#         elif self.start.next == None:
#             self.start = None
#         else:
#             temp = self.start
#             while temp.next.next != None:
#                 temp = temp.next
#             temp.next = None

#     def delete_item(self,data):
#         if self.start == None:
#             pass
#         elif self.start.next == None :
#             if self.start.item == data:
#                 self.start = None
#         else:
#             temp = self.start
#             if temp.item == data:
#                 self.start = temp.next
#             else:
#                 while temp.next != None :
#                     if temp.next.item == data:
#                         temp.next = temp.next.next
#                         break 
#                     temp = temp.next
                



# # driver code s

# mylist = SLL()
# mylist.insert_at_start(20)
# mylist.insert_at_start(40)

# mylist.insert_at_last(60)
# mylist.insert_at_last(70)

# mylist.insert_after(20,25)
# mylist.delete_first()
# mylist.delete_item(70)
# print()
# mylist.display()
# print()
















##again

## linked list
 
# class Node():
#     def __init__(self,item= None,next=None):
#         self.item = item 
#         self.next = next 

# class SLL():
#     def __init__(self,start=None):
#         self.start = start 

#     def is_empty(self):
#         if self.start == None:
#             return True 
#         else:
#             return False

#     def display(self):                  #traverse
#         temp = self.start
#         while temp != None:
#             print(temp.item,end=" ")
#             temp = temp.next

#     def search(self,data):
#         temp = self.start
#         while temp!= None:
#             if temp.item == data:
#                 return temp
#             temp = temp.next
#         return None 

#     def insert_at_start(self,data):
#         n = Node(data,self.start)
#         self.start = n


#     def insert_at_last(self,data):
#         n = Node(data,None)
#         if not self.is_empty():
#             temp = self.start
#             while temp.next != None:
#                 temp =temp.next
#             temp.next = n
#         else:
#             self.start = n

#     def insert_after(self,a,data):
#         temp = self.search(a)

#         if temp != None:
#             n = Node(data,temp.next)
#             temp.next =n
#         else:
#             print("can't find")


#     def delete_at_start(self):        
#         if self.start!= None:
#             self.start = self.start.next

#     def delete_at_end(self):
#         if self.start == None:
#             pass
#         elif self.start.next == None:
#             self.start = None
#         else:
#             temp = self.start
#             while temp.next.next != None:
#                 temp = temp.next
#             temp.next = None


#     def delete_value(self,data):
#         if self.start ==None:
#             pass
#         elif self.start.next == None:
#             if self.start.item == data:
#                 self.start = None 
#         else:
#             temp = self.start
#             while temp.next != None: 
#                 if temp.next.item == data:
#                     temp.next = temp.next.next
#                     break               
#                 temp = temp.next
            


# dev = SLL()
# dev.insert_at_start(10)
# dev.insert_at_start(20)
# dev.insert_at_last(30)
# dev.insert_after(20,50)
# dev.insert_at_last(40)
# dev.display()

# print()
# dev.delete_at_start()
# dev.delete_at_end()
# dev.display()
# print()
# dev.delete_value(10)
# dev.display()




### Again 

class Node():
    def __init__(self,item = None,next = None ):
        self.item = item 
        self.next = next 

class Linkedlist():
    def __init__(self,head=None):
        self.head = head 

    def is_empty(self):
        if self.head == None:
            return True 
        else:
            return False
    
    def traverse(self):
        temp = self.head
        while temp != None:
            print(temp.item,end=" ")
            temp = temp.next



    def insert_at_start(self,data):
        n = Node(data,self.head)
        self.head = n
 
    def delete_at_start(self):
        if self.head != None:
            self.head  =self.head.next

    def insert_at_last(self,data):
        n = Node(data,None)
        if not self.is_empty():
            temp = self.head 
            while temp.next != None:
                temp = temp.next
            temp.next = n
        else:
            self.head = n

    def delete_at_last(self):
        if self.head == None:
            pass
        elif self.head.next ==None:
            self.head = None       
        else :
            temp = self.head 
            while temp.next.next != None:
                temp = temp.next
            temp.next = None
    


    def search(self,data):
        temp = self.head
        while temp != None:
            if temp.item == data :
                return temp
            temp = temp.next
        return None
    
    def insert_after(self,after_data,data):
        temp = self.search(after_data)
        if temp != None:
            n = Node(data,temp.next)
            temp.next = n
        else:
            return "can't find"

    def delete_value(self,data):
        if self.head == None:
            pass
        elif self.head.next == None:
            if self.head.item == data:
                self.head = None
        else:
            temp = self.head 
            while temp.next != None:
                if temp.next.item == data:
                    temp.next = temp.next.next
                    break
                temp = temp.next
                


dev = Linkedlist()
dev.insert_at_start(10)
dev.insert_at_start(20)
dev.insert_at_last(30)
dev.insert_after(20,50)
dev.insert_at_last(40)
dev.traverse()

print()
dev.delete_at_start()
dev.delete_at_last()
dev.traverse()
print()
dev.delete_value(10)
dev.traverse()


















































