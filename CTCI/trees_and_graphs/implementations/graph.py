from typing import NewType


class Vertex:

    def __init__(self, num):
        self.num = num
        self.connected_nodes = {}
    
    def add_nbr(self, nbr, weight=0):
        self.connected_nodes[nbr] = weight

    

class Graph:

    def __init__(self):
        self.vertex_list = {}
    
    def add_vertex(self, num):
        new_vert = Vertex(num)
        print(str(new_vert)+ " added to vertex list.")
        self.vertex_list[num] = new_vert
    
    def add_edge(self, from_v, to, weight=0):
        if from_v not in self.vertex_list:
            from_v = Vertex(from_v)
            self.vertex_list[from_v] = Vertex(from_v)
        if to not in self.vertex_list:
            to = Vertex(to)
            self.vertex_list[to] = Vertex(to)

        self.vertex_list[from_v].add_nbr(to, weight)
        return str(from_v) + " is now connected to: " + str(to) + " with a distance: " + str(weight)
    

a_graph = Graph()
a_graph.add_vertex(1)
a_graph.add_vertex(2)
print(a_graph.add_edge(1, 2, 5))


        
        
        
        