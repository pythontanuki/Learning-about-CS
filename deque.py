class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def peekFront(self):    
        if self.head == None:
            return None
        return self.head.data
        
        
    def peekBack(self):    
        if self.tail == None:
            return None
        return self.tail.data
    
    
    def enqueueFront(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
        else:
            currentNode = self.head
            self.head = newNode
            self.head.next = currentNode
            currentNode.prev = self.head
            self.head.prev = None
    
    
    def enqueueBack(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
        
        else:
            currentNode = self.tail
            self.tail = newNode
            self.tail.next = None
            currentNode.next = self.tail
            self.tail.prev = currentNode
            
    
    def dequeueFront(self):
        if self.head == None:
            return None
        currentNode = self.head
        self.head = self.head.next
        self.head.prev = None
        return currentNode.data

    def deuqueBack(self):
        if self.tail == None:
            return None
        currentNode = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        return currentNode.data



if __name__ == '__main__':
    d = Deque()
    d.enqueFront(101)
    d.enqueBack(3)
    d.enqueFront(45)
    d.enqueBack(34)
    d.enqueBack(2)
    print(d.peekFront())
    print(d.peekBack())
    d.dequeueFront()
    print(d.peekFront())
    print(d.peekBack())
    d.deuqueBack()
    print(d.peekFront())
    print(d.peekBack())















            