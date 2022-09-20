class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        newNode = Node(data)
        tmpNode = self.head
        self.head = newNode
        self.head.next = tmpNode
    
    
    def pop(self):
        if self.head == None:
            return None
        currentNode = self.head
        self.head = self.head.next
        return currentNode.data
    
    
    def peek(self):
        if self.head == None:
            return None
        return self.head.data
    


if __name__ == '__main__':
    S = Stack()
    S.push(2)
    print(S.peek())
    S.push(4)
    print(S.peek())
    S.push(6)
    print(S.peek())
    S.pop()
    print(S.peek())
    S.pop()
    print(S.peek())
    S.pop()
    print(S.peek())
    