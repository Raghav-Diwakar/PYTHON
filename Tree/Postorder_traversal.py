class Node :
    def __init__(self, key):
        self.value = key 
        self.left = None
        self.right = None 

def Postorder (root):
    if root :
        Postorder(root.left)
        Postorder(root.right)
        print(root.value,end=",")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
Postorder(root)