import sys

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

def validate_bst(root, min_=-sys.maxsize, max_=sys.maxsize):
    if root is None:
        return True

    if(
        min_ <= root.value <= max_ and
        validate_bst(root.left_child, min_, root.value) and
        validate_bst(root.right_child, root.value, max_)
    ): return True
    else:
        return False
    

root = Node(5)

root.left_child = Node(4)
root.right_child = Node(6)

print(validate_bst(root))

