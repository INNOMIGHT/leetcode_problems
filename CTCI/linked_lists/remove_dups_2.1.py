# Solution 2.1


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

    def remove_dups(self, l_list):
        list_items = set()
        pointer = l_list.head
        previous = None
        while pointer.next != None:
            if pointer.val in list_items:
                previous.next = pointer.next
            else:
                list_items.add(pointer.val)
                previous = pointer
            pointer = pointer.next

        
        return l_list.display()

        


sol = Solution()
linked_list = SinglyLinkedList()
linked_list.add_node(1)
linked_list.add_node(2)
linked_list.add_node(3)
linked_list.add_node(3)
linked_list.add_node(4)
linked_list.add_node(2)

print(sol.remove_dups(linked_list))
