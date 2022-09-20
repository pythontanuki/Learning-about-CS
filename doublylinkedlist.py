class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class DoublyLinkedList:
    def __init__(self, arr):
        self.head = Node(arr[0])
        currentNode = self.head
        for i in range(1, len(arr)):
            currentNode.next = Node(arr[i])
            currentNode.next.prev = currentNode
            currentNode = currentNode.next
        self.tail = currentNode

    #retrieve the data from designated index
    def at(self, index):
        currentNode = self.head
        for _ in range(index):
            currentNode = currentNode.next
            if currentNode == None:
                break
        return currentNode

    #print all data in order
    def printList(self):
        currentNode = self.head
        while True:
            if currentNode == None:
                break
            print(currentNode.data, end = ' ')
            currentNode = currentNode.next
        print()
    
    #print all data in reverse order
    def printListReverse(self):
        currentNode = self.tail
        while True:
            if currentNode.prev == None:
                break
            print(currentNode.data, end = ' ')
            currentNode = currentNode.prev
        print()
    
    #reverse by iterative
    def reverse_iter(self):
        prevNode = None
        currentNode = self.head
        while currentNode:
            prevNode = currentNode.prev
            currentNode.prev = currentNode.next
            currentNode.next = prevNode
            currentNode = currentNode.prev
        if prevNode:
            self.head = prevNode.prev
    
    #reverse by recursive
    def reverse_recursive(self):
        def _reverse_recursive(currentNode):
            if currentNode == None:
                return None
            prevNode = currentNode.prev
            currentNode.prev = currentNode.next
            currentNode.next = prevNode
            
            if currentNode.prev == None:            
                return currentNode
            return _reverse_recursive(currentNode.prev)
        self.head = _reverse_recursive(self.head)

    #apped to top of the list
    def topInsert(self, data):
        newNode = Node(data)
        self.head.prev = newNode
        newNode.next = self.head
        newNode.prev = None
        self.head = newNode
        
    #insert to last of the list
    def lastInsert(self, data):
        newNode = Node(data)
        self.tail.next = newNode
        newNode.prev = self.tail
        newNode.next = None
        self.tail = newNode
    
    #insert to designated node of the List  
    def nextInsert(self, node, data):
        newNode = Node(data)
        tempNode = node.next
        node.next = newNode
        newNode.prev = node
        newNode.next = tempNode
        if tempNode == None:
            self.tail = newNode
        else:
            tempNode.prev = newNode

    #delete top node
    def popFront(self):
        self.head = self.head.next
        self.head.prev = None
        
    #delete back node
    def popBack(self):
        self.tail = self.tail.prev
        self.tail.next = None
    
    #delete designated node
    def deleteNode(self, index):
        currentNode = self.at(index)
        if currentNode == self.tail: return self.popBack()
        if currentNode == self.head: return self.popFront()
        prevNode = currentNode.prev
        nextNode = currentNode.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        

if __name__ == '__main__':
    numList = DoublyLinkedList([35,23,546,67,86,234,56,767,34,1,98,78,555])
    #printList() 35 23 546 67 86 234 56 767 34 1 98 78 555
    numList.printList()
    
    numList.topInsert(45)
    #printList() 45 35 23 546 67 86 234 56 767 34 1 98 78 555 
    numList.printList()
    
    numList.lastInsert(33)
    #printList() 45 35 23 546 67 86 234 56 767 34 1 98 78 555 33
    numList.printList()
    
    numList.nextInsert(numList.at(5), 1000000)
    #printList() 45 35 23 546 67 86 1000000 234 56 767 34 1 98 78 555 33 
    numList.printList()
    
    numList.popBack()
    #printList() 45 35 23 546 67 86 1000000 234 56 767 34 1 98 78 555
    numList.printList()
    
    numList.popFront()
    #printList() 35 23 546 67 86 1000000 234 56 767 34 1 98 78 555 
    numList.printList()
    
    numList.deleteNode(5)
    #printList() 35 23 546 67 86 234 56 767 34 1 98 78 555
    numList.printList()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    