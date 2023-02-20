class Node :
    def __init__(self,data) :
        self.data = data 
        self.left = None
        self.right = None

    def insert(self , data):
        if data < self.data :
            if self.left :
                self.left.insert(data)
            else :
                self.left = Node(data)
        else :
            if self.right :
                self.right.insert(data)
            else :
                self.right = Node(data)

def InOrder (root):
    if root :
        InOrder(root.left)
        print(root.data,end=" ")
        InOrder(root.right)


root = Node(25)
root.insert(15)
root.insert(10)
root.insert(22)
root.insert(4)
root.insert(12)
root.insert(18)
root.insert(24)
root.insert(50)
root.insert(35)
root.insert(70)
root.insert(31)
root.insert(44)
root.insert(66)
root.insert(90)


InOrder(root)