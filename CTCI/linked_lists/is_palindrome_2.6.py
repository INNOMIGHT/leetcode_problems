class Solution:

    def is_palindrome(self, l1):
        
        # Method 1 Using Stacks
        if l1.head is None: return False
        stack = []
        compare_stack = []
        pointer = l1.head 
        while pointer is not None:
            stack.append(pointer.val)
            pointer = pointer.next
        
        for items in reversed(stack):
            compare_stack.append(items)
        
        if compare_stack == stack:
            return True
        else:
            return False

        # Method 2
        # Make 2 linked list, 1 original and 1 reversed. compare and check.