class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
    
    #push data to Stack
    def push(self, data):
        node = Node(data)
        nextNode = self.head
        self.head = node
        self.head.next = nextNode
    
    #pop from Stack
    def pop(self):
        if self.head == None:
            return None
        currentNode = self.head
        nextNode = self.head.next
        self.head = nextNode
        return currentNode.data

    #retrieve Stack top
    def peek(self):
        if self.head == None:
            return None
        return self.head.data

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    