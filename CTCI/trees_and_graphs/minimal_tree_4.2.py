class Node:

    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None
        self.parent = None


class BinarySearchTree:

    def __init__(self):
        self.root = None
        
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            return self._insert(self.root, val)
    
    def _insert(self, curr_node, val):
        if val < curr_node.val:
            if curr_node.left_child is None:
                new_node = Node(val)
                curr_node.left_child = new_node
            else:
                self._insert(curr_node.left_child, val)
        if val > curr_node.val:
            if curr_node.right_child is None:
                new_node = Node(val)
                curr_node.right_child = new_node
            else:
                self._insert(curr_node.right_child, val)
    
    def search(self, val):
        if self.root is None:
            return False
        else:
            return self._search(self.root, val)
        
    def _search(self, curr_node, val):
        while curr_node:
            if val == curr_node.val:
                return True
            if val < curr_node.val:
                self._search(curr_node.left_child, val)
            else:
                self._search(curr_node.right_child, val)
        
        return False
    
    def display_tree(self):
        if self.root is None:
            return 0
        else:
            return self._display(self.root)
    
    def _display(self, curr_node):
        if curr_node is not None:
                
            self._display(curr_node.left_child)
            print(curr_node.val)
            self._display(curr_node.right_child)
        
        
    

bst = BinarySearchTree()
arr = [4, 5, 1, 3, 2]
for i in arr:
    bst.insert(i)

bst.display_tree()


        
        
        