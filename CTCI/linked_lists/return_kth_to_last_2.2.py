# Solution 2.2


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

    def kth_to_last(self, l_list, k):
        pointer_one = l_list.head
        pointer_two = l_list.head
        for i in range(k):
            pointer_two = pointer_two.next
        
        while pointer_two.next != None:
            pointer_one = pointer_one.next
            pointer_two = pointer_two.next

        return pointer_one.val



a_list = SinglyLinkedList()
a_list.add_node(1)
a_list.add_node(2)
a_list.add_node(3)
a_list.add_node(4)
a_list.add_node(5)
a_list.add_node(6)
a_list.add_node(7)
a_list.add_node(8)
a_list.add_node(9)
a_list.add_node(10)

sol = Solution()
print(sol.kth_to_last(a_list, 4))

