class Node :
    def __init__(self,key) :
        self.left = None
        self.right = None
        self.value = key 


def Preorder(root):
    if root :
        print(root.value,end=",")
        Preorder(root.left)
        Preorder(root.right)
 
root = Node(1)
root.left = Node(2)
root.right =  Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

Preorder(root)