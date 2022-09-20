class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def peekFront(self):
        if self.head == None: return None
        return self.head.data

    def peekBack(self):
        if self.tail == None: return self.peekFront()
        return self.tail.data
    
    def enqueue(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        
        elif self.tail == None:
            self.tail = Node(data)
            self.head.next = self.tail
        
        else:
            self.tail.next = newNode
            self.tail = newNode
    
    def dequeue(self):
        if self.head == None:
            return None
        currentNode = self.head
        if self.head.next == None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return currentNode
    
    
if __name__ == '__main__':
    que = Queue()
    print(que.peekBack())
    print(que.peekFront())
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    print(que.peekFront())
    print(que.peekBack())
    que.dequeue()
    print(que.peekFront())
    print(que.peekBack())
    
    
    













