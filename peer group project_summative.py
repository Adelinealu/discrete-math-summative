from distutils.command.check import check

import lst as lst
import networkx
from kivy.graphics import vertex
from networkx import nodes
from networkx.generators.random_graphs import erdos_renyi_graph

import networkx as nx
import matplotlib.pyplot as plt


class Vertex:
    def __init__(self, n):
        self.name = n


class Graph:
    vertices = {}
    edges = []
    edge_indices = {}
# Add a vertex to the set of vertices, and the graph
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            return True
        else:
            return False
# Add an edge between vertex v1 and v2 with edge weight
# and check if vertex v1 is a valid vertex
    def add_edge(self, u, v, weight=1):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True
        else:
            return False

    def print_graph(self):
        for v, i in sorted(self.edge_indices.items()):
            print(v + ' ', end='')
            for j in range(len(self.edges)):
                print(self.edges[i][j], end='')
            print(' ')


g = Graph()
# print(str(len(g.vertices)))
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

#an undirected graph, an edge between v1 v2 does not
# imply that an edge exists between v2 and v1
#then implement our graph

edges = ['AB', 'AC', 'BC', 'BF', 'DG', 'GF', 'FE', 'GH', 'HJ', 'JI', 'GI', 'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.print_graph()

