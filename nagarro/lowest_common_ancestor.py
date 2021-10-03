class Node:

    def __init__(self, val):
        self.val = val 
        self.left = self.right = None


def lowest_common_ancestor(root, a, b):

    if a.val < root.val and b.val < root.val:
        return lowest_common_ancestor(root.left, a, b)
    
    if a.val > root.val and b.val > root.val:
        return lowest_common_ancestor(root.right, a, b)
    
    return root.val
    

root = Node(5)
one = Node(4)
two = Node(3)
three = Node(6)
four = Node(8)

root.left = two
root.left.left = one
root.right = three
root.right.right = four

print(lowest_common_ancestor(root, four, three))
