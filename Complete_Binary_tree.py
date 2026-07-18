class Node:
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None

def count_node(root):
    if root is None:
        return 0
    return (1 + count_node(root.left) + count_node(root.right))

def is_complete(root, index, numbernode):

    if root is None:
        return True

    if index >= numbernode:
        return False

    return (is_complete(root.left, 2 * index + 1 , numbernode)
            and is_complete(root.right, 2 * index + 2 , numbernode))

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)

node_count = count_node(root)
index = 0

if is_complete(root, index, node_count):
    print("The tree is a complete binary tree")
else:
    print("The tree is not a complete binary tree")
    
