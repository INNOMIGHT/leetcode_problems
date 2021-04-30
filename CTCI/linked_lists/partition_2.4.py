# Solution 2.4

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

    def partition(self, linked_list, node):

        pointer = linked_list.head
        division = None
        while pointer.next is not None:
            if pointer.next.val == node:
                division = pointer
                break
        pointer = linked_list.head
        while pointer.next is not None:
            if pointer.val > node:
                temp = division.next.next
                division.next.next = pointer
                pointer.next = temp
            elif pointer.val < node:
                temp = division.next
                division.next = pointer
                pointer.next = temp
        return linked_list


l_list = SinglyLinkedList()
l_list.add_node(1)
l_list.add_node(7)
l_list.add_node(5)
l_list.add_node(8)
l_list.add_node(4)
l_list.add_node(9)

sol = Solution()
print(sol.partition(l_list, 5))

