class Node :
    def __init__(self,key):
        self.left =  None 
        self.value = key 
        self.right = None
def InOrder (root):
    if root :
        InOrder(root.left)
        print(root.value,end=" ")
        InOrder(root.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
InOrder(root)