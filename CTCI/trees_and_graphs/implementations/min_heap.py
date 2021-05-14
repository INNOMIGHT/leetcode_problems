class BinaryHeap:

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)

    def perc_up(self, current_node):
        parent = current_node // 2
        while parent > 0:
            if self.heap_list[current_node] < self.heap_list[parent]:
                self.swap(parent, current_node)
            parent = parent // 2
            
    def swap(self, bigger, smaller):
        self.heap_list[bigger], self.heap_list[smaller] = self.heap_list[smaller], self.heap_list[bigger]

    def del_min(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.heap_list.pop()
        self.current_size -= 1
        self.perc_down(1)
        return ret_val

    def perc_down(self, top_ele):
        while top_ele * 2 <= self.current_size:
            min_c = self.min_child(top_ele)
            if self.heap_list[top_ele] > self.heap_list[min_c]:
                self.swap(top_ele, min_c)
            top_ele = min_c

        
    def min_child(self, top_ele):
        if (top_ele * 2) + 1 > self.current_size:
            min_c = top_ele * 2
        elif self.heap_list[top_ele*2] < self.heap_list[(top_ele*2)+1]:
            min_c = top_ele * 2
        else:
            min_c = (top_ele * 2) + 1
        return min_c
        
    
    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.heap_list = [0] + a_list[:]
        self.current_size = len(a_list)
        while i > 0:
            self.perc_down(i)
            i -= 1
            print(self.heap_list)
    


bin_heap = BinaryHeap()
bin_heap.build_heap([4, 5, 6, 2, 1])


        
        