class Node :
    def __init__(self,key):
        self.value = key 
        self.left = None 
        self.right = None

def one_child_count(root):
    if root == None:
        return 0 
    if root.left != None and root.right == None :
        return 1 
    elif root.left == None and root.right != None :
        return 1 
    else :
        return one_child_count(root.left) + one_child_count(root.right)

root = Node(1)
root.left = Node(2) 
root.right = Node(3) 
root.right.left = Node(4) 
root.left.right = Node(5)

print(one_child_count(root))