class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def find_depth(root):
    d = 0
    while root:
        d += 1
        root = root.left
    return d

def is_perfect(root,depth,level = 1):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    if root.left and root.right:
        return is_perfect(root.left,depth,level+1) and is_perfect(root.right,depth,level+1)

    return False

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

depth = find_depth(root)

if is_perfect(root,depth):
    print("Perfect Binary Tree")
else:
    print("Not a Perfect Binary Tree")


