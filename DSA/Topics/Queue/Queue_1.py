#link - https://www.youtube.com/watch?v=ahiM09ZhBdI&list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&index=19


# Queue using list


class Queue():
    def __init__(self) :
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self,data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Underflow!!")

    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Underflow!!")
        
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Underflow!!")
        
    def size(self):
        return len(self.items)



q1= Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
print(q1.get_front())

print("dequeued ",q1.dequeue())
print("front =",q1.get_front(),"Rear=",q1.get_rear())
print("size =",q1.size())

























