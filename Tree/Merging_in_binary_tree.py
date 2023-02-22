class Node :
    def __init__(self,key):
        self.value = key 
        self.left , self.right =  None , None

def mergeTree(root1,root2):
    if root1 is None and root2 is None :
        return None
    if root1 is None :
        return root2
    if root2 is None :
        return root1 
    root1.value += root2.value 
    root1.left =  mergeTree(root1.left,root2.left)
    root1.right =  mergeTree(root1.right,root2.right)
def choice(root):
    choice = int(input("Want to insert more element is tree"))

    while choice == "1" :
        n = int("Enter the number want to insert")
        root.insert(n)
def Inorder (root):
    if root :
        Inorder(root.left)
        print(root.value,end=" ")
        Inorder(root.right)
root1 = Node(int(input("Enter the root 1 ")))
choice(root1)
Inorder(root1)