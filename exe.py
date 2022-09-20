class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def reproduceByN(head,n):
    currentNode = head
    List = []
    while True:
        if currentNode.next == None:
            break
        List.append(currentNode.data)
        currentNode = currentNode.next
    List.append(currentNode.data)
    for _ in range(n-1):
        for num in List:
            currentNode.next = SinglyLinkedListNode(num)
            currentNode = currentNode.next
    return head

    

