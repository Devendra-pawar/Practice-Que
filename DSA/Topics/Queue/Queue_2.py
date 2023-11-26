#link - https://www.youtube.com/watch?v=LG8lqbZVmVI&list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&index=20

# Queue implementation using singly linked list concept 


class Node():
    def __init__(self,item = None,next = None):
        self.item = item
        self.next = next

class Queue():
    def __init__(self):
        self.front= None
        self.rear= None
        self.item_count = 0

    def is_empty(self):
        return self.front==None
        #return self.rear==None
        #return self.item-count == 0 
    
    def enqueue(self,data):
        n = Node(data)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next  = n 

        self.rear= n
        self.item_count+=1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("underflow!")
        elif self.front == self.rear :
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next

        self.item_count -=1
    
    def get_front(self):
        if self.is_empty():
            raise IndexError("underflow!")
        
        else:
            return self.front.item
    def get_rear(self):
        if self.is_empty():
            raise IndexError("underflow!")        
        else:
            return self.rear.item
        
    def size(self):
        return self.item_count


q1= Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
print("front=",q1.get_front(),"| rear=",q1.get_rear())

q1.dequeue()
print("front=",q1.get_front(),"| rear=",q1.get_rear())


















































