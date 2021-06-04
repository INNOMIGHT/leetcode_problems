import sys
sys.path.append('E:\\Python\\problem_solving\\CTCI\\trees_and_graphs\\implementations')

from implementations.binary_tree import BinaryTree


def check_balanced(tree):
    if not tree:
        return -1
    return max(check_balanced(tree.left_child), check_balanced(tree.right_child))+1

    
def find_height(tree):
    if tree:
        left = check_balanced(tree.left_child)
        right = check_balanced(tree.right_child)
    if abs(left-right)> 1:
        return False
    else:
        return find_height(tree.left_child) and find_height(tree.right_child)

        
    
tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_left(3)
tree.insert_left(4)
tree.insert_right(5)

print(check_balanced(tree))
