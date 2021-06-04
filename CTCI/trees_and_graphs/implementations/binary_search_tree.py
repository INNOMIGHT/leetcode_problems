class Node:

    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None
        self.parent = None


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.traversal = []


    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            return self._insert(val, self.root)
                
    
    def _insert(self, val, curr_node):
        if val < curr_node.val:
            if curr_node.left_child is None:
                curr_node.left_child = Node(val)
                curr_node.left_child.parent = curr_node
            else:
                self._insert(val, curr_node.left_child)
        
        elif val > curr_node.val:
            if curr_node.right_child is None:
                curr_node.right_child = Node(val)
                curr_node.right_child.parent = curr_node
            else:
                self._insert(val, curr_node.right_child)

        else:
            print("Value already in tree.")

    
    def height(self):
        if self.root is None:
            return 0
        else:
            return self._height(self.root, 0)
    
    def _height(self, curr_node, tree_height):
        if curr_node is None:
            return tree_height
        left_height = self._height(curr_node.left_child, tree_height+1)
        right_height = self._height(curr_node.right_child, tree_height+1)

        return max(left_height, right_height)

    def search(self, val):
        if self.root.val == val:
            return True
        else:
            return self._search(val, self.root)

    def _search(self, val, curr_node):
        if val == curr_node.val:
            return curr_node
        elif val < curr_node.val and curr_node.left_child is not None:
            return self._search(val, curr_node.left_child)
        elif val > curr_node.val and curr_node.right_child is not None:
            return self._search(val, curr_node.right_child)
        else:
            print("Not Present")

    def delete_value(self, value):
        return self.delete_node(self.search(value))
    
    def delete_node(self, node):
        # find min value
        def find_min(n):
            current = n
            while current.left_child is not None:
                current = current.left_child
            return current
        
        def children_present(n):
            children = 0
            if n.left_child is not None:
                children += 1
            if n.right_child is not None:
                children += 1
            return children
        
        num_children_present = children_present(node)
        node_parent = node.parent
        # Case - 1 (When no children are present)
        if num_children_present == 0:
            if node_parent.left_child is not None:
                node_parent.left_child == None
            else:
                node_parent.right_child == None
        
        # Case - 2 (When 1 child is present)
        if num_children_present == 1:
            if node.left_child is not None:
                child = node.left_child
            else:
                child = node.right_child

            if node_parent.left_child == node:
                node_parent.left_child = child
            else:
                node_parent.right_child = child

            child.parent = node_parent

        # Case - 2 (When 2 child is present)
        if num_children_present == 2:
            successor = find_min(node.right_child)

            node.value = successor.value

            self.delete_node(successor)

    def print_tree(self):
        if self.root is not None:
            return self._print_tree(self.root)

    def _print_tree(self, curr_node):
        if curr_node is not None:
            self._print_tree(curr_node.left_child)
            self.traversal.append(curr_node.val)
            self._print_tree(curr_node.right_child)
    
    def successor(self, target):
        self._print_tree(self.root)
        print(self.traversal)
        for i in range(len(self.traversal)):
            if self.traversal[i] == target:
                if i == len(self.traversal):
                    print("It has no successor")
                print(self.traversal[i+1])
        

tree = BinarySearchTree()
tree.insert(5)
tree.insert(6)
tree.insert(2)
tree.insert(4)
tree.insert(1)

tree.successor(4)



