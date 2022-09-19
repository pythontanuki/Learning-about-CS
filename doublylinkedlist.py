class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, arr):
        if len(arr) == 0:
            self.head = Node(None)
            self.tail = self.head
            return
        
        self.head = Node(arr[0])
        currentNode = self.head
        for i in range(1, len(arr)):
            currentNode.next = Node(arr[i])
            currentNode.next.prev = currentNode
            currentNode = currentNode.next
        self.tail = currentNode
    
    def printList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data, end = ' ')
            currentNode = currentNode.next
        print()
    
    def printListReverse(self):
        currentNode = self.tail
        while currentNode is not None:
            print(currentNode.data, end = ' ')
            currentNode = currentNode.prev
        print()
    
    # def reverse(self):
        
    #1-indexed
    def at(self, index):
        currentNode = self.head
        for _ in range(index-1):
            if currentNode.next is None:
                return None
            currentNode = currentNode.next  
        return currentNode
    
    


if __name__ == '__main__':
    doubleyLinkedList = DoublyLinkedList([35,23,546,67,86,234,56,767,34,1,98,78,555])
    doubleyLinkedList.printList()
    print(doubleyLinkedList.tail.data)
    print(doubleyLinkedList.tail.prev.data)
    print(doubleyLinkedList.head.data)
    print(doubleyLinkedList.head.next.data)
    print(doubleyLinkedList.at(5).data)