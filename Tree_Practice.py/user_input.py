
class Node :
    def __init__(self,key):
        self.data = key 
        self.left = None
        self.right = None

def BuildTree():
    rootData = input("Enter the node data : ")
    root = Node(rootData)

    has_left = input(f"Is left child of {rootData} or not(y/n) : ")
    if has_left == 'y' or has_left == "Y":
        root.left = BuildTree()

    has_right = input(f"Is right child of {rootData} or not(y/n) : ")
    if has_right == 'y' or has_right == "Y":
        root.right = BuildTree()

    return root

def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.data,end=" ; ")
        inorder_traversal(node.right)

root = BuildTree()
inorder_traversal(root)