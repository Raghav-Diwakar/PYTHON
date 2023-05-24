
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

def Node_count(root:Node)->int:
    if root is None :
        return 0 
    else :
        return 1 + Node_count(root.left) + Node_count(root.right)


root = BuildTree()
inorder_traversal(root)
a = Node_count(root)
print(a)