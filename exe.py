class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    #get top of the Stack
    def peek(self):
        if self.head == None: return None
        return self.head.data
    
    #push data into Stack
    def push(self, data):    
        newNode = Node(data)
        currentNode = self.head
        self.head = newNode
        self.head.next = currentNode
     
    #pop data from Stack
    def pop(self):
        if self.head == None: return None
        currentNode = self.head
        self.head = self.head.next
        return currentNode.data
    
    #get how many datas in the Stack
    def len(self):
        res = 0
        while True:
            if self.peek() == None:
                break
            self.pop()
            res += 1
        return res

    #clean the Stack
    def clean(self):
        while True:
            if self.peek() == None:
                break
            self.pop()
        
    #take all data from the Stack
    def takeAll(self):
        List = []
        while True:
            if self.peek() == None:
                break
            List.append(self.pop())
        return List[::-1]


def solveStack(s, player):
    for score in player:
        if s.peek() == None:
            s.push(score)
            continue
        if score < s.peek():
            s.clean()
        s.push(score)
    return s

#convert from List to String
def listToString(List):
    res = '['
    for element in List:
        res += str(element)
        res += ','
    res = res [:len(res)-1:]
    res += ']'
    return res


def diceStreakGamble(player1,player2,player3,player4):
    playerList = [player1, player2, player3, player4]
    s = Stack()
    mx = -1
    playerId = -1
    for i in range(len(playerList)):
        s.clean()
        pre = solveStack(s, playerList[i]).takeAll()
        l = len(pre)
        if mx < l:
            mx = l
            playerId = i
            ans = pre
    res = "Winner:"
    res += "Player "
    res += str(playerId+1)
    res += " won $"
    res += str(mx*4)
    res += " by rolling "
    res += listToString(ans)
    return res  


def isParenthesesValid(parentheses):
    Hash = {'{':'}', '(':')', '[':']'}
    S = Stack()
    for parentese in parentheses:
        if parentese in Hash.keys():
            S.push(parentese)
        else:
            if Hash.get(S.peek()) == parentese:
                S.pop()
            else:
                return False
    return S.len() == 0






    

    

