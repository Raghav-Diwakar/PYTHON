class Node :
    def __init__(self,key):
        self.value = key 
        self.left , self.right = None , None

def nodeCount(root):
    if not root :
        return 0
    leftn = nodeCount(root.left)
    rightn = nodeCount(root.right)
    return 1 + leftn + rightn 

root = Node(1) 
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

n = nodeCount(root)
print(n)