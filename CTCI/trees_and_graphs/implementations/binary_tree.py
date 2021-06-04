class BinaryTree(object):
    
    def __init__(self, rootObj):
        self.key = rootObj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if(self.left_child is None):
            self.left_child = BinaryTree(new_node)

        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if(self.right_child is None):
            self.right_child = BinaryTree(new_node)

        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key
    
  
tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_left(3)
tree.insert_left(4)
tree.insert_right(5)


def inorder_traversal(tree):
    if tree:
        inorder_traversal(tree.get_left_child())
        print(tree.get_root_val())
        inorder_traversal(tree.get_right_child())


def level_order(tree):
    if tree:
        queue = []
        queue.append(tree)
        while queue != []:  
            count = len(queue)
            while count > 0:
                element = queue.pop(0)
                print(element.key, end=" ")
                if element.left_child:
                    queue.append(element.left_child)
                if element.right_child:
                    queue.append(element.right_child)
                count -= 1
            print("")

# level_order(tree)
inorder_traversal(tree)
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