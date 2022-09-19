class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def addNewNode(self, newNode):
        tmp = self.next
        self.next = newNode
        newNode.next = tmp

class SinglyLinkedList:
    def __init__(self, arr):
        self.head = Node(arr[0])    
        currentNode = self.head
        for i in range(1, len(arr)):
            currentNode.next = Node(arr[i])
            currentNode = currentNode.next
    
    def at(self, index):
        iterator = self.head
        for _ in range(index):
            if iterator.next == None:
                iterator = None
                break
            iterator = iterator.next
        return iterator
    
    def findNode(self, data):
        iterator = self.head
        while iterator is not None:
            if iterator.data == data:
                return iterator
            if iterator.next == None:
                return None
            iterator = iterator.next
    
    def printList(self):
        iterator = self.head
        while iterator is not None:
            print(iterator.data, end = '')
            iterator = iterator.next
        print()
    
    
    def topInsert(self, newNode):
        newNode.next = self.head
        self.head = newNode
        
    def lastInsert(self, newNode):
        iterator = self.head
        while iterator.next is not None:
            iterator = iterator.next
        iterator.next = newNode
    
    def popFront(self):
        self.head = self.head.next
        
    
    def delete(self, index):
        if index == 0: return self.popFront()
        iterator = self.head
        for i in range(index-1):
            if iterator == None:
                return None
            iterator = iterator.next
        
        iterator.next = iterator.next.next
        

    





