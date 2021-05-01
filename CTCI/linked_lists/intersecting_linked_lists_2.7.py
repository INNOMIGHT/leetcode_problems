# Solution 2.7

class Solution:

    def intersection(self, l1, l2):

        # Step 1: Traverse each linked list to find the length and tails
        pointer_1 = l1.head 
        pointer_2 = l2.head
        l1_length = 0
        l2_length = 0
        
        while pointer_1 is not None:
            l1_length += 1
            pointer_1 = pointer_1.next
        
        tail1 = pointer_1

        while pointer_2 is not None:
            l2_length += 1
            pointer_2 = pointer_2.next

        tail2 = pointer_2 

        # Step 2 If the tails are not same, there is no intersection
        if tail1 != tail2:
            return False
        
        # Step 3 Advance the longer linked list pointer by diff of length
        pointer_1 = l1.head
        pointer_2 = l2.head

        diff_in_length = abs(l1_length - l2_length)
        if l1_length > l2_length:
            for i in range(diff_in_length):
                pointer_1 = pointer_1.next
        else:
            for j in range(diff_in_length):
                pointer_2 = pointer_2.next
        
        # Step 4 Traverse each linked list until pointers are same
        while pointer_1 is not None:
            if pointer_1 == pointer_2:
                return pointer_2
            pointer_2 = pointer_2.next
            pointer_1 = pointer_1.next


