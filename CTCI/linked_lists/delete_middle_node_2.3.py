# Solution 2.3

class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    

    def add_node(self, node):
        new_node = Node(node)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

    
    def display(self):
        current = self.head
        if current.val is None:
            print("List is empty")

        while current is not None:
            print(current.val)
            current = current.next
    
            
class Solution:

    def delete_middle_node(self, node):
        # You are given a node not the head, so
        # copy the next node data to current and delete next node

        if node is None or node.next is None:
            return False
        next_node = Node(node.next.val)
        node.val = next_node.val
        node.next = node.next.next
        return True



l_list = SinglyLinkedList()
for i in range(1, 6):
    node = l_list.add_node(i)

sol = Solution()
print(sol.delete_middle_node(l_list))
