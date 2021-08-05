# Binary Tree Implementation
# class BinaryTree:

#     def __init__(self, root_obj):
#         self.key = root_obj
#         self.left_child = None
#         self.right_child = None

#     def insert_left(self, val):
#         if self.left_child == None:
#             self.left_child = BinaryTree(val)
#         else:
#             tmp = BinaryTree(val)
#             tmp.left_child = self.left_child
#             self.left_child = tmp
    
#     def insert_right(self, val):
#         if self.right_child == None:
#             self.right_child = BinaryTree(val)
#         else:
#             tmp = BinaryTree(val)
#             tmp.right_child = self.right_child
#             self.right_child = tmp        
        
#     def get_root_val(self):
#         return self.key


# tree = BinaryTree(1)
# tree.insert_left(2)
# tree.insert_right(3)
# tree.insert_right(4)
# print(tree.get_root_val())


#Binary Heap Implementation

# class BinaryHeap:

#     def __init__(self):
#         self.heap_list = [0]
#         self.current_size = 0

#     def perc_up(self, curr_node):

#         while curr_node//2 > 0:
#             if self.heap_list[curr_node//2] > self.heap_list[curr_node]:
#                 self.heap_list[curr_node//2], self.heap_list[curr_node] = self.heap_list[curr_node], self.heap_list[curr_node//2]
#             curr_node = curr_node//2
    
#     def insert(self, val):
#         self.heap_list.append(val)
#         self.current_size += 1
#         self.perc_up(self.current_size)

#     def del_min(self):
#         deleted = self.heap_list[1]
#         self.heap_list[1] = self.heap_list[-1]
#         self.heap_list.pop()
#         self.current_size -= 1
#         self.perc_down(1)
#         return str(deleted) + "is the min element which is deleted"

#     def perc_down(self, curr_node):
#         while curr_node*2 <= self.current_size:
#             min_child = self.min_c(curr_node)
#             if self.heap_list[curr_node] > self.heap_list[min_child]:
#                 self.heap_list[curr_node], self.heap_list[min_child] = self.heap_list[min_child], self.heap_list[curr_node]
#             curr_node = min_child

#     def min_c(self, top_ele):
#         if top_ele*2+1 > self.current_size:
#             return top_ele*2
#         elif self.heap_list[top_ele*2] < self.heap_list[top_ele*2+1]:
#             return top_ele*2
#         else:
#             return top_ele*2+1

#     def build_heap(self, a_list):
#         i = len(a_list)//2
#         print(i)
#         self.current_size = len(a_list)
#         self.heap_list = [0] + a_list[:]
#         while i > 0:
#             self.perc_down(i)
#             i = i-1
#             print(self.heap_list)


# binary_h = BinaryHeap()
# binary_h.build_heap([5, 4, 3, 2, 1])

# print(binary_h)
        



        
        
        
        