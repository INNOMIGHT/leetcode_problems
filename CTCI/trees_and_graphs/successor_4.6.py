def successor(tree, target):
    if tree:
        successor(tree.left_child, target)
        tree.root
        successor(tree.right_child, target)
    if tree.root.val == target:
        if tree.root.left_child:
            return tree.root.left_child
        elif tree.root.right_child:
            return tree.root.right_child
        else:
            return tree.root.parent
        