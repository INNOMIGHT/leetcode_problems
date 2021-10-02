class Node:
    
    def __init__(self, val):
        self.val = val
        self.left_child = self.right_child = None

    
def level_order_tree_maker(arr, root, i, n):

    # base condition
    if i < n:
        temp = Node(arr[i])
        root = temp

        root.left_child = level_order_tree_maker(arr, root.left_child, i*2 + 1, n)
        root.right_child = level_order_tree_maker(arr, root.right_child, i*2 + 2, n)

        return root


def prLevel(root, x):
     
    if (not root):
        return
 
    # queue to hold tree node with level
    q = []
 
    # let root node be at level 1
    q.append([root, 1])
 
    p = []
    levels = {}
    # Do level Order Traversal of tree
    while (len(q)):
        p = q[0]
        q.pop(0)
        levels[p[0].val] = p[1]
        print("node: " + str(p[0].val) + " level: " + str(p[1]))
        if (p[0].left_child):
            q.append([p[0].left_child, p[1] + 1])
        if (p[0].right_child):
            q.append([p[0].right_child, p[1] + 1 ])
    
    level_required = 0
    for key in levels.keys():
        if key == x:
            level_required = levels[key] 
    for key in levels.keys():
        if levels[key] == level_required and key != x:
            print(key, end=" ")
            

root = None
root = level_order_tree_maker([1, 2, 3, 4, 5, 6], root, 0, 6)
print(prLevel(root, 5))