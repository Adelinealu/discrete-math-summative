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

edges = ['AB', 'AC', 'BC', 'BF', 'DG', 'GF', 'FE', 'GH', 'HJ', 'JI', 'GI', 'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.print_graph()


def generateGraph():
    # number of nodes
    n = 10
    # probability of edge creation
    p = 0.8
    g = erdos_renyi_graph(n, p)
    print(g.nodes)
    print(g.edges)

    nodes = g.nodes
    edges = g.edges

    check = []
    missing_num = False

    for eachnode in nodes:
        counter = 0
        for everyedge in edges:
            if eachnode in everyedge:
                counter += 1

        if counter == 0:
            missing_num = True

    if missing_num:
        print("The generated graph is not implemented")
    else:
        print("The generated graph is implementedd")
        check.append(0)

    lst = []
    for node in nodes:
        for edge in edges:
            if node in edge:
                lst.append(node)
rounds = int(input("How many graphs would you like to be generated? "))
rounds = float(rounds)
req = 0.0
connected_count = 0.0
euler_count = 0.0
for i in range(int(rounds)):
    result = generateGraph()