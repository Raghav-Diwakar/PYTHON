class Node :
    def __init__(self,key):
        self.value = key 
        self.left = None 
        self.right = None 
def leaf_node_count(root):
    if root == None:
        return 0 
    if root.left == None and root.right == None:
        return 1 
    else :
        return leaf_node_count(root.left) + leaf_node_count(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(leaf_node_count(root))