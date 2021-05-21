import sys
sys.path.append('E:\\Python\\problem_solving\\CTCI\\trees_and_graphs\\implementations')

from implementations.binary_tree import BinaryTree


class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None
        

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head is None:
            self.head = ListNode(val)
        else:
            return self._insert(val, self.head)
    
    def _insert(self, val, curr_node):
        if curr_node.next is None:
            new_node = ListNode(val)
            curr_node.next = new_node
        else:
            self._insert(val, curr_node.next)

    def display(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.val)
            curr_node = curr_node.next
        

tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_left(3)
tree.insert_left(4)
tree.insert_right(5)
depths = {}

depths[tree] = 1
def find_nodes_depth(tree, level):
    if not tree:
        return 0
    else:
        return _find_nodes(tree, level)

def _find_nodes(curr_node, level):
    if curr_node:
        _find_nodes(curr_node.left_child, level+1)
        depths[curr_node] = level
        _find_nodes(curr_node.right_child, level+1)

lists = []
find_nodes_depth(tree, 1)

for i in range(max(depths.values())):
    for node, val in depths.items():
        if val == i+1:
            lists.append(LinkedList())
            lists[i].insert(node)

print(lists[4].display())

    


    