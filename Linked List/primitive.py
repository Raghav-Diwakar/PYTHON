# InsAft

class Node :
    def __init__(self,data) :
        self.data = data 
        self.next = None

class linkedList :
    def  __init__(self) :
        self.head = None
        
    def Traverse(self):
        if self.head == None:
            print("Empty Lisy")
        else :
            temp = self.head
            while temp != None :
                print(temp.data,end=',')
                temp = temp.next

    def InsBeg(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def InsAft(self,prevNode , newdata):
        if prevNode is None :
            print("Previous node is not Exit in LL")
        
        newNode = Node(newdata)
        newNode.next = prevNode.next
        prevNode.next = newNode

    def InsEnd(self, data):
        newNode = Node(data)
        if self.head == None :
            self.head =  newNode
        else :
            temp = self.head
            while temp.next != None :
                temp = temp.next
            temp.next = newNode


